import sys
sys.setrecursionlimit(500000)
H, W = map(int, input().split())
C = [""]*H
for i in range(H):
  C[i] = input().replace(" ","")
  
for i in range(H):
  for j in range(W):
    if C[i][j] == "s":
      sh = i
      sw = j
      break
      
def Search(x, y):
  if not(0<=x<H):
    return
  elif not(0<=y<W):
    return
  elif C[x][y] == "#":
    return
  elif C[x][y] == "g":
    print("Yes")
    sys.exit()
  C[x] = C[x][:y] + "#" + C[x][y+1:]
  Search(x+1, y)
  Search(x-1, y)
  Search(x, y+1)
  Search(x, y-1)
  
Search(sh, sw)
    
print("No") 
