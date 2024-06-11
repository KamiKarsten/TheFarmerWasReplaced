def Cactus():
	worldSize = get_world_size()
	cactiDictionary = {}
	
	def Planting():
		for x in range(worldSize):
			for y in range(worldSize):
				GoTo(x, y)
				TradeIfNeeded(Items.Cactus_Seed, 0)
				measure = Plant(Entities.Cactus)
				
				if measure:
					cactiDictionary[(x,y)] = measure       
				# hier kann direkt auch sortiert werden

	def Sort():
		unsortedPositions = {}
		for x in range(worldSize):
			for y in range(worldSize):
				unsortedPositions[(x,y)] = True

		while unsortedPositions:
			newUnsortedPositions = set()
			for pos in unsortedPositions:
				x, y = pos
				GoTo(x, y)
				currentHeight = measure()

				if y + 1 < worldSize and currentHeight > measure(North):
					swap(North)
					newUnsortedPositions.add((x, y + 1))
					newUnsortedPositions.add((x, y))

				if x + 1 < worldSize and currentHeight > measure(East):
					swap(East)
					newUnsortedPositions.add((x + 1, y))
					newUnsortedPositions.add((x, y))

				if y - 1 >= 0 and currentHeight < measure(South):
					swap(South)
					newUnsortedPositions.add((x, y - 1))
					newUnsortedPositions.add((x, y))

				if x - 1 >= 0 and currentHeight < measure(West):
					swap(West)
					newUnsortedPositions.add((x - 1, y))
					newUnsortedPositions.add((x, y))

			unsortedPositions = newUnsortedPositions
	Planting()
	Sort()
	harvest()