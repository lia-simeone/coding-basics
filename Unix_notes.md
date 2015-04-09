`ls -F` will show you the listings with files and directories specified

Deleting files through Unix is permanent - no recycle bin!
To delete a file, `rm your_file`

By default, `rm` will not delete a non-empty directory
To override, do `rm -r` for recursive. Be very careful!

`cat` will show you the contents of a file in the cmd window (stand for concatenate)

`vi your_file` will create a file called your_file in the working directory and open the vi editor

~ represents the home dir
~another_eid will take you to that person's home directory

`head -your_number` will show you only the top number specified lines from the file
`tail` works the same but starting t the end

> tells the shell to redirect the output to the filename that proceeds (will create or overwrite - think about logs for shell scripts)

A vertical bar | is called a pipe and tells the shell to use the output of the command on the left side as input to the command on the right

*[AB].txt is an OR wildcard meaning look for text files ending in either A or B

Comments use #

history | tail -5 | colrm 1 7 > redo-figure-3.sh
will create a file called redo-figure-3.sh containing the last four commands that I ran
Adding colrm will take out the numbers from the history output, makes it even easier to save and re-run your work

“grep” will search within files, it will look for any matches
“-w” flag will match the word boundaries so only whole word matches
“-n”  flag will give the line numbers of the matches
“-i” flag will make the search case-insensitive
“-v” flag will give you the inverse aka non-match

“find” will search for files or directories,
find . -type d shows dir in pwd and below
find . -type d shows files in pwd and below
maxdepth and mindepth let you control how far below you find will search

For both grep and find, using quotes around the search parameter will prevent the wildcard * from expanding before the command is run


You can create “macro programs” by using a numbered shorthand for the inputs
If your script contains “head -20 $1 | tail -5”
And then you run “bash middle.sh octane.pbd” the $1 will take the first parameter after the script. In this case, octane.pbd
head $2 $1 | tail $3
Will let you run bash middle.sh pentane.pdb -20 -5
$* is a special variable that means all the command-line parameters
Really useful if you want to run a script on all the files in a certain dir, but don’t want to count them


For loops work similar to Python but require a 'done'
    for filename in *.dat
        do
           echo $filename
           head -100 $filename | tail -20
    done
The above will loop through all dat files in the current directory and print lines 81-100 of each file. The echo command prints the individual file names as it loops through and serves as a status check.

Only works in bash
* pressing tab will autocomplete
* up arrow will let you scroll through previous commands
* history will show you all commands run in the current session
* `!command_number` will execute the specified command again
