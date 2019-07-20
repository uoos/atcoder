t = int(input())
S = [input() for i in range(t)]

for i in range(t):
  j = 0
  p = 0
  while j <= len(S[i])-5:
    if S[i][j:j+5] == 'tokyo' or S[i][j:j+5] == 'kyoto':
      j += 5
      p += 1
    else:
      j += 1
  print(p)
