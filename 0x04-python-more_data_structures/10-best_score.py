#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bestval = 0
    bestkey = None
    for c, v in a_dictionary.items():
        if v > bestval:
            bestval = v
            bestkey = c
            return bestkey
