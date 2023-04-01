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
    
    def countBackArcs(self, verify):
        #(u,v)
        count = 0
        for u, v in self.arcList:
            for a, b in self.arcList:
                if u == b and v == a and (verify["d"][v] < verify["d"][u] < verify["f"][u] < verify["f"][v]):
                    count += 1
        return count
