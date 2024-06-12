def CalculateCropYield(entity, amounts=1):
	if entity == Entities.Grass:
		return amount * num_unlocked(Unlocks.Grass) + amount

	elif entity == Entities.Bush:
		return amount * num_unlocked(Unlocks.Trees)

	elif entity == Entities.Tree:
		return (amount * 5) * num_unlocked(Unlocks.Trees)

	elif entity == Entities.Carrots:
		return (amount * 3) * num_unlocked(Unlocks.Carrots)

	elif entity == Entities.Pumpkin:
		return fieldSize**3 * num_unlocked(Unlocks.Pumpkins)

	elif entity == Entities.Sunflower:
		return ((sunflowersPlanted * num_unlocked(Unlocks.Sunflowers)) ** 0.5) * sunflowersPlanted

	elif entity == Entities.Cactus:
		return get_world_size() * amount * num_unlocked(Unlocks.Cactus)

	elif entity == Entities.Treasure:
		return get_world_size()**2 * num_unlocked(Unlocks.Mazes)