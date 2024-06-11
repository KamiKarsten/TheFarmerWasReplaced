def PlantCarrots():
	if(get_ground_type() == Grounds.Turf):
		till()
	
	if(get_entity_type() == Entities.Carrots):
		return
	
	if(num_items(Items.Carrot_Seed) != 0):
		plant(Entities.Carrots)
		return
	
	if not IsTradeable(Items.Carrot_Seed):
		return
		
	trade(Items.Carrot_Seed)
	plant(Entities.Carrots)