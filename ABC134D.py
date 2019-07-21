N = int(input())
A = list(map(int, input().split()))

temp = [0]*N
for i in range(N-1,-1,-1):
  for j in [0,1]:
    temp[i] = j
    if sum(temp[i::i+1])%2 == A[i]:
      break
  else:
    print(-1)
    exit()
print(sum(temp)) 
anslist = []
for i in range(N):
  if temp[i] == 1:
    anslist.append(i+1)
if anslist == []:
  exit()
else:
  print(*anslist)
  exit()
