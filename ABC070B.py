A, B, C, D = map(int, input().split())

if A >= C:
  if A >= D:
    print(0)
  else:
    if B >= D:
      print(D-A)
    else:
      print(B-A)
else:
  if C >= B:
    print(0)
  else:
    if D >= B:
      print(B-C)
    else:
      print(D-C)
