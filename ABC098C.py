n = int(input())
S = input()

l = [0]*n
wl = [0]*n
el = [0]*n

for i in range(n-1):
  if i == 0:
    wl[i+1] = S[i].count("W")
  else:
    wl[i+1] = S[i].count("W")+wl[i]

for i in reversed(range(1,n)):
  if i == n:
    el[i-1] = S[i].count("E")
  else:
    el[i-1] = S[i].count("E")+el[i]
    
for i in range(n):
  l[i] = wl[i] + el[i]
  
print(min(l))
