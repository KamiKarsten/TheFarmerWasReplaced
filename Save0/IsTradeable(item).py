def IsTradeable(item):
	if item == Items.Carrot_Seed:
		currentHay = num_items(Items.Hay)
		currentWood = num_items(Items.Wood)
		
		return currentHay >= 2 and currentWood >= 2
		
	elif item == Items.Empty_Tank:
		currentWood = num_items(Items.Wood)
		
		return currentWood >= 5
	elif item == Items.Pumpkin_Seed:
		currentCarrot = num_items(Items.Carrot)
		
		return currentCarrot >= 1