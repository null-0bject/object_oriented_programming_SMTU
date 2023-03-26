
# просто задачка с codewars 4 kyu. 26 марта 2023

class User:
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    # null.object
    def __init__(self):

        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):

        difference_between_ranks = (self.ranks.index(self.rank)) - self.ranks.index(rank)

        if difference_between_ranks == 0:

            if self.rank == 8:
                self.progress = 0
            else:
                self.progress += 3

        elif difference_between_ranks == 1:
            if self.rank == 8:
                self.progress = 0
            else:
                self.progress += 1

        elif difference_between_ranks >= 2:
            pass

        else:
            self.progress += 10 * (difference_between_ranks ** 2)

        while self.progress >= 100:
            self.progress -= 100
            if self.rank == -1:
                self.rank += 2
            else:
                self.rank += 1
                if self.rank == 8:
                    self.progress = 0



