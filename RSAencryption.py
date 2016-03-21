import random

def find_e(primeList, n):

    for i in range(len(primeList)):
        if (n%primeList[i]==0):
            find_e(primeList, n)
        else:
            return primeList[i]
    
def relative_prime_checker(n):
    primeList = []

    for num in range(1,n):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
            if prime:
                primeList.append(num)
    random.shuffle(primeList)
    return(find_e(primeList, n))

def key_generator(e, n):
    return e^(-1)%(n)

def encrypt(d, n, M):
    return ((M^d)%n)

def RSA(p, q, M):
    N = p*q
    n = (p-1)*(q-1)
    e = (relative_prime_checker(n))
    d = key_generator(e, n)
    print(encrypt(d, n, M))
    

RSA(11, 13, 10)
