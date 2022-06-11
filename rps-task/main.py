import random

print('Welcome To GameTown\n Choose Wisely, The CPU Knows All,\n R = Rock\n P = Paper\n S = Scissors')  

while True:
	player = input("Enter a choice (R, P, S): ")
	possible_actions = ["R", "P", "S"]
	cpu = random.choice(possible_actions)
	print(f"\nYou chose {player}, CPU {cpu}.\n")

	if player == cpu:
		print(f"Both players selected {player}. It's a tie!")
	elif player == "R":
		if cpu == "scissors":
			print("Rock smashes scissors! You win!")
		else:
			print("Paper covers rock! You lose.")
		break
	elif player == "P":
		if cpu == "rock":
			print("Paper covers rock! You win!")
		else:
			print("Scissors cuts paper! You lose.")
		break
	elif player == "S":
		if cpu == "paper":
			print("Scissors cuts paper! You win!")
		else:
			print("Rock smashes scissors! You lose.")
		break
	else:
		print("That's not a valid play. Check your spelling!")