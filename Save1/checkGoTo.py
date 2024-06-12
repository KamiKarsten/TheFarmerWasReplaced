ws = get_world_size()
for i in range(100):
	x = (random() * ws)
	y = (random() * ws)

	x = x - (x % 1)
	y = y - (y % 1)

	GoTo(x,y)
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	quick_print("goto(",x,",",y,") moved drone to (",pos_x,",",pos_y,")", x == pos_x and y == pos_y)