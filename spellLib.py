# Spell Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()

def spells():
	global spellDict
	global damage
	global specialSpellsKeys
	global specialSpells

	spellDict = {"Blink": "Casts a sharp, dark blanket of shadow over the enemy.",
	"Swipe": "Attack the enemy with a ferocious swipe.",
	"Flux": "Paralyzes the enemy for two turns.",
	"Barrage": "The user runs at full speed into the enemy, inflicting more damage than a basic attack.",
	"Cloak": "Cloaks the user in a veil of shadow, making them impossible to hit."}

	damage = {"Blink": 2,
	"Swipe": 4,
	"Flux": 3,
	"Barrage": 5,
	"Cloak": 2}

	specialSpells = {"Flux": "paralyze",
	"Cloak": "invisible"}

	specialSpellsKeys = specialSpells.keys()

	return spellDict, damage, specialSpells, specialSpellsKeys, spellDict, specialSpells

def addSpell(toBeAdded, playerSpells):
	playerSpells.append(toBeAdded)
	cprint("You just gained the spell " + (toBeAdded.upper()), "white", "on_red")
	cprint(("(" + spellDict[toBeAdded] + ")"), "white", "on_red")
	input("")

def useSpell(playerSpells, mana):
	cprint((("----"*8) + "USE A SPELL" + ("----"*8)), "magenta", "on_white")
	print("")
	for x in range(0,len(playerSpells)):
		cprint(str(x) + ": " + playerSpells[x], "white", "on_blue")
		int(x)
		cprint(("  (" + spellDict[playerSpells[x]] + ")"), "white", "on_blue")
		cprint("  Deals " + str(damage[playerSpells[x]]) + " damage", "white", "on_blue")
		cprint("  Costs " + str(damage[playerSpells[x]]) + " mana", "white", "on_blue")
		print("")
	cprint("Please enter the number of the spell you wish to cast: ", "magenta", "on_white")
	spellChoice = input("?: ")
	if spellChoice == False:
		print("Nothing was entered! Using default spell, Blink, instead.")
		spellChoice = "Blink"
		playerDamageToEnemy = 4

	elif int(spellChoice) < int(len(playerSpells)):
		if not(any(playerSpells[int(spellChoice)] in n for n in specialSpellsKeys)) and int(mana) > damage[playerSpells[int(spellChoice)]]:
			cprint(("You cast a " + playerSpells[int(spellChoice)] + " spell!"), "white", "on_magenta")
			cprint(("Dealt " + str(damage[playerSpells[int(spellChoice)]]) + " damage!"), "white", "on_magenta")
			cprint(("Used " + str(damage[playerSpells[int(spellChoice)]]) + " mana."), "white", "on_magenta")
			playerDamageToEnemy = int(damage[playerSpells[int(spellChoice)]])
			mana -= int(damage[playerSpells[int(spellChoice)]])
			int(playerDamageToEnemy)

			# Since it's not in the special list of spells, no effect will be applied to the enemy. #
			sendEffect = "nothing"
		elif mana < damage[playerSpells[int(spellChoice)]]:
			cprint(("Not enough mana!"), "white", "on_magenta")

			sendEffect = "nothing"
			playerDamageToEnemy = 0
		else:
			effect = specialSpells[playerSpells[int(spellChoice)]]
			if effect == "paralyze":
				sendEffect = "paralyze"
			elif effect == "invisible":
				sendEffect = "invisible"
			else:
				sendEffect = "nothing"

			cprint(("You cast a " + playerSpells[int(spellChoice)] + " spell!"), "white", "on_magenta")
			cprint(("Dealt " + str(damage[playerSpells[int(spellChoice)]]) + " damage!"), "white", "on_magenta")
			playerDamageToEnemy = int(damage[playerSpells[int(spellChoice)]])
			int(playerDamageToEnemy)
	else:
		print("Please enter something valid.")
		input("")
		os.system("cls")
		useSpell(playerSpells)

	return playerDamageToEnemy, sendEffect, mana