# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # read calories file
    # count up calories during, and track max
    f = open("data/problem01.txt", "r")
    lines = f.readlines()
    print(lines)
    print(f'length of data = {len(lines)} lines')

    maxCalories = 0
    currentCalories = 0
    maxList = []
    for i in range(len(lines)):
        if lines[i] == '\n' or i == (len(lines) - 1):
            maxList.append(currentCalories)
            print(f'Line {i}, current max calories = {currentCalories}')
            currentCalories = 0
        else:
            currentCalories += int(lines[i])

    print(f'the list of maximum calorie counts: {maxList}')
    maxList.sort()
    print(f'the sorted list of maximum calorie counts: {maxList}')
    print(f'three biggest counts: {maxList[len(maxList)-3:]}')
    print(f'sum of three biggest counts: {sum(maxList[len(maxList)-3:])}')


