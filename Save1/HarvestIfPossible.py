def HarvestIfPossible():
	entityType = get_entity_type() 
	
	if(entityType == None):
		return
	if not can_harvest():
		return
	else:
		harvest()