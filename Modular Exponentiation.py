# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:40:44 2022

@author: Con67
"""
#Modular exponentiation
#Changes ascii of codeword to binomial
#Uses binomial codeword to exponentiate    
def modexp(e,m,n):
    bn = bin(e)[3:]
    x=[0]*(len(bn)+1)
    x[0]=m
    for i in range(len(bn)):
   
        if bn[i] == '0':
            x[i+1] = (x[i]**2) %n
        if bn[i] == '1' :
            x[i+1] = (m*(x[i]**2))%n
    return(x[-1])

#Various results used in investigation
print(modexp(17,72,1363))
print(modexp(985,504,1363))  
print(modexp(-1,30,47))

#Encryption function
#Takes the word, transforms into ascii and returns cypher using modular exponentiation
def encrypt(word,e,n):
    asci=[0]*(len(word))
    message = [0]*(len(asci))
    for i in range(len(word)):
        asci[i]=ord(word[i])
        message[i]=modexp(e,asci[i],n)
    return(message)

#Encrypting Hello World
print(encrypt("Hello world!",17,1363))
 
#Output of print(encrypt("Hello world!",17,1363))
message3=[504, 852, 686, 686, 977, 582, 1162, 977, 791, 686, 1153, 818]

#Decryption function
#Takes cypher and decrypts using private key
#Joins characters to form the string again 
def decrypt(message2,d,n):
    asci2=[0]*(len(message2))
    word2=[0]*(len(message2))
    for i in range(len(message2)):
        asci2[i]=modexp(d,message2[i],n)
        word2[i]=chr(asci2[i])
    return(' '.join(word2))

#Result which returns the message Hello world!
#Private key = 985 and n = 1363
print(decrypt(message3,985,1363))


  
        
        