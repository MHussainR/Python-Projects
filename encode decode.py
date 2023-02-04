import random
# main_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
# 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '<', ',', '>', '.', '?', '/', ':', ';', '"', "'", '{', '[', '}', ']', '|', '\\', '+', '=', '_', '-', '~', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

ranlist = ['[', 'P', 'K', '(', '\\', 'V', 'q', 'J', '-', '&', 'S', 'Y', 't', 'j', '$', 'r', 'F', 'm', '=', 'u', "'", 'p', '_', '6', '|', 'A', '1', 'H', 'v', '!', '}', 'e', ' ', 'a', 'g', 'L', '3', '?', '/', '7', '2', '{', ')', 'n', '5', 'N', ']', ';', '8', '"', 'D', '>', 'E', 'B', 'w', 's', '^', '%', 'l', '4', '`', '9', 'W', 
'Z', ',', 'R', '.', 'C', 'i', '#', 'M', 'c', 'd', '<', 'O', ':', 'f', 'o', '@', 'b', 'z', '0', 'x', '+', 'y', '*', 'Q', 'G', '~', 'X', 'U', 'I', 'k', 'h', 'T']

def encode (n):
    en = ''
    num = random.uniform(1,100)
    num = int(num)
    for i in n:
        a = ranlist.index(i)
        b = a + num
        if b > len(ranlist):
            d = b - len(ranlist)
            c = ranlist[d]
        else:
            c = ranlist[b]
        en += c

    num = str (num)
    t = num+' '+en
    return t

def decode (n,k):
    en = ''
    for i in n:
        a = ranlist.index(i)
        b = a - k
        if b < 0:
            d = len(ranlist) + b
            # d = abs(d)
            c = ranlist[d]
        else:
            # b = abs(b)
            c = ranlist[b]

        en += c

    return (en)

def ad_encode (n):
    a = encode (n)
    l1 = a.split(' ')
    num1 = int(l1[0])
    a1 = num1 // 10
    a2 = num1 % 10

    b = encode (l1[1])
    l2 = b.split(' ')
    num2 = int(l2[0])
    b1 = num2 // 10
    b2 = num2 % 10

    c = encode (l2[1])
    l3 = c.split(' ')
    num3 = int(l3[0])
    c1 = num3 // 10
    c2 = num3 % 10

    t = l3[1]
    print ()
    print ('The Encryped message is:')
    print (c1,b1,a1,t,a2,b2,c2, sep='')

def ad_decode (n, k1, k2, k3):
    a = decode (n, k1)
    b = decode (a, k2)
    c = decode (b, k3)
    print ()
    print ('The Decryped message is:')
    print (c)

def select (n):
    if n == 1:
        a = input('Input a messaage to encrypt: ')
        ad_encode (a)
    elif n == 2:
        a = input('Input letters to decrypt: ')
        b = int(input('Input key 1: '))
        c = int(input('Input key 2: '))
        d = int(input('Input key 3: '))
        ad_decode (a, b, c, d)

while True:
    n = int(input ('To encrypt press 1 and to decrypt press 2 and press 3 to exit: '))
    if n != 3:
        select (n)
    else:
        print ('Program Closing....')
        break