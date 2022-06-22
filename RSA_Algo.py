# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:06:38 2022

@author: HENRY
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:00:29 2022

@author: HENRY
"""
import random

def primeRandomrange(a, b):
    prime_list = []
    for n in range (a,b):
        isPrime = True
        
        for num in range (2, n):
            if n % num == 0:
                isPrime = False
        
        if isPrime:
            prime_list.append(n)
    return prime_list
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def eea(a,b):
    if b==0:
        return (1,0)
    (q,r) = (a//b,a%b)
    (s,t) = eea(b,r)
    return (t, s-(q*t) )
def find_inverse(x,y):
    inv = eea(x,y)[0]
    if inv < 1: 
        inv += y #we only want positive values
    return inv
#Encrypt function
def encrypt( e, ptext):
    #To Unpack
    key = e 
    Eul 
    #Convert each letter in the plaintext to numbers based on the cahracter
    ctext = [(ord(char)** key)% Eul for char in ptext]
    #return array of bytes
    return ctext

#Decrypt Function
def decrypt(d, cipher):
    key = d
    Eul 
    #Generate the plaintext based on the ciphertext
    plainTxt=[chr((char**key)%Eul)for char in cipher]
    #Return the array of bytes as a string 
    return ''.join(plainTxt)
prime_list = primeRandomrange(3, 40)
p = random.choice(prime_list)
q = random.choice(prime_list)
Eul = p * q
val =  (p-1) * (q-1)

print('Generated random prime number p: ', p)    
print('Generated random prime number q: ', q)

print("The Euler function value of {",Eul,"} is :",val)

eRan = primeRandomrange(1, val)


e = random.choice(eRan)

g = gcd(e,val)
while g != 1:
    e = random.choice(eRan)
    g = gcd(e, val)

d = find_inverse(e,val)
print ("Generating your public/private keypairs now . . .")
print("Your public key: (",e,",",Eul,")")
print("Your private key:(",d,",",Eul,")")
print(" ")
msg = input("Enter Message you wish to Encrypt: ")
encrypt_msg = encrypt(d, msg)
print(" ")
print("Encrypting message.....")
print("Your encrypted message is: ")
print(encrypt_msg)
print("Decrypting message....")
ciph=decrypt(e,encrypt_msg)
print("Your decrypted message: ",ciph)