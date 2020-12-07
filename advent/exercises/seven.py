import os.path
import re
from typing import List, Dict, Tuple

from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/seven'

BAG_REGEX = re.compile(r'(?P<bag_count>\d+)? ?(?P<bag_color>\w* \w*) bags?\,?( contain)?')


class Graph(object):

    def __init__(self):
        self.nodes = {}

    def get(self, node_name):
        return self.nodes.get(node_name, None)

    def add(self, node):
        self.nodes[node.name] = node

    def link(self, outer_bag, inner_bag, count: int):
        outer_bag = self.nodes[outer_bag.name]
        inner_bag = self.nodes[inner_bag.name]
        outer_bag.contains(inner_bag, count)
        inner_bag.contained_by(outer_bag)


class Node(object):

    def __init__(self, name):
        self.name = name
        self._contains = {}
        self._contained_by = {}

    def contains(self, other_node, count: int):
        # at some point in the future, maybe these edges store data
        # for now, boolean
        self._contains[other_node.name] = (other_node, count)

    def contained_by(self, other_node):
        self._contained_by[other_node.name] = other_node

    def count_contains(self):
        '''
        recursively pass through all _contains and sum up the edges
        '''

        def _do_count(children: List[Tuple[Node, int]]):
            # tuples are a count of the number of bags and the bag

            # base case: no more children
            if len(children) == 0:
                return 1

            # starts at 1 because of self
            node_count = 1
            # for each child, count all the children + multiply by the number of childs
            for child in children:
                child_factor = child[1]
                child_node = child[0]
                node_count += child_factor * _do_count(list(child_node._contains.values()))

            return node_count

        return _do_count(list(self._contains.values())) - 1 # -1 because original node should not count


    def count_containers(self):
        '''
        recursively pass through all _contained_by until all visited
        '''

        def _do_count(nodes_to_visit: List, visited: Dict):
            # base case: we have visited all the nodes
            if len(nodes_to_visit) == 0:
                return len(visited.keys())
            current_node = nodes_to_visit[0]
            remaining_nodes = nodes_to_visit[1:]
            # skip if already visited
            if current_node.name in visited:
                return _do_count(remaining_nodes, visited)
            # we have not visited this node. mark it as visited
            visited[current_node.name] = True
            # add unvisited neighbors to the list of nodes to touch
            for nodeName, node in current_node._contained_by.items():
                if nodeName not in visited:
                    remaining_nodes.append(node)

            return _do_count(remaining_nodes, visited)

        nodes_to_visit = list(self._contained_by.values())

        # - 1 because our own node name is in the initial visited list
        return _do_count(nodes_to_visit, {self.name: True}) - 1



def parse_bags(rule: str):
    matches = BAG_REGEX.findall(rule)
    # first bag is the outer bag
    outer_bag = matches[0][1]
    final = {"outer_bag": outer_bag}
    inner_bags = []
    for match in matches[1:]:
        if match[1] == 'no other': # special case. e.g 'foo bar bag contains no other bags'
            break
        inner_bags.append({'color': match[1], 'count': int(match[0])})
    final['inner_bags'] = inner_bags

    return final


def make_graph(rules: List[str]):
    bag_graph = Graph()

    for r in rules:
        bag_info = parse_bags(r)

        outer_bag = bag_graph.get(bag_info['outer_bag'])
        if not outer_bag:
            outer_bag = Node(bag_info['outer_bag'])
            bag_graph.add(outer_bag)

        for inner in bag_info['inner_bags']:
            inner_bag = bag_graph.get(inner['color'])
            if not inner_bag:
                inner_bag = Node(inner['color'])
                bag_graph.add(inner_bag)
            bag_graph.link(outer_bag, inner_bag, inner['count'])

    return bag_graph

def main():
    rules = get_input(INPUT_PATH)

    bag_graph = make_graph(rules)

    shiny_gold_bag = bag_graph.get('shiny gold')
    shiny_gold_containers = shiny_gold_bag.count_containers()
    shiny_gold_contains = shiny_gold_bag.count_contains()
    print(f"part 1: {shiny_gold_containers} bags can contain a shiny gold bag")
    print(f"part 2: {shiny_gold_contains} bags are required inside of a shiny gold bag")


if __name__ == "__main__":
    main()