import os
import random
import time


os.system("cls")

def intro() :
	print("___ _  _ ____    ___  _ ____ ____    ____ ____ _  _ ____ ")
	print(" |  |__| |___    |  \ | |    |___    | __ |__| |\/| |___ ")
	print(" |  |  | |___    |__/ | |___ |___    |__] |  | |  | |___ ")
	print("                                                        ")
	print("                                                          ")

intro()

input("Let's play a really fun dice game! Please press enter to get started.")

os.system("cls")

print("Awesome! You need two people to play this game. One of you will be Player 1 and the other will be Player 2.")

time.sleep(8.0)
os.system("cls")

playeronename = input("Player 1, please type your name.")
print("Thank you", playeronename)

time.sleep(2.0)
os.system("cls")

playertwoname = input ("Player 2, please type your name.")
print("Thank you", playertwoname)

time.sleep(2.0)
os.system("cls")

print("Alright", playeronename, "and", playertwoname, "now that we assigned which one of you will go first, lets dicuss the rules for this SUPER AWESOME game!")

time.sleep(6.0)
os.system("cls")

def rules() :
	print("So to begin with, you will need a piece of paper. This is pretty much essential just to keep track of who is winning in the game.")
	time.sleep(6.0)
	print("You will have a choice before you begin the game to choose between two different types of die. A 4-sided die or a 6-sided die.")
	time.sleep(6.0)
	print("On the piece of paper you will write out each number on the die. For example, if you had a 6-sided die you would write out 1 2 3 4 5 6. If you had the 4-sided die you would write out 1 2 3 4.")
	time.sleep(10.0)
	print("After you write out the numbers, Player 1 (", playeronename, ") will roll your dice. Whatever numbers you roll on your dice are the numbers you cross out on your paper." )
	time.sleep(10.0)
	print("So for example, if your dice rolls on a 1 and a 3, you cross 1 and 3 out on your paper. If any of your dice rolls on a number you already crossed out, you forfeit your turn and give the dice to your opponent.")
	time.sleep(10.0)
	print("Then Player 2 (", playertwoname, ") will take their turn. And so on and so forth between each player. We will go through 3 rounds.")
	time.sleep(6.0)
	print("By the end of the 3 rounds, the player who crossed out the most numbers is the WINNER.")
	time.sleep(6.0)
	print("If you both have the same amount of numbers crossed out and have a tie, I challenge you to have a rematch and play again!")

rules()

time.sleep(7.0)

print("Alright, let's get started.")

time.sleep(5.0)
os.system("cls")


print("START OF ROUND!")
time.sleep(5.0)
os.system("cls")

print(playeronename, "You're up!")


dicechoice = int (input("Would you like to play with the 4-sided dice or the 6-sided dice? If you chose 4-sided, please type 4. If you chose 6-sided, please type 6."))

time.sleep(3.0)
os.system("cls")

for x in [1,2,3] :
	if dicechoice == 6 :
		print("Remember, you are using the 6-sided dice. Make sure you have 1 2 3 4 5 6 written on your paper.", playeronename, ", your dice will automatically roll for you in a few seconds." )

	if dicechoice == 4  :
		print("Remember, you are using the 4-sided dice. Make sure you have 1 2 3 4 written on your paper.", playeronename, ", your dice will automatically roll for you in a few seconds." )	
		
	time.sleep(8.0)

	if dicechoice == 6 :
		for answer in [1, 2] :
			answer = (random.randint(1,6))
			print("You rolled a", answer)				
			
	elif dicechoice == 4 :
		for answer in [1,2] :
			answertwo = (random.randint(1,4))
			print("You rolled a", answertwo)	

	print(playeronename, "Don't forget to cross out your numbers! We will wait 10 seconds for you to cross them out.")

	time.sleep(10.0)
	os.system("cls")
		
	print(playertwoname, "You're up! Your dice will automatically roll for you in a few seconds")


	time.sleep(5.0)


	if dicechoice == 6 :
		for answer in [1, 2] :
			answer = (random.randint(1,6))
			print("You rolled a", answer)		

	elif dicechoice == 4 :
		for answer in [1,2] :
			answertwo = (random.randint(1,4))
			print("You rolled a", answertwo)		

	print(playertwoname, "Don't forget to cross out your numbers! We will wait 10 seconds for you to cross them out.")

	time.sleep(10.0)
	os.system("cls")
			
	print("END OF ROUND!")			
	time.sleep(5.0)
	os.system("cls")
	
	
print("Now compare your papers, and whoever crossed out the most numbers is THE WINNER!")

time.sleep(5.0)

winner = input("Please type the name of who won! :) ")
loser= input("Please type the name of who lost! :( ")

print("CONGRATS", winner, "! Great job!")

time.sleep(3.0)

print("Better luck next time", loser, ". Maybe you can challenge", winner, "to a rematch!")

time.sleep(5.0)
os.system("cls")

print("Thank you so much for playing and Have a wonderful day!")