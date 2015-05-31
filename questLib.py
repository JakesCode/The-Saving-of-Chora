# Quest Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
import dialogueLib
import itemLib
colorama.init()

def questInit():
	ongoingQuests = []
	ongoingQuestsDescription = {}
	ongoingQuestsRewards = {}
	ongoingQuestsRequirements = {}

	return ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements

# def checkQuestCompletion(playerItems, ongoingQuestsRequirements, ongoingQuests, position, locations, ongoingQuestsRewards):

# 	reward = False

# 	print(ongoingQuests)
# 	input("")

# 	for z in range(0,len(ongoingQuests)):
# 		for w in range(0,len(ongoingQuestsRequirements[ongoingQuests[z]])):
# 			if ongoingQuestsRequirements[ongoingQuests[z]][w][:5] == "Item:":
# 				for v in range(0,len(playerItems)):
# 					if any(playerItems[v] in d for d in (ongoingQuestsRequirements[ongoingQuests[z]][w])[5:]):
# 						print("Item Quest Completed!")
# 						reward = True
# 						toRemove = ongoingQuestsRequirements[ongoingQuests[z]]
# 						toRemove2 = ongoingQuests.remove(ongoingQuests[z])
# 			elif ongoingQuestsRequirements[ongoingQuests[z]][w][:9] == "Location:":
# 				if locations[position] == (ongoingQuestsRequirements[ongoingQuests[z]][w])[9:]:
# 					print("Location Quest Completed!")
# 					toRemove = ongoingQuestsRequirements[ongoingQuests[z]]
# 					toRemove2 = ongoingQuests.remove(ongoingQuests[z])
# 					reward = True

# 	if reward:
# 		keysList = list(ongoingQuestsRequirements.keys())
# 		for x in range(0,len(keysList)):
# 			print(keysList[x])
# 			input("")

# 		# del ongoingQuestsRequirements[ongoingQuestsRequirements]
# 		# ongoingQuests.remove(toRemove2)

def events(eventID, playerItems, itemDesc, seenDialogues, specialItems, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, health):
	good, bad, alternate = dialogueLib.initPresets()

	if eventID == "Reach Emelle Village":
		dialogueLib.say("Alcea", "Oh my! Did you just come from the Jaded Forest?", good)
		dialogueLib.say("Alcea", "Many have rested here recently due to wounds; it seems that \nwe're losing the forest to the beasts.", good)
		dialogueLib.say("Alcea", "It's a terrible shame; if we lose the forest to beasts, then \nwe'll lose access to Home Town....", good)
		dialogueLib.say("Alcea", "If you want to stay here and rest for a while, you're more than welcome to.", good)
		dialogueLib.say("Alcea", "My father, Zaor, will take you in. He'll even give you a potion\nfor half the price of the shops. He was once wounded from fighting, and the\nprices of potions made everything worse - selling them for half price is his\nway of giving something back.", good)
		dialogueLib.say("Zaor", "Ah! You must be from Home Town. The forest is getting worse;\njust yesterday I saw hideous beasts clambering in the treetops - why can't we\n just all group together and kill the damn things?", alternate)
		dialogueLib.say("Zaor", "But still - it seems as though there's hope. If you got through\nthe forest alive, no doubt you're a good fighter....", alternate)
		dialogueLib.say("Zaor", "You know what? My fighting days are over. Take this:", alternate)
		playerItems, itemDesc, specialItems = itemLib.addItem("Silver Sword", "A beautifully crafted blade. The name 'Zaor' is etched into the side.", playerItems, itemDesc, specialItems, "attack")
		dialogueLib.say("Zaor", "I'm sorry about the name in the side, but it'll do you good.\nI've had that sword for 38 years now, and it's never failed my once. Good luck!", alternate)
		dialogueLib.say("Alcea", "Wait, are you going to fight more beasts?", good)
		dialogueLib.say("Alcea", "You know what? I'll assign you a quest!", good)
		dialogueLib.say("Alcea", "It seems that all the monsters are following the actions of a\nleader - and we think we've seen it.", good)
		dialogueLib.say("Zaor", "Alcea - you can't possibly be asking this gentleman to fight\nthe Nightbody?", alternate)
		dialogueLib.say("Alcea", "I am, father - this man seems strong enough to take the beast down!", good)
		dialogueLib.say("Zaor", "(aside, to you) The Nightbody is too powerful.\nYou can't possibly be thinking of fighting it!", alternate)
		dialogueLib.say("Alcea", "Father - he is strong enough. And he shall be even stronger\nafter he uses one of these: ", good)
		playerItems, itemDesc, specialItems = itemLib.addItem("Powerful Potion", "A bottle of pulsing red liquid. It will heal you by 50 points.", playerItems, itemDesc, specialItems, "heal+")
		dialogueLib.say("Alcea", "I made this the other day. It replenishes your health\nwhilst you're in a battle. If you go and kill the Nightbody, grab some of its blood in this: ", good)
		playerItems, itemDesc, specialItems = itemLib.addItem("Vial", "A small tube made of shiny glass.", playerItems, itemDesc, specialItems, None)
		dialogueLib.say("Alcea", "With the blood of the Nightbody, I can make a potion twice\nas powerful as this health potion, with only a drop. You can do it!", good)

		ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = addQuest("Kill the Nightbody", "A fearsome beast has taken residence in the Jaded Forest, preventing the locals from reaching the other town.", ["Item:Nightbody Blood"], ["EXP:200"], "event1", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)

	elif eventID == "Kill the Nightbody":
		cprint(("The beast stares at you with glowing red eyes. As it lifts its claws\nagain, you see that it is getting weaker. As it raises\nits head to try and attack you, a look of pain falls\nacross its face. Falling to the ground with\na huge crash, it is clear that the Nightbody has been slain."), "white", "on_red")
		input("")
		playerItems, itemDesc = itemLib.removeItem("Vial", playerItems, itemDesc)
		cprint(("Remembering the vial that Alcea gave you, you kneel down to the slain creature.\nLetting some of its blackened blood roll out of the wounds it has\nsustained, you wait until it has filled completely - before turning\nyour back to the beast and walking away."), "white", "on_red")
		playerItems, itemDesc, specialItems = itemLib.addItem("Filled Vial", "A vial completely filled with the blood of the Nightbody.", playerItems, itemDesc, specialItems, None)
		input("")
		cprint(("Now that you have the vial, you should return to Emelle Village."), "white", "on_red")
		ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = addQuest("Return to Emelle Village", "Now that the beast has been slain, it's time to return to Emelle Village.", ["Location: Emelle Village"], ["EXP:50"], "event1", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)
		input("")

	elif eventID == "Return to Emelle Village":
		dialogueLib.say("Alcea", "(surprised) I thought I'd sent you to your death! Oh, father, father!", good)
		dialogueLib.say("Zaor", "(running over) We all thought you'd be killed!", alternate)
		dialogueLib.say("Zaor", "But it's amazing to see you back - without a scratch!", alternate)
		if not("Powerful Potion" in playerItems):
			dialogueLib.say("Alcea", "And.... you didn't use the Powerful Potion?! Amazing!", good)
		else:
			dialogueLib.say("Alcea", "I hope the Powerful Potion worked its magic.... I was worried I'd\nmissed something out in the brewing....", good)
		dialogueLib.say("Alcea", "(handing her the filled vial) What? You actually obtained some of the blood?\nIs there no end to your achievements?!", good)
		playerItems, itemDesc = itemLib.removeItem("Filled Vial", playerItems, itemDesc)
		dialogueLib.say("Alcea", "This is amazing! With this, I can make something so powerful, we can take the forest back!", good)
		dialogueLib.say("Zaor", "She will be up all night now! If she begins brewing something, she\nwon't give up until it's perfect for her!", alternate)
		dialogueLib.say("Zaor", "Do stay the night. I'm sure it will heal any wounds you may have.", alternate)
		health += 50
		dialogueLib.say("In the morning", "", bad)
		dialogueLib.say("Zaor", "I hope you rested well!", good)
		dialogueLib.say("Alcea", "We've asked too much of you. Have a gift, from all of us....", good)
		playerItems, itemDesc, specialItems = itemLib.addItem("Red Sigil", "A piece of fabric with a red symbol on it.", playerItems, itemDesc, specialItems, None)
		dialogueLib.say("Alcea", "That's a Sigil. If you collect all of them, they say something will\nhappen. Each village knows its own sigil, but nobody else's.", good)
		dialogueLib.say("Alcea", "I think you should go for them all!", good)
		dialogueLib.say("Zaor", "Yes! Oh, Alcea - shouldn't you be giving our friend here\nsomething else?", alternate)
		dialogueLib.say("Alcea", "Oh! How could I forget?", good)
		playerItems, itemDesc, specialItems = itemLib.addItem("Nightbody Potion", "A dark liquid with a black haze circling it.", playerItems, itemDesc, specialItems, "heal++")


		return ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, health


def completeQuest(questToBeCompleted, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRequirements,  ongoingQuestsRewards, playerItems, itemDesc, seenDialogues, specialItems, exp, health):
	for x in range(0, len(ongoingQuests)):
		if ongoingQuests[x] == questToBeCompleted:
			# Events
			event = ongoingQuests[x]
			events(event, playerItems, itemDesc, seenDialogues, specialItems, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, health)
			# # Rewards
			# input("")
			# reward = ongoingQuestsRewards[ongoingQuests[x]]
			# for x in range(0,len(ongoingQuestsRewards[ongoingQuests[x]])):
			# 	if ongoingQuestsRewards[ongoingQuests[x]] == None:
			# 		pass
			# 	elif ongoingQuestsRewards[ongoingQuests[x]][:4] == "EXP:":
			# 		exp += int(ongoingQuestsRewards[ongoingQuests[x]][4:])
			# Delete it
			del ongoingQuestsDescription[ongoingQuests[x]]
			del ongoingQuestsRewards[ongoingQuests[x]]
			del ongoingQuestsRequirements[ongoingQuests[x]]


	return ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health

def addQuest(questName, questDescription, requirements, rewards, event, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements):

	ongoingQuests.append(questName)
	ongoingQuestsDescription[questName] = questDescription
	ongoingQuestsRequirements[questName] = requirements
	ongoingQuestsRewards[questName] = rewards
	cprint(("Quest Added!"), "grey", "on_white")
	cprint(("    " + questName), "grey", "on_white")
	cprint(("    " + questDescription), "grey", "on_white")
	print("")

	return ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements


def viewQuests(ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements):
	for x in range(0,len(ongoingQuests)):
		cprint((str(x) + ": " + ongoingQuests[x]), "grey", "on_white")
		cprint(("  " + ongoingQuestsDescription[ongoingQuests[x]]), "grey", "on_white")
		cprint(("    Requirements:"), "grey", "on_white")
		for z in range(0,len(ongoingQuestsRequirements[ongoingQuests[x]])):
			if (ongoingQuestsRequirements[ongoingQuests[x]][z])[:5] == "Item:":
				ongoingQuestsRequirements[ongoingQuests[x]][z] = ongoingQuestsRequirements[ongoingQuests[x]][z][5:]
				cprint(("      " + ongoingQuestsRequirements[ongoingQuests[x]][z]), "grey", "on_white")
			elif (ongoingQuestsRequirements[ongoingQuests[x]][z])[:9] == "Location:":
				ongoingQuestsRequirements[ongoingQuests[x]][z] = ongoingQuestsRequirements[ongoingQuests[x]][z][9:]
				cprint(("      Reach " + ongoingQuestsRequirements[ongoingQuests[x]][z]), "grey", "on_white")
		cprint(("    Rewards:"), "grey", "on_white")
		for y in range(0,len(ongoingQuestsRewards[ongoingQuests[x]])):
			if (ongoingQuestsRewards[ongoingQuests[x]][y])[:4] == "EXP:":
				ongoingQuestsRewards[ongoingQuests[x]][y] = ongoingQuestsRewards[ongoingQuests[x]][y][4:]
				cprint(("      " + ongoingQuestsRewards[ongoingQuests[x]][y] + " EXP"), "grey", "on_white")




# locations = ["Home Town",
# 	"Jaded Forest Entrance *---",
# 	"Jaded Forest Path -*--",
# 	"Jaded Forest Clearing --*-",
# 	"Jaded Forest Opening ---*",
# 	"Cobalt Beck *--",
# 	"Cobalt Beck Bridge -*-",
# 	"Cobalt Beck --*",
# 	"Emelle Village",
# 	"Shaded Path"]

# itemDesc, playerItems, specialItems = itemLib.itemInit()
# seenDialogues = 0

# health = 10
# exp = 10

# position = 8
# playerItems = ["Vial"]
# itemDesc = {"Vial": "It's a fucking vial."}


# ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = questInit()

# ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements = addQuest("Kill the Nightbody", "A fearsome beast has taken residence in the Jaded Forest, preventing the locals from reaching the other town.", ["Item:Nightbody Blood"], ["EXP:200"], "event1", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements)

# input("")


# ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health = completeQuest("Kill the Nightbody", ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements, playerItems, itemDesc, seenDialogues, specialItems, exp, health)

# input("")