"""
--- Day 7: No Space Left On Device ---

Alternate implementation. After realizing I was misusing Python Dictionaries in the previous implementation.

"""
from utility.filesystem_alt import Folder
from utility.listutility import flatten
import utility.logscratch as log


log.enable_log_info = True


def process_folder_listing(file_system, current_path, folder_listing_lines):
    for listing in folder_listing_lines:
        listing_split = listing.split(" ")
        if listing_split[0] == "dir":
            folder_name = listing_split[1]
            if folder_name not in file_system.get_list_of_sub_folders(current_path):
                file_system.sub_folder(current_path).add_sub_folder(folder_name)
        else:
            file_size, file_name = int(listing_split[0]), listing_split[1]
            if file_name not in file_system.get_list_of_file_names(current_path):
                file_system.sub_folder(current_path).add_file(file_name, file_size)


def main_problem_7_1(lines):
    file_system = Folder("root", [], None)

    current_path = []

    command_line_indices = [x for x in range(len(lines)) if lines[x][0] == "$"]

    for i in range(len(command_line_indices)):
        split_command_line = lines[command_line_indices[i]].split(" ")
        command = split_command_line[1]
        if command == "cd":
            sub_folder_name = split_command_line[2]
            if sub_folder_name == ".." and len(current_path) > 0:
                current_path.pop()
            elif sub_folder_name == "/":
                current_path = []
            else:
                if sub_folder_name not in file_system.get_list_of_sub_folders(current_path):
                    file_system.sub_folder(current_path).sub_folders().add_folder(sub_folder_name, current_path)
                current_path.append(sub_folder_name)
        elif command == "ls":
            to_index = len(lines)
            if i + 1 < len(command_line_indices):
                to_index = command_line_indices[i + 1]
            from_index = command_line_indices[i] + 1
            folder_listing_lines = lines[from_index:to_index]
            process_folder_listing(file_system, current_path, folder_listing_lines)

    z = [[1, [{'x': {'y': 'z'}}, 2, [[3], [[5, 4], 2]]]]]
    flattened_z = flatten(z)
    log.info(f"z = {z} and flattened(z) = {flattened_z}")

    folder_sizes = file_system.get_all_folder_sizes()
    folder_sizes['/'] = folder_sizes.pop('')  # quick adjustment
    log.info(folder_sizes)

    log.info(f"Number of folders = {len(folder_sizes)}")

    # folder_sizes = list(itertools.chain.from_iterable(folder_sizes))
    # log.info(folder_sizes)
    log.info("Folder sizes . . .")
    for path in folder_sizes:
        if folder_sizes[path] < 100000:
            log.info(f"100000 list - {path} : {folder_sizes[path]}")

    hundred_k_folder_size_sum = sum([folder_sizes[path] for path in folder_sizes if folder_sizes[path] <= 100000])

    return hundred_k_folder_size_sum, folder_sizes
    # 390163


def read_input_file():
    file = open("data/problem07.txt")
    lines = [line[:-1] for line in file]
    return lines


"""
--- Part Two ---
Alternate implementation.

"""


def main_problem_7_2(folder_sizes):

    log.info("max size at the end is 40,000,000")
    total_current_fs_size = folder_sizes['/']

    log.info(f"current size of all files is {total_current_fs_size}")

    size_to_delete = total_current_fs_size - 40000000
    log.info(f"look for folder of size {size_to_delete} to delete")

    best_folder_size = 1000000000

    for path in folder_sizes:
        if size_to_delete <= folder_sizes[path] < best_folder_size:
            best_folder_size = folder_sizes[path]

    return best_folder_size


def main():
    input_file_lines = read_input_file()
    problem_answer, folder_sizes = main_problem_7_1(input_file_lines)
    print(f"ANSWER TO PROBLEM 7.1, number of small directories = {problem_answer}")
    problem_answer = main_problem_7_2(folder_sizes)
    print(f"ANSWER TO PROBLEM 7.2, number of big directories = {problem_answer}")

    # Correct info from previous implementation
    # ANSWER TO PROBLEM 7.1, number of small directories = 1350966
    # ANSWER TO PROBLEM 7.2, number of big directories = 6296435
    # Number of folders = 196


if __name__ == '__main__':
    main()
