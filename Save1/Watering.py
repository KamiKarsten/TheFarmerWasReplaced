def Watering(waterTankCap, waterLevelCap):
	if num_items(Items.Water_Tank) < waterTankCap:
		trade(Items.Empty_Tank)

	if get_water() < waterLevelCap:
		use_item(Items.Water_Tank)