n, m = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(m)]

AB.sort(key=lambda x: x[0])
x = n
l = 0
for a, b in reversed(AB):
  if b > x :
    continue
  else:
    x = a
    l += 1
    
print(l)
