def games_and_systems(game_count, system_count):
	print(f"I have {game_count} games.")
	print(f"And with a total of {game_count} games, I only need {system_count} game systems in order to play all my games.")
	print("It's crazy how many games exist.")
	print("It's also crazy how many game systems are coming out lately.")

print("just entering integers as arguments.")
games_and_systems(400, 10)

print("Now writing variables and including them as arguments for my function.")
xbox_games = 10
xbox = 1
games_and_systems(xbox_games, xbox)

print("now adding math as arguments")
games_and_systems(200 + 200, 4 + 6)

print("Now adding variables and numbers")
games_and_systems(xbox_games + 5, xbox - 1)
