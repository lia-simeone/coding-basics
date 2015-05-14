###Day 1

#####Python Overview and History
* Created in 1990 by a guy that works at Google, open source
* Quick and light language - works very well for quick tasks, no forced type
* Scripting language like bash, perl, ruby etc.
* Good for quick turnaround, minimal compile step
* Debate on whether it's good for huge projects
* Python is an interpreted language
* Case sensitive
* Python does only superfical checks upfront, evaluates each line when it's executing

######Functions overview
* Common to name your main function "main" (seems confusing given main function)
* Basic program
    #Module for system options
    import sys
    
    def main():
        print sys.argv #prints command line arguments
        
    #Standard boilerplate to call main()     
    if __name__=='__main__'
        main()
* I belive the above executes the main function so you can run this file in Unix with /.hello.py rather than calling python first
* Instructor says this way is more modern
* The handy thing about this method in conjunction with argv is you can pass parameters into your script right from the command line
    def Hello(name):
        name = name + '!!!!!'
        print 'Hello', name
    
    def main():
        Hello(sys.argv[1])
    
    #Standard boilerplate to call main()     
    if __name__=='__main__'
        main()
        
    #If you call this script in Python, it will run function on the name you provide
    ./hello.py Alice
    #returns
    Hello Alice!!!!!

#####Types overview
* `.lower` is a method belonging to strings that converts the string object into lowercase
* `.find()` searches for the supplied parameter within the string
* % work like macro variables in SAS, haven't seen this before!
    'Hi %s I have %d donuts' % ('Alice',42)
* by default, Python strings are not unicode

#####Researching functions
* Run python intepreter and `import your_module`
* `dir(your_module)` will show the symbol defined in that module
* `help(your_module)` will bring up a manual-ish document
* Help can be used on specific functions `help(sys.exit)`
* [docs.python.org] is the official documentation

####Logical check for if a value is contained within a data structure
* Do NOT write a loop!
    # Input
    a = [13, 2, 3]
    2 in a
    # Output
    True
* The `in` is the magic

####List characteristics
* .append() adds an element to the end of the list
* it does not return anything but rather modifies the list in place
    # Input
    a.append(4)
    a
    # Output
    [13, 2, 3, 4]
* .pop() removes the indexed element from the list and returns it to you
    # Intput
    a.pop(0)
    a
    # Output
    13
    [2, 3, 4]
* del removes the indexed element from the list (can also be used to delete variable references)
    # Input
    del a #removes our prior a list
    a = [1, 2, 3]
    del a[1]
    a
    # Output
    [1, 3]


####Sorting
* do NOT use .sort() method - that's old school
* `sorted()` is a standalone function that works on lists or other sequence-like things
* it produces a new list when you sort
    # Input
    a = [4, 2, 1, 6]
    sorted(a)
    # Output
    [1, 2, 4, 6]
* you can assign it to a new variable or write up the existing variable
* there are setting likes reverse etc.
* custom sorting let's you specify the sorting criteria based on the key parameter
    # Input
    a = ['ccc', 'aaaa', 'd', 'bb']
    sorted(a, key=len)
    # Output
    ['d','bb','ccc','aaaa']
* another example might be sorting based on the last letter in a string
    # redefine a
    a[1] = 'aaaz'
    # make a function for last character
    def Last(s):
        return s[-1]
    # Then use that function as the key
    sorted(a, key=List)
    # Output
    ['bb','ccc','d','aaaz']
* tuples naturally let you sort by multiple criteria: it compares first elements to each other, if diff, looks at second elements etc.
    #make a list of tuples
    a = [(1, "b", (2, "a", (1, "a") ]
    # sort it
    sorted(a)
    # Output
    [(1, "a"), (1, "b"), (2, "a")]
 --* if you want to sort by multiple things, write your key function to produce a tuple

    
####Moving between lists and strings
* you can combine the elements from a list into a single string
--* you can loop through a list printing each element but that's inefficient
--* the shortcut is to use `.join` (per Randy's example)
    # Input
    b = ':'.join(a)
    b
    # Output
    'ccc:aaaz:d:bb'
* you can also separate a string into a list
    b.split(':)
    ['ccc','aaaz','d','bb']

####Dictionaries
    d = {}
    d['a']='alpha'
    d['o']='omega' #etc.
    # to retrieve a value, enter the key
    d['a']
* By default, if you use a key that doesn't exist you will get an error
    # get let's you print nothing if doesn't exist
    d.get('x')
    # no output
* To determine if a key is in a dictionary, use in
    'a' in d
    # Output
    True
* .keys() and .values() let's you grab the respective elements (I believe they make a list)
* .items() creates a tuple which each binding of the dictionary
* note dictionaries use a hashing technique that stores elements in seemingly random order
* looping example:
    for k in sorted(d.keys()):
        print 'key:', k, '-->', d[k]
        
####Reading files
* `open()` is a python function to read files
    def Cat(filename):
        f = open(filename, 'rU') #the rU fixes issues with Unix vs. dos line returns
        # QUESTION: how does Python know that the "increment" of f is a line? Other structures are by element.
        for line in f:
            print line, # the trailing comment inhibits a return at the end of the line
        f.close() # not necessary but more correct
--* going line-by-line is a very efficient from a RAM perspective
* `readlines()` reads a file into a list where each line from the file is an element of the list
--*CAUTION this method puts the entire dataset into memory so don't use this for large datasets
    lines = f.readlines()
* `read()` turns a dataset into a single string
--* helpful for find and replace
    text = f.read()
