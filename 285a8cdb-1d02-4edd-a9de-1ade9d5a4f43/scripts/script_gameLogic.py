L3_firstCheck = "26-"
L3_secondCheck = "27-"
L3_thirdCheck = "28-"

smallTableName = "dissidia_1"
bigTableName = "dissidia_2"

smallTableName_solid = "solid_1"
bigTableName_solid = "solid_2"

bossTableName = "boss_solid_2"

def gameLogic_query_activePlayer():
	mute()
	if (len(players) == 1): return players[0]
	return getActivePlayer()
	
def gameLogic_query_inactivePlayer():
	mute()
	if (len(players) == 1): return players[0]
	return players[1] if (getActivePlayer() == players[0]) else players[0]
	
def gameLogic_query_otherPlayer():
	mute()
	if (len(players) == 1): return players[0]
	return players[1] if (players[0] == me) else players[0]
	
def gameLogic_query_boss_playerOne():
	mute()
	if (getGlobalVariable("global_BossFight") == "FALSE"): return None
	
	global_BossFight_PlayerOne_ID = getGlobalVariable("global_BossFight_PlayerOne_ID")
	foundPlayer = None
	for p in players:
		pID = str(p._id)
		if (pID == global_BossFight_PlayerOne_ID):
			foundPlayer = p
			break
	return foundPlayer
	
def gameLogic_query_boss_playerTwo():
	mute()
	if (getGlobalVariable("global_BossFight") == "FALSE"): return None
	
	global_BossFight_PlayerTwo_ID = getGlobalVariable("global_BossFight_PlayerTwo_ID")
	foundPlayer = None
	for p in players:
		pID = str(p._id)
		if (pID == global_BossFight_PlayerTwo_ID):
			foundPlayer = p
			break
	return foundPlayer
	
def gameLogic_query_boss_playerThree():
	mute()
	if (getGlobalVariable("global_BossFight") == "FALSE"): return None
	
	global_BossFight_PlayerThree_ID = getGlobalVariable("global_BossFight_PlayerThree_ID")
	foundPlayer = None
	for p in players:
		pID = str(p._id)
		if (pID == global_BossFight_PlayerThree_ID):
			foundPlayer = p
			break
	return foundPlayer
	
def gameLogic_query_boss_boss():
	mute()
	if (getGlobalVariable("global_BossFight") == "FALSE"): return None
	
	global_BossFight_Boss_ID = getGlobalVariable("global_BossFight_Boss_ID")
	foundPlayer = None
	for p in players:
		pID = str(p._id)
		if (pID == global_BossFight_Boss_ID):
			foundPlayer = p
			break
	return foundPlayer
	
def gameLogic_boss_heroesReady():
	mute()
	me.setGlobalVariable("readyToPlay", "TRUE")
	
def gameLogic_utility_simulate_playerOne(group, x = 0, y = 0):
	mute()
	gameLogic_utility_simulate("P1")
	
def gameLogic_utility_simulate_playerTwo(group, x = 0, y = 0):
	mute()
	gameLogic_utility_simulate("P2")
	
def gameLogic_utility_simulate_playerThree(group, x = 0, y = 0):
	mute()
	gameLogic_utility_simulate("P3")
	
def gameLogic_utility_simulate_boss(group, x = 0, y = 0):
	mute()
	gameLogic_utility_simulate("Boss")
	
def gameLogic_utility_simulate_stop(group, x = 0, y = 0):
	mute()
	gameLogic_utility_simulate("-1")
	
def gameLogic_utility_simulate(simulationType):
	mute()
	setGlobalVariable("global_BossFight_DebugUser_ID", simulationType)
	
def query_forceLoad():
	mute()
	rnd(1, 2)
	update()
	
def gameLogic_event_tableLoaded():
	mute()
	# table.board = "ff7remake_1"
	
	tempCardID = "758f8f9a-f5b8-4ca0-b955-489e21c44d3e"
	tempCard1 =  table.create(tempCardID, -900, -400)
	
	gameLogic_addLimitBreakDeck(table, 0, 0)
	
	for p in players:
		remoteCall(p, "gameLogic_event_showVersion", [me._id])
		remoteCall(p, "gameLogic_resetCamera", [me._id])

def gameLogic_event_deckLoaded(isLimited):
	mute()
	
	lbCards = (card for card in me.piles["Deck"] 
				if card.controller == me 
				and cardLogic_ability_find(card, "LimitBreak") != "N/A")
	for lbCard in lbCards:
		lbCard.moveTo(me.piles["LB Deck"])
	
def gameLogic_event_showVersion(aPlayer):
	mute()
	# table.board = bigTableName
	if (aPlayer == me._id): 
		notify("{} - Client Version: {}".format(me, gameVersion))
		whisper("Load your deck, then press Tab to select deck format.")
		# whisper("Upcoming online tournament 'Zanarkand III - The Grand Summoning'! Join at: https://discord.gg/punrhPtKT5")
	
def gameLogic_event_gameStarted():
	mute()
	# whisper("gameLogic_event_gameStarted")
	global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
	if (global_UsePlaymat == "TRUE"):
		global_UseDamageZone = getGlobalVariable("global_UseDamageZone");
		if (global_UseDamageZone == "TRUE"):
			table.board = bigTableName
		else:
			table.board = smallTableName
	else:
		setGlobalVariable("global_UseDamageZone", "FALSE")
		table.board = ""
	
def gameLogic_event_overrideGameReset():
	mute()
	# whisper("gameLogic_event_overrideGameReset")
	
	theChoices = ["Keep Decks", "Reset Decks", "Cancel"]
	theColors = ["#660000", "#660000", "#111111"]
	askChoiceResult = askChoice("Keep current decks, or reset to load new ones?", theChoices, theColors)
	
	if (askChoiceResult == 1 or askChoiceResult == 2):
		theChoices2 = ["Yes", "No"]
		theColors2 = ["#660000", "#111111"]
		askChoiceResult2 = askChoice("Are you sure you want to reset the game?", theChoices2, theColors2)
		
		if (askChoiceResult2 == 1):
			setGlobalVariable("global_Phase", "N/A")
			setGlobalVariable("global_FirstDraw", "TRUE")
			notify("{} has reset the game.".format(me))
		
			if (askChoiceResult == 1):
				for p in players:
					remoteCall(p, "gameLogic_resetDecks", [me._id])
			elif (askChoiceResult == 2):
				for p in players:
					remoteCall(p, "gameLogic_deleteDecks", [me._id])
					
			global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
			if (global_UsePlaymat == "TRUE"):
				global_UseDamageZone = getGlobalVariable("global_UseDamageZone");
				if (global_UseDamageZone == "TRUE"):
					table.board = bigTableName
				else:
					table.board = smallTableName
			else:
				setGlobalVariable("global_UseDamageZone", "FALSE")
				table.board = ""
		
def gameLogic_resetDecks(aPlayer):
	mute()
	if (aPlayer == me._id): 
		myCards = (card for card in table
					if card.controller == me)
		for aCard in myCards:
			aCard.moveTo(me.Deck)
			
		for aCard in me.hand:
			aCard.moveTo(me.Deck)
			
		for aCard in me.piles["Break Zone"]:
			aCard.moveTo(me.Deck)
			
		for aCard in me.piles["Damage Zone"]:
			aCard.moveTo(me.Deck)
			
		for aCard in me.piles["Removed From Game"]:
			aCard.moveTo(me.Deck)
			
		for aCard in me.Deck:
			# aCard.TypeContainer = aCard.Type
			# aCard.ElementContainer = aCard.Element
			# aCard.JobContainer = aCard.Job
			# aCard.Active = "FALSE"
			# cardLogic_set_powerContainer(aCard, 0, 0, 0)
			aCard.resetProperties()
			
		me.Deck.shuffle()
		
		cardLogic_resetCPCounters()
		me.counters["Damage Taken"].value = 0
		
		me.setGlobalVariable("readyToPlay", "FALSE")
		
		gameLogic_addLimitBreakDeck(table)
	
def gameLogic_deleteDecks(aPlayer):
	mute()
	if (aPlayer == me._id): 
		myCards = (card for card in table 
					if card.controller == me)
		for aCard in myCards:
			aCard.delete()
			
		for aCard in me.hand:
			aCard.delete()
			
		for aCard in me.piles["Break Zone"]:
			aCard.delete()
			
		for aCard in me.piles["Damage Zone"]:
			aCard.delete()
			
		for aCard in me.piles["Removed From Game"]:
			aCard.delete()
			
		for aCard in me.piles["LB Deck"]:
			aCard.delete()
			
		for aCard in me.Deck:
			aCard.delete()
			
		cardLogic_resetCPCounters()
		me.counters["Damage Taken"].value = 0
			
		me.setGlobalVariable("readyToPlay", "FALSE")
		
		gameLogic_addLimitBreakDeck(table)
		
def gameLogic_utility_turnPlaymatOnOrOff(group, x = 0, y = 0):
	mute()
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "TRUE"): return
	
	global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
	if (global_UsePlaymat == "TRUE"):
		setGlobalVariable("global_UsePlaymat", "FALSE")
		setGlobalVariable("global_UseDamageZone", "FALSE")
		table.board = ""
		notify("The playmat has been turned off.")
	else:
		setGlobalVariable("global_UsePlaymat", "TRUE")
		setGlobalVariable("global_UseDamageZone", "TRUE")
		table.board = bigTableName
		notify("The playmat has been turned on.")
		
def gameLogic_utility_turnSolidPlaymatOnOrOff(group, x = 0, y = 0):
	mute()
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "TRUE"): return
	
	global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
	if (global_UsePlaymat == "FALSE"):
		setGlobalVariable("global_UsePlaymat", "TRUE")
		global_UseDamageZone = getGlobalVariable("global_UseDamageZone")
		if (global_UseDamageZone == "TRUE"):
			table.board = bigTableName_solid
		else:
			table.board = smallTableName_solid
	else:
		if (table.board == bigTableName):
			table.board = bigTableName_solid
		elif (table.board == bigTableName_solid):
			table.board = bigTableName
		elif (table.board == smallTableName):
			table.board = smallTableName_solid
		elif (table.board == smallTableName_solid):
			table.board = smallTableName
		
def gameLogic_utility_turnDamageZoneOnOrOff(group, x = 0, y = 0):
	mute()
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "TRUE"): return
	global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
	if (global_UsePlaymat == "FALSE"): return
	
	global_UseDamageZone = getGlobalVariable("global_UseDamageZone")
	if (global_UseDamageZone == "TRUE"):
		setGlobalVariable("global_UseDamageZone", "FALSE")
		table.board = smallTableName
		
		for p in players:
			remoteCall(p, "gameLogic_removeDamageZoneCardsFromTable", [me._id])
	else:
		setGlobalVariable("global_UseDamageZone", "TRUE")
		table.board = bigTableName
		
		for p in players:
			remoteCall(p, "gameLogic_addDamageZoneCardsToTable", [me._id])
			
def gameLogic_utility_turnBossPlaymatOnOrOff(group, x = 0, y = 0):
	mute()
	tempCardID1 = "30aeae70-459b-40aa-9b52-7b281d4d01c1"
	tempCardID2 = "c2de2d63-c055-4aa5-b120-05fba71c77a1"
	
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "TRUE"):
		setGlobalVariable("global_BossFight", "FALSE")
		table.board = smallTableName
		setGlobalVariable("global_UsePlaymat", "TRUE")
		setGlobalVariable("global_UseDamageZone", "FALSE")
		gameLogic_utility_turnDamageZoneOnOrOff(group, x, y)
		# table.height = "800"
		
		# tempCard1 =  table.create(tempCardID1, -900, -500)
	else:
		setGlobalVariable("global_BossFight", "TRUE")
		table.board = bossTableName
		setGlobalVariable("global_UsePlaymat", "TRUE")
		setGlobalVariable("global_UseDamageZone", "TRUE")
		# table.height = "2000"
		
		# tempCard1 =  table.create(tempCardID2, -900, -500)
		
		okCardID = "cc65c309-aaf9-46c5-b6b2-3c9e9f12cbd5"
		errorCardID = "e872ca8a-621e-4d68-b175-9ed9fe5967b6"
		waitCardID = "6b8d8f3f-b59e-4942-b171-e90f4419452a"
		
		table.create(okCardID, 663, 227)
		table.create(errorCardID, 796, 227)
		table.create(waitCardID, 929, 227)
		
		table.create(okCardID, 663, 620)
		table.create(errorCardID, 796, 620)
		table.create(waitCardID, 929, 620)
		
		table.create(okCardID, 663, 1013)
		table.create(errorCardID, 796, 1013)
		table.create(waitCardID, 929, 1013)
		
	table.reset()
	for p in players:
		remoteCall(p, "gameLogic_resetCamera_boss", [me._id])
		
def gameLogic_removeDamageZoneCardsFromTable(aPlayer):
	mute()
	if (aPlayer == me._id): 
		myCards = (card for card in table 
					if card.controller == me 
					and card.Type == "DamageZone")
		for aCard in myCards:
			aCard.delete()
			
def gameLogic_addDamageZoneCardsToTable(aPlayer):
	mute()
	if (aPlayer == me._id): 
		posX = 0
		posY = 0
		incrementY = 0
		playerOne = True if (me._id == 1) else False
		if (playerOne == True):
			posX = -826
			posY = -3
			incrementY = 24
		else:
			posX = 726
			posY = -139
			incrementY = -20
			
		damageCardArray = []
		for aCard in me.piles["Damage Zone"]:
			damageCardArray.append(aCard)
		damageCardArray.reverse()
	
		damageCount = 0
		for aCard in damageCardArray:
			newCard = table.create(aCard.model, posX, posY + (incrementY * damageCount))
			newCard.Active = "FALSE"
			newCard.Type = "DamageZone"
			newCard.orientation = 1
			damageCount = damageCount + 1
		
def gameLogic_utility_declareReaction(group, x = 0, y = 0):
	mute()
	playSound("reaction")
	notify("{} has a reaction!".format(me))
	
def gameLogic_setup_readyPlayer():
	mute()
	readyToPlay = me.getGlobalVariable("readyToPlay")
	if (readyToPlay == "TRUE"):
		whisper("{} is already ready to play.".format(me))
		return
		
	deckLength = len(me.Deck)
	if (deckLength == 0):
		whisper("You must first load a deck before playing.")
		return
		
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "FALSE"): 
		deckErrorMessage = ""
			
		formats = ["Standard", "L3 Constructed", "Title", "Draft/Prerelease", "Custom"] # "Boss"
		formatColors = ["#9D2411", "#5394AE", "#508362", "#b2a43d", "#8b5e89"] # "#484141"
		askChoiceResult = askChoice("Please choose your deck format:", formats, formatColors)
		if (askChoiceResult == 0): return
		askChoiceString = "N/A"
		
		if (askChoiceResult == 4):
			askChoiceString = "Draft/Prerelease"
			
			if (len(me.Deck) < 40):
				deckErrorMessage += "For the {} format, your deck should contain at least 40 cards.".format(askChoiceString)
		elif (askChoiceResult == 5):
			askChoiceString = "Custom"
		else:
			if (askChoiceResult == 1):
				askChoiceString = "Standard"
			elif (askChoiceResult == 2):
				askChoiceString = "L3 Constructed"
				
				olderCards = []
				for aCard in me.Deck:
					if (aCard.SetNumber.startswith(L3_firstCheck) == False and aCard.SetNumber.startswith(L3_secondCheck) == False and aCard.SetNumber.startswith(L3_thirdCheck) == False):
						olderCards.append(cardLogic_get_fullNameString(aCard))
						
				if (len(olderCards) > 0):
					olderCards = list(dict.fromkeys(olderCards))
					olderCards.sort()
					if (deckErrorMessage != ""): deckErrorMessage += "\n\n"
					deckErrorMessage += "The following cards were not released within the last three sets for L3 Constructed format:"
					for olderCard in olderCards:
						deckErrorMessage += "\n- {}".format(olderCard)
					
			elif (askChoiceResult == 3):
				askChoiceString = "Title"
			elif (askChoiceResult == 6):
				askChoiceString = "Boss"
				askChoice("For best results, the Boss should be the person that hosted/created this room.", ["OK"], ["#111111"])
				
			if (len(me.Deck) != 50):
				if (deckErrorMessage != ""): deckErrorMessage += "\n\n"
				deckErrorMessage += "For the {} format, your deck should contain exactly 50 cards.".format(askChoiceString)
				# return
			
		cardNameList = []
		tooManyOfCardNameList = []
		bannedCardNames = []
		for aCard in me.Deck:
			aCardName = cardLogic_get_fullNameString(aCard)
			
			if (askChoiceString != "Draft/Prerelease"):
				cardNameList.append(aCardName)
				if (cardNameList.count(aCardName) > 3):
					if (aCardName not in tooManyOfCardNameList):
						tooManyOfCardNameList.append(aCardName)
			
			anAbility = cardLogic_ability_find(aCard, "BannedInFormat")
			if (anAbility != "N/A"):
				anAbilityList = anAbility.split("|")
				listOfBannedFormats = anAbilityList[1].split(",")
				if (askChoiceString in listOfBannedFormats):
					if (aCardName not in bannedCardNames):
						bannedCardNames.append(aCardName)
						
		if (len(tooManyOfCardNameList) > 0 and askChoiceString != "Custom"):
			if (deckErrorMessage != ""): deckErrorMessage += "\n\n"
			deckErrorMessage += "Your deck contains too many copies of the following cards:"
			for aTooManyCardName in tooManyOfCardNameList:
				deckErrorMessage += "\n- {}".format(aTooManyCardName)
			# return
		
		if (len(bannedCardNames) > 0):
			if (deckErrorMessage != ""): deckErrorMessage += "\n\n"
			deckErrorMessage += "The following card(s) in your deck are currently banned from {} format:".format(askChoiceString)
			for aBannedCardName in bannedCardNames:
				deckErrorMessage += "\n- {}".format(aBannedCardName)
			# return
			
		if (deckErrorMessage != ""):
			playSound("error")
			notify("There is an error with {}'s Deck and they will have to reload.".format(me))
			askChoice(deckErrorMessage, ["OK"], ["#111111"])
			return
		
		notify("{} is ready to play. (Format: {})".format(me, askChoiceString))
		
		me.setGlobalVariable("deckFormat", askChoiceString)
		me.setGlobalVariable("readyToPlay", "TRUE")
		
		if (len(players) == 1):
			setGlobalVariable("global_Phase", "AlmostReady")
		elif (len(players) == 2):
			otherPlayer = gameLogic_query_otherPlayer()
			if (otherPlayer.getGlobalVariable("readyToPlay") == "TRUE"):
				myDieRoll = rnd(1, 6)
				theirDieRoll = rnd(1, 6)
				while (myDieRoll == theirDieRoll):
					myDieRoll = rnd(1, 6)
					theirDieRoll = rnd(1, 6)
				notify("-----")
				notify("A die roll has taken place to determine who should go first:")
				notify("- {} rolled a {}.".format(me, myDieRoll))
				notify("- {} rolled a {}.".format(otherPlayer, theirDieRoll))
				notify("When ready, the player going first can press the Tab key to begin.")
				notify("-----")
				setGlobalVariable("global_Phase", "AlmostReady")
				
				for p in players:
					remoteCall(p, "gameLogic_phases_outputFirstPlayerMessage", [me, myDieRoll, otherPlayer, theirDieRoll])
		# elif (len(players) == 3 or len(players) == 4):
		# 	allGood = False
		# 	for p in players:
		# 		if (p.getGlobalVariable("readyToPlay") == "FALSE"):
		# 			allGood = False
		# 	
		# 	if (allGood == True):
		# 		setGlobalVariable("global_Phase", "AlmostReady")
		else:
			playSound("error")
			askChoice("There are an incorrect number of players found.", ["OK"], ["#111111"])
			return
	else:
		gameLogic_setup_readyPlayer_bossFight()

def gameLogic_setup_readyPlayer_bossFight():
	mute()
	# whisper("Boss fight!")
	
	global_BossFight_PlayerOne_ID = getGlobalVariable("global_BossFight_PlayerOne_ID")
	global_BossFight_PlayerTwo_ID = getGlobalVariable("global_BossFight_PlayerTwo_ID")
	global_BossFight_PlayerThree_ID = getGlobalVariable("global_BossFight_PlayerThree_ID")
	global_BossFight_Boss_ID = getGlobalVariable("global_BossFight_Boss_ID")
	
	p1String = "Player One"
	p2String = "Player Two"
	p3String = "Player Three"
	bossString = "Boss"
	
	if (global_BossFight_PlayerOne_ID != "-1"): p1String = "Player One (Taken)"
	if (global_BossFight_PlayerTwo_ID != "-1"): p2String = "Player Two (Taken)"
	if (global_BossFight_PlayerThree_ID != "-1"): p3String = "Player Three (Taken)"
	if (global_BossFight_Boss_ID != "-1"): bossString = "Boss (Taken)"
	
	theChoices = [p1String, p2String, p3String, bossString, "Start Game (Boss)", "Cancel"]
	theColors = ["#660000", "#660000", "#660000", "#660000", "#660000", "#111111"]
	
	playerID = str(me._id)
	# whisper("'{}' '{}'".format(playerID, global_BossFight_PlayerOne_ID))
	
	askChoiceResult = askChoice("Setup Boss Fight", theChoices, theColors)
	if (askChoiceResult == 1):
		if (global_BossFight_PlayerOne_ID != "-1" and global_BossFight_PlayerOne_ID != playerID):
			askChoice("Player One is already taken.", ["OK"], ["#111111"])
			return
		elif (global_BossFight_PlayerOne_ID == playerID):
			setGlobalVariable("global_BossFight_PlayerOne_ID", "-1")
			me.setGlobalVariable("deckFormat", "")
			# me.setGlobalVariable("readyToPlay", "FALSE")
			notify("Player One has been reset.")
			askChoice("Player One has been reset.", ["OK"], ["#111111"])
			return
	elif (askChoiceResult == 2):
		if (global_BossFight_PlayerTwo_ID != "-1" and global_BossFight_PlayerTwo_ID != playerID):
			askChoice("Player Two is already taken.", ["OK"], ["#111111"])
			return
		elif (global_BossFight_PlayerTwo_ID == playerID):
			setGlobalVariable("global_BossFight_PlayerTwo_ID", "-1")
			me.setGlobalVariable("deckFormat", "")
			# me.setGlobalVariable("readyToPlay", "FALSE")
			notify("Player Two has been reset.")
			askChoice("Player Two has been reset.", ["OK"], ["#111111"])
			return
	elif (askChoiceResult == 3):
		if (global_BossFight_PlayerThree_ID != "-1" and global_BossFight_PlayerThree_ID != playerID):
			askChoice("Player Three is already taken.", ["OK"], ["#111111"])
			return
		elif (global_BossFight_PlayerThree_ID == playerID):
			setGlobalVariable("global_BossFight_PlayerThree_ID", "-1")
			me.setGlobalVariable("deckFormat", "")
			# me.setGlobalVariable("readyToPlay", "FALSE")
			notify("Player Three has been reset.")
			askChoice("Player Three has been reset.", ["OK"], ["#111111"])
			return
	elif (askChoiceResult == 4):
		if (global_BossFight_Boss_ID != "-1" and global_BossFight_Boss_ID != playerID):
			askChoice("The Boss is already taken.", ["OK"], ["#111111"])
			return
		elif (global_BossFight_Boss_ID == playerID):
			setGlobalVariable("global_BossFight_PlayerOne_ID", "-1")
			me.setGlobalVariable("deckFormat", "")
			# me.setGlobalVariable("readyToPlay", "FALSE")
			notify("The Boss has been reset.")
			askChoice("The Boss has been reset.", ["OK"], ["#111111"])
			return
			
	if (askChoiceResult >= 1 and askChoiceResult <= 4):
		deckErrorMessage = ""
		
		deckLength = len(me.Deck)
		#if (askChoiceResult >= 1 and askChoiceResult <= 3):
			#if (deckLength != 50):
				#deckErrorMessage += "Your deck must contain 50 cards."
		#if (askChoiceResult == 4):
			#if (deckLength!= 80 and deckLength != 83):
				#deckErrorMessage += "The Boss Deck should contain 80/83 cards."
		
		cardNameList = []
		tooManyOfCardNameList = []
		for aCard in me.Deck:
			aCardName = cardLogic_get_fullNameString(aCard)
			
			cardNameList.append(aCardName)
			if (cardNameList.count(aCardName) > 3):
				if (aCardName not in tooManyOfCardNameList):
					tooManyOfCardNameList.append(aCardName)
						
		if (len(tooManyOfCardNameList) > 0):
			if (deckErrorMessage != ""): deckErrorMessage += "\n\n"
			deckErrorMessage += "Your deck contains too many copies of the following cards:"
			for aTooManyCardName in tooManyOfCardNameList:
				deckErrorMessage += "\n- {}".format(aTooManyCardName)
			# return
		
		if (deckErrorMessage != ""):
			playSound("error")
			notify("There is an error with {}'s Deck and they will have to reload.".format(me))
			askChoice(deckErrorMessage, ["OK"], ["#111111"])
			return
		
		if (askChoiceResult == 1):
			setGlobalVariable("global_BossFight_PlayerOne_ID", playerID)
			me.setGlobalVariable("deckFormat", "Standard")
			# me.setGlobalVariable("readyToPlay", "TRUE")
			notify("{} has been set as Player One.".format(me))
			askChoice("You are now Player One.", ["OK"], ["#111111"])
			return
		elif (askChoiceResult == 2):
			setGlobalVariable("global_BossFight_PlayerTwo_ID", playerID)
			me.setGlobalVariable("deckFormat", "Standard")
			# me.setGlobalVariable("readyToPlay", "TRUE")
			notify("{} has been set as Player Two.".format(me))
			askChoice("You are now Player Two.", ["OK"], ["#111111"])
			return
		elif (askChoiceResult == 3):
			setGlobalVariable("global_BossFight_PlayerThree_ID", playerID)
			me.setGlobalVariable("deckFormat", "Standard")
			# me.setGlobalVariable("readyToPlay", "TRUE")
			notify("{} has been set as Player Three.".format(me))
			askChoice("You are now Player Three.", ["OK"], ["#111111"])
			return
		elif (askChoiceResult == 4):
			setGlobalVariable("global_BossFight_Boss_ID", playerID)
			me.setGlobalVariable("deckFormat", "Standard")
			# me.setGlobalVariable("readyToPlay", "TRUE")
			notify("{} has been set as the Boss.".format(me))
			askChoice("You are now the Boss.", ["OK"], ["#111111"])
			return
			
	if (askChoiceResult == 5):
		if (global_BossFight_Boss_ID != playerID):
			askChoice("You are not the Boss.", ["OK"], ["#111111"])
			return
		if (global_BossFight_PlayerOne_ID == "-1" and global_BossFight_PlayerTwo_ID == "-1" and global_BossFight_PlayerThree_ID == "-1"):
			askChoice("At least one Player must be added.", ["OK"], ["#111111"])
			return 
		
		p1Player = None 
		p2Player = None 
		p3Player = None
		bossPlayer = None 
		for p in players:
			pID = str(p._id)
			if (pID == global_BossFight_PlayerOne_ID): p1Player = p
			if (pID == global_BossFight_PlayerTwo_ID): p2Player = p
			if (pID == global_BossFight_PlayerThree_ID): p3Player = p
			if (pID == global_BossFight_Boss_ID): bossPlayer = p
		
		outputString = "Get ready for a Boss Fight!"
		outputString += "\n\n{}".format(bossPlayer)
		outputString += "\n\nVS\n"
		if (p1Player != None): outputString += "\n{}".format(p1Player)
		if (p2Player != None): outputString += "\n{}".format(p2Player)
		if (p3Player != None): outputString += "\n{}".format(p3Player)
		
		outputString += "\n\nThe player at the top of the Heroes list will handle turn progression for the Heroes."
		
		for p in players:
			remoteCall(p, "gameLogic_boss_heroesReady", [])
		
		if (p1Player != None): nextTurn(p1Player)
		elif (p2Player != None): nextTurn(p2Player)
		elif (p3Player != None): nextTurn(p3Player)
		query_forceLoad()
		setGlobalVariable("global_Phase", "StartOfTurn")
		playSound("newTurn")
		
		askChoice(outputString, ["OK"], ["#111111"])
				
def gameLogic_phases_outputFirstPlayerMessage(a1, a2, a3, a4):
	outputMessage = "A die roll has taken place to determine who should go first:\n"
	outputMessage += "\n- {} rolled a {}.".format(a1, a2)
	outputMessage += "\n- {} rolled a {}.".format(a3, a4)
	outputMessage += "\n\nWhen ready, the player going first can press the Tab key to begin."

	askChoice(outputMessage, ["OK"], ["#111111"])
	
def gameLogic_phases_nextPhase(group, x = 0, y = 0):
	mute()
	
	# whisper("check 1")
	readyToPlay = me.getGlobalVariable("readyToPlay")
	if (readyToPlay == "FALSE"):
		gameLogic_setup_readyPlayer()
		return
	
	# whisper("check 2")
	global_Phase = getGlobalVariable("global_Phase")
	if (global_Phase == "N/A"):
		whisper("The game has not yet started.")
		return
		
	# whisper("check 3")
	if (global_Phase == "AlmostReady"):
		if (askChoice("Are you going first?", ["Yes", "No"]) == 1):
			nextTurn(me)
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
			playSound("newTurn")
		return
		
	if (gameLogic_query_activePlayer() != me): return
	
	# whisper("check 4 - {}".format(global_Phase))
	if (global_Phase == "StartOfTurn"): gameLogic_phases_goToActivePhase(group)
	elif (global_Phase == "ActivePhase"): gameLogic_phases_goToDrawPhase(group)
	elif (global_Phase == "DrawPhase"): gameLogic_phases_goToMainPhase1(group)
	elif (global_Phase == "MainPhase1"): gameLogic_phases_goToAttackPhase(group)
	elif (global_Phase == "AttackPhase"): gameLogic_phases_goToMainPhase2(group)
	elif (global_Phase == "MainPhase2"): gameLogic_phases_goToEndPhase(group)
	elif (global_Phase == "EndPhase"): gameLogic_phases_changeControl(group)
	
	for p in players:
		remoteCall(p, "gameLogic_phases_removeHighlights", [me._id])
	
def gameLogic_phases_setCurrentPhase(phaseName, phaseString):
	mute()
	global_Phase = getGlobalVariable("global_Phase")
	if (global_Phase == phaseName or global_Phase == "AlmostReady"): return
	setGlobalVariable("global_Phase", phaseName)
	notify("{} enters the {}.".format(me, phaseString))
	
def gameLogic_phases_goToActivePhase(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("ActivePhase", "Active Phase")
	
	me.setGlobalVariable("playCount_Forward", "0")
	me.setGlobalVariable("playCount_Backup", "0")
	me.setGlobalVariable("playCount_Summon", "0")
	me.setGlobalVariable("playCount_Monster", "0")
	
	global_BossFight = getGlobalVariable("global_BossFight")
	debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
	heroOrVillain = ""
	if (global_BossFight == "TRUE"):
		if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"): heroOrVillain = "Hero"
		elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"): heroOrVillain = "Hero"
		elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"): heroOrVillain = "Hero"
		else: heroOrVillain = "Villain"
	
	myCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE")
	if (global_BossFight == "TRUE" and heroOrVillain == "Hero"):
		myCards = (card for card in table 
					if card.controller != gameLogic_query_boss_boss() 
					and card.Active == "TRUE")
	for aCard in myCards:
		if (aCard.orientation != 0):
			if (aCard.filter == None):
				anAbility = cardLogic_ability_find(aCard, "DoesNotActivate")
				if (anAbility == "N/A"):
					aCard.orientation = 0
					
					cardPowerID = cardLogic_get_hudPowerString(aCard)
					cardDamageID = cardLogic_get_hudDamageString(aCard)
					
					existingHUD = (card for card in table 
									if card.owner == me 
									and (card.AbilitiesContainer == cardPowerID or card.AbilitiesContainer == cardDamageID))
					for anHUD in existingHUD:
						anHUD.orientation = aCard.orientation
			else:
				aCard.filter = None
				
	for p in players:
		remoteCall(p, "damageLogic_healAllDamage_atEndOfTurn", [])
		
	vanishers = (card for card in table 
					if card.controller == me 
					and cardLogic_ability_find(card, "Vanish") != "N/A")
	if (global_BossFight == "TRUE" and heroOrVillain == "Hero"):
		vanishers = (card for card in table 
						if card.controller != gameLogic_query_boss_boss() 
						and cardLogic_ability_find(card, "Vanish") != "N/A")
	for aCard in vanishers:
		# whisper("Vanisher - {}".format(cardLogic_get_fullNameObject(aCard)))
		anAbility = cardLogic_ability_find(aCard, "Vanish")
		anAbilityList = anAbility.split("|")
		
		onOffSwitch = anAbilityList[1]
		startCount = anAbilityList[2]
		currentCount = anAbilityList[3]
		# whisper("{} {} {}".format(onOffSwitch, startCount, currentCount))
		if (onOffSwitch == "ON"):
			currentCountInt = int(currentCount)
			newCountInt = currentCountInt - 1
			currentCount = str(newCountInt)
			
			thisMarker = ("Vanished", "Vanished ID")
			aCard.markers[thisMarker] -= 1
			
			if (newCountInt == 0):
				onOffSwitch = "OFF"
			
			newSwitchString = "Vanish" + "|" + onOffSwitch + "|" + startCount + "|" + currentCount
			newAbilities = aCard.AbilitiesContainer.replace(anAbility, newSwitchString)
			aCard.AbilitiesContainer = newAbilities
			# whisper("changed to {} {} {}".format(onOffSwitch, startCount, currentCount))
			
			if (newCountInt == 0):
				notify("{} has returned to the table.".format(cardLogic_get_fullNameObject(aCard)))
				aCard.filter = None
				aCard.Active = "TRUE"
				if (aCard.orientation == 1):
					aCard.orientation = 0
				gameLogic_onPlay_organizeQueue(aCard.Type)
				
				powerLogic_reset(aCard)
				powerLogic_powerBoost_calculate(table)
	
def gameLogic_phases_goToDrawPhase(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("DrawPhase", "Draw Phase")
	
	global_FirstDraw = getGlobalVariable("global_FirstDraw")
	if (global_FirstDraw == "TRUE"):
		setGlobalVariable("global_FirstDraw", "FALSE")
		cardLogic_deck_drawOneCard(me.Deck, x, y)
	else:
		global_BossFight = getGlobalVariable("global_BossFight")
		if (global_BossFight == "FALSE"):
			cardLogic_deck_drawXCards_top(me.Deck, x, y, 2)
		else:
			debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
			heroOrVillain = ""
			if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"): heroOrVillain = "Hero"
			elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"): heroOrVillain = "Hero"
			elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"): heroOrVillain = "Hero"
			else: heroOrVillain = "Villain"
			
			if (heroOrVillain == "Villain"):
				cardLogic_deck_drawXCards_top(me.Deck, x, y, 4)
			else:
				for p in players:
					if (p == gameLogic_query_boss_playerOne() or p == gameLogic_query_boss_playerTwo() or p == gameLogic_query_boss_playerThree()):
						remoteCall(p, "cardLogic_deck_drawXCards_top_remote", [2])
	
def gameLogic_phases_goToMainPhase1(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("MainPhase1", "first Main Phase")
	
	global_BossFight = getGlobalVariable("global_BossFight")
	warpers = (card for card in table 
					if card.controller == me 
					and cardLogic_ability_find(card, "Warp") != "N/A")
	if (global_BossFight == "TRUE" and heroOrVillain == "Hero"):
		warpers = (card for card in table 
						if card.controller != gameLogic_query_boss_boss() 
						and cardLogic_ability_find(card, "Warp") != "N/A")
	for aCard in warpers:
		thisMarker = ("Warping", "Warping ID")
		if (aCard.markers[thisMarker] > 0):
			aCard.markers[thisMarker] -= 1
			if (aCard.markers[thisMarker] == 0):
				notify("{} has warped onto the table.".format(cardLogic_get_fullNameObject(aCard)))
				aCard.filter = None
				aCard.Active = "TRUE"
				if (aCard.orientation == 1):
					aCard.orientation = 0
				gameLogic_onPlay_organizeQueue(aCard.Type)
				
				powerLogic_reset(aCard)
				powerLogic_powerBoost_calculate(table)
			else:
				notify("A Warp counter has been removed from {}.".format(cardLogic_get_fullNameObject(aCard)))
		
	myCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE")
	for aCard in myCards:
		anAbility = cardLogic_ability_find(aCard, "StartOfTurnCounter")
		# whisper("anAbility {}".format(anAbility))
		if (anAbility != "N/A"):
			anAbilityList = anAbility.split("|")
			
			chosenCounter = anAbilityList[1]
			chosenCounterID = chosenCounter + " ID"
			numCounters = int(anAbilityList[2])
			onlyIfEmpty = anAbilityList[3]
			thisCard = anAbilityList[4]
			
			thisMarker = (chosenCounter, chosenCounterID)
			if (onlyIfEmpty == "FALSE" or (onlyIfEmpty == "TRUE" and aCard.markers[thisMarker] == 0)):
				if (thisCard == "ThisCard"):
					aCard.markers[thisMarker] += numCounters
					notify("{} adds {} {}(s) to {}.".format(me, numCounters, chosenCounter, cardLogic_get_fullNameObject(aCard)))
				else:
					searchLogic = thisCard.split("_")
					searchResults = searchLogic_search(searchLogic[0], searchLogic[1], searchLogic[2], "ReturnArray")
					for thisCard in searchResults:
						thisCard.markers[thisMarker] += numCounters
						notify("{} adds {} {}(s) to {}.".format(me, numCounters, chosenCounter, cardLogic_get_fullNameObject(thisCard)))
	
def gameLogic_phases_goToAttackPhase(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("AttackPhase", "Attack Phase")
	
	crystalCards = [card for card in table
				if card.controller == me 
				and card.Active == "TRUE" 
				and cardLogic_ability_find(card, "AutoGainCrystal") != "N/A"]
	for crystalCard in crystalCards:
		if (cardLogic_ability_find(crystalCard, "AutoGainCrystal") != "N/A"):
			abilityList = crystalCard.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				if (anAbilityList[0] == "AutoGainCrystal"):
					if (anAbilityList[1] == "OnAttackPhase"):
						gameLogic_addCrystal(table, 0, 0)
					elif (anAbilityList[1] == "OnAttackPhase2"):
						gameLogic_addCrystal(table, 0, 0)
	
def gameLogic_phases_goToMainPhase2(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("MainPhase2", "second Main Phase")
	
def gameLogic_phases_goToEndPhase(group, x = 0, y = 0):
	mute()
	gameLogic_phases_setCurrentPhase("EndPhase", "End Phase")
	
	# whisper("Hitting function")
	myCards = (card for card in table
					if card.controller == me 
					and card.Active == "TRUE")
	for aCard in myCards:
		anAbility = cardLogic_ability_find(aCard, "EndOfTurnCounter")
		# whisper("anAbility {}".format(anAbility))
		if (anAbility != "N/A"):
			anAbilityList = anAbility.split("|")
			
			chosenCounter = anAbilityList[1]
			chosenCounterID = chosenCounter + " ID"
			numCounters = int(anAbilityList[2])
			onlyIfEmpty = anAbilityList[3]
			thisCard = anAbilityList[4]
			
			thisMarker = (chosenCounter, chosenCounterID)
			if (onlyIfEmpty == "FALSE" or (onlyIfEmpty == "TRUE" and aCard.markers[thisMarker] == 0)):
				if (thisCard == "ThisCard"):
					aCard.markers[thisMarker] += numCounters
					notify("{} adds {} {}(s) to {}.".format(me, numCounters, chosenCounter, cardLogic_get_fullNameObject(aCard)))
				else:
					searchLogic = thisCard.split("_")
					searchResults = searchLogic_search(searchLogic[0], searchLogic[1], searchLogic[2], "ReturnArray")
					for thisCard in searchResults:
						thisCard.markers[thisMarker] += numCounters
						notify("{} adds {} {}(s) to {}.".format(me, numCounters, chosenCounter, cardLogic_get_fullNameObject(thisCard)))
		
	crystalCards = [card for card in table
				if card.controller == me 
				and card.Active == "TRUE" 
				and cardLogic_ability_find(card, "AutoGainCrystal") != "N/A"]
	for crystalCard in crystalCards:
		abilityList = crystalCard.AbilitiesContainer.split("][")
		for anAbility in abilityList:
			anAbilityList = anAbility.split("|")
			if (anAbilityList[0] == "AutoGainCrystal" and anAbilityList[1] == "OnTurnEnd"):
				gameLogic_addCrystal(table, 0, 0)
						
	powerLogic_powerBoost_calculate(table)
	
def gameLogic_phases_changeControl(group, x = 0, y = 0):
	mute()
	
	if (len(me.hand) > 5):
		playSound("error")
		askChoice("You cannot end your turn with more than 5 cards in your hand.", ["OK"], ["#111111"])
		return
	
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "FALSE"):
		if (len(players) == 1):
			nextTurn(me, True)
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
		elif (len(players) == 2):
			nextTurn(gameLogic_query_inactivePlayer())
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
		
		playSound("newTurn")
	else:
		if (len(players) == 1):
			nextTurn(me, True)
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
			playSound("newTurn")
		elif (len(players) == 2):
			nextTurn(gameLogic_query_inactivePlayer())
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
			playSound("newTurn")
		else:
			debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
			heroOrVillain = ""
			if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"): heroOrVillain = "Hero"
			elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"): heroOrVillain = "Hero"
			elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"): heroOrVillain = "Hero"
			else: heroOrVillain = "Villain"
			
			p1Player = None 
			p2Player = None 
			p3Player = None
			bossPlayer = None 
			for p in players:
				pID = str(p._id)
				if (pID == global_BossFight_PlayerOne_ID): p1Player = p
				if (pID == global_BossFight_PlayerTwo_ID): p2Player = p
				if (pID == global_BossFight_PlayerThree_ID): p3Player = p
				if (pID == global_BossFight_Boss_ID): bossPlayer = p
			
			if (heroOrVillain == "Villain"):
				if (p1Player != None): nextTurn(p1Player)
				elif (p2Player != None): nextTurn(p2Player)
				elif (p3Player != None): nextTurn(p3Player)
			else:
				nextTurn(bossPlayer)
			
			query_forceLoad()
			setGlobalVariable("global_Phase", "StartOfTurn")
			playSound("newTurn")
	
def gameLogic_phases_removeHighlights(aPlayer, keepForCard = None):
	mute()
	myCards = (card for card in table 
				if card.controller == me)
	for aCard in myCards:
		if (keepForCard == None):
			cardLogic_set_borderColor(aCard, "")
		else:
			if (aCard != keepForCard):
				cardLogic_set_borderColor(aCard, "")
		
def gameLogic_utility_rollD6(group, x = 0, y = 0):
	mute()
	myDieRoll = rnd(1, 6)
	notify("{} rolled a {} from a six-sided die.".format(me, myDieRoll))
	
def gameLogic_onPlay_organizeQueue(cardType):
	mute()
	# whisper("Organizing queue...")
	# Card width/height is 102/140
	
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "FALSE"):
		playerOne = True if (me._id == 1) else False
		# if (playerOne == True):
		# 	whisper("I am player 1")
		# else:
		# 	whisper("I am player 2")
		
		if (cardType == "Forward" or cardType == "Monster" or cardType == "Forward - Monster"):
			topCount = 0	
			forwardCount = 0
			monsterCount = 0
			topCards = []
			forwardCards = []
			monsterCards = []
			
			myForwards = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and "Forward" in cardLogic_get_type(card))
			for aForward in myForwards:
				topCount = topCount + 1
				forwardCount = forwardCount + 1
				topCards.append(aForward)
				forwardCards.append(aForward)
				
			myMonsters = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and card.Type == "Monster")
			for aMonster in myMonsters:
				topCount = topCount + 1
				monsterCount = monsterCount + 1
				topCards.append(aMonster)
				monsterCards.append(aMonster)
				
			if (monsterCount == 0 or monsterCount > 3 or forwardCount > 5):
				startX = 0
				startY = 0
				increment = 79
				if (playerOne == True):
					startX = -52 - (increment * (topCount - 1))
					startY = 32
				else:
					startX = -52 - (increment * (topCount - 1))
					startY = -172
					topCards.reverse()
					
				for aCard in topCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
			else:
				startX = 0
				startY = 0
				increment = 79
				if (playerOne == True):
					startX = -289 - (increment * (forwardCount - 1))
					startY = 32
				else:
					startX = 185 - (increment * (forwardCount - 1))
					startY = -172
					forwardCards.reverse()
					
				for aCard in forwardCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
					
				startX = 0
				startY = 0
				increment = 79
				if (playerOne == True):
					startX = 343 - (increment * (monsterCount - 1))
					startY = 32
				else:
					startX = -447 - (increment * (monsterCount - 1))
					startY = -172
					monsterCards.reverse()
					
				for aCard in monsterCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
				
		elif (cardType == "Backup"):
			bottomCount = 0
			bottomCards = []
			
			myBackups = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and card.Type == "Backup")
			for aBackup in myBackups:
				bottomCount = bottomCount + 1
				bottomCards.append(aBackup)
				
			startX = 0
			startY = 0
			increment = 79
			if (playerOne == True):
				startX = -290 - (increment * (bottomCount - 1))
				startY = 203
			else:
				startX = 188 - (increment * (bottomCount - 1))
				startY = -343
			
			for aCard in bottomCards:
				aCard.moveToTable(startX, startY)
				startX += (increment * 2)
		elif (cardType == "Summon" or cardType == "Special"):
			summonCount = 0
		
			summonCards = (card for card in table 
							if card.controller == me 
							and (card.Type == "Summon" or card.Type == "Special"))
			
			startX = 0
			startY = 0
			increment = 10
			direction = 1
			if (playerOne == True): 
				startX = 190
				startY = 203
			else:
				direction = -1
				startX = -292
				startY = -343
			
			for aCard in summonCards:
				aCard.moveToTable(startX, startY)
				if (aCard.Type == "Summon"):
					startX += ((102 + increment) * direction)
				else:
					startX += ((102 + increment) * direction)
	else:
		debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
		
		if (cardType == "Forward" or cardType == "Monster" or cardType == "Forward - Monster"):
			topCount = 0	
			forwardCount = 0
			monsterCount = 0
			topCards = []
			forwardCards = []
			monsterCards = []
			
			myForwards = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and "Forward" in cardLogic_get_type(card))
			for aForward in myForwards:
				topCount = topCount + 1
				forwardCount = forwardCount + 1
				topCards.append(aForward)
				forwardCards.append(aForward)
				
			myMonsters = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and card.Type == "Monster")
			for aMonster in myMonsters:
				topCount = topCount + 1
				monsterCount = monsterCount + 1
				topCards.append(aMonster)
				monsterCards.append(aMonster)
				
			if (monsterCount == 0 or monsterCount > 3 or forwardCount > 5):
				startX = 0
				startY = 0
				increment = 79
				if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
					startX = -52 - (increment * (topCount - 1))
					startY = 32
				elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
					startX = -52 - (increment * (topCount - 1))
					startY = 425
				elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
					startX = -52 - (increment * (topCount - 1))
					startY = 818
				else:
					startX = -52 - (increment * (topCount - 1))
					startY = -172
					topCards.reverse()
					
				for aCard in topCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
			else:
				startX = 0
				startY = 0
				increment = 79
				if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
					startX = -289 - (increment * (forwardCount - 1))
					startY = 32
				elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
					startX = -289 - (increment * (forwardCount - 1))
					startY = 425
				elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
					startX = -289 - (increment * (forwardCount - 1))
					startY = 818
				else:
					startX = 185 - (increment * (forwardCount - 1))
					startY = -172
					forwardCards.reverse()
					
				for aCard in forwardCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
					
				startX = 0
				startY = 0
				increment = 79
				if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
					startX = 343 - (increment * (monsterCount - 1))
					startY = 32
				elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
					startX = 343 - (increment * (monsterCount - 1))
					startY = 425
				elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
					startX = 343 - (increment * (monsterCount - 1))
					startY = 32
				else:
					startX = -447 - (increment * (monsterCount - 1))
					startY = -172
					monsterCards.reverse()
					
				for aCard in monsterCards:
					aCard.moveToTable(startX, startY)
					powerLogic_repositionHUD(aCard)
					startX += (increment * 2)
				
		elif (cardType == "Backup"):
			bottomCount = 0
			bottomCards = []
			
			myBackups = (card for card in table 
				if card.controller == me 
				and (card.Active == "TRUE" or "Vanish|ON" in card.AbilitiesContainer or "Warp|" in card.AbilitiesContainer)
				and card.Type == "Backup")
			for aBackup in myBackups:
				bottomCount = bottomCount + 1
				bottomCards.append(aBackup)
				
			startX = 0
			startY = 0
			increment = 79
			if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
				startX = -290 - (increment * (bottomCount - 1))
				startY = 203
			elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
				startX = -290 - (increment * (bottomCount - 1))
				startY = 596
			elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
				startX = -290 - (increment * (bottomCount - 1))
				startY = 989
			else:
				startX = -76 - (increment * (bottomCount - 1))
				startY = -343
			
			for aCard in bottomCards:
				aCard.moveToTable(startX, startY)
				startX += (increment * 2)
		elif (cardType == "Summon" or cardType == "Special"):
			summonCount = 0
		
			summonCards = (card for card in table 
							if card.controller == me 
							and (card.Type == "Summon" or card.Type == "Special"))
			
			startX = 0
			startY = 0
			increment = 10
			direction = 1
			if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
				startX = 190
				startY = 203
			elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
				startX = 190
				startY = 596
			elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
				startX = 190
				startY = 989
			else:
				direction = -1
				startX = -836
				startY = -343
			
			for aCard in summonCards:
				aCard.moveToTable(startX, startY)
				if (aCard.Type == "Summon"):
					startX += ((102 + increment) * direction)
				else:
					startX += ((102 + increment) * direction)
				
def gameLogic_onPlay_alterCardState(cardJustPlayed):
	mute()
	anAbility = ""
	
	anAbility = cardLogic_ability_find(cardJustPlayed, "BecomesElementOnPlay")
	if (anAbility != "N/A"):
		# whisper("{}".format(anAbility));
		anAbilityList = anAbility.split("|")
		newElements = anAbilityList[1].split(",")
		currentElements = cardLogic_get_elementContainer(cardJustPlayed)
		addedElements = []
		for anElement in newElements:
			if (anElement not in currentElements):
				currentElements.append(anElement)
				addedElements.append(anElement)
		if (addedElements):
			cardJustPlayed.ElementContainer = " - ".join(currentElements)
			notify("{} gains the element(s) of {}.".format(cardLogic_get_fullNameString(cardJustPlayed), ", ".join(addedElements)))
			
	autoCounterAbility = cardLogic_ability_find(cardJustPlayed, "AutoCounter")
	if (autoCounterAbility != "N/A"):
		anAbilityList = autoCounterAbility.split("|")
		searchLogic = anAbilityList[2].split("_")
		searchResults = 0
		if (searchLogic[0] == "Quantity"):
			searchResults = int(searchLogic[1])
		else:
			searchResults = searchLogic_search(searchLogic[0], searchLogic[1], searchLogic[2], "ReturnInteger")
		# whisper("autoCounterAbility - {} | {}".format(autoCounterAbility, searchResults))
		if (searchResults != 0):
			# whisper("successful search")
			chosenCounter = anAbilityList[1]
			chosenCounterID = chosenCounter + " ID"
	
			thisMarker = (chosenCounter, chosenCounterID)
			cardJustPlayed.markers[thisMarker] += searchResults
	
			notify("{} adds {} {}(s) to {}.".format(me, searchResults, chosenCounter, cardLogic_get_fullNameObject(cardJustPlayed)))
			
def gameLogic_resetCamera():
	mute()
	table.reset()
	
def gameLogic_resetCamera_boss(aPlayer):
	mute()
	table.reset()
			
def gameLogic_resetCamera(aPlayer):
	mute()
	table.reset()
	table.refit()
	
	myCards = (card for card in table 
				if card.controller == me
				and card.SetNumber == "BOSS-4")
	for aCard in myCards:
		aCard.delete()
	# table.resize(-900, -400, 1800, 2000)
	# askChoice("To reset the camera and divider line, zoom in/out on the table and then hit the F10 key.", ["OK"], ["#111111"])
				
def gameLogic_addCrystal(group, x = 0, y = 0):
	mute()
	
	randomIndex = rnd(0, 3)
	randomID = ""
	if (randomIndex == 0): randomID = "0c994f02-6c22-4769-8dc6-a061063bb033"
	elif (randomIndex == 1): randomID = "5c3c515b-041d-4072-915d-75d36948dd09"
	elif (randomIndex == 2): randomID = "d5b010b5-c8b8-4a47-a8d3-88cf088ac75b"
	elif (randomIndex == 3): randomID = "f4fbeabc-ad9d-4acd-9b56-1be50e424348"
	
	posX = 0
	posY = 0
	incrementY = 0
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "FALSE"):
		playerOne = True if (me._id == 1) else False
		if (playerOne == True):
			posX = 688
			posY = -3 + 160
			incrementY = 24
		else:
			posX = -792
			posY = -139 - 160
			incrementY = -24
	else:
		debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
		
		if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
			posX = 688
			posY = -3
			incrementY = 24
		elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
			posX = 688
			posY = 390
			incrementY = 24
		elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
			posX = 688
			posY = 783
			incrementY = 24
		else:
			posX = -1150
			posY = -139
			incrementY = -24
			
	
	thisIncrement = 0
	existingCards = (aCard for aCard in table 
						if aCard.controller == me
						and aCard.Type == "CrystalPoint")
	for aCard in existingCards:
		thisIncrement = thisIncrement + 1

	newCard = table.create(randomID, posX, posY + (incrementY * thisIncrement))
	newCard.Active = "FALSE"
	newCard.Type = "CrystalPoint"
	newCard.orientation = 1
	cardLogic_set_borderColor(newCard, "Ability")
	
	notify("{} gains 1 {}.".format(me, cardLogic_get_fullNameObject(newCard)))

	powerLogic_powerBoost_calculate(table)

def gameLogic_addLimitBreakDeck(group, x = 0, y = 0):
	mute()
	
	if (getGlobalVariable("global_BossFight") == "TRUE"): return
	
	playerOne = True if (me._id == 1) else False
	if (playerOne == True):
		posX = 688
		posY = -3
	else:
		posX = -792
		posY = -139
	
	newCard = table.create("7f3bc4dc-b5fc-4a42-9e1c-f06da2dc7b63", posX, posY)
	newCard.Active = "FALSE"
	newCard.orientation = 1
	
	thisMarker = ("Limit Break Counter", "Limit Break Counter ID")
	newCard.markers[thisMarker] = 8