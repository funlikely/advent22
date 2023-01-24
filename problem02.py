# --- Day 2: Rock Paper Scissors ---
#
# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage,
# a giant Rock Paper Scissors tournament is already in progress.
#
# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each
# simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is
# selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same
# shape, the round instead ends in a draw.
#
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they
# say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock,
# B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
#
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for
# Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
#
# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores
# for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper,
# and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw,
# and 6 if you won).


from enum import Enum


class Weapon(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def rps_weapon_score_component(w):
    switch = {
        Weapon.ROCK: 1,
        Weapon.PAPER: 2,
        Weapon.SCISSORS: 3
    }
    return switch.get(w, -1)


def rps_result_score_component(w1, w2):
    result = 0
    if w1 == Weapon.ROCK:
        if w2 == Weapon.PAPER:
            result += 6
        elif w2 == Weapon.ROCK:
            result += 3
    elif w1 == Weapon.PAPER:
        if w2 == Weapon.SCISSORS:
            result += 6
        elif w2 == Weapon.PAPER:
            result += 3
    else:
        if w2 == Weapon.ROCK:
            result += 6
        elif w2 == Weapon.SCISSORS:
            result += 3
    return result + rps_weapon_score_component(w2)


def rpc_enum(w1, w2):
    ret_val = 0


def rock_paper_scissors(s1, s2):
    if s1 == 'A':
        if s2 == 'X':
            return 4
        elif s2 == 'Y':
            return 8
        return 3
    elif s1 == 'B':
        if s2 == 'X':
            return 1
        elif s2 == 'Y':
            return 5
        return 9
    if s2 == 'X':
        return 7
    elif s2 == 'Y':
        return 2
    return 6


def translate_data_to_weapons(weapon_data):
    weapons_pairs = []
    for i in range(len(weapon_data)):
        weapons_pairs.append(translate_datum_to_weapon_pair(weapon_data[i]))
    return weapons_pairs


def translate_datum_to_weapon_pair(datum):
    weapon_pair = []
    if datum[0] == 'A':
        weapon_pair.append(Weapon.ROCK)
    elif datum[0] == 'B':
        weapon_pair.append(Weapon.PAPER)
    else:
        weapon_pair.append(Weapon.SCISSORS)

    if datum[-1:] == 'X':
        weapon_pair.append(Weapon.ROCK)
    elif datum[-1:] == 'Y':
        weapon_pair.append(Weapon.PAPER)
    else:
        weapon_pair.append(Weapon.SCISSORS)
    return weapon_pair


def clean_data(dirty_data):
    for i in range(len(dirty_data)):
        dirty_data[i] = dirty_data[i].replace('\n', '').replace(' ', '')
    return dirty_data


def translate_datum_to_second_round_weapon_pair(datum):
    weapon_pair = []
    if datum[0] == 'A':
        weapon_pair.append(Weapon.ROCK)
        if datum[1] == 'X':
            weapon_pair.append(Weapon.SCISSORS)
        elif datum[1] == 'Y':
            weapon_pair.append(Weapon.ROCK)
        else:
            weapon_pair.append(Weapon.PAPER)
    elif datum[0] == 'B':
        weapon_pair.append(Weapon.PAPER)
        if datum[1] == 'X':
            weapon_pair.append(Weapon.ROCK)
        elif datum[1] == 'Y':
            weapon_pair.append(Weapon.PAPER)
        else:
            weapon_pair.append(Weapon.SCISSORS)
    else:
        weapon_pair.append(Weapon.SCISSORS)
        if datum[1] == 'X':
            weapon_pair.append(Weapon.PAPER)
        elif datum[1] == 'Y':
            weapon_pair.append(Weapon.SCISSORS)
        else:
            weapon_pair.append(Weapon.ROCK)
    return weapon_pair


def translate_data_to_second_round_list(data_list):
    result_list = []
    for i in range(len(data_list)):
        result_list.append(translate_datum_to_second_round_weapon_pair(data_list[i]))
    return result_list


if __name__ == '__main__':
    f = open("data/problem02.txt")
    lines = f.readlines()
    lines = clean_data(lines)
    print("first ten clean inputs --> " + str(lines[:10]))
    weapon_list = translate_data_to_weapons(lines)
    print("first ten weapons lists --> " + str(weapon_list[:10]))
    for i in range(0, 10):
        print(
            f"for game {i} between {weapon_list[i][0]} and {weapon_list[i][1]}, the score is "
            f"{rps_result_score_component(weapon_list[i][0], weapon_list[i][1])}")
    total_score = 0
    for rps_match in weapon_list:
        total_score += rps_result_score_component(rps_match[0], rps_match[1])
    print(f"total score for this series of RPS is {total_score}")

    # if X = lose, Y = draw, Z = win,
    second_round_weapon_list = translate_data_to_second_round_list(lines)
    print("Second round!!!!")
    print("first ten weapons lists --> " + str(second_round_weapon_list[:10]))
    for i in range(0, 10):
        print(
            f"for game {i} between {second_round_weapon_list[i][0]} and {second_round_weapon_list[i][1]}, the score is "
            f"{rps_result_score_component(second_round_weapon_list[i][0], second_round_weapon_list[i][1])}")
    total_score = 0
    for rps_match in second_round_weapon_list:
        total_score += rps_result_score_component(rps_match[0], rps_match[1])
    print(f"total score for this series of RPS is {total_score}")
