def CalculateYield(entity, amounts=1):
	def CalculateHayYield(amount):
		return amount * num_unlocked(Unlocks.Grass) + amount
	
	def CalculateBushYield(amount):
		return amount * num_unlocked(Unlocks.Trees)
	
	def CalculateTreeYield(amount):
		return (amount * 5) * num_unlocked(Unlocks.Trees)
		
	def CalculateCarrotYield(amount):
		return (amount * 3) * num_unlocked(Unlocks.Carrots)
			
	def CalculatePumpkinYield(fieldSize):
		return fieldSize**3 * num_unlocked(Unlocks.Pumpkins)
		
	def CalculateSunflowerYield(sunflowersPlanted):
		return ((sunflowersPlanted * num_unlocked(Unlocks.Sunflowers)) ** 0.5) * sunflowersPlanted
		
	def CalculateCactusYield(amount):
		return get_world_size() * amount * num_unlocked(Unlocks.Cactus)
		
	def CalculateTreasureYield(tmp):
		return get_world_size()**2 * num_unlocked(Unlocks.Mazes)
	
	entityCalculationMap = {
		Entities.Grass: CalculateHayYield,
		Entities.Bush: CalculateBushYield,
		Entities.Tree: CalculateTreeYield,
		Entities.Carrots: CalculateCarrotYield,
		Entities.Pumpkin: CalculatePumpkinYield,
		Entities.Sunflower: CalculateSunflowerYield,
		Entities.Cactus: CalculateCactusYield,
		Entities.Treasure: CalculateTreasureYield
	}
	
	if entity in entityCalculationMap:
		return entityCalculationMap[entity](amounts)
	else:
		print("Error")
		do_a_flip()
