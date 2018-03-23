#first variable
types_of_people = 10
#inject variable into string and turn that formatted string into a variable.
x = f"There are {types_of_people} types of people."

#define more variables
binary = "binary"
do_not = "don't"
#inject variable into formatted string whic is stored as the variable y
y = f"Those who know {binary} and those who {do_not}."

#print variable x & y
print(x)
print(y)

#print formatted string containing variables x and y.
#varible y is surrounded by quotes
print(f"I said: {x}")
print(f"I also said: '{y}'")

#a new way to format a string with an embedded variable.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#print string with embedded variable.
print(joke_evaluation.format(hilarious))

#create variables w and e.
w = "This is the left side of..."
e = "a string with a right side."

#concatenate variables w and e and then print them.
#result: one string
print(w + e)