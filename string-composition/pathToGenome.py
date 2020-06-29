def PathToGenome(pattern):
    k = len(pattern[0])
    n = len(pattern)
    text = ""
    text += pattern[0]
    for i in range(1,n):
        text += pattern[i][k-1]
    return text

f = open("dataset_198_3_1.txt")
pattern = f.read().splitlines()
string = PathToGenome(pattern)
f = open("ptg.txt","w")
f.write(string)
f.close()
#print(PathToGenome(pattern))