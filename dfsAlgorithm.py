
time = 1
def dfs(start, struct, pre, post, vis):
    global time
    stack = [start]

    while stack:
        rem = stack[-1] #remember
        if vis[rem] == 0:
            vis[rem] = 1
            pre[rem] = time
            time += 1

        added = False
        for neightbour in struct[rem]:
            if vis[neightbour] == 0:
                stack.append(neightbour)
                added = True
                break
        
        if not added:
            post[rem] = time
            time += 1
            stack.pop()


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
