import os.path
import re
from typing import List, Set

INPUT_PATH = f'{os.path.dirname(__file__)}/input/four'


def is_inty(s: str) -> bool:
    return re.match(r'^\d+$', s) != None


def valid_hgt(hgt: str):
    match = re.match(r'^(\d+)(in|cm)$', hgt)
    if match:
        groups = match.groups()
        val = int(groups[0])
        unit = groups[1]
        if unit == 'cm':
            return 150 <= val <= 193
        else:
            return 59 <= val <= 76
    return False


class Passport(object):
    '''
    passport attributes

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    '''

    REQUIRED_ATTRS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    _passport_re = re.compile(r'(?P<key>\w+)\:(?P<val>[^\s]+)')

    _validation_fxn = {
        'byr': lambda a: is_inty(a) and 1920 <= int(a) <= 2002,
        'iyr': lambda a: is_inty(a) and 2010 <= int(a) <= 2020,
        'eyr': lambda a: is_inty(a) and 2020 <= int(a) <= 2030,
        'hgt': valid_hgt,
        'hcl': lambda a: re.match(r'^#([0-9a-f]){6}$', a) != None,
        'ecl': lambda a: a in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda a: re.match(r'^\d{9}$', a),
    }

    def __init__(self, input_str: str = None):
        self.attrs = {}
        self.current_attrs = set()
        self._valid = True
        if input_str:
            self._from_str(input_str)

    def __repr__(self):
        return self.attrs.__repr__()

    def _from_str(self, input_str: str):
        '''parses key value pairs from string input'''
        matches = self._passport_re.findall(input_str)
        for g in matches:
            self.add_attr(g[0], g[1])

    def add_attr(self, attr_name: str, attr_val: str):
        # todo: validate attr_name
        self.attrs[attr_name] = attr_val
        self.current_attrs.add(attr_name)
        # run validation function
        val_fxn = self._validation_fxn.get(attr_name)
        if val_fxn:
            self._valid = self._valid and val_fxn(attr_val)

    def has_required_attrs(self) -> bool:
        '''checks if passports have the required fields'''
        intersection = self.current_attrs.intersection(self.REQUIRED_ATTRS)
        return intersection == self.REQUIRED_ATTRS

    def valid(self) -> bool:
        '''checks if passport has required fields AND the fields pass validation'''
        return self.has_required_attrs() and self._valid


def parse_passports(passports: str) -> List[Passport]:
    '''
    passports are separated by blank lines and are kv pairs separated by white space
    '''
    split_passports = passports.split('\n\n')
    res = []
    for p in split_passports:
        res.append(Passport(input_str=p))
    return res


def load_passports() -> List[Passport]:
    '''
    reads input file and returns parsed passports
    '''
    with open(INPUT_PATH, 'r') as f:
        content = f.read()

    return parse_passports(content)


def main():
    passports = load_passports()
    has_required_fields = 0
    valid_count = 0
    for p in passports:
        if p.has_required_attrs():
            has_required_fields += 1
        if p.valid():
            valid_count += 1
    print(f"part 1: {has_required_fields} passports have the required fields")
    print(f"part 2: {valid_count} passports are valid")


if __name__ == "__main__":
    main()
