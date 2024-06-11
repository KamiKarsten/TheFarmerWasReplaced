def FarmWood():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			MoveToPosition(x, y)
			HarvestIfPossible()
			PlantTree()

	