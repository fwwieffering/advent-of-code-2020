#!/usr/bin/env python3

# helper functions in this file

def get_input(path: str):
    res = []
    with open(path, "r") as f:
        for line in f:
            res.append(line.strip())
    return res