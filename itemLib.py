# Item Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()

def viewItems():
	# Inventory #
	for x in range(0,len(playerItems)):
		cprint((playerItems[x]), "grey", "on_magenta")
		cprint((itemDesc[playerItems[x]]), "grey", "on_magenta")

def itemInit():
	itemDesc = {}

	return itemDesc

def addItem(itemName, itemDescription, playerItems, itemDesc):
	playerItems.append(itemName)
	itemDesc[itemName] = itemDescription

	cprint(("Gained the " + itemName.upper() + "."), "white", "on_blue")
	input("")

	return playerItems, itemDesc