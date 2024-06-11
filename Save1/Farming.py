def Farming():
	resourceTargets = {
        Items.Hay: 2000,
        Items.Wood: 30000,
        Items.Carrot: 100000,
        Items.Pumpkin: 10000,
        Items.Power: 30000,
        Items.Gold: 20000,
        Items.Cactus: 20000
	}
    resourceActions = {
    	Items.Hay: Hay,
        Items.Wood: Wood,
        Items.Carrot: Carrot,
        Items.Pumpkin: Pumpkin,
        Items.Power: Sunflower,
        Items.Gold: Maze,
        Items.Cactus: Cactus
    }

	for key in resourceTargets:
		if num_items(key) < resourceTargets[key]:
			resourceActions[key]()
			return True
			
	return False