'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def getMaxPrime(n):
    f = 2
    while f *f < n:
        if n % f == 0:
            n = n/f
        else:
            f += 1
    return n


n = 600851475143
f = getMaxPrime(n)
print f       
