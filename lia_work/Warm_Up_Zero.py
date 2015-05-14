#Create a function that advances Fibonacci by one
def fibonacci_sequence():
    ''' helper function
        we're hooking you with a partial answer, just this first time! '''
    fib_of_n, fib_of_n_plus1 = 1, 1
    while True:
        fib_of_n, fib_of_n_plus1 = fib_of_n_plus1, fib_of_n + fib_of_n_plus1
        yield fib_of_n

def no_run_fn():
    #This code will create a new generator
    print fibonacci_sequence().next()
    #This code starts the generator again
    print fibonacci_sequence().next()

    #To advance the generator, I need to define a generator object
    fib_gen=fibonacci_sequence()
    print fib_gen.next()
    print fib_gen.next()
    print fib_gen.next()


    #Output fibonacci less than n
    def fibonacci_not_exceeding(n):
        #Define my generator object
        fib_gen=fibonacci_sequence()
        
        #Assign the variable fib_value
        fib_value=0
        
        while fib_value<n:
            fib_value=fib_gen.next()
            print fib_value

    #Call my function
    fibonacci_not_exceeding(50)

    #Output sum of fibonacci less than n
    def sum_fibonacci_not_exceeding(n):
        #Define my generator object
        fib_gen=fibonacci_sequence()
        
        #Define a varaible to hold my fib_gen output
        fib_value=0
        #Define a variable to hold my running sum
        fib_sum=0
        
        while fib_value<n:
            fib_value=fib_gen.next()
            fib_sum=fib_sum+fib_value
            print fib_value, fib_sum
        
    #Call my function
    sum_fibonacci_not_exceeding(100)

#End of no_run_fn

#Output sum of even fibonacci less than n
def sum_even_fibonacci_not_exceeding(n):
    #Define my generator object
    fib_gen=fibonacci_sequence()
    
    #Define a varaible to hold my fib_gen output
    fib_value=0
    #Define a variable to hold my running sum
    fib_sum=0
    
    while fib_value<n:
        fib_value=fib_gen.next()
        if fib_value%2==0:
            fib_sum=fib_sum+fib_value
    print fib_sum
    return fib_sum
    
#Call my function
sum_even_fibonacci_not_exceeding(89)
sum_even_fibonacci_not_exceeding(4*10**6)

#Answer from Devin
def sum_of_even_valued_fib_not_exceeding(n):
    running_total=0
    for fib in fibonacci_sequence():
        if fib>n:
            return running_total
        if not fib % 2:
            running_total+=fib

#The "for" statement is key. It's a shorthand for advancing the generator iteratively.
#This avoids the awkardness that I had of defining a temporary variable.
#Generators are only important when you have large data. The "itertools" package in Python has lots of pre-written code.               
