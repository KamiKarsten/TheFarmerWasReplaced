clear()

before = num_items(Items.Power)
#till()
#TradeIfNeeded(Items.Pumpkin_Seed)
Sunflower()
#plant(Entities.Pumpkin)
#companion = get_companion()
#while not can_harvest():
#	pass
#harvest()
after = num_items(Items.Power)

#quick_print("companion", companion)
quick_print("expected",CalculateYield(Entities.Sunflower,100))
quick_print("actual",after - before)
