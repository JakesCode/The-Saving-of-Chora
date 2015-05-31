# Item Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()

def useItems(playerItems, itemDesc, specialItems, health, strength, mana):
	keys = list(specialItems.keys())

	for x in range(0,len(playerItems)):
		cprint(str(x) + ": " +  (playerItems[x]), "white", "on_magenta")
		int(x)
		cprint((itemDesc[playerItems[x]]), "white", "on_magenta")
		if any(playerItems[x] in e for e in keys):
			timer = 0
			cprint(("This item has a perk!"), "white", "on_blue")
			if specialItems[playerItems[x]] == "heal":
				cprint(("Heals the player by 20 points."), "grey", "on_cyan")
			elif specialItems[playerItems[x]] == "attack":
				cprint(("Raises the strength of the player by 2, but deals 5 damage to the player."), "grey", "on_cyan")
			elif specialItems[playerItems[x]] == "mana":
				cprint(("Gives the player 10 mana."), "grey", "on_cyan")
			elif specialItems[playerItems[x]] == "heal+":
				cprint(("Heals the player by 50 points."), "grey", "on_cyan")
			elif specialItems[playerItems[x]] == "heal++":
				cprint(("Heals the player by 100 points."), "grey", "on_cyan")
				cprint(("Increases strength by 6."), "grey", "on_cyan")
		print("")
	if len(playerItems) == 0:
		cprint("No items to show!", "blue", "on_white")
		timer = 0
	elif len(playerItems) > 0:
		cprint("Please enter the number of the item you wish to use: ", "magenta", "on_white")
		itemChoice = input("?: ")
		if int(itemChoice) < int(len(playerItems)):
			if any(playerItems[int(itemChoice)] in g for g in specialItems):
				if specialItems[str(playerItems[int(itemChoice)])] == "heal":
					health += 20
					cprint(("Gained 20 health."), "magenta", "on_white")
					del specialItems[str(playerItems[int(itemChoice)])]
					del playerItems[int(itemChoice)]
				elif specialItems[str(playerItems[int(itemChoice)])] == "attack":
					strength += 2
					cprint(("Strength increased by 24."), "magenta", "on_white")
					health -= 5
					cprint(("You took 5 damage!"), "magenta", "on_white")
				elif specialItems[str(playerItems[int(itemChoice)])] == "mana":
					mana += 10
					cprint(("Gained 10 mana."), "magenta", "on_white")
					del specialItems[str(playerItems[int(itemChoice)])]
					del playerItems[int(itemChoice)]
				elif specialItems[str(playerItems[int(itemChoice)])] == "heal+":
					health += 50
					cprint(("Gained 50 health."), "magenta", "on_white")
					del specialItems[str(playerItems[int(itemChoice)])]
					del playerItems[int(itemChoice)]
				elif specialItems[str(playerItems[int(itemChoice)])] == "heal++":
					health += 100
					cprint(("Gained 100 health."), "magenta", "on_white")
					strength += 6
					cprint(("Strength increased by 6."), "magenta", "on_white")
					del specialItems[str(playerItems[int(itemChoice)])]
					del playerItems[int(itemChoice)]
			else:
				cprint(("You can't use that!"), "magenta", "on_white")

	return health, timer, strength, mana


def viewItems(playerItems, itemDesc):
	# Inventory #
	for x in range(0,len(playerItems)):
		cprint((playerItems[x]), "white", "on_magenta")
		cprint((itemDesc[playerItems[x]]), "white", "on_magenta")
		print("")
	if len(playerItems) == 0:
		cprint("No items to show!", "blue", "on_white")

def itemInit():
	itemDesc = {}
	playerItems = []
	specialItems = {}

	return itemDesc, playerItems, specialItems

def addItem(itemName, itemDescription, playerItems, itemDesc, specialItems, perk):
	playerItems.append(itemName)
	itemDesc[itemName] = itemDescription

	if not(perk==None):
		specialItems[itemName] = perk

	cprint(("Gained the " + itemName.upper() + "."), "white", "on_blue")
	input("")

	return playerItems, itemDesc, specialItems

def removeItem(itemName, playerItems, itemDesc):
	playerItems.remove(itemName)
	del itemDesc[itemName]

	# cprint((itemName.upper() + " has been removed from your inventory."), "white", "on_blue")
	# input("")

	return playerItems, itemDesc
