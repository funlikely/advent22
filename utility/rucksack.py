"""
    Problem Three kind of business
"""


def evaluate_item_priority(item):
    """ converts an item (represented by a char) into its numeric priority value """
    if 'a' <= item <= 'z':
        return ord(item) - 96
    elif 'A' <= item <= 'Z':
        return ord(item) - 38
    else:
        return 0


def string_intersection(input1, input2):
    """ returns a set of characters in common between input1 and input2 """
    return set(input1).intersection(input2)


def split_pack(pack):
    if len(pack) % 2 != 0:
        return []
    else:
        cut = len(pack) / 2 + 1
        return [pack[: cut], pack[cut:]]
