def PlantBush():
	if(get_ground_type() == Grounds.Soil):
		till()
	
	plant(Entities.Bush)