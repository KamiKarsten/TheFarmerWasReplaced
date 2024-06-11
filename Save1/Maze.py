def Maze():
	oposite = {
		North: South,
		South: North,
		East: West,
		West: East
	}
		
	directions = {
       	North: (0, 1),
		East: (1, 0),
        West: (-1, 0),
       	South: (0, -1)
    }

	def Solve(x, y, visited):
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True
		
		visited.add((x, y))
		
		for direction in directions:
			dx, dy = directions[direction]
			nextX, nextY = x + dx, y + dy
	
			if (nextX, nextY) not in visited:
				old_x, old_y = x, y
				new_x, new_y = MoveAndCheck(direction, x, y)
				
				if (new_x, new_y) != (x, y):  # Bewegung war erfolgreich
					if(Solve(new_x, new_y, visited)):
						return True
					move(oposite[direction])
		
		visited.remove((x,y))
		return False
	
	def MoveAndCheck(direction, x, y):
		if move(direction):
			return get_pos_x(), get_pos_y()
		return x, y

	startX, startY = get_pos_x(), get_pos_y()
	visited = set()
	Plant(Entities.Hedge)
	Solve(startX, startY, visited)
Maze()