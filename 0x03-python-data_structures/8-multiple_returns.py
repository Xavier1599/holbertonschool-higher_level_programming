#!/usr/bin/python3
from ast import Return


def multiple_returns(sentence):
    cnt = len(sentence)
    if cnt == 0:
        first = None
        return cnt, first
    else:
        first = sentence[0]
        return cnt, first
