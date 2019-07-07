K = int(input())

C = 0
D = 1000-K

for i in [500, 100, 50, 10, 5, 1]:
  if D//i >=1:
    C+= 1*(D//i)
    D-= i*(D//i)
print(C)
