import copy
def dijkstra(WList,s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys()for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)       
    distance[s] = 0    
    for u in WList.keys():
        nextd = min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist = [v for v in WList.keys() if (not visited[v]) and distance[v] == nextd]
        if nextvlist == []:
            break
        nextv = min(nextvlist)        
        visited[nextv] = True        
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if distance[v] > distance[nextv] + d:
                    distance[v] = distance[nextv] + d   
    return(distance)


def shortestCircularRoute(WList,s):
    pathweight=[]
    adj = []
    for node in WList[s]:
        adj.append(node)
    for each_adj in adj:
        wl = copy.deepcopy(WList)
        wl[s].remove(each_adj)
        wl[each_adj[0]].remove((s,each_adj[1]))
        d = dijkstra(wl,each_adj[0])
        pathweight.append(each_adj[1]+ d[s])
    return(min(pathweight))





n = int(input())
edges = eval(input())
S = int(input())
WL = {}
for i in range(n):
    WL[i] = []
for ed in edges: #create dictionary for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(shortestCircularRoute(WL,S))