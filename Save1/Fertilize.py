def Fertilize(fertilizerThreshold=10):
	#überprüfen ob ich mir Fertilizer leisten kann
	if num_items(Items.Fertilizer) < fertilizerThreshold:
		trade(Items.Fertilizer, 10)
	
	use_item(Items.Fertilizer)