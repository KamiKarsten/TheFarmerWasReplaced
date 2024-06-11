def MoveToPosition(x, y):
	currentPositionX = get_pos_x()
	currentPositionY = get_pos_y()
	arrived = False
	
	while(not arrived):
		if currentPositionX > x:
			move(West)
		elif currentPositionX < x:
			move(East)
		
		if currentPositionY > y:
			move(South)
		elif currentPositionY < y:
			move(North)
		
		currentPositionX = get_pos_x()
		currentPositionY = get_pos_y()
		arrived = currentPositionX == x and currentPositionY == y