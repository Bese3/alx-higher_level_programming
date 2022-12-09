#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    keys = []
    values = []

    for key, value in zip(a_dictionary.keys(), a_dictionary.values()):
        keys.append(key)
        values.append(value)

    highest_score_index = 0
    for i in range(len(values)):
        if values[highest_score_index] < values[i]:
            highest_score_index = i

    return list(a_dictionary.keys())[highest_score_index]
