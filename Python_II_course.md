#####Errors and Exceptions
* Arrows indicate the number of levels from a traceback
* The last arrow is the actual error and will show you the line number of the error
* Errors have different categories (described below)
* Python will stop running when it encounters an error
* Syntax - you wrote the code wrong (e.g. forgetting a colon from a function)
* Identation - indenting is inconsistent
* Name - using a variable that doesn't exist, commonly triggered by forgetting quotes around a string or mixing up capitalization, loops need a defined count variable before you can use it
* Item - covers a few specific erros like Index and Key, related to collections like lists, tuples, dictionarys, happens if you reference an index or key that doesn't exist
* IO Error - typically file related as in your reading a file that doesn't exist, but can be other things

#####Assertions
* Statements that check if something is true - important for robust programming
* Code will stop running if result is false and return a message if you specify one, otherwise it will yield an AssertionError with the line number
* Three broad categories: pre-condition, post-condition, and invariant

#####Try, Except
* Let's you structure the code so it does different things if it encounters an error
* Different than assertion because the code can keep running
* Similar to "if else" except it will run everything in the try and then jump to the except if it hits an error (rather than one or the other)

#####Generators
* Similar to functions in structure except they have a yield instead of a return
* Very different from functions in processing as generators read the paramters one at a time and discard the info after each iteration
* Functions read all parameters first and keep it in memory until the function completes
* Think of difference between reading all items in a list and just the first item
* ADD MORE NOTES HERE FROM SMALL DATA COURSE!

#####Glob
* Regular expression
* Glob takes a reg ex and looks for files that match it
* You can search for csv files by doing `glob.glob('*csv')`

#####Object classes - unedited notes!
* You can create a user-defined object using the class statement
* When you create a custom-object, you can instantiate objects into it
* Objects have attributes (basic property) and methods (same as function but requires “self” parameter - a reference to the object)
* You can reference attributes and methods by doing “object.[attr/method] – note an object needs to be defined before doing this
* You can create a new custom object that inherits qualities of an existing class
* _init_  is a method that will execute when a new Cat object is initialized. It’s specific to each object and can be modified independently (different then class attributes where all objects of that class have the same value and you can’t change it).
* 2 underscores before an attribute name make it private – you cannot see it or modify if you make it private


#####Miscellaneous
* If your dictionary key is a list, you can reference items in the list by sticking the indexing together `seasons['spring'][0]` will return March if seasons is a dictionary and spring is a key
* `range()` is a great way of making arthemetic progressions `range(10)` will create a list containing the numbers 0 to 9

## Additions from my own research - should probably be included in Python II

####Module
* A module is a python source file containing classes, functions, and global variables
* can also contain executable code which is run only the first time the module is imported
* each module has it's own private symbol table
* within a module, the module's name is available as the global variable __name__
* the file name is the module name with the .py suffix but you call it without the suffix
    import [your_module]
* specific functions within this module have to called with the module name
    fibo.fib(1000)
* you can gt around this by either:
    # Option 1 - give it a local name:
    fib=fibo.fib
    # Option 2 - import the function directly
    from fibo import fib
    # Option 2b - import all functions individually - not recommended because your function names can overlap
    from fibo import *
* You can execute a module as a script (sounds like %include)
    python fibo.py [arguments]
--* In this case, __name__ is set to "__main__"
--* The benefit is that you can include code in your module that only runs when it's executed as a script
--* You can add this code to test your script and leave it in there if you want to use it as a module later
    # sys is a standard module
    # argv[1] refers to the first paramter passed into the script 
    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))

####Package
* a package is a collection of modules (think of it as a directory)
* any directory with an `__init__.py` file is considered a package
--* leaving the init file empty is considered normal and good if the modules and submodules don't need to share code
* once you import a module or package, the object python creates is always a module (interesting)
* QUESTION: this seems to conflict with the above but it says only functions/variables/classes into the init file are visible, not sub-packages or modules


####Class
* type of data structure, think of it as a blueprint
* let's you encapsulate similar functions and variables
* you define a class with the class operator
    class class_name(object):
        #code here
--* note `(object)` code is mandatory in Python 2.x to explicity call out a new style class. Very important for compatibility!
* a class can contain methods (functions) and attributes (variables)
--* functions require the `self` parameter to refer to things in the class (because you're inside it)
    def area(self)
        return self.x *self.y
--* great example of what self is doing "`jeff.withdraw(100.0)` is just shorthand for `Customer.withdraw(jeff, 100.0)`", it describes which instance to run the method on
* code in the __init__ method runs when we create an instance of the class
    def __init__(self,x,y):
    self.x = x
    self.y = y
* "The rule of thumb is, don't introduce a new attribute outside of the __init__ method, otherwise you've given the caller an object that isn't fully initialized" 

##Not sure if the below should be part of Python II

####Pickle
* Pickling is a way of serializing and de-serializing a Python object structure - converts object into a byte stream
* Data format is ASCII by default, but also has other settings
* Pickles are not an encryption technique meanin they are NOT secure

####Lambda
* an anonymous function that accepts one argument x
* it's used in-line and doesn't require a 'return' to get the value
* makes sense if you only want to use the function once
    # Intput
    addTwo = lambda x: x+2
    addTwo(2)
    # Output
    4
* same idea with traditional function
    # Input
    def addTwo(x):
        return x+2
    addTwo(2)
    # Output
    4

####Sources for these additions
* [Python documentation](https://docs.python.org/2/tutorial/modules.html)
* [Stackoverflow[(http://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package)
* [Info on classes](http://sthurlow.com/python/lesson08/)
* [New- vs. old-style classes](http://stackoverflow.com/questions/4015417/python-class-inherits-object)
* [Another good resource on clases](http://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
* [Pickle usage examples - not sure I get these](http://stackoverflow.com/questions/3438675/common-use-cases-for-pickle-in-python)