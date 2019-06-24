N = int(input())
T = [int(input()) for i in range(N)]

l = []
for i in range(2 ** N):
  m1 = []
  m2 = []
  for j in range(N):
    if ((i >> j) & 1):
      m1.append(T[j])
    else:
      m2.append(T[j])
  tm = max(sum(m1),sum(m2))
  l.append(tm)
  
print(min(l))
