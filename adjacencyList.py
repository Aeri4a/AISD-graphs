
class AdjacencyList:
    def __init__(self, arcList, n):
        #Build structure
        self.adjList = {key+1: [] for key in range(n)}
        for key, value in arcList:
            self.adjList[key].append(value)

