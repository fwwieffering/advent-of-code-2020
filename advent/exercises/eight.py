import os.path
import re
from typing import List
from copy import deepcopy

from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/eight'


class Program(object):

    COMMAND_REGEX = re.compile(r'^(?P<command>\w*) (?P<value>[-+]\d*)$')

    def __init__(self, instructions: List[str], debug=False):
        self.instructions = instructions
        self.compiled_instructions = self._compile_instructions(instructions)
        self.reset()
        self.debug = debug

    def _compile_instructions(self, instructions: List[str]):
        """converts list of command instructions to functions to execute
        this makes it so instructions are only parsed once even if they are run twice

        Args:
            instructions (List[str]): [description]

        Raises:
            ValueError: [description]
            ValueError: [description]
        """
        res = []

        for i in instructions:
            match = self.COMMAND_REGEX.match(i)
            if not match:
                raise ValueError(f"unexpected command input: {i}")
            command = match.group('command')
            val = int(match.group('value'))
            # i wish python had a switch statement
            if command == "acc":
                res.append((self._acc, val))
            elif command == "nop":
                res.append((self._nop, val))
            elif command == "jmp":
                res.append((self._jmp, val))
            else:
                raise ValueError(f"unknown command {command}")
        return res

    def reset(self):
        '''
        resets state between program runs
        '''
        self.instruction_ptr = 0
        self.instruction_history = []
        self.instruction_count = {}
        self.accumulator = 0

    def _log_instruction(self, cmd, val):
        self.instruction_history.append((cmd, val))
        if self.instruction_count.get(self.instruction_ptr):
            self.instruction_count[self.instruction_ptr] += 1
        else:
            self.instruction_count[self.instruction_ptr] = 1

    def _acc(self, val):
        '''
        executes the command at the current instruction_ptr
        modifies the instruction_ptr as needed
        '''
        if self.debug:
            print(f"{self.instruction_ptr} acc {val}")
        self.accumulator += val
        self._log_instruction("acc", val)
        self.instruction_ptr += 1

    def _nop(self, val):
        '''
        does nothing, passes to next instruction
        '''
        if self.debug:
            print(f"{self.instruction_ptr} nop {val}")
        self._log_instruction("nop", val)
        self.instruction_ptr += 1

    def _jmp(self, val):
        if self.debug:
            print(f"{self.instruction_ptr} jmp {val}")
        self._log_instruction("jmp", val)
        self.instruction_ptr += val

    def run(self):
        while True:
            current_instruction_count = self.instruction_count.get(self.instruction_ptr, 0)
            if current_instruction_count > 0:
                if self.debug:
                    print(f"{self.instruction_ptr} would be run twice. accumulator: {self.accumulator}")
                return self.accumulator
            if self.instruction_ptr >= len(self.compiled_instructions):
                if self.debug:
                    print(f"exited successfully")
                return self.accumulator
            cmd, val = self.compiled_instructions[self.instruction_ptr]
            cmd(val)


def main():
    instructions = get_input(INPUT_PATH)
    p = Program(instructions)

    part_1 = p.run()
    print(f"Part 1: value in the accumulator prior to any command being run twice: {part_1}")

    part2_instructions = instructions.copy()
    part2_instructions[265] = "nop -174" # I just guessed. it was a big negative jump near the end
    p2_prog = Program(part2_instructions)
    part_2 = p2_prog.run()
    print(f"Part 2: value in accumulator after program terminates successfully: {part_2}")


if __name__ == "__main__":
    main()