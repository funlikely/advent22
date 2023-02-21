def read_tops_of_crates(crates):
    """Read the last part of each of a set of crates,
       and returns a string of them in sequence. E.g., [['a', 'b'], ['c'], ['d', 'e', 'f']] becomes 'bcf'."""
    tops_of_crates = [crate[-1:][0] for crate in crates]

    return ''.join(tops_of_crates)


def move_crate(crates, from_stack, to_stack):
    """Note: stacks start with index 0."""
    crate = crates[from_stack].pop()
    crates[to_stack].append(crate)

    return crates


def move_crates(crates, from_stack, to_stack, crate_quantity):
    """Note: stacks start with index 0."""
    for i in range(crate_quantity):
        crates = move_crate(crates, from_stack, to_stack)

    return crates


def move_stacks_of_crates(crates, from_stack, to_stack, crate_quantity):
    """Note: stacks start with index 0."""
    crates_to_move = crates[from_stack][-crate_quantity:]
    crates[from_stack] = crates[from_stack][:-crate_quantity]
    crates[to_stack] = crates[to_stack] + crates_to_move

    return crates
