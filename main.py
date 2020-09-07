import random
n = int(input())
start = float(input())
end = float(input())
for i in range(n):
    l = [random.uniform(start,end)]
    for j in l:
        print(round(j,1))
