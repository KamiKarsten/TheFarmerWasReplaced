def CalculateFieldsNeeded(item, amountNeeded):
	fields = 0
	entity = MapItemToEntity(item)

	if entity == Entities.Tree:
		totalYield = 0
		while totalYield < amountNeeded:
			fields += 1
			if fields % 2 == 0:
				totalYield += CalculateCropYield(Entities.Tree)
			else:
				totalYield += CalculateCropYield(Entities.Bush)
		return fields

	while CalculateCropYield(entity, fields) < amountNeeded:
		fields += 1

	return fields