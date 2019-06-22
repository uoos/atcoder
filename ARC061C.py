S = input()
l = len(S)
ans = 0

for i in range(l):
  ans += sum([int(S[i]) * (10**k) * 2**(max(0,l-i-k-2)+i)  for k in range(l-i)])

print(ans)
