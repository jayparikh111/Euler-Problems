'''
2520 is the smallest number that can be divided by each of the numbers
 from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by
 all of the numbers from 1 to 20?
'''

n = 2520
i = range(11,21)
sol = 0
while sol == 0:
    divides = 0
    for j in i:
        if n%j == 0:
            divides += 1
        else:
            divides = 0
            break
    if divides == 10:
        sol = n
        break
    n += 2520
    
print sol    
    