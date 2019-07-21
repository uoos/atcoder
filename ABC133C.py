L, R = map(int, input().split())

a = R//2019*2019
if L <= a <= R:
  print((a * (a+1))%2019)
else:
  C = []
  for i in range(L,R):
    for j in range(i+1, R+1):
      C.append(i*j%2019)
  print(min(C))
  
