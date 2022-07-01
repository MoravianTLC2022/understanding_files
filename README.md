
## Understanding Files

Goals of this exercise:

* Files exist in a directory structure
* An IDE manipulates the underlying file structure
* The terminal is another way to interact with the file structure
* We can execute code in the terminal (i.e. outside the IDE)
* Programs can read and write files

## Background Material

* FIXME Are there videos or readings in O'Reilly Books? (BJC)


## Run Code in the IDE

1. Clone this repo (in the IDE)
2. Look at the file that the program will manipulate
3. Run the code in the IDE
4. Observe changes in the file

## Run Code in the Termanial

1. Open a terminal window and go to the directory 
  * Right Click (or ctrl-click) on `app.py` and then select "Copy Path"
  * Open a terminal and type `cd`, add a space, and then CMD-V to paste the path
  * Run `ls` to see the files
2. Look at the contents of the files
  * Run `cat list-cities.py` to see the code
  * Run `cat cities.txt` to see the data
3. Run the program from the command line
  * Run `python3 list-cities.py` 
4. Add a city to the `cities.txt` file
  * Run `nano cities.txt`
  * Use the arrows (mouse does not work in nano!) to go to the bottom of the file
  * Add another city name
  * Press ctrl-x to exit and save.
  * Press 'y' to confirm to save
  * Press Enter to confirm the same filename
5. Re-Run the program using `python3 list-cities.py`
6. In the IDE, look at `cities.txt`.  Notice that your city is shown

## Understanding Paths

1. Move the `cities.txt` file into a sub-directory
  * Run `mkdir data` to make a directory called `data`
  * Run `mv cities.txt data` to move the file into this folder
2. Re-run the program.  It will give the following error:

   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'cities.txt'
   ```
3. In `list-cities.py`, change the first line to:

  ```
  file1 = open('data/cities.txt')
  ```

4. Re-run the program to see that it works
5. Go into `data` and run the program with `python ../list_cities` and see that it does not work.
6. Can you explain this behavior?

## (Optional) Clone in Terminal:

1. Clone the repo from the command line to a new destination (git clone)
2. Run the program
3. Edit the program and commit the changes (git status, git add, git 
commit)

