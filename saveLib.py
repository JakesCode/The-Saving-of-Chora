# Save Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()


def save(position, health, strength, exp, playerLevel, playerSpells, specialSpells, playerClass, playerItems, itemDesc, specialItems):
	toSave = [position, health, strength, exp, playerLevel, playerSpells, specialSpells, playerClass, playerItems, itemDesc, specialItems]
	with open("saveGame.dat", "a") as saveFile:
		for x in range(0,len(toSave)):
			saveFile.write(str(toSave[x]) + "\n")

def load():
	importedData = open("saveGame.dat", "r+").readlines()
	for x in range(0,len(importedData)):
		position = importedData[0]
		health = importedData[1]
		strength = importedData[2]
		exp = importedData[3]
		playerLevel = importedData[4]
		playerSpells = importedData[5]
		specialSpells = importedData[6]
		playerClass = importedData[7]
		playerItems = importedData[8]
		itemDesc = importedData[9]
		specialItems = importedData[10]
