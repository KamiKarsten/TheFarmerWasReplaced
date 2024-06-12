clear()
fieldStatus = {}
running = True
while running:
	running, fieldStatus = Farming(fieldStatus)
	pass
	
for x in range(get_world_size()):
	for y in range(get_world_size()):
		GoTo(x, y)
		while not can_harvest():
			pass
		harvest()