#---------------------------------------------------------------------------
# Rules used to show menu options
#---------------------------------------------------------------------------

def showRule_debug(list, group, tablePos):
	return False
	
def nameRule_playOrCast(list, group, tablePos):
	if ("Summon" in list[0].Type):
		return "Cast"
	return "Play"
	
def nameRule_playOrCast_forFree(list, group, tablePos):
	if ("Summon" in list[0].Type):
		return "Cast (for free)"
	return "Play (for free)"
	
def nameRule_playOrCast_LimitBreak(list, group, tablePos):
	if ("Summon" in list[0].Type):
		return "Cast (Limit Break)"
	return "Play (Limit Break)"

def showRule_card_onTable(list, group, tablePos):
	return (list[0].SetNumber != "LB-DECK") and list[0].Active == "TRUE"
	
def showRule_forward_onTable(list, group, tablePos):
	return ("Forward" in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE"
	
def showRule_notAForward_onTable(list, group, tablePos):
	return ("Forward" not in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE"
	
def showRule_backup_onTable(list, group, tablePos):
	return ("Backup" in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE"
	
def showRule_backup_onTable_notDull(list, group, tablePos):
	return ("Backup" in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE" and list[0].orientation == 0
	
def showRule_summon_onTable(list, group, tablePos):
	return ("Summon" in cardLogic_get_typeContainer(list[0]))
	
def showRule_monster_onTable(list, group, tablePos):
	return ("Monster" in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE"
	
def showRule_character_onTable(list, group, tablePos):
	return ("Summon" not in cardLogic_get_typeContainer(list[0])) and list[0].Active == "TRUE"
	
def showRule_character_specialAbility_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SpecialAbility1") != "N/A"
	
def showRule_character_specialAbility_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SpecialAbility2") != "N/A"
	
def showRule_character_specialAbility_3(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SpecialAbility3") != "N/A"
	
def nameRule_character_specialAbility_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SpecialAbility1"):
			splitList = anAbilityList[1].split("_")
			return splitList[0]
	return "Error"
	
def nameRule_character_specialAbility_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SpecialAbility2"):
			splitList = anAbilityList[1].split("_")
			return splitList[0]
	return "Error"
	
def nameRule_character_specialAbility_3(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SpecialAbility3"):
			splitList = anAbilityList[1].split("_")
			return splitList[0]
	return "Error"
	
def showRule_character_searchForCard_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SearchForCard1") != "N/A"
	
def showRule_character_searchForCard_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SearchForCard2") != "N/A"
	
def showRule_character_searchForCard_3(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "SearchForCard3") != "N/A"
	
def nameRule_character_searchForCard_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard1"):
			return anAbilityList[1]
	return "Error"
	
def nameRule_character_searchForCard_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard2"):
			return anAbilityList[1]
	return "Error"
	
def nameRule_character_searchForCard_3(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "SearchForCard3"):
			return anAbilityList[1]
	return "Error"
	
def showRule_character_revealCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "RevealCards1") != "N/A"
	
def showRule_character_revealCards_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "RevealCards2") != "N/A"
	
def nameRule_character_revealCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "RevealCards1"):
			if (anAbilityList[1] == "Quantity"):
				return "Reveal the top " + anAbilityList[2] + " card(s) of your Deck"
			elif (anAbilityList[1] == "Target"):
				return "Reveal card(s) from the top of your Deck"
	return "Error"
	
def nameRule_character_revealCards_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "RevealCards2"):
			if (anAbilityList[1] == "Quantity"):
				return "Reveal the top " + anAbilityList[2] + " card(s) of your Deck"
			elif (anAbilityList[1] == "Target"):
				return "Reveal card(s) from the top of your Deck"
	return "Error"
	
def showRule_character_activateCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "ActivateCards1") != "N/A"
	
def showRule_character_activateCards_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "ActivateCards2") != "N/A"
	
def nameRule_character_activateCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "ActivateCards1"):
			return anAbilityList[1]
	return "Error"
	
def nameRule_character_activateCards_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "ActivateCards2"):
			return anAbilityList[1]
	return "Error"
	
def showRule_character_countCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "CountCards1") != "N/A"
	
def nameRule_character_countCards_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "CountCards1"):
			return anAbilityList[1]
	return "Error"
    
def showRule_character_prime_dominant(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "Prime_Dominant") != "N/A"
	
def showRule_character_prime_eikon(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "Prime_Eikon") != "N/A"
    
def nameRule_character_prime_dominant(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "Prime_Dominant"):
			return "Prime into: " + anAbilityList[1]
	return "Error"
    
def nameRule_character_prime_eikon(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	abilityList = passedCard.AbilitiesContainer.split("][")
	for anAbility in abilityList:
		anAbilityList = anAbility.split("|")
		if (anAbilityList[0] == "Prime_Eikon"):
			return "Primed from: " + anAbilityList[1]
	return "Error"
	
def showRule_character_vanish(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "Vanish") != "N/A"
	
def nameRule_character_changeElement(card, chosenElement):
	elementContainerArray = card.ElementContainer.split(" - ")
	for anElement in elementContainerArray:
		if (anElement == chosenElement):
			return "Remove " + chosenElement + " Element"
	return "Add " + chosenElement + " Element"
	
def nameRule_character_changeElement_fire(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Fire")
	
def nameRule_character_changeElement_ice(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Ice")
	
def nameRule_character_changeElement_wind(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Wind")
	
def nameRule_character_changeElement_earth(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Earth")
	
def nameRule_character_changeElement_lightning(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Lightning")
	
def nameRule_character_changeElement_water(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Water")
	
def nameRule_character_changeElement_light(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Light")
	
def nameRule_character_changeElement_dark(list, group, tablePos):
	passedCard = list[0]
	return nameRule_character_changeElement(passedCard, "Dark")
	
def showRule_character_discardAbility(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "DiscardAbility") != "N/A"
	
def showRule_notTopCardOfDeck(list, group, tablePos):
	passedCard = list[0]
	if (group != me.Deck and passedCard != me.Deck[0]): return True
	return False
	
def showRule_notTopCardOfDeck_andInactive(list, group, tablePos):
	passedCard = list[0]
	if (group != me.Deck and passedCard != me.Deck[0]):
		if (passedCard.Active == "FALSE"): 
			return True
		else:
			return False
	return False
	
def nameRule_playmat(list, group, tablePos):
	global_UsePlaymat = getGlobalVariable("global_UsePlaymat")
	if (global_UsePlaymat == "TRUE"): 
		return "Turn Off Playmat"
	else: 
		return "Turn On Playmat"
		
def nameRule_damageZone(list, group, tablePos):
	global_DamageZone = getGlobalVariable("global_UseDamageZone")
	if (global_DamageZone == "TRUE"): 
		return "Hide Damage Zone on Table"
	else: 
		return "Show Damage Zone on Table"
		
def nameRule_bossFight(list, group, tablePos):
	global_BossFight = getGlobalVariable("global_BossFight")
	if (global_BossFight == "TRUE"): 
		return "Turn Off Boss Fight"
	else: 
		return "Turn On Boss Fight"
		
def showRule_character_powerBoost_1(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	theAbility = cardLogic_ability_find(passedCard, "PowerBoost_1st")
	return (theAbility != "N/A" and "Don't Touch!" not in theAbility)
	
def showRule_character_powerBoost_2(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	theAbility = cardLogic_ability_find(passedCard, "PowerBoost_2nd")
	return (theAbility != "N/A" and "Don't Touch!" not in theAbility)
	
def showRule_character_powerBoost_3(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	theAbility = cardLogic_ability_find(passedCard, "PowerBoost_3rd")
	return (theAbility != "N/A" and "Don't Touch!" not in theAbility)
	
def nameRule_character_powerBoost_1(list, group, tablePos):
	passedCard = list[0]
	abilityArray = cardLogic_ability_find(passedCard, "PowerBoost_1st").split("|")
	return abilityArray[7] + " - " + abilityArray[2]
	
def nameRule_character_powerBoost_2(list, group, tablePos):
	passedCard = list[0]
	abilityArray = cardLogic_ability_find(passedCard, "PowerBoost_2nd").split("|")
	return abilityArray[7] + " - " + abilityArray[2]
	
def nameRule_character_powerBoost_3(list, group, tablePos):
	passedCard = list[0]
	abilityArray = cardLogic_ability_find(passedCard, "PowerBoost_3rd").split("|")
	return abilityArray[7] + " - " + abilityArray[2]
	
def showRule_usesPower_onTable(list, group, tablePos):
	passedCard = list[0]
	returnValue1 = (("Forward" in cardLogic_get_typeContainer(passedCard)) and passedCard.Active == "TRUE")
	if (returnValue1 == True): return True
	
	returnValue2 = cardLogic_ability_find(passedCard, "PowerBoost_1st")
	return (returnValue2 != "N/A")
	
def showRule_usesPower_onTable_divider(list, group, tablePos):
	passedCard = list[0]
	returnValue1 = (("Forward" in cardLogic_get_typeContainer(passedCard)) and passedCard.Active == "TRUE")
	if (returnValue1 == False): return False
	
	returnValue2 = cardLogic_ability_find(passedCard, "PowerBoost_1st")
	return (returnValue2 != "N/A")
	
def showRule_bigDivider(list, group, tablePos):
	check1 = showRule_usesPower_onTable(list, group, tablePos)
	check2 = showRule_character_specialAbility_1(list, group, tablePos)
	check3 = showRule_character_searchForCard_1(list, group, tablePos)
	check4 = showRule_character_revealCards_1(list, group, tablePos)
	check5 = showRule_character_activateCards_1(list, group, tablePos)
	check6 = showRule_character_rewarp(list, group, tablePos)
	# notify("{} {} {} {} {}".format(check1, check2, check3, check4, check5))
	return (check1 or check2 or check3 or check4 or check5 or check6)
	
def showRule_character_swapCard(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "CanSwap") != "N/A"
	
def showRule_character_warp(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "Warp") != "N/A"

def showRule_character_rewarp(list, group, tablePos):
	passedCard = list[0]
	if (passedCard.AbilitiesContainer == ""): return False
	return cardLogic_ability_find(passedCard, "Rewarp") != "N/A"
	
def showRule_character_stuckInWarp(list, group, tablePos):
	passedCard = list[0]
	thisMarker = ("Warping", "Warping ID")
	return passedCard.markers[thisMarker] > 0

def showRule_card_LBDeck(list, group, tablePos):
    passedCard = list[0]
    return passedCard.SetNumber == "LB-DECK"