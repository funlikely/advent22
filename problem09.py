"""
--- Day 9: Rope Bridge ---

This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river
far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics;
maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far
enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a
two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head,
you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must
always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...

If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in
that direction so it remains close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...

Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step
diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....

You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail
both start at the same position, overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

This series of motions moves the head right four steps, then up four steps, then left three steps, then down one
step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no
longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference
point):

== REMOVED FOR SPACE AND SANITY ==

After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram,
s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..

So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

"""


def main_problem_9_1(lines, debug_and_log):
    head = (0, 0)
    tail = (0, 0)
    traveled_set = {(0, 0)}

    rope_step_dict = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    for i in range(len(lines)):
        direction_to_move, number_of_steps = lines[i].split(' ')
        number_of_steps = int(number_of_steps)
        for j in range(number_of_steps):
            rope_step = rope_step_dict[direction_to_move]
            head = add_tuple(head, rope_step)
            if head[0] - tail[0] > 1:
                tail = add_tuple(head, (-1, 0))
            elif head[0] - tail[0] < -1:
                tail = add_tuple(head, (1, 0))
            elif head[1] - tail[1] > 1:
                tail = add_tuple(head, (0, -1))
            elif head[1] - tail[1] < -1:
                tail = add_tuple(head, (0, 1))
            traveled_set.add(tail)

    return len(traveled_set)


def add_tuple(a, b):
    return tuple(map(lambda i, j: i + j, a, b))


def read_input_file():
    file = open("data/problem09.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of 
the ropes that broke are now whipping toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being 
hit. Fortunately, your simulation can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope 
and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using 
the same rules as before.

Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now 
occur as follows:

-- excluded --

Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, 
and so it only visits 1 position. However, be careful: more types of motion are possible than before, so you might 
want to visually compare your simulated rope to the one above.

Here's a larger example:

-- excluded --

Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the 
rope visit at least once?

"""


def main_problem_9_2(lines, debug_and_log):
    head = (0, 0)
    tail = (0, 0)
    rope = [(0, 0)] * 10  # rope[0] = head, rope[9] = last knot
    traveled_set = {(0, 0)}
    traveled_list = [(0, 0)]

    rope_step_dict = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    for i in range(len(lines)):
        direction_to_move, number_of_steps = lines[i].split(' ')
        number_of_steps = int(number_of_steps)
        for j in range(number_of_steps):
            rope_step = rope_step_dict[direction_to_move]
            rope[0] = add_tuple(rope[0], rope_step)
            for k in range(9):
                if rope[k][0] - rope[k+1][0] > 1:
                    rope[k+1] = add_tuple(rope[k+1], (1, 0))
                elif rope[k][0] - rope[k+1][0] < -1:
                    rope[k+1] = add_tuple(rope[k+1], (-1, 0))
                if rope[k][1] - rope[k+1][1] > 1:
                    rope[k+1] = add_tuple(rope[k+1], (0, 1))
                elif rope[k][1] - rope[k+1][1] < -1:
                    rope[k+1] = add_tuple(rope[k+1], (0, -1))
            traveled_set.add(rope[9])
            if rope[9] not in traveled_list:
                if debug_and_log:
                    print(f"len of traveled_list = {len(traveled_list)}")
                    print(f"traveled_list = {traveled_list} and rope[9] = {rope[9]}")
                traveled_list.append(rope[9])

    return len(traveled_list)


def main():
    input_file_lines = read_input_file()
    problem_answer = main_problem_9_1(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 9.1, count of rope tail locations = {problem_answer}")
    problem_answer = main_problem_9_2(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 9.2, count of longer rope tail locations = {problem_answer}")

    # ANSWER TO PROBLEM 9.1, count of rope tail locations = 6044
    # ANSWER TO PROBLEM 9.2, count of longer rope tail locations = 2384


if __name__ == '__main__':
    main()
