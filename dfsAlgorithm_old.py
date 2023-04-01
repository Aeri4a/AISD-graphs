# -- DFS Algorithm --

time = 1

def dfs(u, adjList, pre, post, vis):
    global time
    pre[u] = time
    time += 1
    vis[u] = 1

    for v in adjList[u]:
        if vis[v] == 0:
            dfs(v, adjList, pre, post, vis)
	
    post[u] = time
    time += 1


def runDFS(n, adjList):
    global time

    #Prepare result lists
    pre = [0 for i in range(n + 1)]
    post = [0 for i in range(n + 1)]
    vis = [0 for i in range(n + 1)]

    #Start algorithm
    dfs(1, adjList, pre, post, vis)

    #Complete what is still not visited
    while vis[1:].count(0) != 0:
        dfs(vis[1:].index(0)+1, adjList, pre, post, vis)
    
    return time, vis, pre, post