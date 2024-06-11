def PlantItem(item):
	if item == Items.Hay:
		PlantGrass()
	elif item == Items.Carrot:
		PlantCarrots()
	elif item == Items.Wood:
		PlantBush()
	elif item == Items.Pumpkin:
		PlantPumpkin()
