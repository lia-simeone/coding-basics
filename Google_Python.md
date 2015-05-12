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