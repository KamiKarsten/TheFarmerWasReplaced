# hört nicht auf wenn sie keien Seeds mehr hat/ kaufen kann
def Pumpkin(pumpkinMap=None):
	if pumpkinMap == None:
        pumpkinMap = set()
        
	worldSize = get_world_size()
	
	def ProcessTile(x, y):
		if (x, y) in pumpkinMap:
            return		

		GoTo(x, y)
		if get_entity_type() == Entities.Pumpkin:
			if can_harvest():
				pumpkinMap.add((x, y))
		else:
			harvest()
			TradeIfNeeded(Items.Pumpkin_Seed)
			Watering(100,0.8)			
			Plant(Entities.Pumpkin)
	
	def HarvestIfPossible():
		if len(pumpkinMap) == worldSize * worldSize:
			harvest()
		else:
			Pumpkin(pumpkinMap)		

	for x in range(worldSize):
		for y in range(worldSize):
			ProcessTile(x, y)
    
	HarvestIfPossible()