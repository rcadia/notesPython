#
# Tutorial 12
# More list functions
#
# Ross Alejandro A. Bendal
# Monday June 18 2013 - 12:21AM
#
#
########################## SOME LIST FUNCTIONS ###############################

numbers=[8,2,123,556,56,1024,55,6]

print len(numbers) #gets the lenght of index.
print max(numbers) #maximum expression.
print min(numbers) #minimum expression.
numbers[3]=69 #changes index 3 to 69
print numbers
del numbers[3]
print numbers
######################### CONVERT STRING TO LIST ############################

toList = 'dumbass'
print list(toList) #converts the string to a list.

