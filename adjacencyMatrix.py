
class AdjacencyMatrix:
    def __init__(self, arcList, n):
        #Build structure
        self.adjMatrix = [[0 for i in range(n)] for i in range(n)]
        for i in range(len(arcList)):
            u, v = arcList[i]
            self.adjMatrix[u-1][v-1] = 1

    def countBackArcs(self, verify):
        #(u,v)
        count = 0
        for u in range(len(self.adjMatrix)):
            for v in range(len(self.adjMatrix)):
                if self.adjMatrix[u][v] == 1 and not (verify["d"][v+1] < verify["d"][u+1] < verify["f"][u+1] < verify["f"][v+1]):
                    count += 1
        return count