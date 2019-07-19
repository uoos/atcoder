S = input()
T = input()
ls = len(S)
lt = len(T)

for i in range(ls-lt,-1,-1):
  for j in range(lt):
    if S[i+j] != T[j] and S[i+j] != '?':
      break
  else:
    print((S[:i] + T + S[i+lt:]).replace('?','a'))
    break
else:
  print('UNRESTORABLE')
