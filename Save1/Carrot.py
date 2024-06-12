def Carrot(fields, fieldStatus):
	for i in range(fields):
		x, y = get_pos_x(), get_pos_y()		
		HarvestIfPossible()
		Watering(100,0.5)
		TradeIfNeeded(Items.Carrot_Seed)
		expectedYield = Plant(Entities.Carrots)
		fieldStatus[(x,y)] = (Items.Carrot, expectedYield)
		x,y = GetNextPosition()
		GoTo(x,y)
	return fieldStatus