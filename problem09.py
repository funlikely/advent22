"""
--- Day 9
"""


def main_problem_9_1(lines, debug_and_log):
    return 0


def read_input_file():
    file = open("data/problem09.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

"""


def main_problem_9_2(lines, debug_and_log):
    return 0


def main():
    input_file_lines = read_input_file()
    problem_answer = main_problem_9_1(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 9.1, number of visible trees = {problem_answer}")
    problem_answer = main_problem_9_2(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 9.2, max_scenic_score = {problem_answer}")


if __name__ == '__main__':
    main()
