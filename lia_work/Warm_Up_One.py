#First create a function to def is something is a palindrome
def is_a_palindrome(x):
    #turn integer into a string
    y=str(x)[::-1]
    z=int(y)
    return x==z
    
print is_a_palindrome(9009)
print is_a_palindrome(20102)
print is_a_palindrome(12345)

#If my code is working, this test will return 'None'. 
def test_is_a_palindrome():
    #These asserts require a "True" result from the function
    assert is_a_palindrome(9009)
    assert is_a_palindrome(20102)
    assert is_a_palindrome(123454321)
    #These asserts require a "False" result from the function
    assert not is_a_palindrome(9000)
    assert not is_a_palindrome(12345)
    assert not is_a_palindrome(543)
    #This assert throws an assertion error because I tell it to expect False, but the result is True
    '''assert not is_a_palindrome(121)'''

print test_is_a_palindrome()

def largest_palindrome_from_product_of_2_n_digit_numbers(n):
    #Define the palindrome value
    pal_value=0
    for j in range(1,10**n):
        for k in range(1,10**n):
            #Create the product
            q=j*k
            #Test if the product is a palindrome and if it's larger than the current palindrome, then replace it
            if is_a_palindrome(q) and q>pal_value:
                pal_value=q
    return pal_value

print largest_palindrome_from_product_of_2_n_digit_numbers(3)

#Answer from Devin
def largest_palindrome_from_n_digit_number(n):
    #Good idea to test if the n is positive first since this doesn't make sense for negative numbers
    assert n>1
    #Setting the counter at -1 rather than 0 (doesn't matter here)
    largest_palindrome_so_far=-1
    #xrange is a generator which is much better with large numbers since it doesn't take up memory (unlike a list)
    for i in xrange(1,10**n):
        for j in xrange(i,10**n):
            candidate_number=i*j
            if is_a_palindrome(candidate_number):
                #max is handy, but I prefer to using 'and' like I did above
                largest_palindrome_so_far=max(candidate_number,largest_palindrome_so_far)
    return largest_palindrome_so_far