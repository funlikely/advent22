"""
--- Day 10: Cathode-Ray Tube ---

You avoid the ropes, plunge into the river, and swim to shore.

The Elves yell something about meeting back up with them upriver, but the river is too loud to tell exactly what they're saying. They finish crossing the bridge and disappear from view.

Situations like this must be why the Elves prioritized getting the communication system on your handheld device working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen tells you it probably won't be of much immediate use.

Unless, that is, you can design a replacement for the device's video system! It seems to be some kind of cathode-ray tube screen and simple CPU that are both driven by a precise clock circuit. The clock circuit ticks at a constant rate; each tick is called a cycle.

Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

    addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    noop takes one cycle to complete. It has no other effect.

The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.

Consider the following small program:

noop
addx 3
addx -5

Execution of this program proceeds as follows:

    At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. After the first cycle, the noop instruction finishes execution, doing nothing.
    At the start of the second cycle, the addx 3 instruction begins execution. During the second cycle, X is still 1.
    During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes execution, setting X to 4.
    At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth cycle, X is still 4.
    During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes execution, setting X to -1.

Maybe you can learn something by looking at the value of the X register throughout execution. For now, consider the signal strength (the cycle number multiplied by the value of the X register) during the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

For example, consider this larger program:

-- excluded --

The interesting signal strengths can be determined as follows:

    During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420. (The 20th cycle occurs in the middle of the second addx -1, so the value of register X is the starting value, 1, plus all of the other addx values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
    During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.
    During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.
    During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.
    During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.
    During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.

The sum of these signal strengths is 13140.

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
"""


def main_problem_10_1(lines, debug_and_log):
    cycle = 1
    x = 1
    add_amount = 0
    cycles_to_wait = 0
    strengths_of_concern = []
    command = "xxxx"

    while len(lines) > 0:
        # take a command off the queue if we are not waiting for another command
        if cycles_to_wait == 0:
            command = lines[0]
            lines = lines[1:]

            # process the command
            if command[0:4] == 'noop':
                cycles_to_wait = 1
            elif command[0:3] == 'add':
                cycles_to_wait = 2
                add_amount = int(command.split(' ')[1])

        # check strengths during the cycle
        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths_of_concern.append(x * cycle)

        # END of cycle, which is when register X updates and then cycle number increments
        if cycles_to_wait == 0 and add_amount != 0:
            x += add_amount
            add_amount = 0
        cycle = cycle + 1
        if cycles_to_wait > 0:
            cycles_to_wait = cycles_to_wait - 1

    return sum(strengths_of_concern)


def run_a_cycle(cycle, strengths_of_concern, x):
    cycle = cycle + 1


def add_tuple(a, b):
    return tuple(map(lambda i, j: i + j, a, b))


def read_input_file():
    file = open("data/problem10.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---

"""


def main_problem_10_2(lines, debug_and_log):
    return 0


def main():
    input_file_lines = read_input_file()
    problem_answer = main_problem_10_1(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 10.1, sum of signal strengths = {problem_answer}")
    problem_answer = main_problem_10_2(input_file_lines, False)
    print(f"ANSWER TO PROBLEM 10.2, what's going on ? = {problem_answer}")


if __name__ == '__main__':
    main()
