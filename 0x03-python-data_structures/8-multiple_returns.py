#!/usr/bin/python3
def multiple_returns(sentence):
    cnt = len(sentence)
    if cnt == 0:
        first = None
        return cnt, first
    else:
        first = sentence[0]
        return cnt, first
