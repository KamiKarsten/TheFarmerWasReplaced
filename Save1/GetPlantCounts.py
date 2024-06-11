def GetPumkinSize(amount):
		size = 1
		while Pumpkin(size) < amount:
			size += 1
		return size
		
def GetSunflowerQuantity(amount):
		sunflowersPlanted = 1
		while Sunflower(sunflowersPlanted) < amount:
			sunflowersPlanted += 1