def Farming(fieldStatus):
	resourceTargets = {
			Items.Hay: 24000,
			Items.Wood: 55000,
			Items.Carrot: 77000,
			Items.Pumpkin: 11500,
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

	for item in resourceTargets:
		plantedYield = CalculatePlantedYield(fieldStatus, item)
		missingYield = CalculateMissingYield(item)

		if missingYield + plantedYield > 0:
			entity = MapItemToEntity(item)
			fieldsNeeded = CalculateFieldsNeeded(entity, ressourceMissing)
			fieldStatus = resourceActions[item](fieldsNeeded, fieldStatus)
			return (True, fieldStatus)
	return (False, fieldStatus)

	def CalculateMissingYield(item):
		current = num_items(item)
		target = resourceTargets[item]

		if target > current:
			return 0

		return target - current

def CalculatePlantedYield(fieldStatus, item):
	plantedYield = 0
	for pos in fieldStatus:
		crop, expectedYield = fieldStatus[pos]
		if crop == item:
			plantedYield += expectedYield
	return plantedYield