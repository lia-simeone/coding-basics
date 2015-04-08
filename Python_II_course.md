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
* Objects have attributes (basic property) and methods (same as function but requires �self� parameter - a reference to the object
* You can reference attributes and methods by doing �object.[attr/method] � note an object needs to be defined before doing this
* You can create a new custom object that inherits qualities of an existing class
* _init_  is a method that will execute when a new Cat object is initialized. It�s specific to each object and can be modified independently (different then class attributes where all objects of that class have the same value and you can�t change it).
* 2 underscores before an attribute name make it private � you cannot see it or modify if you make it private


#####Miscellaneous
* If your dictionary key is a list, you can reference items in the list by sticking the indexing together `seasons['spring'][0]` will return March if seasons is a dictionary and spring is a key
* `range()` is a great way of making arthemetic progressions `range(10)` will create a list containing the numbers 0 to 9