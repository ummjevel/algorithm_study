import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

d = [0 for i in range(n+5)]


for i in range(n):
    temp = 1024
    for j in range(i):
        if temp > a[j] and a[j] > a[i]:
            d[i] += 1
            temp = a[j]
    d[i] += 1
print(a)
print(d)
print(max(d))
