def Carrot():
	worldSize = get_world_size()
	for x in range(worldSize):
		for y in range(worldSize):
			GoTo(x,y)
			HarvestIfPossible()
			Watering(100,0.5)
			TradeIfNeeded(Items.Carrot_Seed)
			Plant(Entities.Carrots)