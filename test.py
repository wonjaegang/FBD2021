class Player:
    def __init__(self, name):
        self.name = name
        self.previous_num = 0
        self.last_num = 0
        self.last_nums = []
        self.data_sheet = data_sheet = "%s_data_sheet_test.txt" % self.name

        self.victory = True
        self.odds_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.total_rounds = 0
        self.total_victory = 0
        self.total_odds = None

    def write_test_data(self):
        with open(self.data_sheet, "w+") as f:
            f.write("Total rounds : %d\n" % self.total_rounds)
            f.write("Total victory : %d\n" % self.total_victory)
            f.write("Total odds : %s\n" % str(self.total_odds))
            for i, odds in enumerate(self.odds_list):
                f.write("%d : [selected : %d, victory : %d, odds : %f]\n"
                        % (i+1, self.total_rounds, self.total_victory, odds))

    def write_test_data2(self):
        with open(self.data_sheet, "r") as f:
            k = f.read()
        with open(self.data_sheet, "w") as f:
            f.write(k)
            for i, j in enumerate(k):
                if j == ":":
                    f.seek(i)
                    f.write("d")


if __name__ == "__main__":
    P1 = Player("Jaewon")
    P1.write_test_data()


# Total rounds : 0
# Total victory : 0
# Total odds : None
# 001 : [selected: 24, victory: 13, odds : 0.669629]
