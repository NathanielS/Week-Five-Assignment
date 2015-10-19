#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	for suite in range(suites):
        for typecard in range(1, typecard+1):
            cards.append(typecard)
    random.shuffle(Deck)
    
    PlayerAHand = deck[:len(Deck)/2]
    PlayerBHand = deck[len(Deck)/2:]
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	'''
	This is the method that plays one round of War
	The method takes PlayerA and PlayerB as input parameters
	and returns PlayerA and PlayerB after modification
	for the round
	
	Remember, high card wins. I have included a convenience
	function getRank(anyCard) that will return the rank.
	
	See the README.md for the variations of
	the game to program.
	'''
	ACard = PlayerAHand.pop()
	BCard = PlayerBHand.pop()
	
	print("Player A plays " + str(getRank(ACard)))
	print("player B plays " + str(getRank(BCard)))
	
	if getRank(ACard) > getRank(BCard):
		print("Player A wins\n")
		PlayerA.insert(0,ACard)
		PlayerA.insert(0,BCard)
	elif getRank(ACard) < getRank(BCard):
		print("Player B wins\n")
		PlayerB.insert(0,ACard)
		PlayerB.insert(0,BCard)
	else:
		PlayerA.append(ACard)
		PlayerB.append(BCard)
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# See the README.md file for instructions on coding 
	# This module.
	print("War")
	if len(PlayerA) > 5 and len(PlayerB) > 5:
		aHand = []
		bHand = []
		for x in range(5):
			aHand.append(PlayerA.pop())
			bHand.append(PlayerB.pop())
			
	if getRank(aHand[4]) > getRank(bHand[4]):
		PlayerA = aHand + bHand + PlayerA
	elif getRank(aHand[4]) < getRank(bHand[4]):
		PlayerB = aHand + bHand + PlayerB
	else:

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

