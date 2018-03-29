#Here we create a function named cheese_and_crackers
#which takes the arguments cheese_count and
#boxes_of_crackers. The function prints 4 strings
#2 of which are formatted to include the input
#of the arguments. The last line has a \n 
#which causes a line break.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

#a simple print statement describing a way
#that you can enter arguments into a function.
print("We can just give the function numbers directly:")
#you can enter numbers in directly to the function
cheese_and_crackers(20, 30)

#another print statement explaining that you
#can assign numbers to variables and
#and use them as the arguments of a function
#and it will still work.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#you can also do math within your arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#and you can combine both vavriables and math
#and use them as the arguments and the function
#sill still execute properly.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)