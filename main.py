import sys
from arcList import *
from adjacencyList import *
from adjacencyMatrix import *
import dfsAlgorithm_old #implementation for adjacency list

n = 100
M = n*(n-1)/2
d1 = 0.2
m1 = int(M*d1)

arcListObject = ArcList(n, m1)
arcList = arcListObject.arcList
#print(arcList)
#arcList = [(1,2),(1,4),(2,3),(2,4),(3,9),(5,4),(7,3),(7,8),(8,9)]
#arcList = [(1,2),(2,3),(2,4),(3,4),(4,1)]

adjListObject = AdjacencyList(arcList, n)
adjList = adjListObject.adjList
#print(adjList)

adjMatrixObject = AdjacencyMatrix(arcList, n)
adjMatrix = adjMatrixObject.adjMatrix
"""for i in range(len(adjMatrix)):
    print(adjMatrix[i])"""

#Results (pre-d, post-f : contains 0)
time, vis, pre, post = dfsAlgorithm_old.runDFS(n, adjList)
verify = {"d":pre, "f":post}
#print(pre)
#print(post)

test1 = adjListObject.countBackArcs(verify)
print(test1)

test2 = adjMatrixObject.countBackArcs(verify)
print(test2)

test3 = arcListObject.countBackArcs(verify)
print(test3)
