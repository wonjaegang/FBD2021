import game_settings as setting
import os
import random


magic_num = setting.magic_num
max_counting = setting.max_counting
number_of_opponents = setting.number_of_players - 1
opponents_counting_min = number_of_opponents * 1
opponents_counting_max = number_of_opponents * max_counting
opponents_counting_list = list(range(opponents_counting_min, opponents_counting_max + 1))
opponents_counting_odds = []


def load_data_sheet():
    data_sheet = "%s_data_sheet.txt" % "Jaewon_algorithm"
    if not os.path.isfile(data_sheet):
        with open(data_sheet, "w+") as f:
            for _ in range(magic_num):
                for _ in range(opponents_counting_min, opponents_counting_max + 1):
                    f.write("%d " % 0)
                f.write("\n")

    with open(data_sheet, "r") as f:
        for _ in range(magic_num):
            line = f.readline()
            split_int_list = list(map(lambda x: int(x), line.split()))
            opponents_counting_odds.append(split_int_list)


memoization = {}


def calculate_win_rate(previous_num, my_counting):
    my_last_num = previous_num + my_counting

    if my_last_num in memoization:
        return memoization[my_last_num]
    elif previous_num >= magic_num:
        return 1
    elif my_last_num >= magic_num:
        return 0

    win_rate = 0
    for i, opponents_counting in enumerate(opponents_counting_list):
        next_previous_num = my_last_num + opponents_counting
        counting_range = range(max_counting)
        win_rate_by_counting = list(map(lambda x: calculate_win_rate(next_previous_num, x + 1), counting_range))
        win_rate = win_rate + max(win_rate_by_counting) * opponents_counting_odds[my_last_num - 1][i]

    memoization[my_last_num] = win_rate
    return win_rate


def adjust_data_sheet():
    pass


def random_max_index(a):
    max_value = max(a)
    max_index_list = [i for i, j in enumerate(a) if j == max_value]
    return random.choice(max_index_list)


def select_counting(previous_num):
    load_data_sheet()
    counting_range = range(max_counting)
    win_rate_by_counting = list(map(lambda x: calculate_win_rate(previous_num, x + 1), counting_range))
    print(win_rate_by_counting)
    counting = random_max_index(win_rate_by_counting) + 1
    # adjust_data_sheet()
    return counting
