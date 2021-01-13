import game_settings as setting
import os
import random


magic_num = setting.magic_num
max_counting = setting.max_counting
my_counting_range = range(max_counting)
number_of_opponents = setting.number_of_players - 1
opponents_counting_min = number_of_opponents * 1
opponents_counting_max = number_of_opponents * max_counting
opponents_counting_range = range(opponents_counting_min, opponents_counting_max + 1)

opponents_counting_data = []
game_data = []
memoization = {}

data_sheet = "%s_data_sheet.txt" % "Jaewon_algorithm"


def load_data_sheet():
    if not os.path.isfile(data_sheet):
        with open(data_sheet, "w+") as f:
            for _ in range(magic_num):
                for _ in opponents_counting_range:
                    f.write("%d " % 1)
                f.write("\n")

    with open(data_sheet, "r") as f:
        for _ in range(magic_num):
            line = f.readline()
            split_int_list = list(map(lambda x: int(x), line.split()))
            opponents_counting_data.append(split_int_list)


def calculate_win_rate(previous_num, my_counting):
    my_last_num = previous_num + my_counting

    if my_last_num in memoization:
        return memoization[my_last_num]
    elif previous_num >= magic_num:
        return 1
    elif my_last_num >= magic_num:
        return 0

    win_rate = 0
    for i, opponents_counting in enumerate(opponents_counting_range):
        next_previous_num = my_last_num + opponents_counting
        win_rate_by_counting = list(map(lambda x: calculate_win_rate(next_previous_num, x + 1), my_counting_range))
        odds = opponents_counting_data[my_last_num - 1][i] / sum(opponents_counting_data[my_last_num - 1])
        win_rate = win_rate + max(win_rate_by_counting) * odds

    memoization[my_last_num] = win_rate
    return win_rate


def adjust_data_sheet(my_numbers):
    for i in range(len(my_numbers) - 1):
        opponents_counting = my_numbers[i + 1][0] - my_numbers[i][1]
        temp = opponents_counting_data[my_numbers[i][1] - 1][opponents_counting - opponents_counting_min]
        opponents_counting_data[my_numbers[i][1] - 1][opponents_counting - opponents_counting_min] = temp + 1

    with open(data_sheet, "w") as f:
        for i in range(magic_num):
            for j in opponents_counting_range:
                f.write("%d " % opponents_counting_data[i][j - opponents_counting_min])
            f.write("\n")


def random_max_index(a):
    max_value = max(a)
    max_index_list = [i for i, j in enumerate(a) if j == max_value]
    return random.choice(max_index_list)


def flush_previous_data():
    opponents_counting_data.clear()
    game_data.clear()
    memoization.clear()


def select_counting(previous_num):
    flush_previous_data()
    load_data_sheet()
    win_rate_by_counting = list(map(lambda x: calculate_win_rate(previous_num, x + 1), my_counting_range))
    print(win_rate_by_counting)
    print(memoization)
    counting = random_max_index(win_rate_by_counting) + 1
    return counting
