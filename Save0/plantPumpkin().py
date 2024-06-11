def PlantPumpkin():
	if(get_ground_type() == Grounds.Turf):
		till()
	if get_entity_type() == Entities.Pumpkin:
		return
	
	if(not num_items(Items.Pumpkin_Seed) == 0):
		plant(Entities.Pumpkin)
		return
		
	if(not IsTradeable(Items.Pumpkin_Seed)):
		return
	
	trade(Items.Pumpkin_Seed)		
	plant(Entities.Pumpkin)				