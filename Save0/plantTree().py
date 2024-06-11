def PlantTree():
	x, y = GetPosition()
	
	if((x + y) % 2 == 0) and get_entity_type() != Entities.Tree:
		plant(Entities.Tree)