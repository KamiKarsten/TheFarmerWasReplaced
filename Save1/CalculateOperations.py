clear()

def CalculateOperations():
	before = get_op_count()
	
	PlantMaze()
	SolveMaze()
	
	#Pumpkin()
		
	
	return get_op_count() - before -2

def CalculateOperationsAverage(runs):
	sum = 0
	for i in range(runs):
		sum += CalculateOperations()
	average = sum / runs
	
	quick_print("Runs: ", runs)
	quick_print("Average Operations", average)

CalculateOperationsAverage(10)