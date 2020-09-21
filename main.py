import random
print("回数を入力")
n = int(input())
print("最小値を入力")
start = float(input())
print("最大値を入力")
end = float(input())
print("----------")

count = 0

for i in range(n):
    l = [random.uniform(start,end)]
    count += 1
    for j in l:
        bt = round(j,1)
        print(str(count)+'{}'.format(': ')+str(bt))
print("----------")
