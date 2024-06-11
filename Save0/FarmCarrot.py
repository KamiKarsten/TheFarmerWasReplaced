def FarmCarrots():
	rows = get_world_size()
	cols = get_world_size()
    
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                MoveToPosition(row, col)
                HarvestIfPossible()
                PlantItem(Items.Carrot)
        else:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                HarvestIfPossible()
                PlantItem(Items.Carrot)
                		
    for row in range(rows-1, -1, -1):
        if row % 2 == 0:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                HarvestIfPossible()
                PlantItem(Items.Carrot)
        else:
            for col in range(cols):
				MoveToPosition(row, col)
                HarvestIfPossible()
                PlantItem(Items.Carrot)