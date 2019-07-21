N = int(input())
A = list(map(int, input().split()))

if 0 in A:
  if len(set(A)) == 1:
    print("Yes")
    exit()
  elif len(set(A)) == 2:
    if A.count(0) *2 == (len(A)-A.count(0)):
      print("Yes")
      exit()
elif len(set(A)) == 3:
  temp =  list(set(A))
  if A.count(temp[0]) == A.count(temp[1]) == A.count(temp[2]):
    if (temp[0] ^ temp[1]) == temp[2]:
      print("Yes")
      exit()
print("No")

  
  
