# -*- coding: cp1252 -*-
print("Welcome to Harry Harrison's Carpentization IV: Beyond the Window\n'Build a Window to Stand the Test of Time'")
raw_input("Press enter to start the program")
priceOfWood = int( input("How expensive is the wood per metre? (in pounds): ") * 100)
windows = int( input("How many windows would you like?: "))
firstHeight = int( input("How high is your first window? (in meters): "))
firstWidth = int( input("How wide is your first window? (in meters): "))
heights = [firstHeight]
widths = [firstWidth]
totalCost = priceOfWood * firstHeight * firstWidth
windowsDone = 1
while windowsDone != windows:
    heights.extend([int(input("(Window %d) How high is this next window?:" % windowsDone + 1))])
    widths.extend([int(input("How wide is this window?: "))])
    totalCost = (totalCost + heights[windowsDone] * widths[windowsDone] * priceOfWood)
    windowsDone = windowsDone + 1

time = int( input("How long will it take to make a window? (hours): "))
labor = int( input("What are the labor costs per hour? (pounds): "))
totalCost = totalCost + (windows * time * labor)
tC_float = float(totalCost / 100)
print("The total cost is: %f pounds" % tC_float)
