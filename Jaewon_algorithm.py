import game_settings as setting
import os
import random


player_name = "Jaewon"

magic_num = setting.magic_num
max_counting = setting.max_counting
counting_range = range(1, max_counting + 1)

new_game = True

opponents_in_order = []
opponents_counting_data = {}
game_data = [] # Hmmmmmmmmmmmmmm
memoization = {}


def load_opponents_data():
    with open("current_game_data.txt", "r") as f:
        players = f.readline().split()
        for _ in players:
            last_player = players.pop()
            if last_player == player_name:
                opponents_in_order.extend(players)
                break
            else:
                players.insert(0, last_player)


def initialize_data_sheet(opponent):
    with open("DataSheet - %s.txt" % opponent, "w+") as f:
        for _ in range(magic_num):
            for _ in counting_range:
                f.write("%d " % 1)
            f.write("\n")


def read_from_date_sheet(opponent):
    with open("DataSheet - %s.txt" % opponent, "r") as f:
        opponents_counting_data[opponent] = []
        for _ in range(magic_num):
            line = f.readline()
            split_int_list = list(map(lambda x: int(x), line.split()))
            opponents_counting_data[opponent].append(split_int_list)


def load_data_sheet():
    load_opponents_data()
    for opponent in opponents_in_order:
        if not os.path.isfile("DataSheet - %s.txt" % opponent):
            initialize_data_sheet(opponent)
        read_from_date_sheet(opponent)

    global new_game
    new_game = False

# loading data part : revising completed.


def calculate_win_rate(previous_num, my_counting):
    my_last_num = previous_num + my_counting

    if my_last_num in memoization:
        return memoization[my_last_num]
    elif previous_num >= magic_num:
        return 1
    elif my_last_num >= magic_num:
        return 0

    win_rate = 0

    # Should be simplified -> "generalize"
    for count1 in counting_range:
        for count2 in counting_range:
            next_previous_num = my_last_num + count1 + count2
            if next_previous_num >= magic_num:
                next_previous_num = magic_num
            win_rate_by_counting = list(map(lambda x: calculate_win_rate(next_previous_num, x), counting_range))

            oppo1_counting_data = opponents_counting_data[opponents_in_order[0]][my_last_num]
            odds = oppo1_counting_data[count1 - 1] / sum(oppo1_counting_data)
            if my_last_num + count1 < magic_num:
                oppo2_counting_data = opponents_counting_data[opponents_in_order[1]][my_last_num + count1]
                odds *= oppo2_counting_data[count2 - 1] / sum(oppo2_counting_data)

            final_odds = odds
            win_rate += max(win_rate_by_counting) * final_odds

    memoization[my_last_num] = win_rate
    return win_rate


def random_max_index(a):
    max_value = max(a)
    max_index_list = [i for i, j in enumerate(a) if j == max_value]
    return random.choice(max_index_list)


def flush_last_game_data():
    opponents_in_order.clear()
    memoization.clear()
    game_data.clear()
    opponents_counting_data.clear()


def select_counting(previous_num):
#    if previous_num == 29:
#        return 1
#    elif previous_num == 28:
#        return 2
#    elif previous_num == 27:
#        return 3
    if new_game:
        load_data_sheet()
    win_rate_by_counting = list(map(lambda x: calculate_win_rate(previous_num, x + 1), counting_range))
    counting = random_max_index(win_rate_by_counting) + 1
    print(win_rate_by_counting)
    return counting


def load_current_game_result():
    with open("current_game_data.txt", "r") as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            split_line = line.split(': ')
            name = split_line[0]
            if not name == player_name:
                opponent_nums = split_line[1].split()
                opponent_previous_num = int(opponent_nums[0]) - 1
                opponent_counting = int(opponent_nums.pop()) - opponent_previous_num
                opponents_counting_data[name][opponent_previous_num][opponent_counting - 1] += 1


def adjust_data_sheet():
    load_current_game_result()
    for opponent in opponents_in_order:
        with open("DataSheet - %s.txt" % opponent, "w") as f:
            for i in range(magic_num):
                for j in counting_range:
                    f.write("%d " % opponents_counting_data[opponent][i][j - 1])
                f.write("\n")
    flush_last_game_data()
    global new_game
    new_game = True

