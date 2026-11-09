def cardLogic_get_name(card):
	mute()
	return card.Name

def cardLogic_get_name_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's name is {}.".format(cardLogic_get_name(card)))
	
def cardLogic_get_setNumber(card):
	mute()
	return card.SetNumber

def cardLogic_get_setNumber_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's set number is {}.".format(cardLogic_get_setNumber(card)))
	
def cardLogic_get_rarity(card):
	mute()
	return card.Rarity

def cardLogic_get_rarity_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's rarity is {}.".format(cardLogic_get_rarity(card)))
	
def cardLogic_get_fullNameString(card):
	mute()
	rarityLetter = "X"
	if (card.Rarity == "Common"): rarityLetter = "C"
	elif (card.Rarity == "Rare"): rarityLetter = "R"
	elif (card.Rarity == "Hero"): rarityLetter = "H"
	elif (card.Rarity == "Legend"): rarityLetter = "L"
	elif (card.Rarity == "Starter"): rarityLetter = "S"
	elif (card.Rarity == "Boss"): rarityLetter = ""
	elif (card.Rarity == "Promo"): rarityLetter = ""
	return ("{} [{}]".format(card.Name, (card.SetNumber + rarityLetter)))
	
def cardLogic_get_fullNameObject(card):
	mute()
	rarityLetter = "X"
	if (card.Rarity == "Common"): rarityLetter = "C"
	elif (card.Rarity == "Rare"): rarityLetter = "R"
	elif (card.Rarity == "Hero"): rarityLetter = "H"
	elif (card.Rarity == "Legend"): rarityLetter = "L"
	elif (card.Rarity == "Starter"): rarityLetter = "S"
	elif (card.Rarity == "Promo"): rarityLetter = ""
	return ("{} [{}]".format(card, (card.SetNumber + rarityLetter)))
	
def cardLogic_get_fullNameObject_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's Full Name Object is {}.".format(cardLogic_get_fullNameObject(card)))
	
def cardLogic_get_cp(card):
	mute()
	return card.CP	

def cardLogic_get_cp_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's CP is {}.".format(cardLogic_get_cp(card)))
	
def cardLogic_get_element(card):
	mute()
	return card.Element.split(" - ")

def cardLogic_get_element_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's printed elements are {}.".format(cardLogic_get_element(card)))
	
def cardLogic_get_elementContainer(card):
	mute()
	return card.ElementContainer.split(" - ")

def cardLogic_get_elementContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's current elements are {}.".format(cardLogic_get_elementContainer(card)))
	
def cardLogic_get_elementColorCode(element):
	mute()
	if (element == "Fire"): return "#9d2411"
	elif (element == "Ice"): return "#5394ae"
	elif (element == "Wind"): return "#508362"
	elif (element == "Earth"): return "#b2a43d"
	elif (element == "Lightning"): return "#8b5e89"
	elif (element == "Water"): return "#3461a1"
	elif (element == "Light"): return "#c1c1c1"
	elif (element == "Dark"): return "#2c2523"
	else: return "#660000"
	
def cardLogic_get_type(card):
	mute()
	return card.Type.split(" - ")

def cardLogic_get_type_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's printed types are {}.".format(cardLogic_get_type(card)))
	
def cardLogic_get_typeContainer(card):
	mute()
	return card.TypeContainer.split(" - ")

def cardLogic_get_typeContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's current types are {}.".format(cardLogic_get_typeContainer(card)))
	
def cardLogic_get_job(card):
	mute()
	return card.Job.split(" - ")

def cardLogic_get_job_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's printed jobs are {}.".format(cardLogic_get_job(card)))
	
def cardLogic_get_jobContainer(card):
	mute()
	return card.JobContainer.split(" - ")

def cardLogic_get_jobContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's current jobs are {}.".format(cardLogic_get_jobContainer(card)))
	
def cardLogic_get_category(card):
	mute()
	return card.Category.split(" - ")

def cardLogic_get_category_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's printed categories are {}.".format(cardLogic_get_category(card)))
	
def cardLogic_get_categoryContainer(card):
	mute()
	return card.CategoryContainer.split(" - ")

def cardLogic_get_categoryContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's current categories are {}.".format(cardLogic_get_categoryContainer(card)))
	
def cardLogic_get_power(card):
	mute()
	thisPower = card.Power
	if (thisPower == ""): thisPower = "0"
	return thisPower

def cardLogic_get_power_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's printed power is {}.".format(cardLogic_get_power(card)))
	
def cardLogic_get_powerContainer(card):
	mute()
	return card.PowerContainer.split("|")
	
def cardLogic_set_powerContainer(card, permanentPower, temporaryPower, listedPower):
	mute()
	powerString = "{}|{}|{}|{}".format(card.Power, permanentPower, temporaryPower, listedPower)
	card.PowerContainer = powerString

def cardLogic_get_powerContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's current power levels are {}.".format(cardLogic_get_powerContainer(card)))
	
def cardLogic_get_permanentPower(card):
	mute()
	return int(card.PowerContainer.split("|")[1])

def cardLogic_get_permanentPower_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's permanent power is {}.".format(cardLogic_get_permanentPower(card)))
	
def cardLogic_get_temporaryPower(card):
	mute()
	return int(card.PowerContainer.split("|")[2])

def cardLogic_get_temporaryPower_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's temporary power is {}.".format(cardLogic_get_temporaryPower(card)))
	
def cardLogic_get_totalPower(card):
	mute()
	powerArray = card.PowerContainer.split("|")
	totalPower = int(powerArray[0]) + int(powerArray[1]) + int(powerArray[2])
	return totalPower

def cardLogic_get_totalPower_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's total power is {}.".format(cardLogic_get_totalPower(card)))
	
def cardLogic_get_listedPower(card):
	mute()
	return int(card.PowerContainer.split("|")[3])
	
def cardLogic_get_multicard(card):
	mute()
	return card.Multicard

def cardLogic_get_multicard_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's Multicard status is {}.".format(cardLogic_get_multicard(card)))
	
def cardLogic_get_exBurst(card):
	mute()
	return card.EXBurst

def cardLogic_get_exBurst_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's EX Burst status is {}.".format(cardLogic_get_exBurst(card)))
	
def cardLogic_get_active(card):
	mute()
	return card.Active
	
def cardLogic_get_position_debug(card, x = 0, y = 0):
	mute()
	cardX, cardY = card.position
	whisper("X: {} Y: {}".format(cardX, cardY))

def cardLogic_get_index_debug(card, x = 0, y = 0):
	mute()
	whisper("DEBUG - Index: {}".format(card.index))
	# card.index = 1
	
def cardLogic_set_faceUpOrDown(card, x = 0, y = 0):
	mute()
	if (card.isFaceUp == True):
		card.isFaceUp = False
	else:
		card.isFaceUp = True

def cardLogic_get_active_debug(card, x = 0, y = 0):
	mute()
	whisper("This card's Active status is {}.".format(cardLogic_get_active(card)))
	
def cardLogic_get_freezeColor():
	mute()
	return "#8847caff"
	
def cardLogic_get_targetColor():
	mute()
	return "#88dbc621"
	
def cardLogic_get_abilityContainer(card):
	mute()
	return card.AbilitiesContainer
	
def cardLogic_get_abilityContainer_debug(card, x = 0, y = 0):
	mute()
	whisper("abilityContainer: '{}'".format(cardLogic_get_abilityContainer(card)))
	
def cardLogic_get_hudPowerString(card):
	mute()
	return str(card.model) + " - " + str(card._id) + " - PWR"
	
def cardLogic_get_hudDamageString(card):
	mute()
	return str(card.model) + " - " + str(card._id) + " - DMG"
	
def cardLogic_set_borderColor(card, color):
	if (card.group != table):
		card.highlight = None
		return

	# whisper("highlight {} {}".format(card, color))
	if (color == ""):
		card.highlight = None
	elif (color == "Attack"):
		card.highlight = "#e62222"
	elif (color == "Defend"):
		card.highlight = "#2263e6"
	elif (color == "PartyAttack"):
		card.highlight = "#9522e6"
	elif (color == "Ability"):
		card.highlight = "#FFDFBF"
	elif (color == "SpecialAbility"):
		card.highlight = "#ff9201"
	elif (color == "RevealMatch"):
		card.highlight = "#eb91c2"
	elif (color == "EXBurst"):
		card.highlight = "#4287f5"
	elif (color == "LimitBreak"):
		card.highlight = "#ffcb17"
	
def cardLogic_ability_find(card, abilityName):
	mute()
	if (card.AbilitiesContainer == ""): return "N/A"
	
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == abilityName):
			return anAbility
	
	return "N/A"
	
def cardLogic_ability_findOnField(abilityName):
	mute()
	
	returnCount = 0
	returnArray = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and abilityName in card.AbilitiesContainer);
	for aCard in returnArray:
		returnCount += 1
	
	return returnCount
	
def cardLogic_deck_drawOneCard(group, x = 0, y = 0):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
	
	group[0].moveTo(me.hand)
	notify("{} draws a card. [Hand {} / Deck {}]".format(me, len(me.hand), len(group)))
	
	powerLogic_powerBoost_calculate(table)
		
def cardLogic_deck_drawXCards_top(group, x = 0, y = 0, drawThisMany = None):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	if (drawThisMany == None):
		drawThisMany = askInteger("How many cards would you like to draw?", 2)
		if (drawThisMany == None or drawThisMany < 1): return
		
	
	if (len(group) < drawThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to draw.", ["OK"], ["#111111"])
		return
		
	for index in range(0, drawThisMany):
		group[0].moveTo(me.hand)
	notify("{} draws {} cards. [Hand {} / Deck {}]".format(me, drawThisMany, len(me.hand), len(group)))
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_deck_drawXCards_top_remote(numCards):
	mute()
	cardLogic_deck_drawXCards_top(me.Deck, 0, 0, numCards)
	
def cardLogic_deck_drawXCards_bottom(group, x = 0, y = 0, drawThisMany = None):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	if (drawThisMany == None):
		drawThisMany = askInteger("How many cards would you like to draw?", 2)
		if (drawThisMany == None or drawThisMany < 1): return
		
	
	if (len(group) < drawThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to draw.", ["OK"], ["#111111"])
		return
		
	for index in range(0, drawThisMany):
		group[len(group) - 1].moveTo(me.hand)
	notify("{} draws {} cards from the bottom of their Deck. [Hand {} / Deck {}]".format(me, drawThisMany, len(me.hand), len(group)))
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_deck_drawFiveOrMulligan(group, x = 0, y = 0):
	mute()
	# whisper("drawFiveOrMulligan")
	if (len(group) < 5):
		playSound("error")
		askChoice("Your Deck doesn't have five cards to draw.", ["OK"], ["#111111"])
		return
		
	if (len(me.hand) == 0):
		group.shuffle()
		for index in range(0, 5):
			group[0].moveTo(me.hand)
		notify("{} draws an initial hand of 5 cards. [Hand {} / Deck {}]".format(me, len(me.hand), len(group)))
		whisper("Press F12 to mulligan.")
	else:
		# group.shuffle()
		for aCard in me.hand:
			aCard.moveToBottom(me.Deck)
		for index in range(0, 5):
			group[0].moveTo(me.hand)
		notify("{} mulligans and draws 5 new cards. [Hand {} / Deck {}]".format(me, len(me.hand), len(group)))
	
def cardLogic_deck_shuffle(group, x = 0, y = 0):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	group.shuffle()
	notify("{} shuffles their Deck.".format(me))
	
def cardLogic_deck_takeDamage(group, x = 0, y = 0):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	damageCard = group[0]
	damageCard.moveTo(me.piles["Damage Zone"])
	me.counters["Damage Taken"].value += 1
	notify("{} takes 1 damage.".format(me))
	notify("{} places {} into the Damage Zone.".format(me, cardLogic_get_fullNameObject(damageCard)))
	
	if (len(players) > 1):
		otherPlayer = gameLogic_query_otherPlayer()
		notify("{} - {} damage | {} - {} damage".format(me, len(me.piles["Damage Zone"]), otherPlayer, len(otherPlayer.piles["Damage Zone"])))
	
	if (damageCard.EXBurst == "TRUE"):
		playSound("exBurst")
		notify("The EX Burst for {} has been triggered!".format(cardLogic_get_fullNameObject(damageCard)))
		
		if (cardLogic_ability_find(damageCard, "AutoGainCrystal") != "N/A"):
			abilityList = damageCard.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				if (anAbilityList[0] == "AutoGainCrystal"):
					if (anAbilityList[1] == "OnEXBurst"):
						gameLogic_addCrystal(table, 0, 0)
					elif (anAbilityList[1] == "OnEXBurstDamage"):
						if (searchLogic_search("Player", "DamageZone", "ContainerSize,GreaterThanOrEqualTo," + anAbilityList[2], "ReturnInteger") > 0):
							gameLogic_addCrystal(table, 0, 0)
		
	global_UseDamageZone = getGlobalVariable("global_UseDamageZone")
	if (global_UseDamageZone == "TRUE"):
		posX = 0
		posY = 0
		incrementY = 0
		global_BossFight = getGlobalVariable("global_BossFight")
		if (global_BossFight == "FALSE"):
			playerOne = True if (me._id == 1) else False
			if (playerOne == True):
				posX = -826
				posY = -3
				incrementY = 24
			else:
				posX = 726
				posY = -139
				incrementY = -24
		else:
			debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
		
			if ((gameLogic_query_boss_playerOne() == me and debugPlayer == "-1") or debugPlayer == "P1"):
				posX = -826
				posY = -3
				incrementY = 24
			elif ((gameLogic_query_boss_playerTwo() == me and debugPlayer == "-1") or debugPlayer == "P2"):
				posX = -826
				posY = 390
				incrementY = 24
			elif ((gameLogic_query_boss_playerThree() == me and debugPlayer == "-1") or debugPlayer == "P3"):
				posX = -826
				posY = 783
				incrementY = 24
			else:
				posX = 856
				posY = -139
				incrementY = -24
	
		newCard = table.create(damageCard.model, posX, posY + (incrementY * (len(me.piles["Damage Zone"]) - 1)))
		newCard.Active = "FALSE"
		newCard.Type = "DamageZone"
		newCard.orientation = 1
		if (damageCard.EXBurst == "TRUE"):
			cardLogic_set_borderColor(newCard, "EXBurst")
		currentAbilities = newCard.AbilitiesContainer
		if (currentAbilities == ""):
			newCard.AbilitiesContainer = "CanSwap"
		else:
			newCard.AbilitiesContainer = currentAbilities + "][CanSwap"
			
		for p in players:
			remoteCall(p, "gameLogic_phases_removeHighlights", [me._id, newCard])
	else:
		for p in players:
			remoteCall(p, "gameLogic_phases_removeHighlights", [me._id])
			
	powerLogic_powerBoost_calculate(table)

def cardLogic_deck_millXCards_top(group, x = 0, y = 0, millThisMany = None, sendToBreakZone = True):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	if (millThisMany == None):
		millThisMany = askInteger("How many cards would you like to mill?", 1)
		if (millThisMany == None or millThisMany < 1): return
		
	
	if (len(group) < millThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to mill.", ["OK"], ["#111111"])
		return
		
	for index in range(0, millThisMany):
		if (sendToBreakZone == True):
			group[0].moveTo(me.piles["Break Zone"])
		else:
			group[0].moveTo(me.piles["Removed From Game"])
			
	if (sendToBreakZone == True):
		notify("{} mills {} cards to the Break Zone. [Deck {}]".format(me, millThisMany, len(group)))
	else:
		notify("{} mills {} cards to Removed From Game. [Deck {}]".format(me, millThisMany, len(group)))
		
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_deck_millXCards_bottom(group, x = 0, y = 0, millThisMany = None, sendToBreakZone = True):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	if (millThisMany == None):
		millThisMany = askInteger("How many cards would you like to mill?", 1)
		if (millThisMany == None or millThisMany < 1): return
		
	
	if (len(group) < millThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to mill.", ["OK"], ["#111111"])
		return
		
	for index in range(0, millThisMany):
		if (sendToBreakZone == True):
			group[len(group) - 1].moveTo(me.piles["Break Zone"])
		else:
			group[len(group) - 1].moveTo(me.piles["Removed From Game"])
			
	if (sendToBreakZone == True):
		notify("{} mills {} cards from the bottom of their Deck to the Break Zone. [Deck {}]".format(me, millThisMany, len(group)))
	else:
		notify("{} mills {} cards from the bottom of their Deck to Removed From Game. [Deck {}]".format(me, millThisMany, len(group)))
		
	powerLogic_powerBoost_calculate(table)
		
def cardLogic_rfg_millXCards_top(group, x = 0, y = 0):
	mute()
	cardLogic_deck_millXCards_top(group, x, y, None, False)
	
def cardLogic_rfg_millXCards_bottom(group, x = 0, y = 0):
	mute()
	cardLogic_deck_millXCards_bottom(group, x, y, None, False)
	
def cardLogic_deck_revealXCards_top(group, x = 0, y = 0):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	revealThisMany = askInteger("How many cards would you like to reveal?", 1)
	if (revealThisMany == None or revealThisMany < 1): return
		
	
	if (len(group) < revealThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to reveal.", ["OK"], ["#111111"])
		return
		
	cardLogic_revealCards("N/A", "Quantity", "{}".format(revealThisMany), "N/A", True)
	
def cardLogic_deck_revealXCards_bottom(group, x = 0, y = 0):
	mute()
	if (len(group) == 0):
		playSound("error")
		askChoice("Your Deck is empty.", ["OK"], ["#111111"])
		return
		
	revealThisMany = askInteger("How many cards would you like to reveal?", 1)
	if (revealThisMany == None or revealThisMany < 1): return
		
	
	if (len(group) < revealThisMany):
		playSound("error")
		askChoice("Your Deck doesn't have enough cards to reveal.", ["OK"], ["#111111"])
		return
		
	cardLogic_revealCards("N/A", "Quantity", "{}".format(revealThisMany), "N/A", False)
	
def cardLogic_move_toHand(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group == me.Deck):
		# notify("{} adds {} into their Hand. [Hand {}]".format(me, cardLogic_get_fullNameString(card), len(me.hand)))
		notify("{} adds a card into their Hand. [Hand {}]".format(me, len(me.hand) + 1))
	else:
		notify("{} adds {} into their Hand. [Hand {}]".format(me, cardLogic_get_fullNameObject(card), len(me.hand) + 1))
	
	card.moveTo(me.hand)
	# card.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(card, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(card, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for aCard in me.piles["The Void"]:
			if (aCard.Name == voidName):
				voidCards.append(aCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			card.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveTo(me.hand)
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(dominantCard)))
			
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_move_toBreakZone(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group == me.Deck):
		notify("{} moves {} into the Break Zone.".format(me, cardLogic_get_fullNameString(card)))
	else:
		notify("{} moves {} into the Break Zone.".format(me, cardLogic_get_fullNameObject(card)))
	
	card.moveTo(me.piles["Break Zone"])
	# card.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(card, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(card, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for aCard in me.piles["The Void"]:
			if (aCard.Name == voidName):
				voidCards.append(aCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			card.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveTo(me.piles["Break Zone"])
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(dominantCard)))
			
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_move_toRemoved(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group == me.Deck):
		notify("{} removes {} from the game.".format(me, cardLogic_get_fullNameString(card)))
	else:
		notify("{} removes {} from the game.".format(me, cardLogic_get_fullNameObject(card)))
	
	card.moveTo(me.piles["Removed From Game"])
	# card.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(card, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(card, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for aCard in me.piles["The Void"]:
			if (aCard.Name == voidName):
				voidCards.append(aCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			card.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveTo(me.piles["Removed From Game"])
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(dominantCard)))
			
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_move_toYourVoid(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group == me.Deck):
		notify("{} banishes a card to the Void!".format(me))
	else:
		notify("{} banishes {} to the Void!".format(me, cardLogic_get_fullNameObject(card)))
	
	card.moveTo(me.piles["The Void"])
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_move_toTheirVoid(card, x = 0, y = 0):
	mute()
	if (len(players) == 1): return
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group == me.Deck):
		notify("{} banishes a card to the Void!".format(me))
	else:
		notify("{} banishes {} to the Void!".format(me, cardLogic_get_fullNameObject(card)))
	
	card.resetProperties()
	
	otherPlayer = gameLogic_query_otherPlayer()
	card.moveToTable(0, 0)
	card.isFaceUp = False
	card.controller = otherPlayer
	
	
	for p in players:
		if (p == otherPlayer):
			remoteCall(p, "cardLogic_move_toTheirVoid_helper", [card])
			
	powerLogic_powerBoost_calculate(table)
			
def cardLogic_move_toTheirVoid_helper(card):
	mute()
	card.controller = me
	card.moveTo(me.piles["The Void"])
	
def cardLogic_move_toTopOfDeck(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group != me.Deck and card.group != me.hand):
		notify("{} moves {} to the top of their deck.".format(me, cardLogic_get_fullNameObject(card)))
	else:
		notify("{} moves a card to the top of their deck.".format(me))
		
	card.moveTo(me.Deck)
	# card.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(card, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(card, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for aCard in me.piles["The Void"]:
			if (aCard.Name == voidName):
				voidCards.append(aCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			card.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveTo(me.Deck)
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(dominantCard)))
			
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_move_toBottomOfDeck(aCard, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(aCard).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
	
	if (aCard.group == table):
		powerLogic_cleanupHUD(aCard)
	
	targetColorString = "#" + cardLogic_get_targetColor()[3:]
	# equals = False
	# if (str(aCard.filter) == targetColorString): equals = True
	# whisper("{} | {} | {}".format(str(aCard.filter), targetColorString, equals))
	movedRandomly = False
	if (aCard.group == table and str(aCard.filter) == targetColorString):
		randomTargets = []
		targetedCards = (card for card in table 
							if card.owner == me 
							and str(card.filter) == targetColorString)
		for thisTarget in targetedCards:
			randomTargets.append(thisTarget)
			thisTarget.select(False)
		numRandomTargets = len(randomTargets)
		# whisper("{}".format(numRandomTargets))
		if (numRandomTargets > 1):
			askChoiceResult = askChoice("Send the targeted cards to the bottom of your Deck in a random order?", ["Yes", "No"], ["#660000", "#111111"])
			if (askChoiceResult != 1): return
			for index in range(0, numRandomTargets):
				randomIndex = rnd(0, len(randomTargets) - 1)
				theCard = randomTargets[randomIndex]
				theCard.moveToBottom(me.Deck)
				theCard.resetProperties()
				randomTargets.remove(theCard)
				
			notify("{} moves the targeted cards to the bottom of their deck in a random order.".format(me))
			movedRandomly = True
	
	if (movedRandomly == True): return
	
	if (aCard.group != me.Deck and aCard.group != me.hand):
		notify("{} moves {} to the bottom of their deck.".format(me, cardLogic_get_fullNameObject(aCard)))
	else:
		notify("{} moves a card to the bottom of their deck.".format(me))
		
	aCard.moveToBottom(me.Deck)
	# aCard.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(aCard, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(aCard, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for bCard in me.piles["The Void"]:
			if (bCard.Name == voidName):
				voidCards.append(bCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			aCard.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveToBottom(me.Deck)
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(aCard), cardLogic_get_fullNameObject(dominantCard)))
			
	aCard.resetProperties()
	
	powerLogic_powerBoost_calculate(table)

def cardLogic_move_topFromDeck(card, x = 0, y = 0):
	mute()
	hudCheck = cardLogic_get_fullNameString(card).split(" ")[0]
	if (hudCheck == "Power" or hudCheck == "Damage"): return
    
	underThisMany = askInteger("How many cards from the top?", 4)
	if (underThisMany == None or underThisMany < 1): return
	if (underThisMany > len(me.Deck)): underThisMany = len(me.Deck)
	
	if (card.group == table):
		powerLogic_cleanupHUD(card)
	
	if (card.group != me.Deck and card.group != me.hand):
		notify("{} moves {} under the top {} card(s) of their deck.".format(me, cardLogic_get_fullNameObject(card), underThisMany))
	else:
		notify("{} moves a card under the top {} card(s) of their deck.".format(me, underThisMany))
		
	card.moveTo(me.Deck, underThisMany)
	# card.resetProperties()
	
	# powerLogic_powerBoost_calculate(table)
	
	anAbility = cardLogic_ability_find(card, "Prime_Eikon")
	anAbility2 = cardLogic_ability_find(card, "AlternateName")
	if (anAbility != "N/A" and anAbility2 != "N/A"):
		anAbilityList = anAbility2.split("|")
		voidName = anAbilityList[1]
		voidCards = []
		for bCard in me.piles["The Void"]:
			if (bCard.Name == voidName):
				voidCards.append(bCard)
		if (len(voidCards) > 0):
			# whisper("Good!");
			dominantCard = voidCards[0]
			card.moveTo(me.piles["Removed From Game"]);
			dominantCard.moveTo(me.Deck, underThisMany)
			notify("The primed {} was replaced with {}.".format(cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(dominantCard)))
			
	card.resetProperties()
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_discard_gainCP(card, x = 0, y = 0):
	mute()
	chosenElement = "N/A"
	
	printedElements = cardLogic_get_element(card)
	if (len(printedElements) == 1):
		chosenElement = printedElements[0]
	else:
		elementColors = []
		for anElement in printedElements:
			if (anElement == "Fire"): elementColors.append("#9d2411")
			elif (anElement == "Ice"): elementColors.append("#5394ae")
			elif (anElement == "Wind"): elementColors.append("#508362")
			elif (anElement == "Earth"): elementColors.append("#b2a43d")
			elif (anElement == "Lightning"): elementColors.append("#8b5e89")
			elif (anElement == "Water"): elementColors.append("#3461a1")
			elif (anElement == "Light"): elementColors.append("#c1c1c1")
			elif (anElement == "Dark"): elementColors.append("#2c2523")
			else: return "#660000"
		askChoiceResult = askChoice("Choose an element:", printedElements, elementColors)
		if (askChoiceResult == 0): return
		chosenElement = printedElements[askChoiceResult - 1]
		
	if (chosenElement == "N/A"): return
	counterName = chosenElement + " CP"
	me.counters[counterName].value += 2
	card.moveTo(me.piles["Break Zone"])
	notify("{} discards {} and gains 2 {}. [Hand {}]".format(me, cardLogic_get_fullNameObject(card), counterName, len(me.hand)))
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_discard_noCP(card, x = 0, y = 0):
	mute()
	card.moveTo(me.piles["Break Zone"])
	notify("{} discards {}. [Hand {}]".format(me, cardLogic_get_fullNameObject(card), len(me.hand)))
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_playOrCast(cardToPlay, x = 0, y = 0, forFree = "FALSE", autoCast = "FALSE", discardAbility = "FALSE", warping = "FALSE", rewarping = "FALSE"):
	mute()
	deckFormat = me.getGlobalVariable("deckFormat")
	
	playOrCast = "play"
	if (autoCast == "TRUE" or cardToPlay.Type == "Summon"): playOrCast = "cast"
	
	# Backup Check
	if (deckFormat != "Custom" and cardToPlay.Type == "Backup"):
		bottomCount = 0
		
		myBackups = (card for card in table 
			if card.controller == me 
			and card.Active == "TRUE" 
			and card.Type == "Backup")
		for aBackup in myBackups:
			bottomCount = bottomCount + 1
			
		bottomCountMax = 5
		global_BossFight = getGlobalVariable("global_BossFight")
		if (global_BossFight == "TRUE"):
			debugPlayer = getGlobalVariable("global_BossFight_DebugUser_ID")
			if ((gameLogic_query_boss_boss() == me and debugPlayer == "-1") or debugPlayer == "Boss"):
				bottomCountMax = 10
			
		if (bottomCount == bottomCountMax):
			playSound("error")
			askChoice("You may only have a maximum of {} Backups.".format(bottomCountMax), ["OK"], ["#111111"])
			return
			
	# Name Check (for non-Title format)
	if (deckFormat != "Title" and deckFormat != "Custom" and cardToPlay.Multicard == "FALSE" and cardToPlay.Type != "Summon" and discardAbility == "FALSE" and warping == "FALSE"):
		sameNameString = "";
		myCardsWithSameName = (card for card in table
								if card.controller == me 
								and card.Active == "TRUE" 
								and card.Name == cardToPlay.Name)
		for aSameName in myCardsWithSameName:
			sameNameString += "\n- {}".format(cardLogic_get_fullNameString(aSameName))
		
		myCardsWithAltName1 = (card for card in table
								if card.controller == me 
								and card.Active == "TRUE" 
								and ("AlternateName|" + card.Name) in cardToPlay.AbilitiesContainer)
		for aSameName in myCardsWithAltName1:
			# whisper("match alt name 1")
			sameNameString += "\n- {}".format(cardLogic_get_fullNameString(aSameName))
			
		myCardsWithAltName2 = (card for card in table
								if card.controller == me 
								and card.Active == "TRUE" 
								and ("AlternateName|" + cardToPlay.Name) in card.AbilitiesContainer)
		for aSameName in myCardsWithAltName2:
			# whisper("match alt name 2")
			sameNameString += "\n- {}".format(cardLogic_get_fullNameString(aSameName))
								
		
		if (sameNameString != ""):
			fullSameNameString = "You cannot have these cards in play at the same time:"
			fullSameNameString += "\n\n- {}".format(cardLogic_get_fullNameString(cardToPlay))
			fullSameNameString += sameNameString
			
			playSound("error")
			askChoice(fullSameNameString, ["OK"], ["#111111"])
			return
			
	# Name Check (for Title format)
	if (deckFormat == "Title" and cardToPlay.Multicard == "FALSE" and cardToPlay.Type != "Summon" and discardAbility == "FALSE" and warping == "FALSE"):
		sameCardString = "";
		mySameCards = (card for card in table 
						if card.controller == me 
						and card.Active == "TRUE" 
						and card.Name == cardToPlay.Name 
						and card.SetNumber == cardToPlay.SetNumber)
		for aSameCard in mySameCards:
			sameCardString = "{}".format(cardLogic_get_fullNameString(aSameCard))
		
		if (sameCardString != ""):
			playSound("error")
			askChoice("You cannot control two copies of {} in Title format.".format(sameCardString), ["OK"], ["#111111"])
			return
			
	# Light/Dark Check
	playedLight = "FALSE"
	lightCardCount = 0;
	lightCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and searchLogic_factor_elementContainer(card, "Is", "Light") == "TRUE")
	for aCard in lightCards:
		lightCardCount += 1
	# whisper("lightCardCount - {}".format(lightCardCount))
	if (searchLogic_factor_element(cardToPlay, "Is", "Light") == "TRUE" and cardToPlay.Type != "Summon"):
		if (lightCardCount == 0):
			playedLight = "FALSE"
		else:
			# whisper("checkLight - {}  AND  {}".format(cardLogic_ability_find(cardToPlay, "CauseFloodOfLight"), cardLogic_ability_findOnField("AllowFloodOfLight")))
			if (cardLogic_ability_find(cardToPlay, "CauseFloodOfLight") != "N/A" or cardLogic_ability_findOnField("AllowFloodOfLight") != 0):
				playedLight = "FALSE"
			else:
				playedLight = "TRUE"
	if (playedLight == "TRUE"):
		playSound("error")
		askChoice("You already have a Light character in play.", ["OK"], ["#111111"])
		return
	
	playedDark = "FALSE"
	darkCardCount = 0;
	darkCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and searchLogic_factor_elementContainer(card, "Is", "Dark") == "TRUE")
	for aCard in darkCards:
		darkCardCount += 1
		# whisper("darkCardCount - {}".format(darkCardCount))
	if (searchLogic_factor_element(cardToPlay, "Is", "Dark") == "TRUE" and cardToPlay.Type != "Summon"):
		if (darkCardCount == 0):
			playedDark = "FALSE"
		else:
			# whisper("checkDark - {}  AND  {}".format(cardLogic_ability_find(cardToPlay, "CauseFloodOfDark"), cardLogic_ability_findOnField("AllowFloodOfDark")))
			if (cardLogic_ability_find(cardToPlay, "CauseFloodOfDark") != "N/A" or cardLogic_ability_findOnField("AllowFloodOfDark") != 0):
				playedDark = "FALSE"
			else:
				playedDark = "TRUE"
	if (playedDark == "TRUE"):
		playSound("error")
		askChoice("You already have a Dark character in play.", ["OK"], ["#111111"])
		return
		
	# whisper("checkCount - {} AND {}".format(lightCardCount, darkCardCount))
	if (cardToPlay.Type != "Summon"):
		if ((searchLogic_factor_element(cardToPlay, "Is", "Light") == "TRUE" and darkCardCount > 0) or (searchLogic_factor_element(cardToPlay, "Is", "Dark") == "TRUE" and lightCardCount > 0)):
			playSound("error")
			askChoice("You cannot have Light and Dark characters in play at the same time.", ["OK"], ["#111111"])
			return
			
	costToPlay = int(cardToPlay.CP)
	costReducedBy = 0
	totalCP = 0
	
	# Cost increase
	taxingCards = (card for card in table 
					if card.Active == "TRUE" 
					and card.SetNumber == "18-105")
	for aCard in taxingCards:
		if (cardToPlay.Type != "Backup"):
			costToPlay += 1
			if (aCard.controller != me and searchLogic_search("Opponent", "DamageZone", "ContainerSize,GreaterThanOrEqualTo,5", "ReturnInteger") > 0):
				costToPlay += 1
	
	# Checking to see if the cost can be reduced
	if (forFree != "TRUE" and warping == "FALSE"):
		minimumOne = "FALSE"
		
		if (cardLogic_ability_find(cardToPlay, "CheaperOnMyTurn") != "N/A"):
			abilityList = cardToPlay.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				# whisper("{}".format(abilityList))
				if (anAbilityList[0] == "CheaperOnMyTurn"):
					if (gameLogic_query_activePlayer() == me): 
						costReducedBy += int(anAbilityList[1])
		
		# Check the card to be played first
		if (cardLogic_ability_find(cardToPlay, "CostReduction") != "N/A"):
			abilityList = cardToPlay.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				# whisper("{}".format(abilityList))
				if (anAbilityList[0] == "CostReduction" and anAbilityList[1] == "Self"):
					searchVariables = anAbilityList[2].split("_")
					if ("Crystals" in searchVariables[2]):
						# whisper("CRYSTAL REDUCTION")
						crystalArray = (card for card in table 
										if card.controller == me
										and card.Type == "CrystalPoint")
						crystalCount = 0
						for aCrystal in crystalArray:
							crystalCount = crystalCount + 1
						costReducedBy += crystalCount
					else:
						searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger", cardToPlay)
						# whisper("costReduction returned {} matching results.".format(searchResults))
						if (searchResults >= int(anAbilityList[3])):
							if (anAbilityList[4] == "X"):
								costReducedBy += searchResults
							elif (anAbilityList[4] == "-X"):
								costReducedBy -= searchResults
							elif ("SecondFactor" in anAbilityList[4]):
								secondSearchVariables = anAbilityList[4].split("_")
								secondSearchResults = searchLogic_search(secondSearchVariables[1], secondSearchVariables[2], secondSearchVariables[3], "ReturnInteger", cardToPlay)
								costReducedBy += secondSearchResults
							else:
								costReducedBy += int(anAbilityList[4])
					if (anAbilityList[5] == "MinimumOne"): minimumOne = "TRUE"
		
		# Checking cards that are already on the field
		aoeCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "CostReduction") != "N/A")
		for aoeCard in aoeCards:
			abilityList = aoeCard.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				if (anAbilityList[0] == "CostReduction" and anAbilityList[1] == "AoE"):
					searchVariables = anAbilityList[2].split("_")
					searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger", cardToPlay)
					# whisper("costReduction returned {} matching results.".format(searchResults))
					if (searchResults >= int(anAbilityList[3])):
						if (anAbilityList[4] == "X"):
							costReducedBy += searchResults
						elif ("SecondFactor" in anAbilityList[4]):
							secondSearchVariables = anAbilityList[4].split("_")
							secondSearchResults = searchLogic_search(secondSearchVariables[1], secondSearchVariables[2], secondSearchVariables[3], "ReturnInteger", cardToPlay)
							costReducedBy += secondSearchResults
						else:
							costReducedBy += int(anAbilityList[4])
						if (anAbilityList[5] == "MinimumOne"): minimumOne = "TRUE"
						
	paidWithCrystal = "FALSE"
	paidWithCrystalColorless = "FALSE"
	crystalPayCard = cardToPlay
	crystalAbility = cardLogic_ability_find(cardToPlay, "PayWithCrystal")
	if (forFree == "FALSE" and warping == "FALSE"):
		if (crystalAbility != "N/A"):
			numCrystals = 0
			existingCrystals = (aCard for aCard in table 
								if aCard.controller == me
								and aCard.Type == "CrystalPoint")
			for aCrystal in existingCrystals:
				crystalPayCard = aCrystal
				numCrystals = numCrystals + 1
			
			if (numCrystals > 0):
				crystalSelection = askChoice("Pay with a Crystal?", ["Yes", "No"], ["#660000", "#111111"])
				# whisper("crystalSelection: {}".format(crystalSelection))
				if (crystalSelection != 1 and crystalSelection != 2): return
				if (crystalSelection == 1):
					paidWithCrystal = "TRUE"
					anAbilityList = crystalAbility.split("|")
					costReducedBy += int(anAbilityList[1])
					
					crystalAbility2 = cardLogic_ability_find(cardToPlay, "PaidWithCrystalColorless")
					if (crystalAbility2 != "N/A"):
						paidWithCrystalColorless = "TRUE"
	
	costToPlay -= costReducedBy
	if (costToPlay < 0): costToPlay = 0
	if (costToPlay == 0 and minimumOne == "TRUE"): costToPlay = 1
	
	playPhrase = ""
	if (warping == "TRUE"):
		warpAbility = cardLogic_ability_find(cardToPlay, "Warp")
		if (rewarping == "TRUE"):
			warpAbility = cardLogic_ability_find(cardToPlay, "Rewarp")
		anAbilityList = warpAbility.split("|")
		cpCost = anAbilityList[1]
		
		elementsArray = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
		abilityCosts = cpCost.split("/")
		counterTotal = 0
		neededTotal = 0
		for index in range(0, 8):
			counterName = elementsArray[index] + " CP"
			counterValue = me.counters[counterName].value
			neededValue = int(abilityCosts[index])
			if (neededValue > counterValue):
				playSound("error")
				askChoice("You have {} {}. You need at least {} {} in order to Warp.".format(counterValue, counterName, neededValue, counterName), ["OK"], ["#111111"])
				return
			counterTotal += counterValue
			neededTotal += neededValue
		neededTotal += int(abilityCosts[8])
		if (neededTotal > counterTotal):
			cpDiff = neededTotal - counterTotal
			playSound("error")
			askChoice("You need an additional {} CP in order to Warp.".format(cpDiff), ["OK"], ["#111111"])
			return
	elif (costToPlay > 0 and forFree != "TRUE"):
		costError = ""
		printedElements = cardLogic_get_element(cardToPlay)
		allElementsArray = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
		for anElement in allElementsArray:
			counterName = anElement + " CP"
			counterValue = me.counters[counterName].value
			totalCP += counterValue
			if (counterValue == 0 and anElement in printedElements and anElement != "Light" and anElement != "Dark" and paidWithCrystalColorless == "FALSE"):
				noColorProblem = "FALSE"
				
				aoeCardsSwiftcast = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "Swiftcast") != "N/A")
				for aoeCard in aoeCardsSwiftcast:
					abilityList = aoeCard.AbilitiesContainer.split("][")
					for anAbility in abilityList:
						anAbilityList = anAbility.split("|")
						if (anAbilityList[0] == "Swiftcast" and anAbilityList[1] == "AoE"):
							searchVariables = anAbilityList[2].split("_")
							searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger", cardToPlay)
							if (searchResults > 0):
								noColorProblem = "TRUE"
								
				if (cardLogic_ability_find(cardToPlay, "Swiftcast") != "N/A"):
					abilityList = cardToPlay.AbilitiesContainer.split("][")
					for anAbility in abilityList:
						anAbilityList = anAbility.split("|")
						if (anAbilityList[0] == "Swiftcast" and anAbilityList[1] == "Self"):
							searchVariables = anAbilityList[2].split("_")
							searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger", cardToPlay)
							if (searchResults > 0):
								noColorProblem = "TRUE"
								
				if (cardLogic_ability_find(cardToPlay, "FourLords") != "N/A"):
					abilityList = cardToPlay.AbilitiesContainer.split("][")
					for anAbility in abilityList:
						anAbilityList = anAbility.split("|")
						if (anAbilityList[0] == "FourLords"):
							searchVariables = anAbilityList[1].split("_")
							searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger")
							if (searchResults > 0):
								noColorProblem = "TRUE"
				
				if (noColorProblem == "FALSE" and deckFormat != "Title"):
					if (costError != ""): costError += "\n\n"
					costError += "You need at least one {} CP to {} {}.".format(anElement, playOrCast, cardLogic_get_fullNameString(cardToPlay))
		if (totalCP < costToPlay):
			if (costError != ""): costError += "\n\n"
			costError += "You need at least {} CP to {} {}.".format(costToPlay, playOrCast, cardLogic_get_fullNameString(cardToPlay))
			
		if (costError != ""):
			playSound("error")
			askChoice(costError, ["OK"], ["#111111"])
			return
			
		playPhrase = "with {} CP".format(totalCP)
		if (paidWithCrystal == "TRUE"):
			playPhrase = "with {} CP and a Crystal".format(totalCP)
	else:
		playPhrase = "for free"
		
	if (warping == "TRUE"):
		warpAbility = cardLogic_ability_find(cardToPlay, "Warp")
		if (rewarping == "TRUE"):
			warpAbility = cardLogic_ability_find(cardToPlay, "Rewarp")
		anAbilityList = warpAbility.split("|")
		warpTurns = anAbilityList[2]
		
		thisMarker = ("Warping", "Warping ID")
		
		cardToPlay.moveToTable(0, 0)
		
		notify("{} is warping {}, who will appear in {} turns.".format(me, cardLogic_get_fullNameObject(cardToPlay), warpTurns))
		cardToPlay.filter = "#88535657"
		cardToPlay.Active = "FALSE"
		cardToPlay.markers[thisMarker] = int(warpTurns)
		gameLogic_onPlay_organizeQueue(cardToPlay.Type)
		
		return
	
	cardToPlay.moveToTable(0, 0)
	cardToPlay.Active = "TRUE"
	
	anLBAbility = cardLogic_ability_find(cardToPlay, "LimitBreak")
	if (anLBAbility != "N/A"):
		playSound("limitBreak")
		cardLogic_set_borderColor(cardToPlay, "LimitBreak")
		notify("{} Limit Breaks with {}!".format(me, cardLogic_get_fullNameObject(cardToPlay)))
	else:
		if (discardAbility == "FALSE"):
			if (cardToPlay.Type == "Summon"):
				notify("{} casts {} {}. [Hand {}]".format(me, cardLogic_get_fullNameObject(cardToPlay), playPhrase, len(me.hand)))
			elif (cardToPlay.Type == "Backup"):
				cardToPlay.orientation = 1
				notify("{} plays {} dulled {}. [Hand {}]".format(me, cardLogic_get_fullNameObject(cardToPlay), playPhrase, len(me.hand)))
			else:
				notify("{} plays {} {}. [Hand {}]".format(me, cardLogic_get_fullNameObject(cardToPlay), playPhrase, len(me.hand)))
			
	if (discardAbility == "TRUE"):
		oldType = cardToPlay.Type
		cardToPlay.Type = "Special"
		gameLogic_onPlay_organizeQueue(cardToPlay.Type)
		cardToPlay.Type = oldType
	else:
		gameLogic_onPlay_organizeQueue(cardLogic_get_type(cardToPlay)[0])
		gameLogic_onPlay_alterCardState(cardToPlay)
	
	if (discardAbility == "FALSE"):
		cardToPlayTypes = cardLogic_get_type(cardToPlay)
		for aType in cardToPlayTypes:
			playCount = me.getGlobalVariable("playCount_" + aType)
			playCountInt = int(playCount) + 1
			me.setGlobalVariable("playCount_" + aType, playCountInt)
	
	cardLogic_resetCPCounters()
	
	if (discardAbility == "TRUE"):
		cardToPlay.Active = "FALSE"
		cardLogic_set_borderColor(cardToPlay, "Ability")
		notify("{} discards {} to use its Ability.".format(me, cardLogic_get_fullNameObject(cardToPlay)))
	
	counterCards = (card for card in table
					if card.controller == me 
					and card.Active == "TRUE" 
					and card != cardToPlay 
					and cardLogic_ability_find(card, "Counter") != "N/A")
	for aCard in counterCards:
		anAbility = cardLogic_ability_find(aCard, "Counter")
		anAbilityList = anAbility.split("|")
		if (anAbilityList[2] != "N/A"):
			searchResults = searchLogic_search("Player", "CardToPlay", anAbilityList[2], "ReturnInteger", cardToPlay)
			# whisper("searchResults = {}".format(searchResults))
			if (searchResults > 0):
				chosenCounter = anAbilityList[1]
				chosenCounterID = chosenCounter + " ID"
				
				increment = 1
				incrementAbility = cardLogic_ability_find(aCard, "IncrementCounter")
				if (incrementAbility != "N/A"):
					incrementAbilityList = incrementAbility.split("|")
					increment = int(incrementAbilityList[1])
		
				thisMarker = (chosenCounter, chosenCounterID)
				aCard.markers[thisMarker] += increment
		
				notify("{} adds {} {} to {}.".format(me, increment, chosenCounter, cardLogic_get_fullNameObject(aCard)))

	crystalCards = [card for card in table
				if card.controller == me 
				and card.Active == "TRUE" 
				and cardLogic_ability_find(card, "AutoGainCrystal") != "N/A"]
	for crystalCard in crystalCards:
		abilityList = crystalCard.AbilitiesContainer.split("][")
		for anAbility in abilityList:
			anAbilityList = anAbility.split("|")
			if (anAbilityList[0] != "AutoGainCrystal"):
				continue
			if (anAbilityList[1] == "OnPlay"):
				if (crystalCard == cardToPlay):
					gameLogic_addCrystal(table, 0, 0)
			elif (anAbilityList[1] == "OnPlay2"):
				if (crystalCard == cardToPlay):
					gameLogic_addCrystal(table, 0, 0)
					gameLogic_addCrystal(table, 0, 0)
			elif (anAbilityList[1] == "OnPlayDamage"):
				if (crystalCard == cardToPlay):
					if (searchLogic_search("Player", "DamageZone", "ContainerSize,GreaterThanOrEqualTo," + anAbilityList[2], "ReturnInteger") > 0):
						gameLogic_addCrystal(table, 0, 0)
			elif (anAbilityList[1] == "OnEXBurst" or anAbilityList[1] == "OnEXBurstDamage" or anAbilityList[1] == "OnTurnEnd" or anAbilityList[1] == "OnAttackPhase" or anAbilityList[1] == "OnAttackPhase2"):
				doNothingVar = 0
			else:
				searchLogic = anAbilityList[1].split("_")
				# whisper("{}".format(searchLogic))
				searchResults = searchLogic_search(searchLogic[0], searchLogic[1], searchLogic[2], "ReturnArray")
				if (cardToPlay in searchResults):
					gameLogic_addCrystal(table, 0, 0)
				
	if (paidWithCrystal == "TRUE"):
		crystalPayCard.delete()
	powerLogic_powerBoost_calculate(table)
	powerLogic_powerBoost_calculate(table)
	
	return "Success"
	
def cardLogic_playOrCast_forFree(card, x = 0, y = 0):
	mute()
	cardLogic_playOrCast(card, x, y, "TRUE")
	
def cardLogic_playOrCast_warp(card, x = 0, y = 0):
	mute()
	cardLogic_playOrCast(card, x, y, "FALSE", "FALSE", "FALSE", "TRUE")

def cardLogic_playOrCast_rewarp(card, x = 0, y = 0):
	mute()
	card.moveTo(me.piles["Break Zone"])
	cardLogic_playOrCast(card, x, y, "FALSE", "FALSE", "FALSE", "TRUE", "TRUE")
	
def cardLogic_playOrCast_LimitBreak(lbCard, x = 0, y = 0):
	mute()
	
	anAbility = cardLogic_ability_find(lbCard, "LimitBreak")
	if (anAbility == "N/A"):
		playSound("error")
		askChoice("{} is not able to Limit Break.".format(cardLogic_get_fullNameString(lbCard)), ["OK"], ["#111111"])
		return
	
	anAbilityList = anAbility.split("|")
	limitCost = int(anAbilityList[1]) + 1
	
	currentLB = 0
	cardX = 0
	cardY = 0
	tableCards = (card for card in table 
				if card.controller == me 
				and card.SetNumber == "LB-DECK")
	thisMarker = ("Limit Break Counter", "Limit Break Counter ID")
	for tableCard in tableCards:
		currentLB += tableCard.markers[thisMarker]
		cardX, cardY = tableCard.position
	# whisper("cost {} current {}".format(limitCost, currentLB))
	
	if (limitCost > currentLB):
		playSound("error")
		askChoice("You need at least {} LB to Limit Break with {}.".format(limitCost, cardLogic_get_fullNameString(lbCard)), ["OK"], ["#111111"])
		return
    
	copyOfCard = table.create(lbCard.model, cardX, cardY)
	
	playResult = cardLogic_playOrCast(copyOfCard, x, y)
	# whisper("playResult: {}".format(playResult))
	if (playResult == "Success"):
		modifierX = 0
		modifierY = 0
		atLeastOneSelected = False

		playerOne = True if (me._id == 1) else False
		if (playerOne == True):
			posX = 868
			posY = -3
			modifierX = -20
			modifierY = 30
		else:
			posX = -972
			posY = -139
			modifierX = 20
			modifierY = -30
            
		tableCards = (card for card in table 
						if card.controller == me 
						and card.SetNumber == "LB-DECK")
		thisMarker = ("Limit Break Counter", "Limit Break Counter ID")
    
		selectedCards = (card for card in me.piles["LB Deck"] 
						if card.targetedBy == me)
		for selectedCard in selectedCards:
			whisper("target: {}".format(cardLogic_get_fullNameString(selectedCard)))
			atLeastOneSelected = True

		for tableCard in tableCards:
			if (atLeastOneSelected == True):
				startPos = 8 - tableCard.markers[thisMarker]
			
				selectedCards_2 = (card for card in me.piles["LB Deck"] 
									if card.targetedBy == me)
				for selectedCard in selectedCards_2:
					newCard = table.create(selectedCard.model, posX, posY + (modifierY * startPos))
					newCard.Active = "FALSE"
					newCard.orientation = 1
				
					startPos += 1;
					
					selectedCard.target(False);
                
				finalCard = table.create(copyOfCard.model, posX - modifierX, posY + (modifierY * startPos))
				finalCard.Active = "FALSE"
				finalCard.orientation = 1
			
			tableCard.markers[thisMarker] -= limitCost
		
		return
	else:
		copyOfCard.delete()
	
def cardLogic_removeWarpCounter(card, x = 0, y = 0):
	mute()
	
	thisMarker = ("Warping", "Warping ID")
	if (card.markers[thisMarker] > 0):
		card.markers[thisMarker] -= 1
		if (card.markers[thisMarker] == 0):
			notify("{} has warped onto the table.".format(cardLogic_get_fullNameObject(card)))
			card.filter = None
			card.Active = "TRUE"
			if (card.orientation == 1):
				card.orientation = 0
			gameLogic_onPlay_organizeQueue(card.Type)
			
			powerLogic_reset(card)
			powerLogic_powerBoost_calculate(table)
		else:
			notify("A Warp counter has been removed from {}.".format(cardLogic_get_fullNameObject(card)))
	
def cardLogic_dullOrActivate(card, x = 0, y = 0):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer and "Backup" not in cardTypeContainer and "Monster" not in cardTypeContainer): return
	
	if (card.orientation == 0): cardLogic_dull(card)
	else: cardLogic_activate(card)
	
	cardPowerID = cardLogic_get_hudPowerString(card)
	cardDamageID = cardLogic_get_hudDamageString(card)
	
	existingHUD = (card for card in table 
					if card.owner == me 
					and (card.AbilitiesContainer == cardPowerID or card.AbilitiesContainer == cardDamageID))
	for anHUD in existingHUD:
		anHUD.orientation = card.orientation
		
	powerLogic_repositionHUD(card)

def cardLogic_dull(dullCard, forceDull = False):
	mute()
	
	gainCP = "FALSE"
	elementToGain = "";
	if (dullCard.Type == "Backup" and forceDull == False):
		numChoices = 0
		choiceContainer = []
		choiceColors = []
		allElements = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
		
		elementContainer = cardLogic_get_elementContainer(dullCard)
		extraElementsList = []
		anAbility = cardLogic_ability_find(dullCard, "CanDullForElement")
		if (anAbility != "N/A"):
			anAbilityList = anAbility.split("|")
			extraElementsList = anAbilityList[1].split(",")
			
		leoMoogles = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "BackupsCanDullForAnyElement") != "N/A")
		for aCard in leoMoogles:
			anAbility = cardLogic_ability_find(aCard, "BackupsCanDullForAnyElement")
			anAbilityList = anAbility.split("|")
			searchLogicArray = anAbilityList[1].split("_")
			searchResultsArray = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
			if (dullCard in searchResultsArray):
				extraElementsList = allElements
		filoElements = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "BackupsCanDullForMoreElements") != "N/A")
		for aCard in filoElements:
			anAbility = cardLogic_ability_find(aCard, "BackupsCanDullForMoreElements")
			anAbilityList = anAbility.split("|")
			searchLogicArray = anAbilityList[1].split("_")
			searchResultsArray = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
			if (dullCard in searchResultsArray):
				extraElementsList = anAbilityList[2].split(",")
		
		anAbility = cardLogic_ability_find(dullCard, "CanDullCopyElement")
		if (anAbility != "N/A"):
			anAbilityList = anAbility.split("|")
			searchLogicArray = anAbilityList[1].split("_")
			searchResultsArray = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
			for aCard in searchResultsArray:
				aCardElements = cardLogic_get_elementContainer(aCard)
				for theElement in aCardElements:
					extraElementsList.append(theElement)
		
		for anElement in allElements:
			if (anElement in elementContainer or anElement in extraElementsList):
				choiceContainer.append("Gain {} CP".format(anElement))
				choiceColors.append(cardLogic_get_elementColorCode(anElement))
				numChoices += 1
		choiceContainer.append("Dull (No CP)")
		choiceColors.append(cardLogic_get_elementColorCode("MenuColor"))
		
		askNum = askChoice("Gain CP? Or Dull?", choiceContainer, choiceColors) - 1
		if (askNum >= 0 and askNum < numChoices):
			chosenElement = choiceContainer[askNum].split(" ")[1]
			counterName = chosenElement + " CP"
			me.counters[counterName].value += 1
			dullCard.orientation = 1
			notify("{} dulls {} and gains 1 {} CP.".format(me, cardLogic_get_fullNameObject(dullCard), chosenElement))
			gainCP = "TRUE"
		elif (askNum != numChoices):
			return
			
	if (gainCP == "FALSE"):
		dullCard.orientation = 1
		notify("{} dulls {}.".format(me, cardLogic_get_fullNameObject(dullCard)))
	
def cardLogic_activate(card):
	mute()
	card.orientation = 0
	notify("{} activates {}.".format(me, cardLogic_get_fullNameObject(card)))
	
def cardLogic_freezeOrUnfreeze(card, x = 0, y = 0):
	mute()
	# whisper("{}".format(card.filter))
	
	if ("Forward" not in cardLogic_get_typeContainer(card) and "Backup" not in cardLogic_get_typeContainer(card) and "Monster" not in cardLogic_get_typeContainer(card)): return
	if (card.filter == None): cardLogic_freeze(card)
	else: cardLogic_unfreeze(card)
	
def cardLogic_freeze(card):
	card.filter = cardLogic_get_freezeColor()
	notify("{} has been frozen.".format(cardLogic_get_fullNameObject(card)))
	
def cardLogic_unfreeze(card):
	card.filter = None
	notify("{} is no longer frozen.".format(cardLogic_get_fullNameObject(card)))
	
def cardLogic_specialAbility_1(card, x = 0, y = 0):
	mute()
	cardLogic_specialAbility(card, "SpecialAbility1")
	
def cardLogic_specialAbility_2(card, x = 0, y = 0):
	mute()
	cardLogic_specialAbility(card, "SpecialAbility2")
	
def cardLogic_specialAbility_3(card, x = 0, y = 0):
	mute()
	cardLogic_specialAbility(card, "SpecialAbility3")
	
def cardLogic_specialAbility(card, whichAbility):
	mute()
	
	anAbility = cardLogic_ability_find(card, whichAbility)
	# notify("{}".format(anAbility))
	
	saSections = anAbility.split("_")
	abilityName = saSections[0].split("|")[1]
			
	# Dull check
	if (saSections[2] == "Yes" and card.orientation != 0):
		playSound("error")
		askChoice("{} is dulled. It needs to be active in order to use {}.".format(cardLogic_get_fullNameString(card), abilityName), ["OK"], ["#111111"])
		return
		
	# GlobalSpecial check
	useGlobalSpecial = False
	anyCardInHand = False
	costTargets = []
	chosenSpecialist = card
	crystalCost = False
	chosenCrystal = None
	globalSpecialists = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "GlobalSpecial") != "N/A")
	for aCard in globalSpecialists:
		anAbility = cardLogic_ability_find(aCard, "GlobalSpecial")
		anAbilityList = anAbility.split("|")
		searchLogicArray = anAbilityList[1]
		searchResults = searchLogic_search("Player", "Table", searchLogicArray, "ReturnArray")
		if (card in searchResults):
			menuNames_GS = []
			menuColors_GS = []
			menuNames_GS.append("Yes")
			menuColors_GS.append("#9d2411")
			menuNames_GS.append("No")
			menuColors_GS.append("#111111")
			askNum_GS = askChoice("Use the ability of {}?".format(cardLogic_get_fullNameString(aCard)), menuNames_GS, menuColors_GS)
			if (askNum_GS == 1): 
				if (anAbilityList[2] == "N/A"): 
					useGlobalSpecial = True 
					chosenSpecialist = aCard
				elif (anAbilityList[2] == "Crystal"):
					crystalArray = (card for card in table 
									if card.controller == me
									and card.Type == "CrystalPoint")
					crystalCount = 0
					for aCrystal in crystalArray:
						crystalCount = crystalCount + 1
						chosenCrystal = aCrystal
					if (crystalCount == 0):
						askChoice("You need a Crystal in order to use {}'s ability.".format(cardLogic_get_fullNameString(aCard)), ["OK"], ["#111111"])
						return
					else:
						useGlobalSpecial = True 
						chosenSpecialist = aCard
						crystalCost = True
				elif (anAbilityList[2] == "AnyCardInHand"):
					useGlobalSpecial = True
					anyCardInHand = True
					charactersInHand = (aCard for aCard in me.hand)
					for aCard in charactersInHand:
						costTargets.append(aCard)
					if (len(costTargets) == 0):
						playSound("error")
						askChoice("You don't have any cards in your hand. You need to discard one in order to use {}.".format(card.Name, abilityName), ["OK"], ["#111111"])
						return
		
	# Character check
	if (useGlobalSpecial == False):
		charactersInHand = (aCard for aCard in me.hand 
						if card.Name == aCard.Name)
		for aCard in charactersInHand:
			costTargets.append(aCard)
		if (saSections[3] != "None"):
			searchLogicArray = searchLogic_search("Player", "Hand", saSections[3], "ReturnArray")
			for aCard in searchLogicArray:
				costTargets.append(aCard)
		if (len(costTargets) == 0):
			playSound("error")
			askChoice("You don't have any cards named {} in your hand. You need to discard one in order to use {}.".format(card.Name, abilityName), ["OK"], ["#111111"])
			return
		
	# Cost check
	elementsArray = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
	abilityCosts = saSections[1].split("/")
	counterTotal = 0
	neededTotal = 0
	for index in range(0, 8):
		counterName = elementsArray[index] + " CP"
		counterValue = me.counters[counterName].value
		neededValue = int(abilityCosts[index])
		if (neededValue > counterValue):
			playSound("error")
			askChoice("You have {} {}. You need at least {} {} in order to use {}.".format(counterValue, counterName, neededValue, counterName, abilityName), ["OK"], ["#111111"])
			return
		counterTotal += counterValue
		neededTotal += neededValue
	neededTotal += int(abilityCosts[8])
	if (neededTotal > counterTotal):
		cpDiff = neededTotal - counterTotal
		playSound("error")
		askChoice("You need an additional {} CP in order to use {}.".format(cpDiff, abilityName), ["OK"], ["#111111"])
		return
		
	# Additional field check
	if (saSections[4] != "None"):
		searchLogicCount = searchLogic_search(saSections[4], saSections[5], saSections[6], "ReturnInteger")
		if (searchLogicCount == 0):
			playSound("error")
			askChoice("You do not meet the additional requirements needed to use {}.".format(abilityName), ["OK"], ["#111111"])
			return
			
	# Choose card from hand
	if (useGlobalSpecial == False or anyCardInHand == True):
		menuNames = []
		menuColors = []
		for aCard in costTargets:
			mName = "{} ({})".format(aCard.Name, aCard.SetNumber)
			menuNames.append(mName)
			menuColors.append(cardLogic_get_elementColorCode(aCard.Element))
		menuNames.append("Cancel")
		menuColors.append("#111111")
		askNum = askChoice("To use {}, which card are you discarding from your hand?".format(abilityName), menuNames, menuColors)
		if (askNum == 0 or askNum > len(costTargets)): return
		chosenDiscard = costTargets[askNum - 1]
	
		# Discard and show highlight
		cardLogic_resetCPCounters()
		chosenDiscard.moveTo(me.piles["Break Zone"])
		cardLogic_set_borderColor(card, "SpecialAbility")
		notify("{} discards {} to the Break Zone to use {}'s special ability, {}!".format(me, cardLogic_get_fullNameObject(chosenDiscard), cardLogic_get_fullNameObject(card), abilityName))
		playSound("specialAbility")
		if (saSections[2] == "Yes"): cardLogic_dull(card, True)
	else:
		if (crystalCost == True):
			chosenCrystal.moveTo(me.piles["Break Zone"])
		cardLogic_set_borderColor(chosenSpecialist, "Ability")
		cardLogic_resetCPCounters()
		cardLogic_set_borderColor(card, "SpecialAbility")
		notify("{} uses {}'s special ability, {}!".format(me, cardLogic_get_fullNameObject(card), abilityName))
		playSound("specialAbility")
		if (saSections[2] == "Yes"): cardLogic_dull(card, True)
	
def cardLogic_resetCPCounters():
	mute()
	allElementsArray = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
	for anElement in allElementsArray:
		counterName = anElement + " CP"
		me.counters[counterName].value = 0
		
def cardLogic_searchForCard_1(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard1"):
			searchString = anAbilityList[2]
			cardLogic_searchForCard(card, searchString)
	
def cardLogic_searchForCard_2(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard2"):
			searchString = anAbilityList[2]
			cardLogic_searchForCard(card, searchString)
			
def cardLogic_searchForCard_3(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard3"):
			searchString = anAbilityList[2]
			cardLogic_searchForCard(card, searchString)
			
def cardLogic_searchForCard(card, searchString):
	mute()
	# whisper("{}".format(searchString))
	searchList = searchString.split("_")
	
	searchPile = None
	locationName = searchList[1]
	if (locationName == "Deck"):
		searchPile = me.Deck
		notify("{} is searching their Deck for a card...".format(me))
	elif (locationName == "BreakZone"):
		searchPile = me.piles["Break Zone"]
		notify("{} is searching their Break Zone for a card...".format(me))
		
	cardLogic_set_borderColor(card, "Ability")
	searchResults = searchLogic_search(searchList[0], searchList[1], searchList[2], "ReturnArray")
	if (len(searchResults) == 0):
		playSound("error")
		askChoice("There were no valid search targets.", ["OK"], ["#111111"])
		return
	else:
		searchResults.sort(cardLogic_searchForCard_sorting)
		for aCard in searchResults:
			aCard.moveTo(searchPile, 0)
		searchPile.lookAt(-1)
		#if (locationName == "Deck"):
			#whisper("Please remember to shuffle your Deck after searching.")
			
		searchReminderPopup = me.getGlobalVariable("searchReminderPopup")
		if (searchReminderPopup == "FALSE"):
			askChoice("To use the ability of the first card in your deck (position 0), or play it onto the field, you will need to drag it to a different spot before those abilities will show up in the menu. Also, please remember to shuffle your Deck if you are searching the Deck.", ["OK"], ["#111111"])
			me.setGlobalVariable("searchReminderPopup", "TRUE")

def cardLogic_searchForCard_sorting(card1, card2):
	mute()
	
	nameValue1 = card1.Name
	nameValue2 = card2.Name
	if (nameValue1 > nameValue2): return -1
	elif (nameValue1 < nameValue2): return 1
	
	setString1 = card1.SetNumber.split("-")[0]
	setString2 = card2.SetNumber.split("-")[0]
	
	if (setString1 != "PR" and setString2 != "PR"):
		setNumber1 = int(setString1)
		setNumber2 = int(setString2)
		if (setNumber1 > setNumber2): return -1
		elif (setNumber1 < setNumber2): return 1
		
		cardNumber1 = int(card1.SetNumber.split("-")[1])
		cardNumber2 = int(card2.SetNumber.split("-")[1])
		if (cardNumber1 > cardNumber2): return -1
		elif (cardNumber1 < cardNumber2): return 1
	elif (setString1 == "PR" and setString2 != "PR"): return -1
	elif (setString1 != "PR" and setString2 == "PR"): return 1
	else:
		cardNumber1 = int(card1.SetNumber.split("-")[1])
		cardNumber2 = int(card2.SetNumber.split("-")[1])
		if (cardNumber1 > cardNumber2): return -1
		elif (cardNumber1 < cardNumber2): return 1
	
	return 0
	
def cardLogic_turnIntoAForward(cardToChange, x = 0, y = 0):
	mute()
	defaultPower = 1000
	if (cardToChange.Power != ""): defaultPower = int(cardToChange.Power)
	
	anAbility = cardLogic_ability_find(cardToChange, "InnerStrength")
	if (anAbility != "N/A"):
		anAbilityList = anAbility.split("|")
		abilityPower = int(anAbilityList[1])
		if (abilityPower > defaultPower):
			defaultPower = abilityPower
			
	beastmasters = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and cardLogic_ability_find(card, "Beastmaster") != "N/A")
	for aCard in beastmasters:
		# whisper("Beastmaster - {}".format(cardLogic_get_fullNameObject(aCard)))
		anAbility = cardLogic_ability_find(aCard, "Beastmaster")
		anAbilityList = anAbility.split("|")
		searchLogicArray = anAbilityList[1].split("_")
		searchResults = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
		if (cardToChange in searchResults):
			abilityPower = int(anAbilityList[2])
			if (abilityPower > defaultPower):
				defaultPower = abilityPower
				
	printedPower = 0
	if (cardToChange.Power != ""): printedPower = int(cardToChange.Power)
	
	typeContainerArray = cardToChange.TypeContainer.split(" - ")
	typeContainerArray.append("Forward")
	cardToChange.TypeContainer = " - ".join(typeContainerArray)
	cardLogic_set_borderColor(cardToChange, "Ability")
	notify("{} has become a Forward with {} power.".format(cardLogic_get_fullNameObject(cardToChange), defaultPower))
	
	powerLogic_calculate(cardToChange, defaultPower - printedPower)
	
def cardLogic_stopBeingAForward(cardToChange, x = 0, y = 0):
	mute()
	
	typeContainerArray = cardToChange.TypeContainer.split(" - ")
	typeContainerArray.remove("Forward")
	cardToChange.TypeContainer = " - ".join(typeContainerArray)
	notify("{} is no longer a Forward.".format(cardLogic_get_fullNameObject(cardToChange)))
	
	powerLogic_cleanupHUD(cardToChange)
	cardLogic_set_powerContainer(cardToChange, 0, 0, 0)
	
def cardLogic_revealCards_1(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "RevealCards1"):
			cardLogic_revealCards(card, anAbilityList[1], anAbilityList[2], anAbilityList[3])
			
def cardLogic_revealCards_2(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "RevealCards2"):
			cardLogic_revealCards(card, anAbilityList[1], anAbilityList[2], anAbilityList[3])
			
def cardLogic_revealCards(card, revealType, quantity, correctTargets, fromTop = True):
	mute()
	
	newTargetsArray = []
	correctTargetsArray = correctTargets.split("AND")
	for aTarget in correctTargetsArray:
		aTargetArray = aTarget.split(",")
		
		if (aTargetArray[0] == "Type" and aTargetArray[2] == "PlayerChoice"):
			typeChoiceArray = ["Forward", "Backup", "Summon", "Monster", "Cancel"]
			askChoiceResult = askChoice("Select a Type of card:", typeChoiceArray, ["#660000", "#660000", "#660000", "#660000", "#111111"])
			if (askChoiceResult < 1 or askChoiceResult > 4): return
			aTargetArray[2] = typeChoiceArray[(askChoiceResult - 1)]
		
		newTarget = ",".join(aTargetArray)
		newTargetsArray.append(newTarget)
	newTargetString = "AND".join(newTargetsArray)
	# notify(newTargetString)
	
	cardsFromTop = -1
	if (revealType == "Quantity"):
		cardsFromTop = int(quantity)
	elif (revealType == "Target"):
		foundCards = 0
		foundTarget = int(quantity)
		for index in range(0, len(me.Deck)):
			cardToCheck = me.Deck[index]
			searchResults = searchLogic_search("Player", "CardToPlay", newTargetString, "ReturnInteger", cardToCheck)
			if (cardsFromTop == -1 and searchResults > 0):
				foundCards = foundCards + 1
				if (foundCards >= foundTarget):
					# whisper("Breaking")
					cardsFromTop = (index + 1)
					break
		
	if (cardsFromTop == -1):
		playSound("error")
		askChoice("There were no valid search targets.", ["OK"], ["#111111"])
		return
		
	if (cardsFromTop > len(me.Deck)):
		cardsFromTop = len(me.Deck)
		
	# cardsFromTop += 20
	
	startX = 0
	endX = 0
	posY = 0
	foundY = 0
	direction = -1
	playerOne = True if (me._id == 1) else False
	if (playerOne == True):
		startX = 185
		endX = 485
		posY = 203
		foundY = -20
	else:
		startX = -233
		endX = -533
		posY = -343
		foundY = 20
	
	middleX = startX + ((endX - startX) / 2)
	intervalX = ((endX - startX) / cardsFromTop)
	
	
	foundATarget = False
	for index in range(0, cardsFromTop):
		actualX = startX + middleX + (intervalX * direction * (index + 1))
		# whisper("{}".format(actualX))
		thisCard = me.Deck[0]
		if (fromTop == False):
			thisCard = me.Deck[len(me.Deck) - 1]
		if (newTargetString != "N/A" and searchLogic_search("Player", "CardToPlay", newTargetString, "ReturnInteger", thisCard) > 0):
			thisCard.moveToTable(actualX, posY + foundY)
			cardLogic_set_borderColor(thisCard, "RevealMatch")
			foundATarget = True
		else:
			thisCard.moveToTable(actualX, posY)
		
	if (fromTop == True):
		notify("{} reveals the top {} card(s) of their Deck.".format(me, cardsFromTop))
	else:
		notify("{} reveals the bottom {} card(s) of their Deck.".format(me, cardsFromTop))
	if (foundATarget == True):
		notify("A target card was found!")
	elif (foundATarget == False and newTargetString != "N/A"):
		notify("No target cards were found...")
		
def cardLogic_activateCards_1(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "ActivateCards1"):
			cardLogic_activateCards(card, anAbilityList[2])
			
def cardLogic_activateCards_2(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "ActivateCards2"):
			cardLogic_activateCards(card, anAbilityList[2])
			
def cardLogic_activateCards(card, correctTargets):
	mute()
	
	readyCount = 0
	searchResultsArray = searchLogic_search("Player", "Table", correctTargets, "ReturnArray")
	for aCard in searchResultsArray:
		if (aCard.orientation != 0):
			aCard.orientation = 0
			readyCount += 1
			
	cardLogic_set_borderColor(card, "Ability")
	notify("{} readies their cards.".format(me))
	if (readyCount == 0):
		notify("But no targets were found...")

def cardLogic_countCards_1(card, x = 0, y = 0):
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "CountCards1"):
			cardLogic_countCards(card, anAbilityList[2])
	
def cardLogic_countCards(card, correctTargets):
	mute()
	
	totalCount = 0
	
	searchVariables = correctTargets.split("_")
	allSearchStrings = searchVariables[2].split("-OR-")
	for searchString in allSearchStrings:
		searchResultsArray = searchLogic_search(searchVariables[0], searchVariables[1], searchString, "ReturnArray")
		numFound = len(searchResultsArray)
		if (card.Name == "Golbez" and (card.SetNumber == "2-109" or card.SetNumber == "PR-024") and numFound > 1): numFound = 1
		totalCount += numFound
	
	askChoice("Number of cards found: {}".format(totalCount), ["OK"], ["#111111"])
	
def cardLogic_vanish(card, x = 0, y = 0):
	mute()
	
	mute()
	abilityList = card.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "Vanish"):
			onOffSwitch = anAbilityList[1]
			startCount = anAbilityList[2]
			currentCount = anAbilityList[3]
			
			thisMarker = ("Vanished", "Vanished ID")
			
			if (onOffSwitch == "OFF"): 
				onOffSwitch = "ON"
				currentCount = startCount
				notify("{} has vanished!".format(cardLogic_get_fullNameObject(card)))
				card.filter = "#88535657"
				card.Active = "FALSE"
				card.markers[thisMarker] = int(startCount)
			else:
				onOffSwitch = "OFF"
				currentCount = "0"
				notify("{} has returned to the table.".format(cardLogic_get_fullNameObject(card)))
				card.filter = None
				card.Active = "TRUE"
				card.markers[thisMarker] = 0
				gameLogic_onPlay_organizeQueue(card.Type)
				
			newSwitchString = "Vanish" + "|" + onOffSwitch + "|" + startCount + "|" + currentCount
			newAbilities = card.AbilitiesContainer.replace(anAbility, newSwitchString)
			card.AbilitiesContainer = newAbilities
			
			powerLogic_reset(card)
			powerLogic_powerBoost_calculate(table)
		
def cardLogic_changeElement(card, chosenElement):
	mute()
	
	removeElement = False
	elementContainerArray = card.ElementContainer.split(" - ")
	for anElement in elementContainerArray:
		if (anElement == chosenElement):
			elementContainerArray.remove(chosenElement)
			card.ElementContainer = " - ".join(elementContainerArray)
			cardLogic_set_borderColor(card, "Ability")
			notify("{} loses the {} element.".format(cardLogic_get_fullNameObject(card), chosenElement))
			removeElement = True
			
	if (removeElement == False):
		elementContainerArray.append(chosenElement)
		card.ElementContainer = " - ".join(elementContainerArray)
		cardLogic_set_borderColor(card, "Ability")
		notify("{} gains the {} element.".format(cardLogic_get_fullNameObject(card), chosenElement))
		
def cardLogic_changeElement_fire(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Fire")
	
def cardLogic_changeElement_ice(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Ice")
	
def cardLogic_changeElement_wind(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Wind")
	
def cardLogic_changeElement_earth(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Earth")
	
def cardLogic_changeElement_lightning(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Lightning")
	
def cardLogic_changeElement_water(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Water")
	
def cardLogic_changeElement_light(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Light")
	
def cardLogic_changeElement_dark(card, x = 0, y = 0):
	mute()
	cardLogic_changeElement(card, "Dark")
	
def cardLogic_attack(card, x = 0, y = 0):
	mute()
	
	if ("Forward" not in cardLogic_get_typeContainer(card)): return
	if (card.Active != "TRUE"): return
	
	cardLogic_set_borderColor(card, "Attack")
	notify("{} declares an attack with {}.".format(me, cardLogic_get_fullNameObject(card)))
	
def cardLogic_partyAttack(card, x = 0, y = 0):
	mute()
	
	if ("Forward" not in cardLogic_get_typeContainer(card)): return
	if (card.Active != "TRUE"): return
	
	cardLogic_set_borderColor(card, "PartyAttack")
	notify("{} declares a party attack including {}.".format(me, cardLogic_get_fullNameObject(card)))
	
def cardLogic_defend(card, x = 0, y = 0):
	mute()
	
	if ("Forward" not in cardLogic_get_typeContainer(card)): return
	if (card.Active != "TRUE"): return
	
	cardLogic_set_borderColor(card, "Defend")
	notify("{} defends with {}.".format(me, cardLogic_get_fullNameObject(card)))
	
def cardLogic_removeHighlights(card, x = 0, y = 0):
	mute()
	cardLogic_set_borderColor(card, "");
	
def cardLogic_declareAbility(card, x = 0, y = 0):
	mute()
	
	cardLogic_set_borderColor(card, "Ability")
	notify("{} uses the ability of {}.".format(me, cardLogic_get_fullNameObject(card)))
	
def cardLogic_removeHighlights(card, x = 0, y = 0):
	mute()
	cardLogic_set_borderColor(card, "");
	
def cardLogic_addCounter(card, x = 0, y = 0):
	mute()
	
	availableCounters = cardLogic_identifyAvailableCounters(card)
	# whisper("Counters - {}".format(availableCounters))
	
	availableCounters.append("Cancel")
	choiceColors = []
	for aCounter in availableCounters:
		choiceColors.append(cardLogic_get_elementColorCode("MenuColor"))
		
	askNum = askChoice("Which counter will be added?", availableCounters, choiceColors)
	# whisper("{}".format(askNum))
	if (askNum == 0 or askNum == len(availableCounters)): return
	
	chosenCounter = availableCounters[askNum - 1]
	chosenCounterID = chosenCounter + " ID"
	
	thisMarker = (chosenCounter, chosenCounterID)
	card.markers[thisMarker] += 1
	
	notify("{} adds one {} to {}.".format(me, availableCounters[askNum - 1], cardLogic_get_fullNameObject(card)))
	
	# whisper("powerLogic");
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_removeCounter(card, x = 0, y = 0):
	mute()
	
	availableCounters = cardLogic_identifyAvailableCounters(card)
	# whisper("Counters - {}".format(availableCounters))
	
	availableCounters.append("Cancel")
	choiceColors = []
	for aCounter in availableCounters:
		choiceColors.append(cardLogic_get_elementColorCode("MenuColor"))
		
	askNum = askChoice("Which counter will be added?", availableCounters, choiceColors)
	# whisper("{}".format(askNum))
	if (askNum == 0 or askNum == len(availableCounters)): return
	
	chosenCounter = availableCounters[askNum - 1]
	chosenCounterID = chosenCounter + " ID"
	
	thisMarker = (chosenCounter, chosenCounterID)
	if (card.markers[thisMarker] > 0):
		card.markers[thisMarker] -= 1
	
		notify("{} removes one {} from {}.".format(me, availableCounters[askNum - 1], cardLogic_get_fullNameObject(card)))
		
		powerLogic_powerBoost_calculate(table)
	
def cardLogic_identifyAvailableCounters(passedCard):
	mute()
	
	availableCounters = []
	
	activeCards = (card for card in table
					if card.Active == "TRUE" 
					and cardLogic_ability_find(card, "Counter") != "N/A")
	for aCard in activeCards:
		anAbility = cardLogic_ability_find(aCard, "Counter")
		anAbilityList = anAbility.split("|")
		availableCounters.append(anAbilityList[1])
		
	keys = list(dict.fromkeys(passedCard.markers))
	# whisper("keys - {}".format(keys))
	for aKey in keys:
		availableCounters.append(aKey[0])
	
	availableCounters = list(dict.fromkeys(availableCounters))
	availableCounters.sort()
				
	return availableCounters
	
def cardLogic_discardAbility(card, x = 0, y = 0):
	cardLogic_playOrCast(card, 0, 0, "TRUE", "TRUE", "TRUE")
	
def cardLogic_setTarget(card, x = 0, y = 0):
	mute()
	if (card.filter == None): 
		card.filter = cardLogic_get_targetColor()
		card.select(False)
	else: card.filter = None
	
def cardLogic_breakZone_removeAll(group, x = 0, y = 0):
	mute()
	if (len(me.piles["Break Zone"]) < 1): return
	askChoiceResult = askChoice("Send all cards in your Break Zone to be Removed From Game?", ["Yes", "No"], ["#660000", "#111111"])
	if (askChoiceResult != 1): return
	
	for aCard in me.piles["Break Zone"]:
		aCard.moveTo(me.piles["Removed From Game"])
	notify("{} removes all cards in their Break Zone from the game.".format(me))
	
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_breakZone_removeCharacters(group, x = 0, y = 0):
	mute()
	cardLogic_breakZone_removeCards("Character")
	
def cardLogic_breakZone_removeForwards(group, x = 0, y = 0):
	mute()
	cardLogic_breakZone_removeCards("Forward")
	
def cardLogic_breakZone_removeBackups(group, x = 0, y = 0):
	mute()
	cardLogic_breakZone_removeCards("Backup")
	
def cardLogic_breakZone_removeSummons(group, x = 0, y = 0):
	mute()
	cardLogic_breakZone_removeCards("Summon")
	
def cardLogic_breakZone_removeMonsters(group, x = 0, y = 0):
	mute()
	cardLogic_breakZone_removeCards("Monster")
	
def cardLogic_breakZone_removeCards(cardType):
	mute()
	if (len(me.piles["Break Zone"]) < 1): return
	askChoiceResult = askChoice("Send all {}s in your Break Zone to be Removed From Game?".format(cardType), ["Yes", "No"], ["#660000", "#111111"])
	if (askChoiceResult != 1): return
	
	removedOne = False
	for aCard in me.piles["Break Zone"]:
		if (aCard.Type == cardType or (cardType == "Character" and aCard.Type != "Summon")):
			aCard.moveTo(me.piles["Removed From Game"])
			removedOne = True
	if (removedOne == True):
		notify("{} removes all {}s in their Break Zone from the game.".format(me, cardType))
		
	powerLogic_powerBoost_calculate(table)
	
def cardLogic_addDefaultCounter(card, x = 0, y = 0):
	mute()
	defaultCounter = cardLogic_ability_find(card, "Counter")
	if (defaultCounter != "N/A"):
		counterName = defaultCounter.split("|")[1]
		thisMarker = (counterName, counterName + " ID")
		card.markers[thisMarker] += 1
	
		notify("{} adds one {} to {}.".format(me, counterName, cardLogic_get_fullNameObject(card)))
		
		powerLogic_powerBoost_calculate(table)
	else:
		currentMarkers = card.markers
		keyList = list(currentMarkers)
		if (len(keyList) == 1):
			counterName = str(keyList[0][0])
			# whisper("{}".format(counterName))
			thisMarker = (counterName, counterName + " ID")
			card.markers[thisMarker] += 1
	
			notify("{} adds one {} to {}.".format(me, counterName, cardLogic_get_fullNameObject(card)))
			
			powerLogic_powerBoost_calculate(table)
		else:
			availableCounters = cardLogic_identifyAvailableCounters(card)
			# whisper("available counters - {}".format(availableCounters))
			if (len(availableCounters) == 1):
				counterName = availableCounters[0]
				# whisper("{}".format(counterName))
				thisMarker = (counterName, counterName + " ID")
				card.markers[thisMarker] += 1
	
				notify("{} adds one {} to {}.".format(me, counterName, cardLogic_get_fullNameObject(card)))
				
				powerLogic_powerBoost_calculate(table)
				
def cardLogic_removeDefaultCounter(card, x = 0, y = 0):
	mute()
	removedCounter = False
	
	defaultCounter = cardLogic_ability_find(card, "Counter")
	if (defaultCounter != "N/A"):
		counterName = defaultCounter.split("|")[1]
		thisMarker = (counterName, counterName + " ID")
		if (card.markers[thisMarker] > 0):
			card.markers[thisMarker] -= 1
		
			notify("{} removes one {} from {}.".format(me, counterName, cardLogic_get_fullNameObject(card)))
			powerLogic_powerBoost_calculate(table)
			removedCounter = True
	
	if (removedCounter == False):
		currentMarkers = card.markers
		keyList = list(currentMarkers)
		if (len(keyList) == 1):
			counterName = str(keyList[0][0])
			# whisper("{}".format(counterName))
			thisMarker = (counterName, counterName + " ID")
			if (card.markers[thisMarker] > 0):
				card.markers[thisMarker] -= 1
		
				notify("{} removes one {} from {}.".format(me, counterName, cardLogic_get_fullNameObject(card)))
				powerLogic_powerBoost_calculate(table)
				removedCounter = True
				
def cardLogic_showPile(group, x = 0, y = 0):
	mute()
	group.lookAt(-1)
	
def cardLogic_swapCard(card, x = 0, y = 0):
	if (len(me.hand) == 0):
		playSound("error")
		askChoice("You have no cards in your hand", ["OK"], ["#111111"])
		return
	    
	swapTargets = []
	cardsInHand = (aCard for aCard in me.hand)
	for aCard in cardsInHand:
		swapTargets.append(aCard)
	swapTargets = swapTargets[::-1]
	
	# Choose card from hand
	menuNames = []
	menuColors = []
	for aCard in swapTargets:
		mName = "{} ({})".format(aCard.Name, aCard.SetNumber)
		menuNames.append(mName)
		menuColors.append(cardLogic_get_elementColorCode(aCard.Element))
	
	# menuNames = menuNames[::-1]
	# menuColors = menuColors[::-1]
	
	menuNames.append("Cancel")
	menuColors.append("#111111")
	askNum = askChoice("Swap with which card from your hand?", menuNames, menuColors)
	if (askNum == 0 or askNum > len(swapTargets)): return
	chosenCard = swapTargets[askNum - 1]
	
	# whisper("{}".format(chosenCard))
	
	damageZoneCard = (aCard for aCard in me.piles["Damage Zone"]
						if aCard.SetNumber == card.SetNumber)
	for aCard in damageZoneCard:
		# whisper("{}".format(aCard))
		
		cardX, cardY = card.position
		newCard = table.create(chosenCard.model, cardX, cardY)
		newCard.Active = "FALSE"
		newCard.Type = "DamageZone"
		newCard.orientation = 1
		currentAbilities = newCard.AbilitiesContainer
		if (currentAbilities == ""):
			newCard.AbilitiesContainer = "CanSwap"
		else:
			newCard.AbilitiesContainer = currentAbilities + "][CanSwap"
		cardLogic_set_borderColor(newCard, "Ability")
		
		notify("{} swaps {} in their Damage Zone with {}.".format(me, cardLogic_get_fullNameObject(card), cardLogic_get_fullNameObject(newCard)))
		aCard.moveTo(me.Hand)
		chosenCard.moveTo(me.piles["Damage Zone"])
        
		card.delete()
        
		break
	
	remoteCall(me, "cardLogic_swapCard_reset", [])
  
def cardLogic_swapCard_reset():
	mute()
	# whisper("in function")
    
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
	
	thisIncrement = 0
	existingCards = (aCard for aCard in table 
						if aCard.controller == me
						and aCard.Type == "DamageZone")
	for aCard in existingCards:
		aCard.sendToBack()
		aCard.moveToTable(posX, posY + (incrementY * thisIncrement))
		thisIncrement = thisIncrement + 1
		# whisper("{} - {}".format(aCard, aCard.index))
        
def cardLogic_freeVoid(group, x = 0, y = 0):
	mute()
	if (len(players) == 1): return
	
	notify("{} is giving the cards in their Void back to their opponent.".format(me))
	for aCard in me.piles["The Void"]:
		aCard.resetProperties()
		
		otherPlayer = gameLogic_query_otherPlayer()
		aCard.moveToTable(0, 0)
		# aCard.isFaceUp = False
		aCard.controller = otherPlayer
		
def cardLogic_showLBDeck(card, x = 0, y = 0):
	mute()
	me.piles["LB Deck"].lookAt(-1)
    
def cardLogic_prime_dominant(dominantCard, x = 0, y = 0):
	mute()
	deckFormat = me.getGlobalVariable("deckFormat")
	
	if (dominantCard.AbilitiesContainer == ""): return False
	abilityList = dominantCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "Prime_Dominant"):
			targetName = anAbilityList[1]
			targetCost = anAbilityList[2]
			
			noColorProblem = "FALSE"
				
			aoeCardsPrimecast = (card for card in table 
				if card.controller == me 
				and card.Active == "TRUE" 
				and cardLogic_ability_find(card, "Primecast") != "N/A")
			for aoeCard in aoeCardsPrimecast:
				abilityList = aoeCard.AbilitiesContainer.split("][")
				for anAbility in abilityList:
					anAbilityList = anAbility.split("|")
					if (anAbilityList[0] == "Primecast" and anAbilityList[1] == "AoE"):
						searchVariables = anAbilityList[2].split("_")
						searchResults = searchLogic_search(searchVariables[0], searchVariables[1], searchVariables[2], "ReturnInteger", dominantCard)
						if (searchResults > 0):
							noColorProblem = "TRUE"
			
			# Cost check
			elementsArray = ["Fire", "Ice", "Wind", "Earth", "Lightning", "Water", "Light", "Dark"]
			abilityCosts = targetCost.split("/")
			counterTotal = 0
			neededTotal = 0
			for index in range(0, 8):
				counterName = elementsArray[index] + " CP"
				counterValue = me.counters[counterName].value
				neededValue = int(abilityCosts[index])
				if (neededValue > counterValue and noColorProblem == "FALSE"):
					playSound("error")
					askChoice("You have {} {}. You need at least {} {} in order to Prime {}.".format(counterValue, counterName, neededValue, counterName, targetName), ["OK"], ["#111111"])
					return
				counterTotal += counterValue
				neededTotal += neededValue
			neededTotal += int(abilityCosts[8])
			if (neededTotal > counterTotal):
				cpDiff = neededTotal - counterTotal
				playSound("error")
				askChoice("You need an additional {} CP in order to Prime {}.".format(cpDiff, targetName), ["OK"], ["#111111"])
				return
				
			# Name Check (for non-Title format)
			if (deckFormat != "Title" and deckFormat != "Custom"):
				sameNameString = "";
				myCardsWithSameName = (card for card in table
										if card.controller == me 
										and card.Active == "TRUE" 
										and card.Name == targetName)
				for aSameName in myCardsWithSameName:
					sameNameString += "\n- {}".format(cardLogic_get_fullNameString(aSameName))
					
				myCardsWithAltName2 = (card for card in table
										if card.controller == me 
										and card.Active == "TRUE" 
										and ("AlternateName|" + targetName) in card.AbilitiesContainer)
				for aSameName in myCardsWithAltName2:
					# whisper("match alt name 2")
					sameNameString += "\n- {}".format(cardLogic_get_fullNameString(aSameName))
										
				
				if (sameNameString != ""):
					fullSameNameString = "You cannot have these cards in play at the same time:"
					fullSameNameString += "\n\n- {}".format(targetName)
					fullSameNameString += sameNameString
					
					playSound("error")
					askChoice(fullSameNameString, ["OK"], ["#111111"])
					return
					
			# Target check (in deck)
			foundTarget = False
			foundTargetArray = []
			for bCard in me.Deck:
				if (bCard.Name == targetName):
					foundTarget = True
					foundTargetArray.append(bCard)
			if (foundTarget == False):
				playSound("error")
				askChoice("There are no valid targets named {} in your Deck.".format(targetName), ["OK"], ["#111111"])
				return
				
			# Should be good
			menuNames = []
			menuColors = []
			for aCard in foundTargetArray:
				mName = "{} ({})".format(aCard.Name, aCard.SetNumber)
				menuNames.append(mName)
				menuColors.append(cardLogic_get_elementColorCode(aCard.Element))
			menuNames.append("Cancel")
			menuColors.append("#111111")
			askNum = askChoice("Select your Prime target from your Deck:", menuNames, menuColors)
			if (askNum == 0 or askNum > len(foundTargetArray)): return
			chosenEikon = foundTargetArray[askNum - 1]
			
			dominantName = cardLogic_get_fullNameObject(dominantCard)
			dominantShortName = dominantCard.Name
			# whisper("dominantName: {}".format(dominantName))
			currentOrientation = dominantCard.orientation;
			
			powerLogic_cleanupHUD(dominantCard)
			dominantCard.moveTo(me.piles["The Void"])
			
			chosenEikon.moveToTable(0, 0)
			chosenEikon.Active = "TRUE"
			chosenEikon.orientation = currentOrientation
			
			chosenEikon.AbilitiesContainer = chosenEikon.AbilitiesContainer + "][AlternateName|" + dominantShortName
			if (cardLogic_ability_find(chosenEikon, "Prime_Eikon") != "N/A"):
				chosenEikon.AbilitiesContainer = chosenEikon.AbilitiesContainer.replace("Prime_Eikon|N/A", "Prime_Eikon|" + dominantShortName + " " + dominantName)
			else:
				chosenEikon.AbilitiesContainer = chosenEikon.AbilitiesContainer + "][Prime_Eikon|" + dominantShortName + " " + dominantName
			
			cardLogic_set_borderColor(chosenEikon, "Ability")
			cardLogic_resetCPCounters()
			cardLogic_set_borderColor(chosenEikon, "SpecialAbility")
			notify("{}'s {} has Primed into {}!".format(me, dominantName, cardLogic_get_fullNameObject(chosenEikon)))
			playSound("specialAbility")
			
			gameLogic_onPlay_organizeQueue(chosenEikon.Type)
			
			cardLogic_deck_shuffle(me.Deck, 0, 0)
			
			powerLogic_powerBoost_calculate(table)
    
def cardLogic_prime_eikon(card, x = 0, y = 0):
	mute()