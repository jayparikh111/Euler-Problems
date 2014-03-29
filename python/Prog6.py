'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
'''

sum_square = 0
square_sum = 0
for i in range(1,100+1):
    sum_square += (i**2)
    square_sum += i
        
square_sum *= square_sum

print square_sum - sum_square    
    