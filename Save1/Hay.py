def Hay(fields, fieldStatus):
	for i in range(fields):
		x, y = get_pos_x(), get_pos_y()
		HarvestIfPossible()
		expectedYield = Plant(Entities.Grass)
		fieldStatus[(x,y)] = (Items.Hay, expectedYield)
		x, y = GetNextPosition()
		GoTo(x, y)
	return fieldStatus