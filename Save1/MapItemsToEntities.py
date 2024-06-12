def MapItemToEntity(item):
	itemEntityMap = {
		Items.Hay: Entities.Grass,
	    Items.Wood: Entities.Bush,
	    Items.Carrot: Entities.Carrots,
	    Items.Pumpkin: Entities.Pumpkin,
	    Items.Power: Entities.Sunflower,
	    Items.Gold: Entities.Treasure,
	    Items.Cactus: Entities.Cactus
	}

	if num_unlocked(Unlocks.Trees) > 0:
		itemEntityMap[Items.Wood] = Entities.Tree

	if item in itemEntityMap:
		return itemEntityMap[item]

	return None