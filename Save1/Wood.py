def Wood():
	worldSize = get_world_size()
	for x in range(worldSize):
		for y in range(worldSize):
			GoTo(x,y)
			HarvestIfPossible()
			Plant(Entities.Tree)