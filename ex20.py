#importing a module argv which allows the
#terminal to input arguments.
from sys import argv
#These are the arguments that the terminal
#will take.
script, input_file = argv
#creating a function named print_all
#that takes the argument 'f'. The function
#print_all reads the argument which will be
#the name of a file, and the prints what it reads.
def print_all(f):
	print(f.read())
#defining a function named rewind which takes
#the argument f. The function itself tells 
#the system to "seek" the beginning of the
#file aka 0.
def rewind(f):
	f.seek(0)
#another function named print_a_line which
#takes two arguments 1) line count and 2) f.
#the function prints the argument entered for 
#line_count, but also prints out the reading
#the file line that the system is on.
def print_a_line(line_count, f):
	print(line_count, f.readline())
#Here we create a variable by the name of
#current_file. This varible opens input_file
current_file = open(input_file)
#prints a line
print("First let's print the whole file:\n")
#call our function print_all which takes the
#argument current_file which was the varible that 
#we defined up above which opens the input file that 
#we specified in our argument via the terminal.
print_all(current_file)
#prints a line
print("Now let's rewind, kind of like a tape.")
#calling on our function "rewind" to seek the
#beginning of current_file which is defined as
#simply opening the input_file that we specified
#in our argument in the terminal.
rewind(current_file)
#printing yet another line.
print("Let's print three lines:")
#defining variable current_line
#as the integer 1. Then calls on the function
#prints_a_line taking the argument current_line
#and current_file. current_line is simply
#the line number as defined in the variable
#and current_file is the input_file that we
#open when calling upon that variable which 
#we defined earlier in the script.
current_line = 1
print_a_line(current_line, current_file)
#current line now defined as 1 + 1 = 2, and
#current_file is read as the next line in
#sequence. This process repeats itself until
#the end.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
