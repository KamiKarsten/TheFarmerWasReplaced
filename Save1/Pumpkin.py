# wenn size > 7 dann gibts probleme
# hört nicht auf wenn sie keien Seeds mehr hat/ kaufen kann
def Pumpkin(size, fieldStatus, pumpkinMap=None):
	if pumpkinMap == None:
        pumpkinMap = set()
        
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
			fieldStatus[(x,y)] = None
	
	def HarvestIfPossible():
		if len(pumpkinMap) == size * size:
			harvest()
		else:
			Pumpkin(size, fieldStatus, pumpkinMap)		

	for x in range(size):
		for y in range(size):
			ProcessTile(x, y)
    
	HarvestIfPossible()
	return fieldStatus