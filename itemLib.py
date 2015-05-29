# Item Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()

def viewItems(playerItems, itemDesc):
	# Inventory #
	for x in range(0,len(playerItems)):
		cprint((playerItems[x]), "white", "on_magenta")
		cprint((itemDesc[playerItems[x]]), "white", "on_magenta")
	if len(playerItems) == 0:
		cprint("No items to show!", "blue", "on_white")

def itemInit():
	itemDesc = {}
	playerItems = []

	return itemDesc, playerItems

def addItem(itemName, itemDescription, playerItems, itemDesc):
	playerItems.append(itemName)
	itemDesc[itemName] = itemDescription

	cprint(("Gained the " + itemName.upper() + "."), "white", "on_blue")
	input("")

	return playerItems, itemDesc

def removeItem(itemName, playerItems, itemDesc):
	playerItems.remove(itemName)
	del itemDesc[itemName]

	cprint((itemName.upper() + " was deleted."), "white", "on_blue")
	input("")

	return playerItems, itemDesc
