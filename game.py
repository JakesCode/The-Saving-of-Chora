def initLocations():
	descriptions = {"Home Town": "A peaceful town",
	"Jaded Forest Entrance *---": "An opening in the thick wall of tall flowers and robust logs.",
	"Jaded Forest Path -*--": "A pristine woodland, decorated with intricate flowers.",
	"Jaded Forest Clearing --*-": "A circle in the center of the forest. It is covered in strange markings.",
	"Jaded Forest Opening ---*": "The path leads out of the forest here. The sound of water can be heard.",
	"Cobalt Beck *--": "This crystal-clear stream of water gushes past rocks below you.",
	"Cobalt Beck Bridge -*-": "The bridge is sturdy, built with wood from the Jaded Forest.",
	"Cobalt Beck --*": "The path becomes wider here as you enter the next village.",
	"Emelle Village": "Wooden huts populate the lush green land. The village is famous for its fish.",
	"Shaded Path": "A small path in the shade.",
	"Lunar Woods Entrance *-----": "A stunning, blue-tinted forest entrance.",
	"Lunar Woods Path -*----": "Glowing flowers dance in the gentle breeze.",
	"Lunar Woods River --*---": "Turquoise water flows past light-coloured rocks.",
	"Lunar Woods Flower Patch ---*--": "Blue flowers sway with the wind.",
	"Lunar Woods Clearing ----*-": "Light from outside the forest penetrates the glow of the flowers.",
	"Lunar Woods Opening -----*": "The blue glow of the forest weakens as you get further away."}

	locations = ["Home Town",
	"Jaded Forest Entrance *---",
	"Jaded Forest Path -*--",
	"Jaded Forest Clearing --*-",
	"Jaded Forest Opening ---*",
	"Cobalt Beck *--",
	"Cobalt Beck Bridge -*-",
	"Cobalt Beck --*",
	"Emelle Village",
	"Shaded Path",
	"Lunar Woods Entrance *-----",
	"Lunar Woods Path -*----",
	"Lunar Woods River --*---",
	"Lunar Woods Flower Patch ---*--",
	"Lunar Woods Clearing ----*-",
	"Lunar Woods Opening -----*"]

	hostileLocations = ["Jaded Forest Path -*--",
	"Jaded Forest Clearing --*-",
	"Cobalt Beck Bridge -*-",
	"Lunar Woods Flower Patch ---*--"]
	return locations, descriptions, hostileLocations


def enemies(position, ongoingQuests):
	names = ["Cinderman", "Thornfoot"]
	stats = {"Cinderman": 10,
	"Thornfoot": 15}
	enemyDamage = {"Cinderman": 2,
	"Thornfoot": 2}
	if int(position) > 5 and position < 10:
		names = ["Cinderman", "Thornfoot", "Boulderchild", "Vextooth"]
		stats = {"Cinderman": 10,
		"Thornfoot": 15,
		"Boulderchild": 20,
		"Vextooth": 20}
		enemyDamage = {"Cinderman": 2,
		"Thornfoot": 2,
		"Boulderchild": 4,
		"Vextooth": 4}
	elif "Kill the Nightbody" in ongoingQuests and position == 3:
		names = ["Nightbody"]
		stats = {"Nightbody": 40}
		enemyDamage = {"Nightbody": 6}
	elif int(position) > 10 and position < 16:
		names = ["Blue Flower Nymph", "Purple Flower Nymph", "Red Flower Nymph"]
		stats = {"Blue Flower Nymph": 5,
		"Purple Flower Nymph": 5,
		"Red Flower Nymph": 5}
		enemyDamage = {"Blue Flower Nymph": 2,
		"Purple Flower Nymph": 2,
		"Red Flower Nymph": 2}

	return names, stats, enemyDamage


def mainScreen(hostileLocations):
	if any(locations[int(position)] in s for s in hostileLocations):
		cprint(locations[int(position)].center(80), "white", "on_red")
		cprint(descriptions[locations[int(position)]].center(80), "white", "on_red")
	else:
		cprint(locations[int(position)].center(80), "white", "on_cyan")
		cprint(descriptions[locations[int(position)]].center(80), "white", "on_cyan")
	print("")

def death():
	os.system("cls")
	print("")
	print("")
	print("")
	print("")
	print("")
	time.sleep(0.25)
	cprint("                          ╔═╗╔═╗╔╦╗╔═╗   ╔═╗╦  ╦╔═╗╦═╗                         ", "red", "on_white")
	time.sleep(0.25)
	cprint("                          ║ ╦╠═╣║║║║╣    ║ ║╚╗╔╝║╣ ╠╦╝                         ", "red", "on_white")
	time.sleep(0.25)
	cprint("                          ╚═╝╩ ╩╩ ╩╚═╝   ╚═╝ ╚╝ ╚═╝╩╚═                         ", "red", "on_white")
	print("")
	print("")
	print("")
	print("")
	print("")
	time.sleep(0.25)
	time.sleep(0.25)
	print("")
	cprint("                        ╔═╗╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗╔╦╗                       ", "red", "on_white")
	time.sleep(0.25)
	cprint("                        ╚═╗╠═╝╠═╣║  ║╣   ║  ╠═╣ ║║║╣  ║                        ", "red", "on_white")
	time.sleep(0.25)
	cprint("                        ╚═╝╩  ╩ ╩╚═╝╚═╝  ╚═╝╩ ╩═╩╝╚═╝ ╩                        ", "red", "on_white")
	input("")
	leave = True
	# Clear the keyboard buffer #
	while msvcrt.kbhit():
		msvcrt.getch()
	sys.exit()

def effect(givenEffect):
	if givenEffect == "paralyze":
		cprint(("Enemy is paralyzed for two turns!"), "blue", "on_yellow")
		paralyzed = True

	if givenEffect == "invisible":
		cprint(("A dark haze surrounds you, blocking the enemy's view of you."), "blue", "on_yellow")
		invisible = True

	return givenEffect

def battle(strength, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, position):
	global enemyBaseHealth
	global health
	global exp

	enemyGo = True

	enemyChoice = (randint(1,len(names))-1)
	print("")
	os.system("cls")
	mainScreen(hostileLocations)
	if "Kill the Nightbody" in ongoingQuests and position == 3:
		cprint(("The trees above you shake violently as a large creature runs through it."), "white", "on_red")
		cprint(("As you stand, rooted to the spot with fear, a mass of dark flesh and seething\nred eyes appears before you, as if from thin air."), "white", "on_red")
		input("")
		cprint(("As your brain seeks to flee, you feel a rush of adrenaline surge within you.\nGrabbing the Silver Sword you obtained from Zaor, you hold it high and\nprepare to run at the beast."), "white", "on_red")
		cprint(("The Nightbody stares as you with gigantic flame-red eyes and, with a\npiercing shriek, advances towards you...."), "white", "on_red")
		input("")
		os.system("cls")
		mainScreen(hostileLocations)
	else:
		cprint((names[enemyChoice] + " appeared!"), "white", "on_red")
		cprint(("Enemy has " + str(stats[names[enemyChoice]]) + " health!"), "white", "on_red")
	print("")

	enemyBaseHealth = int(stats[names[enemyChoice]])
	enemyName = names[enemyChoice]

	while enemyBaseHealth > 0:
		if int(health)<=0:
			death()

		cprint((enemyName + " Health: " + str(enemyBaseHealth)), "white", "on_red")
		cprint(("Health: " + str(health)), "white", "on_blue")
		cprint(("Mana: " + str(mana)), "white", "on_blue")
		int(health)
		int(mana)
		int(enemyBaseHealth)
		print("")
		cprint("S - Use a Spell", "white", "on_blue")
		cprint("B - Basic Attack (deals " + str(strength) + " damage)", "white", "on_blue")
		cprint("I - Use an Item", "white", "on_blue")
		int(strength)
		print("")
		battleChoice = input("Please enter one of the letters above.... ")
		battleChoice.lower()
		if battleChoice == "b":
			enemyBaseHealth = basicPunch(enemyBaseHealth, strength)
			timer = 0
		elif battleChoice == "i":
			os.system("cls")
			mainScreen(hostileLocations)
			health, timer, strength, mana = itemLib.useItems(playerItems, itemDesc, specialItems, health, strength, mana)
		elif battleChoice == "s":
			int(enemyBaseHealth)
			os.system("cls")
			mainScreen(hostileLocations)
			playerDamageToEnemy, sendEffect, mana = spellLib.useSpell(playerSpells, mana)
			int(enemyBaseHealth)
			int(playerDamageToEnemy)
			enemyBaseHealth -= playerDamageToEnemy

			if sendEffect == "nothing":
				timer = 0
			else:
				givenEffect = effect(sendEffect)
				if sendEffect == "paralyze":
					timer = 2
				elif sendEffect == "invisible":
					timer = 4

		else:
			timer = 0

		input("")
		os.system("cls")
		mainScreen(hostileLocations)

		# Enemy Turn #

		# If the timer ain't 0, say what's happening to the enemy. #
		if timer != 0:
			if givenEffect == "paralyze":
				cprint(("Enemy is paralyzed for " + str(timer) + " more turns!"), "white", "on_cyan")
				print("")
				int(timer)
				enemyGo = False
			elif givenEffect == "invisible":
				cprint(("A mysterious cloak of shadow masks you for " + str(timer) + " more turns!"), "white", "on_cyan")
				print("")
				int(timer)
				enemyGo = True

		if enemyGo == True:
			if enemyBaseHealth > 0:
				enemyHitChance = randint(1,int(enemyBaseHealth))
				int(enemyBaseHealth)
				if enemyHitChance < 3:
					cprint("Enemy Misses!", "white", "on_red")
				else:
					cprint("Enemy Attacks!", "white", "on_red")
					cprint(enemyName + " dealt " + str(enemyDamage[enemyName]) + " damage!", "white", "on_red")
					int(enemyDamage[enemyName])
					health -= enemyDamage[enemyName]
					print("")
					cprint("You now have " + str(health) + " health.", "white", "on_blue")
					int(health)
				input("")
				os.system("cls")
				mainScreen(hostileLocations)
			elif enemyBaseHealth <= 0:
				cprint("The " + enemyName + " dropped to the floor!", "white", "on_red")
				input("")
		else:
			if givenEffect == "paralyze":
				cprint(("The enemy is still paralyzed; rooted to the spot."), "white", "on_cyan")
				cprint(("The enemy will continue to be paralyzed for " + str(timer) + " more turns...."), "white", "on_cyan")
			elif givenEffect == "invisible":
				cprint(("The shadow continues to swirl around you."), "white", "on_cyan")
				cprint(("The shadow will mask you for another " + str(timer) + " turns...."), "white", "on_cyan")

		# If the timer ain't 0, take one off of it, as the round has ended. #
		if timer != 0:
			if (timer-1)==0:
				cprint(("Effect has worn off!"), "blue", "on_yellow")
				enemyGo = True
				timer -= 1


	# BATTLE END #
	os.system("cls")
	mainScreen(hostileLocations)
	endNumber = strength*health
	startNumber = 0
	cprint((enemyName + " defeated!"), "white", "on_magenta")
	cprint(("Strength: " + str(strength)), "white", "on_magenta")
	int(strength)
	cprint(("Health: " + str(health)), "white", "on_magenta")
	int(health)
	cprint(("EXP: " + str(startNumber)), "white", "on_magenta")
	time.sleep(2)
	while startNumber != endNumber:
		os.system("cls")
		mainScreen(hostileLocations)
		startNumber+=1
		cprint((enemyName + " defeated!"), "white", "on_magenta")
		cprint(("Strength: " + str(strength)), "white", "on_magenta")
		int(strength)
		cprint(("Health: " + str(health)), "white", "on_magenta")
		int(health)
		cprint(("EXP: " + str(startNumber)), "white", "on_magenta")
		time.sleep(0.05)
	time.sleep(1)
	os.system("cls")
	mainScreen(hostileLocations)
	cprint(("EXP Gained: " + str(endNumber)), "white", "on_magenta")
	int(endNumber)
	exp += endNumber
	input("")
	os.system("cls")
	mainScreen(hostileLocations)
	if "Kill the Nightbody" in ongoingQuests and position == 3:
		ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health = questLib.completeQuest("Kill the Nightbody", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRequirements,  ongoingQuestsRewards, playerItems, itemDesc, seenDialogues, specialItems, exp, health)
	input("")

def monsterChance(strength, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, position):
	chance = randint(1,20)
	if any(locations[int(position)] in s for s in hostileLocations):
		cprint("(Location is hostile.... watch your step!)", "blue", "on_yellow")
		if chance < 5:
			battle(strength, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, position)
		elif "Kill the Nightbody" in ongoingQuests and position == 3:
			battle(strength, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, position)

def information():
	os.system("cls")
	mainScreen(hostileLocations)
	print("")
	print("Health: " + str(health))
	print("Locaton: " + locations[position])
	print("EXP: " + str(exp))
	int(exp)
	print("Description of Location: " + descriptions[locations[position]])
	print("Player Level: " + str(playerLevel))
	print("")

def showHelp():
	os.system("cls")
	mainScreen(hostileLocations)
	cprint("Commands: ", "red", "on_white")
	print("")
	cprint(("S: See current spells."), "blue", "on_white")
	cprint(("C: See information about your character."), "blue", "on_white")
	cprint(("I: View your items."), "blue", "on_white")
	cprint(("B: Move back one location."), "blue", "on_white")
	cprint(("F: Save the game."), "blue", "on_white")
	cprint(("Q: View your quests."), "blue", "on_white")
	print("")
	print("During battle, colours are used to signal whose turn it is.")
	cprint("White on BLUE signals that it's YOUR turn.", "white", "on_blue")
	cprint("and white on RED signals that it's the ENEMIES turn.", "white", "on_red")
	print("")
	print("Type the letter when the following appears: ")
	print("		Type a command, type 'help', or press enter to move on.... ")
	print("")
	cprint("Press the Enter key to continue....", "blue", "on_white")

def basicPunch(enemyBaseHealth, strength):
	cprint(("Attacked the enemy!"), "grey", "on_green")
	print("")
	cprint(("Dealt " + str(strength) + " damage!"), "grey", "on_green")
	int(strength)
	enemyBaseHealth-=int(strength)
	return enemyBaseHealth

def parseCommand(command, position):
	global health
	global rank
	global strength

	command.lower()

	if command == "help":
		showHelp()
	if command == "c":
		information()
	if command == "f":
		saveLib.save(position, health, strength, exp, playerLevel, playerSpells, playerClass, seenDialogues, rank, playerItems, itemDesc, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)
	if command == "":
		cprint(("You chose to move on...."), "grey", "on_cyan")
		position += 1
	if command == "b":
		if locations[position] == "Home Town":
			cprint(("You can't go back!"), "grey", "on_cyan")
		else:
			cprint(("You chose to go back...."), "grey", "on_cyan")
			position -= 1
	if command == "q":
		questLib.viewQuests(ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)

	if command == "i":
		os.system("cls")
		mainScreen(hostileLocations)
		itemLib.viewItems(playerItems, itemDesc)

	## CLASS STUFF ##
	if command == "frajan":
		health = 24
		spellLib.addSpell("Blink", playerSpells)
		strength = 4
		rank = "Frajan"

	if command == "tezad":
		health = 22
		spellLib.addSpell("Blink", playerSpells)
		strength = 3
		rank = "Tezad"

	if command == "oslid":
		health = 19
		spellLib.addSpell("Blink", playerSpells)
		spellLib.addSpell("Swipe", playerSpells)
		strength = 2
		rank = "Oslid"

	return position

def checkForEvents(playerItems, itemDesc, seenDialogues, specialItems, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, exp, health):
	if position == 1 and seenDialogues == 1:
		os.system("cls")
		mainScreen(hostileLocations)
		print("You need to be careful! Dangerous monsters roam these lands....")
		print("")
		print("Some areas are under control - but others are ruled by evil beasts.")
		print("If an area is unsafe, this will appear at the top of your screen: ")
		print("")
		cprint("(Location is hostile.... watch your step!)", "blue", "on_yellow")
		print("")
		print("If a creature ever attacks you, your best option is to use brute force.")
		print("However, with the right amount of training, you can master spells too.")
		print("")
		print("Spells are more customisable, moving to the will of the user.")
		print("If you use brute force, it's you and your weapon, and nothing else.")
		print("")
		print("If you happen to defeat the entity, you will gain experience points.")
		print("Experience points can be used to hone abilities, and buy weapons and spells.")
		print("")
		print("Good luck!")
		print("")
		cprint("Press the Enter key to continue....", "blue", "on_white")
		input("")
		os.system("cls")
		mainScreen(hostileLocations)

		seenDialogues += 1

	if position == 5 and seenDialogues == 2:
		os.system("cls")
		mainScreen(hostileLocations)
		print("What's this?")
		print("")
		print("There appears to be a small pendant on the ground.")
		print("It is covered in tiny jewels, all of which glint in the sun.")
		print("")
		playerItems, itemDesc, specialItems = itemLib.addItem("Pendant", "A piece of jewellery, covered in small gems.", playerItems, itemDesc, specialItems, None)

		seenDialogues += 1

	if position == 8 and seenDialogues == 3:
		os.system("cls")
		mainScreen(hostileLocations)
		ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health = questLib.completeQuest("Reach Emelle Village", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRequirements,  ongoingQuestsRewards, playerItems, itemDesc, seenDialogues, specialItems, exp, health)
		seenDialogues += 1

	if position == 8 and "Filled Vial" in playerItems and seenDialogues == 4:
		os.system("cls")
		mainScreen(hostileLocations)
		ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health = questLib.completeQuest("Return to Emelle Village", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRequirements,  ongoingQuestsRewards, playerItems, itemDesc, seenDialogues, specialItems, exp, health)
		seenDialogues += 1

	return seenDialogues

def titleScreen():
	print("")
	print("")
	time.sleep(0.05)
	cprint("          \│/  ╔╦╗┬ ┬┌─┐  ╔═╗┌─┐┬  ┬┬┌┐┌┌─┐  ┌─┐┌─┐  ╔═╗┬ ┬┌─┐┬─┐┌─┐  \│/      ", "cyan", "on_red")
	time.sleep(0.05)
	cprint("          ─ ─   ║ ├─┤├┤   ╚═╗├─┤└┐┌┘│││││ ┬  │ │├┤   ║  ├─┤│ │├┬┘├─┤  ─ ─      ", "white", "on_red")
	time.sleep(0.05)
	cprint("          /│\   ╩ ┴ ┴└─┘  ╚═╝┴ ┴ └┘ ┴┘└┘└─┘  └─┘└    ╚═╝┴ ┴└─┘┴└─┴ ┴  /│\      ", "white", "on_red")
	time.sleep(0.05)
	print("")
	print("")
	time.sleep(0.05)
	cprint("                                 \│/  ╔╗ ╦ ╦  \│/                              ", "cyan", "on_white")
	time.sleep(0.05)
	cprint("                                 ─ ─  ╠╩╗╚╦╝  ─ ─                              ", "blue", "on_white")
	time.sleep(0.05)
	cprint("                                 /│\  ╚═╝ ╩   /│\                              ", "blue", "on_white")
	print("")
	time.sleep(0.05)
	print("")
	time.sleep(0.05)
	cprint("              \│/       ╦╔═╗╦╔═╔═╗  ╔═╗╔╦╗╦═╗╦╔╗╔╔═╗╔═╗╦═╗        \│/          ", "cyan", "on_magenta")
	time.sleep(0.05)
	cprint("              ─ ─       ║╠═╣╠╩╗║╣   ╚═╗ ║ ╠╦╝║║║║║ ╦║╣ ╠╦╝        ─ ─          ", "white", "on_magenta")
	time.sleep(0.05)
	cprint("              /│\      ╚╝╩ ╩╩ ╩╚═╝  ╚═╝ ╩ ╩╚═╩╝╚╝╚═╝╚═╝╩╚═        /│\          ", "white", "on_magenta")
	time.sleep(0.05)
	print("")
	time.sleep(0.05)
	print("")
	print("")
	time.sleep(0.05)
	print("")
	time.sleep(0.05)
	cprint("                         ╔═╗╦═╗╔═╗╔═╗╔═╗  ╔═╗╔╗╔╔╦╗╔═╗╦═╗                      ", "cyan")
	time.sleep(0.05)
	cprint("                         ╠═╝╠╦╝║╣ ╚═╗╚═╗  ║╣ ║║║ ║ ║╣ ╠╦╝                      ", "white")
	time.sleep(0.05)
	cprint("                         ╩  ╩╚═╚═╝╚═╝╚═╝  ╚═╝╝╚╝ ╩ ╚═╝╩╚═                      ", "white")
	time.sleep(0.05)

	# Clear the keyboard buffer #
	while msvcrt.kbhit():
		msvcrt.getch()

def intro(seenDialogues):
	os.system("cls")
	mainScreen(hostileLocations)
	print("Adventurer!")
	print("How is it that you're already old enough to go off into the world?")
	print("")
	print("It does not seem two minutes since your father met me....")
	print("He was a very brave individual - and clearly, so are you.")
	print("")
	print("Welcome to the world of Chora!")
	print("The world you live in is very powerful - the earth itself breathes life,")
	print("the creatures themselves hold mystical forces within their strength,")
	print("and the very essence of the world is controlled by ranks of humans!")
	print("")
	cprint("Press the Enter key to continue....", "blue", "on_white")
	input("")

	os.system("cls")
	mainScreen(hostileLocations)
	print("Now.... what rank would you like to be?")
	print("")
	print("FRAJAN            |           TEZAD            |            OSLID")
	print("")
	print("Fearless warriors.     Use magic for leisure.     Hunters with great strength.")
	print("")
	classChoice = input("Please enter either A, B or C.... ")
	classChoice.lower()

	if classChoice=="a" or classChoice=="b" or classChoice=="c":
		if classChoice=="a":
			health = 24
			spellLib.addSpell("Blink", playerSpells)
			strength = 4
			rank = "Frajan"
		if classChoice=="b":
			health = 22
			spellLib.addSpell("Blink", playerSpells)
			strength = 3
			rank = "Tezad"
		if classChoice=="c":
			health = 19
			spellLib.addSpell("Blink", playerSpells)
			spellLib.addSpell("Swipe", playerSpells)
			strength = 2
			rank = "Oslid"
	else:
		print("Please enter something valid....")
		input("")
		os.system("cls")
		seenDialogues = checkForEvents(playerItems, itemDesc, seenDialogues, specialItems, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)

	print("Ah! So you've joined the rank of " + rank + "!")
	print("That means you'll be starting with " + str(health) + " health.")
	int(health)
	print("")
	print("I've also got a quest for you!")
	print("Make it to Emelle Village, and you'll meet some people.")
	print("Do it and you'll get 50 EXP!")
	questLib.addQuest("Reach Emelle Village", "Here we go!", ["Location:Emelle Village"], ["EXP:50"], None, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)
	print("")
	print("Very well then! If you're stuck at any time, type 'help'.")
	print("I wish you luck! Come back and see us sometime....")
	print("")
	cprint("Press the Enter key to continue....", "blue", "on_white")
	input("")
	os.system("cls")
	mainScreen(hostileLocations)
	seenDialogues += 1

	return health, strength, rank, seenDialogues

def init():
	position = 0
	# health (given by the beginning bit)
	# strength (given by the beginning bit)
	exp = 0
	playerLevel = 1
	playerSpells = []
	playerClass = ""
	seenDialogues = 0
	mana = 0
	# rank (given by the beginning bit)

	locations, descriptions, hostileLocations = initLocations()
	spellDict, damage, specialSpells, specialSpellsKeys, spellDict, specialSpells = spellLib.spells()
	itemDesc, playerItems, specialItems = itemLib.itemInit()
	ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = questLib.questInit()
	names, stats, enemyDamage = enemies(position, ongoingQuests)


	return position, exp, playerLevel, playerSpells, playerClass, seenDialogues, locations, descriptions, hostileLocations, names, stats, enemyDamage, damage, specialSpells, specialSpellsKeys, itemDesc, playerItems, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements

# def addLevel(amount):
# 	# Making things easier for the 'checkExpLevel' function. #
# 	global playerLevel

# 	playerLevel += amount
# 	cprint("Level Up!", "red", "on_yellow")
# 	cprint(("You are now level " + str(playerLevel)), "white", "on_red")
# 	int(playerLevel)
# 	input("")
# 	os.system("cls")
# 	mainScreen(hostileLocations)

# def checkExpLevel(playerLevel):
# 	# Checks the level of EXP. If it's high enough, the player goes up a level. #
# 	if exp in range(50, 100):
# 		addLevel(1)
# 		spellLib.addSpell("Swipe", playerSpells)
# 	elif exp in range(101, 200):
# 		addLevel(1)
# 		spellLib.addSpell("Barrage", playerSpells)
# 	elif exp in range(201, 500):
# 		pass

######################## END OF FUNCTIONS ###########################

global playerSpells
global playerItems
global timer
global seenDialogues
global specialItems

# Battle Related #

paralyzed = False
invisible = False
timer = 0

# Custom Libraries #

import spellLib
import itemLib
import dialogueLib
import saveLib
import questLib

# Other Libraries #

from random import randint
import os
import time
from time import sleep
from termcolor import *
import colorama
import sys
import msvcrt
import ast

# Initializing things #

colorama.init()
good, bad, alternate = dialogueLib.initPresets()

######################## END OF SETUP ###########################

os.system("title The Saving of Chora - A Python Text Adventure Game by Jake Stringer")

titleScreen()
input("")
os.system("cls")

cprint("Load a save file?", "white", "on_red")
cprint("Enter 'y' for yes, 'n' for no, or 'r' to make a new file: ", "white", "on_red")
saveChoice = input("?: ")
saveChoice.lower()
if saveChoice == "y":

	position, health, strength, exp, playerLevel, playerSpells, playerClass, seenDialogues, rank, playerItems, itemDesc, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = saveLib.load()
	locations, descriptions, hostileLocations = initLocations()
	names, stats, enemyDamage = enemies(position, ongoingQuests)
	spells, damage, specialSpells, specialSpellsKeys, spellDict, specialSpells = spellLib.spells()
	cprint("Save file loaded successfully.", "white", "on_blue")

	print("")
	cprint(("Health: " + str(health)), "white", "on_magenta")
	int(health)
	cprint(("Strength: " + str(strength)), "white", "on_magenta")
	int(strength)
	cprint(("Mana: " + str(mana)), "white", "on_magenta")
	int(mana)
	cprint(("EXP: " + str(exp)), "white", "on_magenta")
	int(exp)
	print("")
	cprint(("Location: " + locations[position]), "white", "on_magenta")
	cprint("Location description: ", "grey", "on_cyan")
	cprint("    " + descriptions[locations[position]], "grey", "on_cyan")
	if any(locations[int(position)] in s for s in hostileLocations):
		cprint("(Location is hostile.... watch your step!)", "white", "on_red")
	print("")
	cprint(("Items: "), "white", "on_magenta")
	for x in range(0,len(playerItems)):
		cprint(("  " + str(x) + ": " + playerItems[x]), "blue", "on_white")
		int(x)
		cprint(("    " + itemDesc[playerItems[x]]), "blue", "on_white")
	print("")
	cprint(("Spells: "), "white", "on_magenta")
	for x in range(0,len(playerSpells)):
		cprint("  " + str(x) + ": " + playerSpells[x], "white", "on_blue")
		int(x)
		cprint(("  (" + spellDict[playerSpells[x]] + ")"), "white", "on_blue")
		cprint("  Deals " + str(damage[playerSpells[x]]) + " damage", "white", "on_blue")
	questLib.viewQuests(ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)
		
	print("")
	cprint("Press the enter key to return to your game....", "grey", "on_yellow")
	input("")

elif saveChoice == "n":
	cprint("Save file not opened.", "white", "on_red")
	input("")
	position, exp, playerLevel, playerSpells, playerClass, seenDialogues, locations, descriptions, hostileLocations, names, stats, enemyDamage, damage, specialSpells, specialSpellsKeys, itemDesc, playerItems, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = init()
	health, strength, rank, seenDialogues = intro(seenDialogues)
elif saveChoice == "r":
	saveLib.newGame()
	position, exp, playerLevel, playerSpells, playerClass, seenDialogues, locations, descriptions, hostileLocations, names, stats, enemyDamage, damage, specialSpells, specialSpellsKeys, itemDesc, playerItems, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = init()
	health, strength, rank, seenDialogues = intro(seenDialogues)
	cprint("Save file has been wiped.", "white", "on_red")
else:
	print("Nothing valid entered.")
	cprint("Save file not opened.", "white", "on_red")
	input("")
	position, exp, playerLevel, playerSpells, playerClass, seenDialogues, locations, descriptions, hostileLocations, names, stats, enemyDamage, damage, specialSpells, specialSpellsKeys, itemDesc, playerItems, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = init()
	health, strength, rank, seenDialogues = intro(seenDialogues)

input("")
os.system("cls")

while 1<2:
	names, stats, enemyDamage = enemies(position, ongoingQuests)
	locations, descriptions, hostileLocations = initLocations()
	mainScreen(hostileLocations)
	seenDialogues = checkForEvents(playerItems, itemDesc, seenDialogues, specialItems, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, exp, health)
	# questLib.checkQuestCompletion(playerItems, ongoingQuestsRequirements, ongoingQuests, position, locations, ongoingQuestsRewards)
	monsterChance(strength, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, position)
	cprint("Type a command, type 'help', or press enter to move on.... ", "white", "on_blue")
	command = input("?: ")
	position = parseCommand(command, position)

	input("")

	os.system("cls")
