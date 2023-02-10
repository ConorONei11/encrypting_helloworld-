# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:31:34 2022

@author: Con67
"""
#Extended Euclidean algorithm
a=1632
b=642
 
#Finding gcd of two intgers a and b
def gcd(a,b):
    while b>0:
      r=a%b
      a=b
      b=r
    return(a)

print(gcd(1632,642))
print(gcd(51525,99157))
print(gcd(51527,99157))

#Finding gcd of two integers a and b
#Also finding n and m where n*a+m*b = gcd(a,b)
#When returned, a=gcd, x1=n and y1=b
def gcd2(a,b):
    x0=0
    x1=1
    y0=1
    y1=0
    while b>0:
        q=a//b
        r=a%b
        a=b
        b=r
        x00=x1-q*x0
        x1=x0
        x0=x00
        y00=y1-q*y0
        y1=y0
        y0=y00
    return(a,x1,y1)

print(gcd2(1288,17))
print(gcd2(98496,289))