
## Understanding Files

Goals of this exercise:

* Files exist in a directory structure
* An IDE manipulates the underlying file structure
* The terminal is another way to interact with the file structure
* We can execute code in the terminal (i.e. outside the IDE)
* Programs can read and write files

## Background Material

* FIXME Are there videos or readings in O'Reilly Books? (BJC)


## Steps

Review:

1. Clone this repo (in the IDE)
2. Look at the file that the program will manipulate
3. Run the code in the IDE
4. Observe changes in the file

New material:

1. Open a terminal window and go to the directory (cd, ls)
2. Look at the contents of the files (cat, less)
3. Run the program from the command line (python3)
4. Look at the changes in the file (cat, less)
5. Edit the file from the command (nano); change is seen in IDE


Clone in Terminal:

1. Clone the repo from the command line to a new destination (git clone)
2. Run the program
3. Edit the program and commit the changes (git status, git add, git 
commit)


Paths:

1. Make a directory called `data` and move the `cities.txt` into this folder
2. Re-run the program - file not found error

   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'cities.txt'
   ```
3. Change the python code to add the diretory name
4. Re-run the program to see that it works
5. Go into `data` and run the program with `python ../list_cities` and see that it does not work.

