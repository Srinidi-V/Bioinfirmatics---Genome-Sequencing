def overlap(patterns):
    k = len(patterns[0])
    adjlist = dict()
    for i in patterns:
        dummy = []
        for j in patterns:
            if i[1:] == j[:k-1] and i!=j:
                dummy.append(j)
        if len(dummy)>0:
            adjlist[i]=dummy
    print(adjlist)
    return adjlist

g = open("dataset_198_10.txt")
patterns = g.read().splitlines()
ans = overlap(patterns)
f=open('oal.txt','a')
for key, value in ans.items():
    if len(value) > 0:
        answer = key+ " -> "+ ",".join(value)
        f.write(answer)
        f.write("\n")
    else:
        answer = key+" -> "+value
        f.write(answer)
        f.write("\n")
f.close()