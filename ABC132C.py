N = int(input())
D = list(map(int, input().split()))

D = sorted(D)
if D[int(N/2-1)] == D[int(N/2)]:
  print(0)
else:
  ans = D[int(N/2)] - D[int(N/2-1)]
  print(ans)
