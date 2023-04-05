import sys, time, json, xlsxwriter
from arcList import *
from adjacencyList import *
from adjacencyMatrix import *
import dfsAlgorithm  #implementation for adjacency list

# -- DATA PART --
# -- GENERATE RANGES --
startNumber = 1000
n = 10
step = 1000
dataRange = [
  x for x in range(startNumber, startNumber + (n - 1) * step + 1, step)
]

# -- TEMPLATES --
# - Topological Sort Time
tempTimeTS = [{
  "name": "elements",
  "data": []
}, {
  "name": "timeTSd02",
  "data": []
}, {
  "name": "timeTSd04",
  "data": []
}]

# - Count Back Arcs
tempArcs = [{
  "name": "elements",
  "data": []
}, {
  "name": "arcsNumberD02",
  "data": []
}, {
  "name": "arcsNumberD04",
  "data": []
}]

# - Count Back Arcs Time for all structures
tempTimeArcsD02 = [{
  "name": "elements",
  "data": []
}, {
  "name": "timeAdjListD02",
  "data": []
}, {
  "name": "timeAdjMatrixD02",
  "data": []
}, {
  "name": "timeArcListD02",
  "data": []
}]

tempTimeArcsD04 = [{
  "name": "elements",
  "data": []
}, {
  "name": "timeAdjListD04",
  "data": []
}, {
  "name": "timeAdjMatrixD04",
  "data": []
}, {
  "name": "timeArcListD04",
  "data": []
}]

# -- DENSITY: 20% and 40% --
d02 = 0.2
d04 = 0.4

# -- GENERATE DATA --
for r in dataRange:
  # - Maximal number of arches, 20% of maximal, 40% of maximal -
  M = r * (r - 1) / 2
  m02 = int(M * d02)
  m04 = int(M * d04)
  
  # - Headers for templates -
  tempTimeTS[0]["data"].append(r)
  tempArcs[0]["data"].append(r)
  tempTimeArcsD02[0]["data"].append(r)
  tempTimeArcsD04[0]["data"].append(r)
  
  ### -= Structures =- ###
  for m in [m02, m04]:
    # - Creating arc list -
    arcListObject = ArcList(r, m)
    arcList = arcListObject.arcList
  
    # - Creating adjacency matrix | Based on Arc -
    adjacencyListObject = AdjacencyList(arcList, r)
    adjacencyList = adjacencyListObject.adjList
  
    # - Creating adjacency list | Based on Arc -
    adjacencyMatrixObject = AdjacencyMatrix(arcList, r)
    adjacencyMatrix = adjacencyMatrixObject.adjMatrix
    
    # -= Topological Sort | Based on AdjList [Task 2] =-
    topTimeStart = time.time()
    timeX, vis, pre, post = dfsAlgorithm.runDFS(r, adjacencyList)
    topTimeResult = time.time() - topTimeStart
    verify = {"d": pre, "f": post}

    # -= Counting Back Arcs [Task 3 & 4] =-
    # - Adjacency List
    AdjListTimeStart = time.time()
    backArcsAdjList = adjacencyListObject.countBackArcs(verify)
    AdjListTimeResult = time.time() - AdjListTimeStart

    # - Adjacency Matrix
    AdjMatrixTimeStart = time.time()
    backArcsAdjMatrix =   adjacencyMatrixObject.countBackArcs(verify)
    AdjMatrixTimeResult = time.time() - AdjMatrixTimeStart

    # - Arc List
    ArcListTimeStart = time.time()
    backArcsArcList = arcListObject.countBackArcs(verify)
    ArcListTimeResult = time.time() - ArcListTimeStart

    
    if m == m02:
      tempTimeTS[1]["data"].append(topTimeResult)
      tempArcs[1]["data"].append(backArcsAdjList)
      tempTimeArcsD02[1]["data"].append(AdjListTimeResult)
      tempTimeArcsD02[2]["data"].append(AdjMatrixTimeResult)
      tempTimeArcsD02[3]["data"].append(ArcListTimeResult)
    else:
      tempTimeTS[2]["data"].append(topTimeResult)
      tempArcs[2]["data"].append(backArcsAdjList)
      tempTimeArcsD04[1]["data"].append(AdjListTimeResult)
      tempTimeArcsD04[2]["data"].append(AdjMatrixTimeResult)
      tempTimeArcsD04[3]["data"].append(ArcListTimeResult)

    print("Done: ", r)
#-------------------------
# --- JSON DATA ---
with open("tempTimeTS.json", "w", encoding="utf-8") as file:
    json.dump(tempTimeTS, file, indent=2)
  
with open("tempArcs.json", "w", encoding="utf-8") as file:
    json.dump(tempArcs, file, indent=2)
  
with open("tempTimeArcsD02.json", "w", encoding="utf-8") as file:
    json.dump(tempTimeArcsD02, file, indent=2)
  
with open("tempTimeArcsD04.json", "w", encoding="utf-8") as file:
    json.dump(tempTimeArcsD04, file, indent=2)

  
# --- EXCEL DATA ---
workbook = xlsxwriter.Workbook("results-excel.xlsx")

# - Topological Sort Time
wsTOP = workbook.add_worksheet("TOPsort")
for idx, t in enumerate(tempTimeTS):
  wsTOP.write(0, idx, t["name"])
  for i in range(len(t["data"])):
    wsTOP.write(i+1, idx, t["data"][i])

# - Count Back Arcs
wsCARCS = workbook.add_worksheet("countARCS")
for idx, t in enumerate(tempArcs):
    wsCARCS.write(0, idx, t["name"])
    for i in range(len(t["data"])):
        wsCARCS.write(i+1, idx, t["data"][i])

# - Count Back Arcs Time
# - Density 0.2
wsCARCSTimeD02 = workbook.add_worksheet("countARCSTimeD02")
for idx, t in enumerate(tempTimeArcsD02):
    wsCARCSTimeD02.write(0, idx, t["name"])
    for i in range(len(t["data"])):
        wsCARCSTimeD02.write(i+1, idx, t["data"][i])
# - Density 0.4
wsCARCSTimeD04 = workbook.add_worksheet("countARCSTimeD04")
for idx, t in enumerate(tempTimeArcsD04):
    wsCARCSTimeD04.write(0, idx, t["name"])
    for i in range(len(t["data"])):
        wsCARCSTimeD04.write(i+1, idx, t["data"][i])

workbook.close()