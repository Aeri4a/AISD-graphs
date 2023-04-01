import sys
from arcList import *
from adjacencyList import *
from adjacencyMatrix import *
import dfsAlgorithm #implementation for adjacency list

#Technical
sys.setrecursionlimit(100000)

n = 6000
M = n*(n-1)/2
d1 = 0.2
m1 = int(M*d1)

arcListObject = ArcList(n, m1)
arcList = arcListObject.arcList
print(len(arcList))

adjacencyListObject = AdjacencyList(arcList, n)
adjacencyList = adjacencyListObject.adjList
#print(adjacencyList)

adjacencyMatrixObject = AdjacencyMatrix(arcList, n)
adjacencyMatrix = adjacencyMatrixObject.matrix
#print(adjacencyMatrix)

#Results (pre-d, post-f : contains 0)
time, vis, pre, post = dfsAlgorithm.runDFS(n, adjacencyList)
print("Pre", len(pre))
print("Post", len(post))
print("test")