#####Python in bash
* Type `python` to enter python mode
* You will see `>>>` to indicate you are in python
* Type `exit()` to go back to bash

#####List comprehension
* Very important and used in a lot of places
* Way of making a new list where each element is the result of operation applied to each member (or another sequence)
* [See this link for more information](https://docs.python.org/2/tutorial/datastructures.html)
* `print [x for x in triplicate([1,2,3])` means execute triplicate for the values 1, 2, and 3 and put the result into a list
* Usage can be basic `[i for i in range(5)]` will create a list `[1,2,3,4,5]`
* Or more complex `[(i,i*2) for i in range(5)] will create a list [(0,0),(1,1),(2,4),(3,6),(4,8)]`
* You can create dictionaries too `{key: value for key,value in ((0,'a'),(1,'b'))}` will create a dictionary `{0:'a',1:'b'}`


#####Generators
* As noted in Python II, generators have the same syntax as a function except they use yield rather than return
* If you call a function that creates a generator, that will restart the generator
* In order to advance the generator, you need to assign it to a generator object and then call next on that generator object
    my_generator_object=mygeneratorfunction()
    my_generator_object.next()

#####Debugging
* Python has a very handy debugger built in
* To use it, add the following line to your script `import pdb;pdb.set_trace()`
* This code will stop the script wherever you insert the debugger
* You you can then print the variables to see their assignments
* To exit the debugger, do control+C

#####Zippers
* Very handy for merging two things together
* `zip(['a','b','c'],range(3))` will create a list `[('a',0),('b',1),('c',2)]`
* Note zippers must have the same number of fields for them to work

#####Miscellaneous
* There are different types of strings - r stands for literal, u is Unicode
* Hash map is another name for a dictionary (Python may use this terminology in giving errors)
* Similar to head, you can use cut to truncate the width of a file
* `cat your_file | head -1 | cut -c -200` will show you the first 200 characters of the first line of your_file