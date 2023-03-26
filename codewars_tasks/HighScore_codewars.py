class HighScoreTable:

    def __init__(self, length):

        self.scores = list()
        self.scores_length = length

    def update(self, score):
        # FIRST_INPUT---------------
        if not self.scores:
            self.scores.append(score)
            return
        # --------------------------

        if len(self.scores) != self.scores_length:
            self.scores.append(score)
        else:
            if score > min(self.scores):
                self.scores[self.scores.index(min(self.scores))] = score

        # -----------------------------------
        self.scores.sort(reverse=True)
        # OUTPUT-----------------------------

    def reset(self):
        self.scores = []