def searchLogic_factor_cardName(card, operation, nameString):
	mute()
	# whisper("{} {} {}".format(card, operation, nameString))
	if (operation == "Is" and nameString == card.Name): return "TRUE"
	elif (operation == "IsNot" and nameString != card.Name): return "TRUE"
	elif (operation == "IsOneOf"):
		nameArray = nameString.split("OR")
		for aName in nameArray:
			if (aName == card.name): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_setNumber(card, operation, setNumberString):
	mute()
	if (operation == "Is" and setNumberString == card.SetNumber): return "TRUE"
	elif (operation == "IsNot" and setNumberString != card.SetNumber): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_cp(card, operation, cpString):
	mute()
	cpInt = int(cpString)
	cardCPInt = int(card.CP)
	if (operation == "Equals" and cardCPInt == cpInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and cardCPInt >= cpInt): return "TRUE"
	elif (operation == "LessThanOrEqualTo" and cardCPInt <= cpInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_element(card, operation, elementString):
	mute()
	if (operation == "Is"):
		if (elementString == "Multi-Element" and "-" in card.Element): return "TRUE"
		elif (elementString != "Multi-Element" and elementString in cardLogic_get_element(card)): return "TRUE"
	elif (operation == "IsNot"):
		if (elementString == "Multi-Element" and "-" not in card.Element): return "TRUE"
		elif (elementString != "Multi-Element" and elementString not in cardLogic_get_element(card)): return "TRUE"
	elif (operation == "IsOnly" and elementString in cardLogic_get_element(card) and "-" not in cardLogic_get_element(card)): return "TRUE"
	elif (operation == "IsOneOf"):
		elementArray = elementString.split("OR")
		for anElement in elementArray:
			if (anElement in cardLogic_get_element(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_elementContainer(card, operation, elementString):
	mute()
	if (operation == "Is" and elementString in cardLogic_get_elementContainer(card)): return "TRUE"
	elif (operation == "IsNot" and elementString not in cardLogic_get_elementContainer(card)): return "TRUE"
	elif (operation == "IsOneOf"):
		elementArray = elementString.split("OR")
		for anElement in elementArray:
			if (cardLogic_get_elementContainer(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_totalElements(foundCardsArray, operation, sizeString):
	mute()
	elementsArray = []
	for aCard in foundCardsArray:
		aCardElements = cardLogic_get_elementContainer(aCard)
		for anElement in aCardElements:
			if (anElement not in elementsArray): elementsArray.append(anElement)
		
	sizeInt = int(sizeString)
	if (operation == "GreaterThanOrEqualTo" and len(elementsArray) >= sizeInt): return "TRUE"
	elif (operation == "LessThanOrEqualTo" and len(elementsArray) <= sizeInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_type(card, operation, typeString):
	mute()
	# whisper("{} - {}".format(cardLogic_get_fullNameString(card), cardLogic_get_type(card)))
	if (operation == "Is" and typeString in cardLogic_get_type(card)): return "TRUE"
	elif (operation == "IsNot" and typeString not in cardLogic_get_type(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_typeContainer(card, operation, typeString):
	mute()
	if (operation == "Is" and typeString in cardLogic_get_typeContainer(card)): return "TRUE"
	elif (operation == "IsNot" and typeString not in cardLogic_get_typeContainer(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_job(card, operation, jobString):
	mute()
	if (operation == "Is" and jobString in cardLogic_get_job(card)): return "TRUE"
	elif (operation == "IsNot" and jobString not in cardLogic_get_job(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_jobContainer(card, operation, jobString):
	mute()
	if (operation == "Is" and jobString in cardLogic_get_jobContainer(card)): return "TRUE"
	elif (operation == "IsNot" and jobString not in cardLogic_get_jobContainer(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_onlyJobs(card, operation, jobsString):
	mute()
	jobsArray = jobsString.split("/")
	# whisper("{}".format(jobsArray))
	cardJobs = cardLogic_get_jobContainer(card)
	# whisper("{}".format(cardJobs))
	for aJob in cardJobs:
		if (aJob in jobsArray):
			return "TRUE"
	return "FALSE"
	
def searchLogic_factor_oneOfEachJob(foundCardsArray, operation, jobsString):
	mute()
	jobsArray = jobsString.split("/")
	for aJob in jobsArray:
		foundTheJob = False
		for aCard in foundCardsArray:
			aCardJobs = cardLogic_get_jobContainer(aCard)
			for cardJob in aCardJobs:	
				if (aJob == cardJob): foundTheJob = True
		if (foundTheJob == False): return "FALSE"
	return "TRUE"
	
def searchLogic_factor_totalJobs(foundCardsArray, operation, sizeString):
	mute()
	jobsArray = []
	for aCard in foundCardsArray:
		aCardJobs = cardLogic_get_jobContainer(aCard)
		for aJob in aCardJobs:
			if (aJob not in jobsArray): jobsArray.append(aJob)
		
	sizeInt = int(sizeString)
	if (operation == "GreaterThanOrEqualTo" and len(jobsArray) >= sizeInt): return "TRUE"
	elif (operation == "LessThanOrEqualTo" and len(jobsArray) <= sizeInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_category(card, operation, categoryString):
	mute()
	if (operation == "Is" and categoryString in cardLogic_get_category(card)): return "TRUE"
	elif (operation == "IsNot" and categoryString not in cardLogic_get_category(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_categoryContainer(card, operation, categoryString):
	mute()
	if (operation == "Is" and categoryString in cardLogic_get_categoryContainer(card)): return "TRUE"
	elif (operation == "IsNot" and categoryString not in cardLogic_get_categoryContainer(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_nameOrJob(card, operation, searchString):
	mute()
	if (operation == "Is" and searchString == card.Name): return "TRUE"
	elif (operation == "Is" and searchString in cardLogic_get_jobContainer(card)): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_power(card, operation, powerString):
	mute()
	powerInt = int(powerString)
	cardPowerInt = int(cardLogic_get_power(card))
	# whisper("{} - {} {} {}".format(cardLogic_get_fullNameObject(card), cardPowerInt, operation, powerInt))
	if (operation == "Equals" and cardPowerInt == powerInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and cardPowerInt >= powerInt): return "TRUE"
	elif (operation == "LessThanOrEqualTo" and cardPowerInt <= powerInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_totalPower(card, operation, powerString):
	mute()
	powerInt = int(powerString)
	cardTotalPowerInt = int(cardLogic_get_totalPower(card))
	if (operation == "Equals" and cardTotalPowerInt == powerInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and cardTotalPowerInt >= powerInt): return "TRUE"
	elif (operation == "LessThanOrEqualTo" and cardTotalPowerInt <= powerInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_containerSize(foundCardsArray, operation, sizeString):
	mute()
	sizeInt = int(sizeString)
	if (operation == "LessThanOrEqualTo" and len(foundCardsArray) <= sizeInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and len(foundCardsArray) >= sizeInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_playCountSummon(card, operation, sizeString):
	mute()
	sizeInt = int(sizeString)
	playCountString = me.getGlobalVariable("playCount_Summon")
	playCountInt = int(playCountString)
	if (operation == "LessThanOrEqualTo" and playCountInt <= sizeInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and playCountInt >= sizeInt): return "TRUE"
	return "FALSE"
	
def searchLogic_factor_orientation(card, operation, activeOrDull):
	mute()
	if (activeOrDull == "Active" and card.orientation == 0): return "TRUE"
	elif (activeOrDull == "Dull" and card.orientation != 0): return "TRUE"
	return "FALSE"
    
def searchLogic_factor_exBurst(card, operation, conditionString):
	mute()
	if (conditionString == "True" and card.EXBurst == "TRUE"): 
		return "TRUE"
	if (conditionString == "False" and card.EXBurst == "FALSE"): 
		return "TRUE"
	
	return "FALSE"
	
def searchLogic_factor_crystals(foundCardsArray, operation, sizeString):
	mute()
	# whisper("crystals foundCardsArray - {}".format(foundCardsArray))
	# whisper("crystals operation - {}".format(operation))
	# whisper("crystals sizeString - {}".format(sizeString))
	
	crystalArray = (card for card in table 
					if card.controller == me
					and card.Type == "CrystalPoint")
	crystalCount = 0
	for aCrystal in crystalArray:
		crystalCount = crystalCount + 1
	
	sizeInt = int(sizeString)
	# whisper("crystals sizeInt - {}".format(sizeInt))
	# whisper("crystals crystalCount - {}".format(crystalCount))
	if (operation == "LessThanOrEqualTo" and crystalCount <= sizeInt): return "TRUE"
	elif (operation == "GreaterThanOrEqualTo" and crystalCount >= sizeInt): return "TRUE"
	return "FALSE"

def searchLogic_factor_counter(card, operation, counterName):
	mute()
	thisMarker = (counterName, counterName + " ID")
	
	if (operation == "Is" and card.markers[thisMarker] > 0): return "TRUE"
	return "FALSE"

def searchLogic_factor_counterSize(card, operation, counterString):
	mute()
	# whisper("keyword - {} {} {}".format(cardLogic_get_fullNameString(card), operation, counterString))
	counterArray = counterString.split("/")
	thisMarker = (counterArray[0], counterArray[0] + " ID")
	numRequired = int(counterArray[1])
	
	if (operation == "Is" and card.markers[thisMarker] >= numRequired): return "TRUE"
	return "FALSE"
    
def searchLogic_factor_keyword(card, operation, myKeyword):
    mute()
    # whisper("keyword - {} {} {}".format(card, operation, myKeyword))
    if (operation == "Contains" or operation == "Is"):
        if (card.Abilities.find(myKeyword) != -1):
            return "TRUE"
    elif (operation == "Kain"):
        if (card.Abilities.find("Haste") != -1 or card.Abilities.find("First Strike") != -1):
            return "TRUE"
    
    return "FALSE"
	
def searchLogic_factor_specialCondition(foundCardsArray, operation, specialName):
	mute()
	# whisper("specialName {} {} {}".format(specialName, operation, foundCardsArray))
	
	if (specialName == "Meia"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_typeContainer(aCard, "Is", "Forward") == "TRUE"):
				if (searchLogic_factor_elementContainer(aCard, "Is", "Light") == "TRUE" or searchLogic_factor_jobContainer(aCard, "Is", "Warrior of Light") == "TRUE"):
					specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Graff"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_typeContainer(aCard, "Is", "Forward") == "TRUE"):
				if (searchLogic_factor_elementContainer(aCard, "Is", "Earth") == "TRUE" or searchLogic_factor_categoryContainer(aCard, "Is", "MOBIUS") == "TRUE"):
					specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Clan Gully"):
		foundLuso = False
		foundAdelle = False
		foundCid = False
		foundHurdy = False
		foundCount = 0
		clanGullyCount = 0
		for aCard in foundCardsArray:
			if (searchLogic_factor_cardName(aCard, "Is", "Luso") == "TRUE" and foundLuso == False): 
				foundLuso = True
				foundCount += 1
			if (searchLogic_factor_cardName(aCard, "Is", "Adelle") == "TRUE" and foundAdelle == False): 
				foundAdelle = True
				foundCount += 1
			if (searchLogic_factor_cardName(aCard, "Is", "Cid of Clan Gully") == "TRUE" and foundCid == False): 
				foundCid = True
				foundCount += 1
			if (searchLogic_factor_cardName(aCard, "Is", "Hurdy") == "TRUE" and foundHurdy == False): 
				foundHurdy = True
				foundCount += 1
			if (searchLogic_factor_cardName(aCard, "Is", "Clan Gully") == "TRUE"): clanGullyCount += 1
		if (foundLuso and foundAdelle and foundCid and foundHurdy): return "TRUE"
		elif ((foundCount + clanGullyCount) >= 4): return "TRUE"
	elif (specialName == "GoodKingMoogleMog"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_cardName(aCard, "Is", "Moogle (XIV)") == "TRUE"):
				specialCardsArray.append(aCard)
			if (searchLogic_factor_job(aCard, "Is", "Moogle") == "TRUE" and searchLogic_factor_cp(aCard, "LessThanOrEqualTo", "3") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Machina"):
		# whisper("Machina specialCondition")
		if (len(players) == 1): return "FALSE"
		myNumberOfCards = 0
		myCards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE")
		for aCard in myCards:
			myNumberOfCards = myNumberOfCards + 1
			
		theirNumberOfCards = 0
		theirCards = (card for card in table 
						if card.controller != me 
						and card.Active == "TRUE")
		for aCard in theirCards:
			theirNumberOfCards = theirNumberOfCards + 1
		
		# whisper("{} > {}".format(theirNumberOfCards, myNumberOfCards))
		if (theirNumberOfCards > myNumberOfCards):
			return "TRUE"
	elif (specialName == "Exdeath"):
		# whisper("Exdeath specialCondition")
		myNumberOfCards = 0
		myNumberOfCards += len(me.piles["Removed From Game"])
		if (len(players) > 1):
			opponent = players[1] if (players[0] == me) else players[0]
			myNumberOfCards += len(opponent.piles["Removed From Game"])
		# whisper("myNumberOfCards - {}".format(myNumberOfCards))
		if (myNumberOfCards >= 10):
			return "TRUE"
	elif (specialName == "Wakka"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_element(aCard, "Is", "Water") == "TRUE" or searchLogic_factor_category(aCard, "Is", "X") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Damage3"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_search("Player", "DamageZone", "ContainerSize,GreaterThanOrEqualTo,3", "ReturnInteger") > 0):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Damage5"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_search("Player", "DamageZone", "ContainerSize,GreaterThanOrEqualTo,5", "ReturnInteger") > 0):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "MatchBoth"):
		specialCardsCount1 = 0
		specialCardsCount2 = 0
		targetName1 = operation.split("/")[0]
		targetName2 = operation.split("/")[1]
		for aCard in foundCardsArray:
			if (searchLogic_factor_cardName(aCard, "Is", targetName1) == "TRUE"):
				specialCardsCount1 += 1
				# whisper("{} is {}, specialCardsCount1 = {}".format(aCard, targetName1, specialCardsCount1))
			if (searchLogic_factor_cardName(aCard, "Is", targetName2) == "TRUE"):
				specialCardsCount2 += 1
				# whisper("{} is {}, specialCardsCount2 = {}".format(aCard, targetName2, specialCardsCount2))
		# whisper("MatchBoth | {} {} | {} {}".format(targetName1, specialCardsCount1, targetName2, specialCardsCount2))
		if (specialCardsCount1 > 0 and specialCardsCount2 > 0):
			return "TRUE"
	elif (specialName == "Bikke"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_cardName(aCard, "Is", "Viking") == "TRUE" or searchLogic_factor_jobContainer(aCard, "Is", "Pirate") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) >= 2):
			return "TRUE"
	elif (specialName == "Astrius"):
		# whisper("Astrius 1")
		specialCardCount = 0
		specialCardCount += searchLogic_search("Player", "BreakZone", "Category,Is,FFBE", "ReturnInteger")
		# whisper("Astrius 2 - {}".format(specialCardCount))
		specialCardCount += searchLogic_search("Player", "RemoveFromGame", "Category,Is,FFBE", "ReturnInteger")
		# whisper("Astrius 3 - {}".format(specialCardCount))
		if (specialCardCount >= 7):
			return "TRUE"
	elif (specialName == "Joshua"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_element(aCard, "Is", "Fire") == "TRUE" or searchLogic_factor_category(aCard, "Is", "XVI") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Warp"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			abilityList = aCard.AbilitiesContainer.split("][")
			for anAbility in abilityList:
				anAbilityList = anAbility.split("|")
				if (anAbilityList[0] == "Warp"):
					specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "RamuhXVI"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_element(aCard, "Is", "Lightning") == "TRUE" or searchLogic_factor_category(aCard, "Is", "XVI") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
	elif (specialName == "Syldra"):
		specialCardsArray = []
		for aCard in foundCardsArray:
			if (searchLogic_factor_name(aCard, "Is", "Faris") == "TRUE" and searchLogic_factor_cp(aCard, "LessThanOrEqualTo", "6") == "TRUE"):
				specialCardsArray.append(aCard)
			elif (searchLogic_factor_type(aCard, "Is", "Forward") == "TRUE" and searchLogic_factor_cp(aCard, "LessThanOrEqualTo", "4") == "TRUE" and searchLogic_factor_element(aCard, "IsNot", "Multi-Element") == "TRUE"):
				specialCardsArray.append(aCard)
		if (len(specialCardsArray) > 0):
			return "TRUE"
    
	return "FALSE"
	
def searchLogic_search(playerString, locationName, factors, returnType, cardToPlay = "NULL"):
	mute()
	# whisper("searchLogic_search - {}, {}, {}, {}".format(playerString, locationName, factors, returnType))
	
	foundCardsArray = []
	
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "FALSE"):
		# Controller
		cardController = me
		if (playerString != "Player"):
			if (len(players) == 1): 
				if (returnType == "ReturnInteger"): return -1
				else: return []
			cardController = players[1] if (players[0] == me) else players[0]
			
		# Location
		location = table
		if (locationName == "Deck"): location = cardController.Deck
		elif (locationName == "BreakZone"): location = cardController.piles["Break Zone"]
		elif (locationName == "DamageZone"): location = cardController.piles["Damage Zone"]
		elif (locationName == "RemoveFromGame"): location = cardController.piles["Removed From Game"]
		elif (locationName == "Hand"): location = cardController.hand
		
		# Get all of the available cards in the location specified
		if (locationName == "CardToPlay"): foundCardsArray.append(cardToPlay)
		else:
			foundCardsList = (card for card in location 
								if card.controller == cardController 
								and ("Forward" in cardLogic_get_type(card) or "Backup" in cardLogic_get_type(card) or "Summon" in cardLogic_get_type(card) or "Monster" in cardLogic_get_type(card)))
			# whisper("foundCardsList - {}".format(foundCardsList))
			if (locationName == "Table"):
				activeCardsList = []
				for aCard in foundCardsList:
					if (aCard.Active == "TRUE"): activeCardsList.append(aCard)
				foundCardsList = activeCardsList
			for aCard in foundCardsList:
				foundCardsArray.append(aCard)
			# whisper("foundCardsArray - {}".format(foundCardsArray))
	else:
		heroOrVillain = ""
		heroArray = []
		villainArray = []
		
		p1 = gameLogic_query_boss_playerOne()
		p2 = gameLogic_query_boss_playerTwo()
		p3 = gameLogic_query_boss_playerThree()
		theBoss = gameLogic_query_boss_boss()
		
		if (p1 == me): heroOrVillain = "Hero"
		elif (p2 == me): heroOrVillain = "Hero"
		elif (p3 == me): heroOrVillain = "Hero"
		else: heroOrVillain = "Villain"
		
		if (p1 != None): heroArray.append(p1)
		if (p2 != None): heroArray.append(p2)
		if (p3 != None): heroArray.append(p3)
		if (theBoss != None): villainArray.append(theBoss)
		
		if (locationName == "CardToPlay"): foundCardsArray.append(cardToPlay)
		else:
			theArray = []
			if (playerString == "Player"):
				if (heroOrVillain == "Hero"):
					theArray.append(me)
				elif (heroOrVillain == "Villain"):
					theArray.append(me)
			else:
				if (heroOrVillain == "Hero"):
					theArray = villainArray
				elif (heroOrVillain == "Villain"):
					theArray = heroArray
			
			for thePlayer in theArray:
				location = table
				if (locationName == "Deck"): location = thePlayer.Deck
				elif (locationName == "BreakZone"): location = thePlayer.piles["Break Zone"]
				elif (locationName == "DamageZone"): location = thePlayer.piles["Damage Zone"]
				elif (locationName == "RemoveFromGame"): location = thePlayer.piles["Removed From Game"]
				elif (locationName == "Hand"): location = thePlayer.hand
				
				foundCardsList = (card for card in location 
									if card.controller == thePlayer 
									and ("Forward" in cardLogic_get_type(card) or "Backup" in cardLogic_get_type(card) or "Summon" in cardLogic_get_type(card) or "Monster" in cardLogic_get_type(card)))
				# whisper("foundCardsList - {}".format(foundCardsList))
				if (locationName == "Table"):
					activeCardsList = []
					for aCard in foundCardsList:
						if (aCard.Active == "TRUE"): activeCardsList.append(aCard)
					foundCardsList = activeCardsList
				for aCard in foundCardsList:
					foundCardsArray.append(aCard)
			
	factorArray = factors.split("AND")
	for aFactor in factorArray:
		# whisper("{}".format(aFactor));
		if (aFactor == "N/A"):
			# whisper("N/A")
			doNothing = "TRUE"
		else: 
			factorParts = aFactor.split(",")
			# whisper("factorParts {}".format(factorParts))
			lessCardsArray = []
			for aCard in foundCardsArray:
				if (factorParts[0] == "Name" and searchLogic_factor_cardName(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "SetNumber" and searchLogic_factor_setNumber(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "CP" and searchLogic_factor_cp(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Element" and searchLogic_factor_element(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "ElementContainer" and searchLogic_factor_elementContainer(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Type" and searchLogic_factor_type(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "TypeContainer" and searchLogic_factor_typeContainer(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Job" and searchLogic_factor_job(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "JobContainer" and searchLogic_factor_jobContainer(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "OnlyJobs" and searchLogic_factor_onlyJobs(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "OneOfEachJob" and searchLogic_factor_oneOfEachJob(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "TotalJobs" and searchLogic_factor_totalJobs(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Category" and searchLogic_factor_category(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "CategoryContainer" and searchLogic_factor_categoryContainer(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "NameOrJob" and searchLogic_factor_nameOrJob(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Power" and searchLogic_factor_power(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "TotalPower" and searchLogic_factor_totalPower(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "ContainerSize" and searchLogic_factor_containerSize(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "PlayCountSummon" and searchLogic_factor_playCountSummon(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Orientation" and searchLogic_factor_orientation(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)	
				elif (factorParts[0] == "TotalElements" and searchLogic_factor_totalElements(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "SpecialCondition" and searchLogic_factor_specialCondition(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "EXBurst" and searchLogic_factor_exBurst(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Crystals" and searchLogic_factor_crystals(foundCardsArray, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Counter" and searchLogic_factor_counter(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "CounterSize" and searchLogic_factor_counterSize(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "Keyword" and searchLogic_factor_keyword(aCard, factorParts[1], factorParts[2]) == "TRUE"): lessCardsArray.append(aCard)
				elif (factorParts[0] == "DivideThenRound"): lessCardsArray.append(aCard)
			foundCardsArray = lessCardsArray
			# whisper("len - {}".format(len(foundCardsArray)))
			
			if (factorParts[0] == "DivideThenRound"):
				sizeInt = int(factorParts[2])
				foundLength = len(foundCardsArray)
				# whisper("{} {}".format(foundLength, sizeInt))
				foundRemaining = foundLength % sizeInt
				if (foundRemaining != 0):
					foundLength = foundLength - foundRemaining
				numCards = foundLength / sizeInt
				# whisper("{} {} - {}".format(foundLength, foundRemaining, numCards))
				
				roundCardsArray = []
				for x in range(0, numCards):
					roundCardsArray.append(foundCardsArray[x])
				
				foundCardsArray = roundCardsArray
		
	if (returnType == "ReturnInteger"): return len(foundCardsArray)
	else: return foundCardsArray