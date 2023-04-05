import random

class ArcList:
    def __init__(self, n, m1):
        #Generate structure
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
                if not (verify["d"][v] < verify["d"][u] < verify["f"][u] < verify["f"][v]): # z not sprawdza acyklicznosc, bez not cyklicznosc
                    count += 1
        return count
