# Problem Three kind of business

def evaluate_item_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - 96
    elif 'A' <= item <= 'Z':
        return ord(item) - 38
    else:
        return 0
