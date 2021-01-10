import game_settings


def select_counting(previous_num):
    print("Choose your counting, from 1 to %d" % game_settings.max_counting)
    counting = int(input())
    return counting
