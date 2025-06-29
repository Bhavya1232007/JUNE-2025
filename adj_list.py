v,e=map(int,input().split())
edges=[]
for j in range(e):
    lst = list(map(int,input().split()))
    edges.append(lst)
adjList = []
for i in range(v):
    lst2=[]
    adjList.append(lst2)
for n,m in edges:
    adjList[n].append(m)
    adjList[m].append(n)
print(adjList)
