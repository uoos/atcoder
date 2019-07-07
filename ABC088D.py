H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

C = 0
for i in range(H):
  for j in range(W):
    if S[i][j] == ".":
      C += 1
    
S[0][0] = 0
for l in range(C-1):
  for i in range(H):
    for j in range(W):
      if S[i][j] == l:     
        for k in [[0,1],[1,0],[-1,0],[0,-1]]:
          if not(0 <= i + k[0] < H):
            continue
          elif not(0 <= j + k[1] < W):
            continue
          elif S[i+k[0]][j+k[1]] != ".":
            continue
          else:
            S[i+k[0]][j+k[1]] = S[i][j]+1
        
if S[H-1][W-1] == ".":
  print(-1)
  exit()
  
ans = C - S[H-1][W-1] -1
print(ans)
