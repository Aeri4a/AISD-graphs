
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
                if self.adjMatrix[v][u] == 1 and self.adjMatrix[u][v] == 1 and (verify["d"][v] < verify["d"][u] < verify["f"][u] < verify["f"][v]):
                    print(u,v)
                    count += 1
        return count