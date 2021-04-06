
class Highscore:

    def __init__(self):
        self.highscore_path = "highscores.txt"
        self.to_show = 10
        self.high_scores = []
        self.current = 0
        self.rows = 0
        try:
            with open(self.highscore_path) as f:
                self.rows = sum(1 for _ in f)
        except Exception:
            with open(self.highscore_path, 'w') as f:
                f.write('')
            self.rows = 0

    def insert(self, name, score):
        if name == "":
            name = "PLAYER"
        self.high_scores = []
        with open(self.highscore_path) as f:
            self.rows = sum(1 for _ in f)
        with open(self.highscore_path, 'r') as f:
            for i in range(self.rows):
                tmp = f.readline().replace('\n', '')
                tmp = tmp.split()
                self.high_scores.append([tmp[0], int(tmp[2])])
            self.high_scores.append([name, int(score)])
            self.rows += 1
            if self.rows > 10:
                self.rows = 10
        n = 1
        while n < len(self.high_scores):
            for i in range(len(self.high_scores) - n):
                if self.high_scores[i][1] < self.high_scores[i + 1][1]:
                    self.high_scores[i], self.high_scores[i + 1] = self.high_scores[i + 1], self.high_scores[i]
            n += 1
        self.high_scores = self.high_scores[:10]
        with open(self.highscore_path, 'w') as f:
            for i in self.high_scores:
                f.write(i[0] + ' : ' + str(i[1]) + '\n')
