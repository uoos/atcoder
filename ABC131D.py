N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]

AB.sort(key = lambda x:x[1])
t = 0

for i in range(N):
  t += AB[i][0]
  if t > AB[i][1]:
    print("No")
    exit()

print("Yes")
