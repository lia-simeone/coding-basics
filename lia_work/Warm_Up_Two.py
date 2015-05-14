'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square_minus_square_sum_difference(n):
     sum_of_squares=0
     running_sum=0
     for x in range(1,n+1):
        sum_of_squares=sum_of_squares+(x**2)
        running_sum=running_sum+x
     square_of_sum=running_sum**2
     return square_of_sum-sum_of_squares

print sum_square_minus_square_sum_difference(10)
print sum_square_minus_square_sum_difference(100)

def test_sum_square_minus_square_sum_difference():
    assert 2640 == sum_square_minus_square_sum_difference(10)
    assert 25164150 == sum_square_minus_square_sum_difference(100)

#Answer from Devin
def sum_square_minus_square_sum_difference(n):
    #map is a functional programming tool that's similar to a generator, it takes a function and a collection as inputs.
    #It applies the function to each member of the collection
    #lamba is an inline function e.g. lambda x:x**2 will take x and square it
    return sum(range(n+1))**2 - sum(map(lambda i: i**2,range(n+1)))
