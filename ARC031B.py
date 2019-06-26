a = [list(input()) for i in range(10)]
import sys
sys.setrecursionlimit(500000)
import copy
d = [["x"]*10 for i in range(10)]

def s(x, y):
  if not(0<=x<10):
    return
  elif not(0<=y<10):
    return
  elif A[x][y] == "x":
    return
  A[x][y] = "x"
  s(x+1, y)
  s(x-1, y)
  s(x, y+1)
  s(x, y-1)

for i in range(10):
  for j in range(10):
    A = copy.deepcopy(a)
    A[i][j] = "o"
    s(i, j)
    if A == d:
      print("YES")
      exit()
      
print("NO")
