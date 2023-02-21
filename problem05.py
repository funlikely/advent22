"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in
stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be
rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or
fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which
crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle
input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N
is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains
a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one
stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2
to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first
crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up
below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in
stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

"""
from utility.crate import read_tops_of_crates, move_crates, move_stacks_of_crates


def get_initial_crates_config(lines):
    """
        [F]         [L]     [M]
        [T]     [H] [V] [G] [V]
        [N]     [T] [D] [R] [N]     [D]
        [Z]     [B] [C] [P] [B] [R] [Z]
        [M]     [J] [N] [M] [F] [M] [V] [H]
        [G] [J] [L] [J] [S] [C] [G] [M] [F]
        [H] [W] [V] [P] [W] [H] [H] [N] [N]
        [J] [V] [G] [B] [F] [G] [D] [H] [G]
         1   2   3   4   5   6   7   8   9
     """
    initial_crates = []
    for i in range(9):
        stack_i = [line[1 + 4 * i] for line in lines[:8] if line[1 + 4 * i] != ' '][::-1]
        initial_crates.append(stack_i)

    print(initial_crates)
    """[['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'], ['V', 'W', 'J'], ['G', 'V', 'L', 'J', 'B', 'T', 'H'], ['B', 'P', 
    'J', 'N', 'C', 'D', 'V', 'L'], ['F', 'W', 'S', 'M', 'P', 'R', 'G'], ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'], 
    ['D', 'H', 'G', 'M', 'R'], ['H', 'N', 'M', 'V', 'Z', 'D'], ['G', 'N', 'F', 'H']] """

    return initial_crates


def main_problem_5_1(lines, debug_and_log):

    crates = get_initial_crates_config(lines)

    for i in range(10, len(lines)):
        move_command = lines[i].split(" ")
        from_stack, to_stack, quantity = map(int, [move_command[3], move_command[5], move_command[1]])
        crates = move_crates(crates, from_stack - 1, to_stack - 1, quantity)  # need to adjust for 0 based lists
        if debug_and_log and i < 20:
            print(f"{lines[i]} - {crates}")
    
    crate_string = read_tops_of_crates(crates)

    return crate_string


def read_input_file():
    file = open("data/problem05.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a 
CrateMover 9000 - it's a CrateMover 9001. 

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup 
holder, and the ability to pick up and move multiple crates at once. 

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the 
same order, resulting in this new configuration: 

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to 
be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each 
stack? 

"""


def main_problem_5_2(lines, debug_and_log):
    crates = get_initial_crates_config(lines)

    for i in range(10, len(lines)):
        move_command = lines[i].split(" ")
        from_stack, to_stack, quantity = map(int, [move_command[3], move_command[5], move_command[1]])
        crates = move_stacks_of_crates(crates, from_stack - 1, to_stack - 1, quantity)  # need to adjust for 0 based
        # lists
        if debug_and_log and i < 20:
            print(f"{lines[i]} - {crates}")

    crate_string = read_tops_of_crates(crates)

    return crate_string


if __name__ == '__main__':
    input_file_lines = read_input_file()

    problem_answer = main_problem_5_1(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 5.1, series of crates = {problem_answer}")
    problem_answer = main_problem_5_2(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 5.2, series of crates = {problem_answer}")
