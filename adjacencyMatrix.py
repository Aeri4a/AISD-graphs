
class AdjacencyMatrix:
    def __init__(self, arcList, n):
        self.matrix = [[0 for i in range(n)] for i in range(n)]
        for i in range(len(arcList)):
            x, y = arcList[i]
            self.matrix[x-1][y-1] = 1