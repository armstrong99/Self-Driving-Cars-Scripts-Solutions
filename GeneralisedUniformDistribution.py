#  Modify your code to create probability vectors, p, of arbitrary 
#  size, n. Use n=5 to verify that your new solution matches 
#  the previous one.
from decimal import Decimal

p=[]
n=5

for i in range(n):
    result = (Decimal(1) / Decimal(n))
    p.append(( float(result) ) )
 

print p