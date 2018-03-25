# this line tell your terminal that it
# will be taking commands instead of the
# script requesting commands.
from sys import argv

# these are the arguements that the terminal 
# will take and use to execute the code.
script, filename = argv

# this line contains the open function 
# which will act on the file and open it whenever
# the text variable is called upon because
# the function is stored as the variable txt.
txt = open(filename)

#this formatted line prints the text which
#pronounces your file name.
print(f"Here's your file {filename}:")
#prints the code stored in the variable txt
#which tells the system to open the script
#and read it.
print(txt.read())

#prompts user to type the  file name again.
print("Type the filename again:")
#tells system to ask for input form user starting
#with the > symbol. Then it stores that input
#in a varible named file_again.
file_again = input("> ")

#we then create another variable names txt_again
#that contains the function to open the file_again
#variable.
txt_again = open(file_again)

#the we print the read version of
# the text_again variable.
print(txt_again.read())