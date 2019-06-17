N, K = map(int,input().split())
A = list(map(int,input().split()))
 
count = 0
sum1 = 0
l = 0
for i in range(N):
  sum1 += A[i]
  while sum1 >= K:
    count += N - i
    sum1 -= A[l]
    l += 1 
 
print(count)
