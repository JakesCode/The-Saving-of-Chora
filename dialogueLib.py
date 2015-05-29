# Dialogue Library for Python Adventure Game #
# Copyright Jake Stringer 2015 #

from termcolor import *
import colorama
import sys
import os
colorama.init()

def initPresets():

	good = {"grey": "on_cyan"}

	bad = {"grey": "on_red"}

	alternate = {"white": "on_blue"}

	return good, bad, alternate

def say(name, line, preset):
	initPresets()
	presetKeys = list(preset.keys())
	cprint(("****"*9) + name + ("****"*9), presetKeys[0], preset[presetKeys[0]])
	print("")
	print(line)
	print("")
	cprint(("****"*18), presetKeys[0], preset[presetKeys[0]])
	input("")
	print("")