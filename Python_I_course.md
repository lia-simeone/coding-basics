#####Python benefits
* Uses an interpreter to execute the program meaning you can write a program on a Mac, Windows, Unix Linux etc. and it will run on any platform with an interpreter
* Can be a web server (not sure what this means)
* Multi-paradigm meaning it can be functional object-oriented or straight-up programming etc.
* Loosely-typed meaning you don't have to assign a data type upfront and you can change them as you go `happy='true' happy=10 happy=['lia','test']`

#####Basic data types
* String - you can use single or double quotes, but don't mix, there is some difference in how variables resolve, strings are immutable
* Number - integers, float (decimals), long for big numbers that won't fit in an integer, to explicity cast a number as float use `float(yournumber)`
* Boolean - True or False (case sensitive)

#####Collections
* List - defined by [ ], can contain any mix of strings, numbers, other lists, size is fixed upfront but can be changed by doing `yourlist.append(newvalue)` (mutable object)
* Tuple - defined by (), can contain a mix of types but cannot be changed (immutable object)
* Sets - defined by {}, unordered containing no duplicates, in addition to curly brackets, can be created using the `set()` function
* Dictionary -  pairs defined by {key:value,key:value,...}, you use the key to lookup the value, can be modified, keys cannot be mutable

#####Comments
* Single line comments are denotes by a #
* Multi-line comments are denoted by triple quotes (''' or """)
* Note: comments need to have proper indentation just like the rest of Python! While not executed, comments are still read.

#####Indexing
* Zero-based indexing meaning the first item is `[0]` or first data point is `[0,0]`
* For datasets, format is [rows,columns]
* The starting range is inclusive but the ending is not `[0,10]` will give you rows 0-9 (which is 10 total rows)
* Magic colon - leaving off the starting or ending points will return everything from the beginning forward or beginning backward, leaving off both will give you everything `[:10] [7:] [:]`
* You can reverse index meaning count from the back, the last item is `element=’oxygen’ element[1:-1] is ‘xyge’`
* You can also move from back to front by changing the step to -1

#####Importing libraries
* `import.numpy` will import everything in the numpy library
* `from matplotlib import pyplot` will only load the pyplot function from the matplotlib library

#####Functions
* Define functions by `def yourfunctionname():` 
* Parameters are optional
* Multiple parameters should be separated by commas
* Parameters within the function should not be in quotes
* Function end are definitely purely by indentation
* You must return to get the output of the function
* You can explicity define parameters and they don't have to be in order

#####Call stack
* Variables created in the body of the program are global and can be used anywhere
* Variables created inside a function are local to that function
* You have two variables with the same now, the most recent one will be used
* If you want to modify a global variable inside a function, do `global your_variable`

#####Loops
    for variable in collection:
        do things to variable


* "variable" is any name that you chose
* "collection" can be a string, list, tuple, etc but not a number
* Don't forget the colon to start the loop!

#####If statements
    If your_criteria:
        do something
    elif other_criteria:
        do something else
    else final_criteria:
        do last thing

#####Miscellaneous
* You can assign multiple variables at once `first,second='Grace','Hopper'` assigns Grace to first and Hopper to second
* `Type()` shows you the data type of an object
* `Len()` shows you the length of a string, list, tuple
* Commas concatenate items of any data type and automatically puts a space between them
* Plus signs only concatenate the same data type and smooshes them together directly
* Shape is a variable that contains the number of rows and columns (relevant to dataframes I believe)
* Typical math functions like max, min, mean, std dev are available
* Single equal sign is assignment =
* Double equal sign is a logical check ==
* Short-hand for iterating on a variable `i=i+1` is `i+=1`
