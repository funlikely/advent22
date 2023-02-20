"""
--- Day 4: Camp Cleanup ---

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been
assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned
a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the
assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big
list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

For the first few pairs, this list means:

    Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second
    Elf was assigned sections 6-8 (sections 6, 7, 8). The Elves in the second pair were each assigned two sections.
    The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also
    got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger
numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully
contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in
the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most
in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

"""


def main_problem_four_one(lines):

    redundant_count = 0

    for line in lines:
        ab, cd = line.split(",")
        a, b = map(int, ab.split("-"))
        c, d = map(int, cd.split("-"))

        if redundancy_exists(a, b, c, d):
            redundant_count += 1
            if redundant_count % 10 == 1:
                print(f"found redundancy number {redundant_count}: {a}-{b} {c}-{d}")

    return redundant_count


def read_input_file():
    file = open("data/problem04.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number 
of pairs that overlap at all. 

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,
7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap: 

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""


def main_problem_four_two(lines, log_and_debug):

    intersect_count = 0

    for line in lines:
        ab, cd = line.split(",")
        a, b = map(int, ab.split("-"))
        c, d = map(int, cd.split("-"))

        if intersect_count < 80 and log_and_debug:
            print(f"{a}-{b} {c}-{d}, intersect? {intersection_exists(a, b, c, d)}")

        if intersection_exists(a, b, c, d):
            intersect_count += 1
            if intersect_count % 10 == 1 and log_and_debug and False:
                print(f"found intersect number {intersect_count}: {a}-{b} {c}-{d}")

    return intersect_count


def redundancy_exists(a, b, c, d):
    """ Detects redundancy between two intervals (a,b) and (c,d). """
    return [a, c, d, b] == sorted([a, b, c, d]) or [c, a, b, d] == sorted([a, b, c, d])


def intersection_exists(a, b, c, d):
    """ Detects intersection between two intervals (a,b) and (c,d). """
    # intersect --> not distinct
    #           --> (a,b) is entirely before or after (c,d)
    #           --> ([a, b, c, d] is sorted OR [c, d, a, b] is sorted]) AND (b != c) AND (a != d)
    return not (([a, b, c, d] == sorted([a, b, c, d]) or [c, d, a, b] == sorted([a, b, c, d])) and b != c and a != d)


if __name__ == '__main__':
    input_file_lines = read_input_file()

    problem_answer = main_problem_four_one(input_file_lines)
    print(f"ANSWER TO PROBLEM 4.1, total number of redundant assignments = {problem_answer}")
    problem_answer = main_problem_four_two(input_file_lines, True)
    print(f"ANSWER TO PROBLEM 3.2, total number of intersecting assignments = {problem_answer}")


