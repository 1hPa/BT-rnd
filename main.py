import random
print("回数を入力")
n = int(input())
print("最小値を入力")
start = float(input())
print("最大値を入力")
end = float(input())
for i in range(n):
    l = [random.uniform(start,end)]
    for j in l:
        print(round(j,1))
