n = int(input())
lista = []
for i in range(n):
  lista.append(int(input()))

count = 1
fp = lista[0]
if fp == 2:
  print(count)
  exit()

for i in range(n):
  fp = lista[fp-1]
  count += 1
  if fp == 2:
    print(count)
    exit()
print(-1)
       
