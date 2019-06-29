r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
CC = [list(input()) for i in range(r)] 

dot = 0
for i in CC:
  dot += i.count(".")

CC[sy-1][sx-1] = 0

for i in range(dot-1):
  for l in range(r):
    for m in range(c):
      if CC[l][m]== i:
        y1 = l
        x1 = m
        for j,k in [[1,0],[0,1],[-1,0],[0,-1]]:
          if not(0 <= y1+j < r):
            continue
          elif not(0<= x1+k < c):
            continue
          elif CC[y1+j][x1+k] == ".":
            CC[y1+j][x1+k] = CC[y1][x1]+1
    
ans = CC[gy-1][gx-1]
print(ans)

