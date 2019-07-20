n = int(input())
W = [int(input()) for i in range(n)]

count = [W[0]]
for i in W:
  count.sort()
  if i in count:
    continue
  else:
    for j in range(len(count)):
      if count[j] > i:
        count[j] = i
        break
    else:
      count.append(i)
      
print(len(count))
