import math
from decimal import Decimal

def calc(x, a, e):
     sum1 = 0
     sum2 = 0
     k = 1     
     while (True):
        sum1 += (Decimal(math.sin(x**k)))/((a**(2*k))*math.factorial(2*k))
        k += 1
        sum2 += (Decimal(math.sin(x**k)))/((a**(2*k))*math.factorial(2*k))
        if(math.fabs(sum2-sum1) < e):
            return sum2
       
