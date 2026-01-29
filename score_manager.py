import time
from constant import MAX_STRIKES, COMBO_TIME_WINDOW


class ScoreManager:
    def __init__(self):
        self.score = 0        # current score
        self.strikes = 0      # number of strikes
        self.last_hits = []   # times when fruits were hit

    def add_point(self):
        # add 1 point
        self.score += 1

    def add_combo(self, nb_fruits):
        # combo bonus = fruits - 1
        bonus = nb_fruits - 1
        self.score += bonus

    def add_strike(self):
        # add one strike
        self.strikes += 1

    def check_combo(self, fruits_hit, time_window):
        # get current time
        current_time = time.time()

        # keep only hits inside the time window
        fruits_hit = [
            t for t in fruits_hit
            if current_time - t <= time_window
        ]

        # return number of fruits in the combo
        return len(fruits_hit)

    def register_hit(self):
        # save hit time
        self.last_hits.append(time.time())

    def get_score(self):
        # return score
        return self.score

    def is_game_over(self):
        # game over if too many strikes
        return self.strikes >= MAX_STRIKES