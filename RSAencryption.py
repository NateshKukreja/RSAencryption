def relative_prime_checker(n):
    for i in range(1, n):
        if (n%i !=0):
            for j in range(1, i//2):
                if ((n%j != 0) and (i%j !=0)):
                    return i

def RSA(p, q):
    n = (p-1)*(q-1)
    print(relative_prime_checker(n))

RSA(257, 337)
    
