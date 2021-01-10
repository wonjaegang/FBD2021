import random
import game_settings


def select_counting(_):
    counting = random.choice(list(range(1, 1 + game_settings.max_count)))
    return counting
