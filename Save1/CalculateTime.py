clear()
def CalculateTime():
	timeA = get_time()
	
	#Do something
	
	PlantMaze()
	SolveMaze()
	
	#Pumpkin()
	
	return get_time() - timeA
	
def CalculateTimeAverage(runs):
	sum = 0
	for i in range(runs):
		sum += CalculateTime()
	average = sum / runs
	
	quick_print("Runs: ", runs)
	quick_print("Average time", average)
	
CalculateTimeAverage(10)