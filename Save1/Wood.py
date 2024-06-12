def Wood(fields, fieldStatus):
	for i in range(fields):
		x, y = get_pos_x(), get_pos_y()		
		HarvestIfPossible()
		expectedYield = Plant(Entities.Tree)
		fieldStatus[(x,y)] = (Items.Wood, expectedYield)
		x,y = GetNextPosition()
		GoTo(x,y)
	return fieldStatus