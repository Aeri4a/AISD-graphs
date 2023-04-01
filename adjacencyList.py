
class AdjacencyList:
    def __init__(self, arcList, n):
        #Build structure
        self.adjList = {key+1: [] for key in range(n)}
        for key, value in arcList:
            self.adjList[key].append(value)

    def countBackArcs(self, verify):
        #(u,v)
        count = 0
        for u in range(1, len(self.adjList)+1):
            for v in self.adjList[u]:
                if u in self.adjList[v] and (verify["d"][v] < verify["d"][u] < verify["f"][u] < verify["f"][v]):
                    count += 1
        return count