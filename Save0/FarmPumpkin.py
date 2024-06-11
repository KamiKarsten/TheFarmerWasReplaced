def FarmPumpkin():
	rows = get_world_size()
	cols = get_world_size()
    sum = 0
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                MoveToPosition(row, col)
                PlantPumpkin()
                if(get_entity_type() == Entities.Pumpkin and can_harvest()):
					sum = sum + 1
        else:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                PlantPumpkin()
                if(get_entity_type() == Entities.Pumpkin and can_harvest()):
					sum = sum + 1
		if(sum == rows*cols):
			harvest()
	sum = 0 		
    for row in range(rows-1, -1, -1):
        if row % 2 == 0:
            for col in range(cols-1, -1, -1):
                MoveToPosition(row, col)
                PlantPumpkin()
                if(get_entity_type() == Entities.Pumpkin and can_harvest()):
					sum = sum + 1
        else:
            for col in range(cols):
				MoveToPosition(row, col)
                PlantPumpkin()
                if(get_entity_type() == Entities.Pumpkin and can_harvest()):
					sum = sum + 1
		if(sum == rows*cols):
			harvest()