N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
count = 0
for i in range(N):
  D = D + L[i]
  count += 1
  if D > X :
    print(count)
    exit()
print(count+1)
