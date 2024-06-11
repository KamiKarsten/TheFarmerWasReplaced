def Sunflower():
	worldSize = get_world_size()
	measurements = set()
	sunflowerDictionary = {}
		
	def Planting(amount):
		flowersPlanted = 0
		for x in range(worldSize):
			for y in range(worldSize):
				GoTo(x,y)
				
				if flowersPlanted >= amount:
					return flowersPlanted
				
				TradeIfNeeded(Items.Sunflower_Seed)
				Watering(100,0.8)
				pedal = Plant(Entities.Sunflower)
				
				if pedal:
					flowersPlanted += 1
					sunflowerDictionary[(x, y)] = pedal
					measurements.add(pedal)
		return flowersPlanted
 
	def Harvest():
		while measurements:
			maxPedal = max(measurements)
			to_remove = []
			for position in sunflowerDictionary:
				x, y = position
				pedal = sunflowerDictionary[position]
				
				if pedal == maxPedal:
					GoTo(x, y)
					if (get_entity_type() == Entities.Sunflower 
						and can_harvest() 
						and measure() == maxPedal
						):
						harvest()
						to_remove.append((x, y))
			
			for pos in to_remove:
				sunflowerDictionary.pop(pos)
						
			if not HasOtherWithSamePedal(maxPedal):
				measurements.remove(maxPedal)
				
	def HasOtherWithSamePedal(maxPedal):
		for key in sunflowerDictionary:
			if sunflowerDictionary[key] == maxPedal:
				return True
		return False
	
	planted = Planting(100)
	if planted > 0:
		Harvest()
	
Sunflower()