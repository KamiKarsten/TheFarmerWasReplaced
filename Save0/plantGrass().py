def PlantGrass():
	if(get_ground_type() == Grounds.Soil):
		till()
	
	if(get_entity_type() == Entities.Grass):
		return
		
	plant(Entities.Grass)