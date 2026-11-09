def powerLogic_add_1000(card, x = 0, y = 0):
	mute()
	powerLogic_calculate(card, 1000)
	
def powerLogic_subtract_1000(card, x = 0, y = 0):
	mute()
	powerLogic_calculate(card, -1000)
	
def powerLogic_calculate(card, newPower):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer): return
	if (card.Active == "FALSE"): return
	
	printedPower = int(cardLogic_get_power(card))
	permanentPower = cardLogic_get_permanentPower(card)
	temporaryPower = cardLogic_get_temporaryPower(card)
	listedPower = cardLogic_get_listedPower(card)
	
	permanentPower += newPower
	listedPower = printedPower + permanentPower + temporaryPower
	
	if (newPower > 0):
		cardLogic_set_powerContainer(card, permanentPower, temporaryPower, listedPower)
		notify("{} gains {} power. ({})".format(cardLogic_get_fullNameObject(card), newPower, listedPower))
	elif (newPower < 0):
		if (listedPower <= 0): return
	
		cardLogic_set_powerContainer(card, permanentPower, temporaryPower, listedPower)
		notify("{} loses {} power. ({})".format(cardLogic_get_fullNameObject(card), (newPower * -1), listedPower))
		
	# whisper("{} {} {}".format(cardLogic_get_fullNameObject(card), temporaryPower, listedPower))
	powerLogic_updatePWR(card, temporaryPower, listedPower)
	
	
def powerLogic_updatePWR(card, temporaryPower, listedPower):
	mute()
	
	cardID = cardLogic_get_hudPowerString(card)
	existingHUD = (card for card in table 
					if card.owner == me 
					and card.AbilitiesContainer == cardID)
	for anHUD in existingHUD:
		anHUD.delete()
		
	cardPower = 0
	if (card.Power != ""): cardPower = int(card.Power)
	if (listedPower == cardPower): return
		
	templateID = ""
	if (listedPower == 1000): templateID = "d7860f6c-ad65-444f-91a0-06123ae09af4"
	elif (listedPower == 2000): templateID = "652c9ef4-fc2d-4168-86b8-15ef55d0bd6d"
	elif (listedPower == 3000): templateID = "23d165a1-a2e2-41fd-ada2-76c736038714"
	elif (listedPower == 4000): templateID = "2ad478f6-d8e1-433d-bf79-ce6733d6f47a"
	elif (listedPower == 5000): templateID = "91c43d1f-4fec-4551-bbd7-dca08ae71862"
	elif (listedPower == 6000): templateID = "2a9eaa92-0b80-40ba-a07c-d695ebdfe48b"
	elif (listedPower == 7000): templateID = "a86233c8-9dc8-4371-a1f0-1d3e315e7c1c"
	elif (listedPower == 8000): templateID = "69a8050f-35fb-4927-b4f9-b62b8ba867e8"
	elif (listedPower == 9000): templateID = "72cc80ba-7ab0-4c37-afd1-1c23bd61a373"
	elif (listedPower == 10000): templateID = "2be499d1-ef79-4bbb-b457-1fdafff08fa6"
	elif (listedPower == 11000): templateID = "21b97be6-31ab-4635-98fb-d74f526b854b"
	elif (listedPower == 12000): templateID = "1a53d1df-94bd-440a-a558-4cd1d0e5f2f6"
	elif (listedPower == 13000): templateID = "9030cf30-50cb-43af-868c-638484be1d81"
	elif (listedPower == 14000): templateID = "3120efea-d200-49ee-ac5f-b5a403c38e8e"
	elif (listedPower == 15000): templateID = "881a6c23-e168-4fe1-9167-c10ab358ae80"
	elif (listedPower == 16000): templateID = "3e28a4e2-47df-43f6-833f-f1d99d8a1721"
	elif (listedPower == 17000): templateID = "862c5336-fd10-43a2-8daa-791ee57d066c"
	elif (listedPower == 18000): templateID = "9a00a14a-1a38-4091-b966-ec731e2f646c"
	elif (listedPower == 19000): templateID = "823e0cef-a983-4aa5-be0f-4c9b6d98c1df"
	elif (listedPower == 20000): templateID = "18d99a8b-bb76-4426-b5b4-41032327a8be"
	elif (listedPower == 21000): templateID = "c929fc50-dfbc-461a-8818-1d39d1c2eaa3"
	elif (listedPower == 22000): templateID = "27d8cd65-753d-4227-84e3-b530717c7439"
	elif (listedPower == 23000): templateID = "4a35338b-9062-437f-aaef-9d6e80b30bfc"
	elif (listedPower == 24000): templateID = "1175ecd2-94fd-4662-ae25-c083d98469e4"
	elif (listedPower == 25000): templateID = "f4b40069-0eab-461f-88f1-f33fdf687c47"
	elif (listedPower == 26000): templateID = "34fe0736-dd6e-4ed8-a527-858487dd3ee0"
	elif (listedPower == 27000): templateID = "548f9e45-d5af-4381-b5f4-13a397e9b277"
	elif (listedPower == 28000): templateID = "9b2648b2-3631-49c2-8c47-c987c49e362b"
	elif (listedPower == 29000): templateID = "d95ee566-f6b5-4120-9ae4-5971332e2e85"
	else: templateID = "c3572e32-39c7-424e-9ecb-0add7f807674"
	
	# whisper("{}".format(templateID))
	
	cardX, cardY = card.position
	playerOne = True if (me._id == 1) else False
	if (playerOne == True): 
		if (card.orientation != 1):
			cardY += 120
		else:
			cardY += 120
	else: 
		if (card.orientation != 1):
			cardY += 0
		else:
			cardY += 0
	
	thisHUD = table.create(templateID, cardX, cardY)
	if (card.orientation == 1): thisHUD.orientation = 1
	thisHUD.AbilitiesContainer = cardID
	
def damageLogic_add_1000(card, x = 0, y = 0):
	mute()
	damageLogic_calculate(card, 1000)
	
def damageLogic_subtract_1000(card, x = 0, y = 0):
	mute()
	damageLogic_calculate(card, -1000)
	
def damageLogic_healAllDamage(card, x = 0, y = 0):
	mute()
	damageLogic_calculate(card, -99000)
	
def damageLogic_healAllDamage_atEndOfTurn():
	mute()
	myForwards = (card for card in table 
					if card.controller == me 
					and card.Active == "TRUE" 
					and "Forward" in cardLogic_get_typeContainer(card))
	for aForward in myForwards:
		damageLogic_healAllDamage(aForward)
		
def damageLogic_calculate(card, newDamage):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer): return
	if (card.Active == "FALSE"): return
	
	cardID = cardLogic_get_hudDamageString(card)
	currentDamage = 0
	existingHUD = (card for card in table 
					if card.owner == me 
					and card.AbilitiesContainer == cardID)
	for anHUD in existingHUD:
		currentDamage = int(anHUD.Power)
		
	oldDamage = currentDamage
	currentDamage += newDamage

	if (newDamage > 0):
		damageLogic_updateDMG(card, currentDamage)
		notify("{} takes {} damage. ({})".format(cardLogic_get_fullNameObject(card), newDamage, currentDamage))
	elif (newDamage < 0):
		damageLogic_updateDMG(card, currentDamage)
		if (currentDamage > 0):
			notify("{} heals {} damage. ({})".format(cardLogic_get_fullNameObject(card), (newDamage * -1), currentDamage))
		elif (oldDamage > 0):
			notify("{} is healed of all damage.".format(cardLogic_get_fullNameObject(card)))
		
		
def damageLogic_updateDMG(card, currentDamage):
	mute()
	
	cardID = cardLogic_get_hudDamageString(card)
	existingHUD = (card for card in table 
					if card.owner == me 
					and card.AbilitiesContainer == cardID)
	for anHUD in existingHUD:
		anHUD.delete()
		
	if (currentDamage <= 0): return
		
	templateID = ""
	if (currentDamage == 1000): templateID = "dac71e81-e38f-4675-81b8-0d19d330cd7f"
	elif (currentDamage == 2000): templateID = "0efc0b6b-8612-4b0f-a7a2-30801121e12d"
	elif (currentDamage == 3000): templateID = "847fb8e4-ce17-4611-8729-c5054595694f"
	elif (currentDamage == 4000): templateID = "c85f91ef-ccdf-4e28-9477-6eaa0bf33d3a"
	elif (currentDamage == 5000): templateID = "8f97f195-b956-43b1-99f5-3f1d829b042e"
	elif (currentDamage == 6000): templateID = "bce1ea01-3c4d-499d-9870-a9a3584ffa86"
	elif (currentDamage == 7000): templateID = "07ca5acb-1e3f-444a-9594-f1557de817c2"
	elif (currentDamage == 8000): templateID = "2b081780-87ca-4f43-8449-03ab9cd8926d"
	elif (currentDamage == 9000): templateID = "02e6c240-ddda-490a-80c0-87c85176c10f"
	elif (currentDamage == 10000): templateID = "84cf50ed-b505-4f92-9f69-6ed30e6337ec"
	elif (currentDamage == 11000): templateID = "7817a568-bb8a-4975-bd0a-84be5d0a85db"
	elif (currentDamage == 12000): templateID = "0ae4d41f-b1d6-4443-bab5-2f2db5cff8de"
	elif (currentDamage == 13000): templateID = "ab4bed3a-a803-4e01-abe4-482545aa1a73"
	elif (currentDamage == 14000): templateID = "68b7d365-bbe8-48ac-ba53-70dd1ee508df"
	elif (currentDamage == 15000): templateID = "0b9579e8-c666-4361-8518-607441564047"
	elif (currentDamage == 16000): templateID = "fb6350c8-db83-496a-bb4b-8b09953c4987"
	elif (currentDamage == 17000): templateID = "f192466b-e104-45be-a3aa-07c662ba62f2"
	elif (currentDamage == 18000): templateID = "470987aa-ae38-4953-baa3-1d1294875a83"
	elif (currentDamage == 19000): templateID = "da318c4e-4ec5-4c5b-8eef-d98712c4cf0f"
	elif (currentDamage == 20000): templateID = "6707b822-afbd-425a-ab1a-69b33abbc430"
	elif (currentDamage == 21000): templateID = "89b08cc2-998d-4d1c-b4ac-21c708bcd0ba"
	elif (currentDamage == 22000): templateID = "0b77c71d-6236-4543-9025-d46f80ba0d79"
	elif (currentDamage == 23000): templateID = "89849b2a-c1fe-402e-ab07-b97cef20598c"
	elif (currentDamage == 24000): templateID = "d5f5cb90-a1ef-4c84-8736-4e970337f920"
	elif (currentDamage == 25000): templateID = "49d84f33-0783-4b92-a17b-677287901be1"
	elif (currentDamage == 26000): templateID = "79a10777-537e-43fa-ac00-d6f8f7d27ee7"
	elif (currentDamage == 27000): templateID = "f4f10553-79b0-4d22-a750-a5ad8da21e7a"
	elif (currentDamage == 28000): templateID = "825b392d-adb9-4bf1-be9d-743794e582b9"
	elif (currentDamage == 29000): templateID = "08bbd767-894f-4541-be5b-f018460b36b5"
	else: templateID = "513ecbb9-6e29-4a98-ad1f-61ce02162a72"
	
	cardX, cardY = card.position
	playerOne = True if (me._id == 1) else False
	if (playerOne == True): 
		if (card.orientation != 1):
			cardX += 0
			cardY += 0
		else:
			cardX += 120
			cardY += 120
	else: 
		if (card.orientation != 1):
			cardX -= 0
			cardY += 120
		else:
			cardX -= 120
			cardY -= 0
	
	thisHUD = table.create(templateID, cardX, cardY)
	if (card.orientation == 1): thisHUD.orientation = 1
	thisHUD.AbilitiesContainer = cardID
	
def powerLogic_cleanupHUD(card):
	cardPowerID = cardLogic_get_hudPowerString(card)
	cardDamageID = cardLogic_get_hudDamageString(card)
	
	existingHUD = (card for card in table 
					if card.owner == me 
					and (card.AbilitiesContainer == cardPowerID or card.AbilitiesContainer == cardDamageID))
	for anHUD in existingHUD:
		anHUD.delete()
		
def powerLogic_repositionHUD(card):
	cardPowerID = cardLogic_get_hudPowerString(card)
	
	cardX, cardY = card.position
	playerOne = True if (me._id == 1) else False
	if (playerOne == True): 
		if (card.orientation != 1):
			cardY += 120
		else:
			cardY += 120
	else: 
		if (card.orientation != 1):
			cardY += 0
		else:
			cardY += 0
	
	existingHUD = (card for card in table 
					if card.owner == me 
					and card.AbilitiesContainer == cardPowerID)
	for anHUD in existingHUD:
		anHUD.moveToTable(cardX, cardY)
		
	cardDamageID = cardLogic_get_hudDamageString(card)
	
	cardX, cardY = card.position
	playerOne = True if (me._id == 1) else False
	if (playerOne == True): 
		if (card.orientation != 1):
			cardX += 0
			cardY += 0
		else:
			cardX += 120
			cardY += 120
	else: 
		if (card.orientation != 1):
			cardX -= 0
			cardY += 120
		else:
			cardX -= 120
			cardY -= 0
	
	existingHUD = (card for card in table 
					if card.owner == me 
					and card.AbilitiesContainer == cardDamageID)
	for anHUD in existingHUD:
		anHUD.moveToTable(cardX, cardY)
		
def powerLogic_fixTable(args):
	mute()
	index = 0
	for aCard in args.cards:
		if (args.fromGroups[index] == table and args.toGroups[index] == table):
			powerLogic_repositionHUD(aCard)
		if (args.fromGroups[index] == table and args.toGroups[index] != table):
			powerLogic_cleanupHUD(aCard)
			aCard.resetProperties()
			powerLogic_powerBoost_calculate(table)
			
def powerLogic_double(card, x = 0, y = 0):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer): return
	if (card.Active == "FALSE"): return
	
	printedPower = int(cardLogic_get_power(card))
	permanentPower = cardLogic_get_permanentPower(card)
	temporaryPower = cardLogic_get_temporaryPower(card)
	listedPower = cardLogic_get_listedPower(card)
	if (listedPower == 0): listedPower = printedPower
	
	newPermanentPower = permanentPower + listedPower
	newListedPower = listedPower + listedPower
	
	cardLogic_set_powerContainer(card, newPermanentPower, temporaryPower, newListedPower)
	notify("{} has its power doubled. ({})".format(cardLogic_get_fullNameObject(card), newListedPower))
		
	powerLogic_updatePWR(card, temporaryPower, newListedPower)
	
def powerLogic_halve(card, x = 0, y = 0):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer): return
	if (card.Active == "FALSE"): return
	
	printedPower = int(cardLogic_get_power(card))
	permanentPower = cardLogic_get_permanentPower(card)
	temporaryPower = cardLogic_get_temporaryPower(card)
	listedPower = cardLogic_get_listedPower(card)
	if (listedPower == 0): listedPower = printedPower
	if (listedPower == 1000): return
	
	halvedPower = listedPower / 2
	if ((halvedPower % 1000) != 0):
		halvedPower -= 500
		
	newPermanentPower = permanentPower - halvedPower
	newListedPower = listedPower - halvedPower
	
	cardLogic_set_powerContainer(card, newPermanentPower, temporaryPower, newListedPower)
	notify("{} has its power halved. ({})".format(cardLogic_get_fullNameObject(card), newListedPower))
		
	powerLogic_updatePWR(card, temporaryPower, newListedPower)
	
def powerLogic_reset(card, x = 0, y = 0):
	mute()
	cardTypeContainer = cardLogic_get_typeContainer(card)
	if ("Forward" not in cardTypeContainer): return
	
	printedPower = int(cardLogic_get_power(card))
	permanentPower = 0
	temporaryPower = 0
	listedPower = cardLogic_get_listedPower(card)
	if (listedPower == 0): listedPower = printedPower
	
	newPermanentPower = permanentPower + listedPower
	
	cardLogic_set_powerContainer(card, 0, 0, 0)
		
	powerLogic_updatePWR(card, printedPower, printedPower)
	
def powerLogic_powerBoost_1(card, x = 0, y = 0):
	mute()
	
	boostLogic = cardLogic_ability_find(card, "PowerBoost_1st")
	if (boostLogic == ""): return
	
	powerLogic_powerBoost_update(card, boostLogic)
	
	
def powerLogic_powerBoost_2(card, x = 0, y = 0):
	mute()
	
	boostLogic = cardLogic_ability_find(card, "PowerBoost_2nd")
	if (boostLogic == ""): return
	
	powerLogic_powerBoost_update(card, boostLogic)
	
def powerLogic_powerBoost_3(card, x = 0, y = 0):
	mute()
	
	boostLogic = cardLogic_ability_find(card, "PowerBoost_3rd")
	if (boostLogic == ""): return
	
	powerLogic_powerBoost_update(card, boostLogic)
	
def powerLogic_powerBoost_update(card, boostLogic):
	mute()
	
	boostLogicArray = boostLogic.split("|")
	switchVar = boostLogicArray[2]
	
	newSwitchVar = ""
	if (switchVar == "ON"): newSwitchVar = "OFF"
	if (switchVar == "OFF"): newSwitchVar = "ON"
	if (switchVar == "ACTIVE"): newSwitchVar = "DISABLED"
	if (switchVar == "DISABLED"): newSwitchVar = "ACTIVE"
	
	boostLogicArray[2] = newSwitchVar
	newBoostLogic = "|".join(boostLogicArray)
	
	newAbilities = card.AbilitiesContainer.replace(boostLogic, newBoostLogic)
	card.AbilitiesContainer = newAbilities
	
	if (newSwitchVar == "ON" or newSwitchVar == "OFF"):
		powerLogic_powerBoost_applyManualBoost(card, newBoostLogic, newSwitchVar)
	
	powerLogic_powerBoost_calculate(table)
	
def powerLogic_powerBoost_calculate(group, x = 0, y = 0, doNotCallAgain = "FALSE"):
	mute()
	
	forwardCount = 0
	myForwards = (card for card in table 
					if card.owner == me 
					and card.Active == "TRUE" 
					and "Forward" in card.TypeContainer)
	for aForward in myForwards:
		forwardCount += 1
		
		permanentPower = cardLogic_get_permanentPower(aForward)
		listedPower = cardLogic_get_listedPower(aForward)
		if (listedPower == 0): listedPower = int(cardLogic_get_power(aForward))
		cardLogic_set_powerContainer(aForward, permanentPower, 0, listedPower)
	# whisper("forwardCount - {}".format(forwardCount))
	
	if (forwardCount != 0):
		boostCards = (card for card in table 
						if card.owner == me 
						and card.Active == "TRUE" 
						and "PowerBoost" in card.AbilitiesContainer)
		for aBoostCard in boostCards:
			boost1 = cardLogic_ability_find(aBoostCard, "PowerBoost_1st")
			boost2 = cardLogic_ability_find(aBoostCard, "PowerBoost_2nd")
			boost3 = cardLogic_ability_find(aBoostCard, "PowerBoost_3rd")
			
			if (boost1 != "N/A"): powerLogic_powerBoost_applyBoost(aBoostCard, boost1)
			if (boost2 != "N/A"): powerLogic_powerBoost_applyBoost(aBoostCard, boost2)
			if (boost3 != "N/A"): powerLogic_powerBoost_applyBoost(aBoostCard, boost3)
		
		myForwards2 = (card for card in table 
						if card.owner == me 
						and card.Active == "TRUE" 
						and "Forward" in card.TypeContainer)
		for aForward in myForwards2:
			printedPower = int(cardLogic_get_power(aForward))
			permanentPower = cardLogic_get_permanentPower(aForward)
			temporaryPower = cardLogic_get_temporaryPower(aForward)
			listedPower = cardLogic_get_listedPower(aForward)
			
			totalPower = printedPower + permanentPower + temporaryPower
			# whisper("{} - {} | {} | {} | {} - Current: {}".format(cardLogic_get_fullNameObject(aForward), printedPower, permanentPower, temporaryPower, totalPower, listedPower))
			
			if (totalPower != listedPower):
				difference = totalPower - listedPower
				if (difference > 0):
					notify("{} gains {} power. ({})".format(cardLogic_get_fullNameObject(aForward), difference, totalPower))
				else:
					notify("{} loses {} power. ({})".format(cardLogic_get_fullNameObject(aForward), (difference * -1), totalPower))
				powerLogic_updatePWR(aForward, 0, totalPower)
				cardLogic_set_powerContainer(aForward, permanentPower, temporaryPower, totalPower)
	
	# whisper("Checking opponents")
	if (doNotCallAgain == "FALSE"):
		theirForwardsCount = []
		theirForwards = (card for card in table 
							if card.owner != me 
							and card.Active == "TRUE" 
							and "Forward" in card.TypeContainer 
							and "PowerBoost" in card.AbilitiesContainer 
							and "Opponent" in card.AbilitiesContainer)
		for aForward in theirForwards:
			theirForwardsCount.append(aForward)
		# whisper("Their forwards: {}".format(len(theirForwardsCount)))
		if (len(theirForwardsCount) > 0):
			for p in players:
				if (p != me):
					remoteCall(p, "powerLogic_powerBoost_calculate", [group, 0, 0, "TRUE"])
		
def powerLogic_powerBoost_applyBoost(card, boostLogic):
	mute()
	# whisper("{}".format(boostLogic))
	
	boostLogicArray = boostLogic.split("|")
	statusVar = boostLogicArray[1]
	switchVar = boostLogicArray[2]
	searchLogic = boostLogicArray[3]
	targetLogic = boostLogicArray[4]
	powerBoost = int(boostLogicArray[5])
	powerMultiplier = boostLogicArray[6]
	powerMultiplierArray = powerMultiplier.split("_")
	
	if (statusVar == "Auto" and switchVar == "DISABLED"): return
	if (statusVar == "Manual"): return
	
	searchCount = 0
	if (searchLogic != "N/A"):
		searchLogicArray = searchLogic.split("_")
		searchResults = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
		for aCard in searchResults:
			searchCount += 1
		# Opponent zero-cards-in-hand exception
		# whisper("Zero check")
		if (searchLogicArray[0] == "Opponent" and searchLogicArray[1] == "Hand" and "ContainerSize,LessThanOrEqualTo" in searchLogicArray[2] and len(players) > 1 and len(gameLogic_query_otherPlayer().hand) == 0):
			searchCount += 1
		if (searchLogicArray[0] == "Player" and searchLogicArray[1] == "Hand" and "ContainerSize,LessThanOrEqualTo" in searchLogicArray[2] and len(me.hand) == 0):
			searchCount += 1
		# whisper("searchCount {}".format(searchCount))
		if (searchCount == 0): return
		
	targetArray = []
	targetCount = 0
	if (targetLogic == "ThisCard"):
		targetArray.append(card)
		targetCount = 1
	else:
		targetLogicArray = targetLogic.split("_")
		targetArray = searchLogic_search(targetLogicArray[0], targetLogicArray[1], targetLogicArray[2], "ReturnArray")
		for aCard in targetArray:
			targetCount += 1
		# whisper("targetCount - {}".format(targetCount))
		if (targetCount == 0): return
		
	if (powerMultiplierArray[0] == "Size"):
		powerBoost = powerBoost * searchCount
	elif (powerMultiplierArray[0] == "Counter"):
		# whisper("{} - {}".format(powerMultiplierArray[0], powerMultiplierArray[1]))
		thisMarker = (powerMultiplierArray[1], powerMultiplierArray[1] + " ID")
		
		counterTotal = 0
		for aCard in targetArray:
			counterTotal = counterTotal + aCard.markers[thisMarker]
		powerBoost = powerBoost * counterTotal
		
	for aCard in targetArray:
		permanentPower = cardLogic_get_permanentPower(aCard)
		temporaryPower = cardLogic_get_temporaryPower(aCard)
		listedPower = cardLogic_get_listedPower(aCard)
		
		temporaryPower += powerBoost
	
		cardLogic_set_powerContainer(aCard, permanentPower, temporaryPower, listedPower)

def powerLogic_powerBoost_applyManualBoost(card, boostLogic, onOrOff):
	mute()
	
	boostLogicArray = boostLogic.split("|")
	statusVar = boostLogicArray[1]
	switchVar = boostLogicArray[2]
	searchLogic = boostLogicArray[3]
	targetLogic = boostLogicArray[4]
	powerBoost = int(boostLogicArray[5])
	powerMultiplier = boostLogicArray[6]
	powerMultiplierArray = powerMultiplier.split("_")
	
	searchCount = 0
	if (searchLogic != "N/A"):
		searchLogicArray = searchLogic.split("_")
		searchResults = searchLogic_search(searchLogicArray[0], searchLogicArray[1], searchLogicArray[2], "ReturnArray")
		for aCard in searchResults:
			searchCount += 1
		if (searchCount == 0): return
		
	targetArray = []
	targetCount = 0
	if (targetLogic == "ThisCard"):
		targetArray.append(card)
		targetCount = 1
	else:
		targetLogicArray = targetLogic.split("_")
		targetArray = searchLogic_search(targetLogicArray[0], targetLogicArray[1], targetLogicArray[2], "ReturnArray")
		for aCard in targetArray:
			targetCount += 1
		# whisper("targetCount - {}".format(targetCount))
		if (targetCount == 0): return
		
	if (powerMultiplierArray[0] == "Size"):
		powerBoost = powerBoost * searchCount
	elif (powerMultiplierArray[0] == "Counter"):
		counterTotal = 0
		for aCard in targetArray:
			counterTotal = counterTotal + aCard.markers[powerMultiplierArray[1]]
		powerBoost = powerBoost * counterTotal
		
	for aCard in targetArray:
		permanentPower = cardLogic_get_permanentPower(aCard)
		temporaryPower = cardLogic_get_temporaryPower(aCard)
		listedPower = cardLogic_get_listedPower(aCard)
		
		if (onOrOff == "ON"):
			permanentPower += powerBoost
		else:
			permanentPower -= powerBoost
	
		cardLogic_set_powerContainer(aCard, permanentPower, temporaryPower, listedPower)