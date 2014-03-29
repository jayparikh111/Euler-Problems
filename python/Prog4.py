'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindrom(n):
    return int(str(n) + str(n)[::-1])

found = False
firstHalf = 998
while not found:
    firstHalf -= 1
    palindrm = palindrom(firstHalf)
    for i in range(999,99,-1):
        if ((palindrm/i) > 999 or (i*i) < palindrm):
            break
        
        if (palindrm%i) == 0:
            found = True
            factor1 = palindrm / i
            factor2 = i
            break


print factor1,'*',factor2
