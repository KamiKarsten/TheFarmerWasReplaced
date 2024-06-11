#optimierungsbedard mit range und wesentlich kürzer
def GoTo(x, y):
    currentX, currentY = get_pos_x(), get_pos_y()
    gridSize = get_world_size()
	x = x - (x % 1)
    y = y - (y % 1)
	
	if x < 0 or x >= gridSize or y < 0 or y >= gridSize:
        quick_print("Unknown coordinates. Movement cancelt.")
        do_a_flip()
        return
	    
    deltaX = (x - currentX) % gridSize
    if deltaX > gridSize / 2:
        deltaX -= gridSize

    while deltaX != 0:
        if deltaX > 0:
            move(East)
            currentX = (currentX + 1) % gridSize
            deltaX -= 1
        else:
            move(West)
            currentX = (currentX - 1) % gridSize
            if currentX < 0:
                currentX += gridSize
            deltaX += 1

    deltaY = (y - currentY) % gridSize
    if deltaY > gridSize / 2:
        deltaY -= gridSize

    while deltaY != 0:
        if deltaY > 0:
            move(North)
            currentY = (currentY + 1) % gridSize
            deltaY -= 1
        else:
            move(South)
            currentY = (currentY - 1) % gridSize
            if currentY < 0:
                currentY += gridSize
            deltaY += 1
GoTo(0,0)