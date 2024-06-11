expected = 10000

item = Items.Hay

while(num_items(item) < expected):
	Farm(item)

HarvestAll()
ResetDrone()
	