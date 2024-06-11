def TradeIfNeeded(item, itemThreshold=10, amount=get_world_size()**2):
	#prüfe ob ich mir amount leisten kann
	if item == Items.Carrot_Seed and num_items(Items.Carrot_Seed) <= itemThreshold:
		trade(Items.Carrot_Seed, amount)
	if item == Items.Pumpkin_Seed and num_items(Items.Pumpkin_Seed) <= itemThreshold:
		trade(Items.Pumpkin_Seed, amount)
	if item == Items.Sunflower_Seed and num_items(Items.Sunflower_Seed) <= itemThreshold:
		trade(Items.Sunflower_Seed, amount)
	if item == Items.Fertilizer and num_items(Items.Fertilizer) <= itemThreshold:
		trade(Items.Fertilizer, amount)
	if item == Items.Cactus_Seed and num_items(Items.Cactus_Seed) <= itemThreshold:
		trade(Items.Cactus_Seed, amount)