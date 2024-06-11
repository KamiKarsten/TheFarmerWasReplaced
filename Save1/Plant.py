#Planting function. Takes entities as parameter
def Plant(entity):
	if entity == None:
		return
	if get_entity_type() == entity and not get_entity_type() == Entities.Sunflower:
		return
	
	if entity == Entities.Grass:
		if get_ground_type() == Grounds.Soil:
			till()
	
	elif entity == Entities.Tree:
		x = get_pos_x()
		y = get_pos_y()
		#Das nochmal überdenken ob das hier rein sollte
		if(x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
			plant(Entities.Tree)
			return	
		
		plant(Entities.Bush)
		return
		
	elif entity == Entities.Carrots:
		if get_ground_type() == Grounds.Turf:
			till()
		
	elif entity == Entities.Pumpkin:
		if(get_ground_type() == Grounds.Turf):
			till()

	elif entity == Entities.Sunflower:
		if get_ground_type() == Grounds.Turf:
			till()
		
		if get_entity_type() == Entities.Sunflower:
			return measure()
		
		if plant(Entities.Sunflower):
			return measure()
		
		return
		
	elif entity == Entities.Cactus:
		if get_ground_type() == Grounds.Turf:
			till()
		if plant(Entities.Cactus):
			return measure()
	
	elif entity == Entities.Hedge:
		while get_entity_type() != Entities.Hedge:
			if get_entity_type() != Entities.Bush:
				if can_harvest():
					harvest()
				plant(Entities.Bush)
			Fertilize()
		return
		
	plant(entity) 