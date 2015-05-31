# Save Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
import ast
colorama.init()

def newGame():
	newFile = open("saveGame.dat", "w")
	newFile.write("")


def save(position, health, strength, exp, playerLevel, playerSpells, playerClass, seenDialogues, rank, playerItems, itemDesc, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements):
	playerClass = None
	toSave = [position, health, strength, exp, playerLevel, playerSpells, playerClass, seenDialogues, rank, playerItems, itemDesc, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements]
	with open("saveGame.dat", "w") as saveFile:
		for x in range(0,len(toSave)):
			saveFile.write(str(toSave[x]) + "\n")

def load():
	importedData = open("saveGame.dat", "r+").readlines()
	for x in range(0,len(importedData)):
		position = ast.literal_eval(importedData[0])
		health = ast.literal_eval(importedData[1])
		strength = ast.literal_eval(importedData[2])
		exp = ast.literal_eval(importedData[3])
		playerLevel = ast.literal_eval(importedData[4])

		playerSpellsString = importedData[5]
		playerSpells = ast.literal_eval(playerSpellsString)

		# playerClass = ast.literal_eval(importedData[6])
		playerClass = None

		seenDialogues = ast.literal_eval(importedData[7])
		rank = importedData[8]

		playerItemsString = importedData[9]
		playerItems = ast.literal_eval(playerItemsString)

		itemDescString = importedData[10]
		itemDesc = ast.literal_eval(itemDescString)

		specialItemsString = importedData[11]
		specialItems = ast.literal_eval(specialItemsString)

		manaString = importedData[12]
		mana = ast.literal_eval(manaString)

		ongoingQuestsString = importedData[13]
		ongoingQuests = ast.literal_eval(ongoingQuestsString)

		ongoingQuestsDescriptionString = importedData[14]
		ongoingQuestsDescription = ast.literal_eval(ongoingQuestsDescriptionString)

		ongoingQuestsRewardsString = importedData[15]
		ongoingQuestsRewards = ast.literal_eval(ongoingQuestsRewardsString)

		ongoingQuestsRequirementsString = importedData[16]
		ongoingQuestsRequirements = ast.literal_eval(ongoingQuestsRequirementsString)

	return position, health, strength, exp, playerLevel, playerSpells, playerClass, seenDialogues, rank, playerItems, itemDesc, specialItems, mana, ongoingQuests, ongoingQuestsDescription, ongoingQuestsRewards, ongoingQuestsRequirements