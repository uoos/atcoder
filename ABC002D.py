N, M = map(int, input().split())
L = [input().replace(" ","") for i in range(M)]

cl = []
for i in range(2 ** N):
  l = []
  l2 = []
  for j in range(N):
    if ((i >> j) & 1):
      l.append(j+1)
  for k in range(len(l)-1):
    for m in range(len(l)-k-1):
      l2.append(str(l[k])+str(l[k+m+1]))
  if set(l2) == set(L)&set(l2):
    cl.append(len(l))

print(max(cl))
