# Introduction to cryptohack

# ord() converts to decimal, chr() converts to char

# bytes.fromhex() hex to bytes 

# imports
import base64 as b64

# CHALL 1

crypt1 = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
res = []
for i in crypt1:
    res.append(chr(i))

result = ''.join(res)
print(result)


# CHALL 2

crypt2 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

res1 = bytes.fromhex(crypt2)

print (res1)


# CHALL 3

crypt3 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

res2 = bytes.fromhex(crypt3)

res2 = b64.b64encode(res2)

print(res2)


#CHALL 4

from Crypto.Util.number import *

crypt4 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

res = long_to_bytes(crypt4)

print(res)


# CHALL 5

chall5 = "label"
chall5 = [ord(x) for x in chall5] # returns an array
chall5 = [13 ^ i for i in chall5]
chall5 = ''.join(chr(o) for o in chall5) 
print(chall5) 


# CHALL 6

# Use zip() for key value pair ord1:ord2


# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0


k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# return an array of bytes
ord_k1 = [i for i in bytes.fromhex(k1)] 
print("k1",ord_k1)
ord_k2k1 = [i for i in bytes.fromhex(k2_k1)]
print("k2k1", ord_k2k1)
ord_k2_k3 = [i for i in bytes.fromhex(k2_k3)]
print("k2k3", ord_k2_k3)
ord_f_k1_k3_k2 = [i for i in bytes.fromhex(flag_k1_k3_k2)]
print("f_k1_k3_k2",ord_f_k1_k3_k2)

# use commutative property to get key2 and key 3

k2 = [key1 ^ key2 for (key1,key2) in zip(ord_k1, ord_k2k1)]
print("k2",k2)

k3 = [key2 ^ key3 for (key2, key3) in zip(k2, ord_k2_k3)]
print("k3",k3)

# xor everything together

flag_k2_k3 = [k2k3 ^ flag_ord for (k2k3, flag_ord) in zip(ord_k2_k3, ord_f_k1_k3_k2)]

final_flag = [k1 ^ flag_ord for (k1, flag_ord) in zip(ord_k1, flag_k2_k3)]

final = "".join(chr(o)for o in final_flag)

print(final)

# CHALL 7

chall7 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

chall7 = [i for i in bytes.fromhex(chall7)]

for order in range(256):
    chall7flag = [order ^ i for i in chall7]
    chall7flag1 = "".join(chr(o) for o in chall7flag)
    if chall7flag1.startswith("crypto"):
        print(chall7flag1)
print(chall7)


