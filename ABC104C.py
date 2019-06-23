D, G = map(int, input().split())
PC = [list(map(int,input().split())) for i in range(D)]

l = []
for i in range(2 ** D):
  t = 0
  c = 0
  for j in range(D):
    if ((i >> j) & 1):
      t += (j+1)*100*PC[j][0]+PC[j][1]
      c += PC[j][0]
  if t >= G:
    l.append(c)
  else:
    ck = []
    for j in range(D):
      if ((i >> j) & 1):
        continue
      else:
        ck.append(j)
    if ck == []:
      continue
    ckm = max(ck)
    for k in range(PC[ckm][0]):
      t += (ckm+1)*100
      c += 1
      if t >= G:
        l.append(c)
        break
      
print(min(l))
