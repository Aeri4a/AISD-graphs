import random

class ArcList:
    def __init__(self, n, m1):
        self.test = "test"
        self.arcList = set()
        while len(self.arcList) < m1:
            x = random.randint(1, n)
            y = random.randint(1, n)

            self.arcList.add((x,y))

        self.arcList = list(self.arcList)