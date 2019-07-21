N = int(input())
A = [int(input()) for i in range(N)]

maxA = max(A)
max_in = A.index(max(A))
ANS = [maxA]*N
ANS[max_in] = max(A[:max_in]+A[max_in+1:])

for i in ANS:
    print(i)
