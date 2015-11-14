from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	how_much = int(choice)
	
	if how_much <= 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	elif how_much > 50:
		dead("You greedy bastard!")
	else:
		print "Man, learn to type a number. Let's try again!"
		gold_room()


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	
	while True:
		print "How are you going to move the bear?"
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you than slaps your face off.")
			
		elif choice == "taunt bear":
			print "The bear has moved from the door. You can go through it now."
			
			choice_gold = raw_input("> ")
			
			if choice_gold == "open door":
				gold_room()
			else:
				print "I got no idea what that means."
			
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	print why, "You are dead, good job!"
	exit(0)


def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()
