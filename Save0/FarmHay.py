def FarmHay():
    rows = get_world_size()
	cols = get_world_size()
    
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                MoveToPosition(row, col)
                if(get_entity_type() != Entities.Grass):
					PlantItem(Items.Hay)
				HarvestIfPossible()
        else:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                if(get_entity_type() != Entities.Grass):
					PlantItem(Items.Hay)
				HarvestIfPossible()
                		
    for row in range(rows-1, -1, -1):
        if row % 2 == 0:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                if(get_entity_type() != Entities.Grass):
					PlantItem(Items.Hay)
				HarvestIfPossible()
        else:
            for col in range(cols):
				MoveToPosition(row, col)
				if(get_entity_type() != Entities.Grass):
					PlantItem(Items.Hay)
				HarvestIfPossible()
