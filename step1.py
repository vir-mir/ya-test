# -*- coding: utf-8 -*-


def list_to_dict(list_key, list_val):
    result = {}
    list_key_length = len(list_key)

    for index, val in enumerate(list_val):
        if list_key_length > index:
            result[list_key[index]] = val
        else:
            result[None] = val

    return result

if __name__ == '__main__':
    print(list_to_dict(['ke1', 'ke2', 'ke3', 'ke4', 'ke5', 'ke6'], [1, 2, 3, 4, 5]))
    print(list_to_dict(['ke1', 'ke2', 'ke3', 'ke4'], [1, 2, 3, 4, 5]))
    print(list_to_dict(['ke1', 'ke2', 'ke3', 'ke4', 'st'], [1, 2, 3, 4, 5]))
