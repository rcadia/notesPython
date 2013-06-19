#
# Hands on exercises # 2
# Modules and Functions
#
# Ross Alejandro A. Bendal
# Wednesday - June 19 2013 - 7:23
#
#
################### E COMMERCE EXAMPLE ###############################
cost1 = 15
cost2 = 20

cost3 = 5
cost4 = 10
def sumCart(item1, item2 = 5):  # Arguments can have a defined value in case that the user upplied only one value.
    totalCost = item1 + item2
    print totalCost

sumCart(cost3, cost4) # This will run and the second argument will overwrite the pre-defined value of that second argument.
sumCart(cost1) # This will run since the second argument in sumCart has a pre-defined value.

################## USING RETURN FUNCTION VS. PRINT ####################

print 'RETURN FUNCTION:'
cost1 = 15
cost2 = 20

cost3 = 5
cost4 = 10
def sumCart(item1, item2 = 5):  # Arguments can have a defined value in case that the user upplied only one value.
    totalCost = item1 + item2
    return totalCost # Returns the output value to wherever it originated, rather than printing it.

cart1 = sumCart(cost3, cost4) # We created a variable so that sumCart can return the value on this variable 
cart2 = sumCart(cost1)

print cart1
print cart2

################# LISTS OF MULTIPLE COST ################################
print 'list of multiple cost'
costs = [5,10,15,20]

def sumCart(items):
    totalCost = 0  # Total cost will be the one that will handle all the sum.
    for x in costs: # X will get all the index on the list one by one and process them.
        totalCost += x # totalCost will start at 0 and will increment by the index available, summing it all up on totalCost.
    return totalCost
print sumCart(costs)

################# BUILT IN FUNCTIONS ####################################
print 'BUILT IN FUNCTION'
numberString = 10
print 'the value is: '+str(numberString)

bool = True
print 'the value is: ' +str(bool)

string = 'Hello World'
print 'Numbers of characters: '+str(len(string)) #counts the string characters then converts it to string for concatination.

numberRound = 10.6
print int(numberRound) # Removes all the numbers after the decimal.

parseInt = '10'
print int(parseInt) # Parses the string to integer. It's now a number!!

rangeNum = range(11) # Count starts to zero to less one of what you put in. Printed in list function.
print rangeNum

rangeNum = range(11, 0, -1)
print rangeNum
