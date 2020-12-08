import pytest

from advent.exercises import eight


def test_init_program():
    instructions = [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
    ]

    p = eight.Program(instructions, debug=True)
    res = p.run()
    assert res == 5