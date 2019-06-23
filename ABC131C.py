A, B, C, D = map(int, input().split())

import fractions
ccount = ((B//C*C)-((A-1)//C*C +C))//C +1
dcount = ((B//D*D)-((A-1)//D*D +D))//D +1
lcm = (C * D) // fractions.gcd(C, D)
cdcount = ((B//lcm*lcm)-((A-1)//lcm*lcm +lcm))//lcm +1
count = B - A + 1 - ccount - dcount + cdcount
print(int(count))
