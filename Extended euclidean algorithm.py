# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:31:34 2022

@author: Con67
"""
#Extended Euclidean algorithm

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

#We have that with N = 1363, p = 29 and q = 47
#(p-1)(q-1) = 1288
#Therefore 1288 is used with public key e = 17 in order to find private key d
print(gcd2(1288,17))

#-303 is outside range, therefore add 1288 to get 985. (Which is to be used in order to decrypt!!)
