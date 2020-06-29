def CompositionGraph(patterns):
    k = len(patterns[0])
    y = k - 1
    nodes = set()
    for i in patterns:
        for j in range(k-y+1):
            sub = i[j:j+y]
            nodes.add(sub)
    adjList = dict()
    nodes = list(nodes)
    nodes.sort()
    for j in nodes:
        dummy = []
        for i in patterns:
            a = i[1:]
            a1 = i[:k-1]
            if j==a1:
                dummy.append(a)
        dummy.sort()
        if j not in adjList:
            adjList[j] = dummy
    return adjList

#patterns = ["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"]
g = open("dataset_200_8.txt")
patterns = g.read().splitlines()
ans = CompositionGraph(patterns)
f=open('oal.txt','a')
for key, value in ans.items():
    if len(value) > 0:
        answer = key+ " -> "+ ",".join(value)
        f.write(answer)
        f.write("\n")
f.close()