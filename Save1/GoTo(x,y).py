def GoTo(x = 0, y = 0, size = get_world_size()):
	halfSize = size // 2
	deltaX = (x - get_pos_x()) % size
	deltaY = (y - get_pos_y()) % size
	
	if halfSize > deltaX:
		for i in range(deltaX):
			move(East)
	else:
		for i in range(size - deltaX):
			move(West)
	if halfSize > deltaY:
		for i in range(deltaY):
			move(North)
	else:
		for i in range(size - deltaY):
			move(South)