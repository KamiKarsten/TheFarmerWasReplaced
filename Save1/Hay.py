def Hay():
	worldSize = get_world_size()
	#ab aktuelle postion 
	#solang anzahl berechneter felder für amount
	#amout muss freischaltung berücksichtigen
	for x in range(worldSize):
		for y in range(worldSize):
			GoTo(y,x)
			HarvestIfPossible()
			Plant(Entities.Grass)