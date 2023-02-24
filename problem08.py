"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

"""
import numpy as np


def main_problem_8_1(lines, debug_and_log):

    forest_array = np.array([[int(a) for a in line] for line in lines])
    (forest_height, forest_width) = forest_array.shape

    visibility_array = np.array([[True] * forest_width] * forest_height)

    if debug_and_log:
        print(f"part of the forest:")
        print(forest_array[:15, :15])
        print(f"dimensions of forest = {forest_array.shape}")
        print(f"dimensions of visibility array = {visibility_array.shape}")

    return 0


def read_input_file():
    file = open("data/problem08.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

"""


def main_problem_8_2(folder_sizes, debug_and_log):

    return 0


def main():
    input_file_lines = read_input_file()
    problem_answer = main_problem_8_1(input_file_lines, True)
    print(f"ANSWER TO PROBLEM 8.1, number of visible trees = {problem_answer}")
    problem_answer = main_problem_8_2(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 8.2, number of invisible trees? = {problem_answer}")


if __name__ == '__main__':
    main()
