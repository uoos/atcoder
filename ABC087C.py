n = int(input())
a1list = list(map(int, input().split()))
a2list = list(map(int, input().split()))

countlist = []
for i in range(n):
  p = sum(a1list[0:i+1]) + sum(a2list[i:n])
  countlist.append(p)
  
print(max(countlist))
