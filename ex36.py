from sys import exit

def eddie():
	print("You're in the middle of gunfire!")
	print("Run away! or Start shooting?")

	choice = input("> ")

	if "run" in choice:
		print("You are shot in in the head while running away and find yourself back on the beach")
		start()
	elif "shooting" in choice:
		print("You win the shoot out and become friends with a junkie named Eddie! Congratulations!")
		start()
	else:
		print("Wrong Answer!")
		start()
		

def jake():
	print("You're in the middle of New York and you see a kid about to get hit by a car.")
	print("What do you do?")
	print("Watch the boy get hit or push him out of the way?")

	choice = input("> ")

	if "watch" in choice:
		print("You pathetic soul")
		start()
	elif "push" in choice:
		print("You saved the boy! There are other worlds than these!")
		start()
	else:
		print("indecision is worse than no decision")
		start()

def sussanah():
	print("You are now friends with handicapped schizophrenic woman!")
	start()


def start():
	print("You are in the middle of a beach and three doors stand before you.")
	print("Door 1, Door 2, Door 3")
	print("Which door do you take? 1, 2 or 3?")

	choice = input("> ")

	if choice == "1":
		eddie()
	elif choice == "2":
		jake()
	elif choice == "3":
		sussanah()
	else:
		print("You are eaten alive by the lobstrosities!")

start()
