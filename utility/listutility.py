def flatten(size_list):
    if not isinstance(size_list, list):
        return flatten([size_list])
    if len(size_list) == 1:
        if isinstance(size_list[0], list):
            return flatten(size_list[0])
        else:
            return [size_list]
    else:
        if isinstance(size_list[0], list):
            return flatten(size_list[0]) + flatten(size_list[1:])
        else:
            return flatten([size_list[0]]) + flatten(size_list[1:])
