def GetNextPosition(x, y):
	worldSize = get_world_size()
	
	y += 1
	if y >= worldSize:
		y = 0
		x += 1
		if x >= worldSize:
			x = 0
	return x, y