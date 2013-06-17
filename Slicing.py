#
# Tutorial - 9
# Slicing
#
# Ross Alejandro A. Bendal
# Monday - June 17, 2013 - 10:39PM
#
#
######################### SLICING ###########################################

example = [0,1,2,3,4,5,6,7,8,9] #lists that are in a variable. Indexes.

print example[4:8]  #First parameter is where you want to start then the second is where you want to stop.
print example[4:10] #Increment one more digit in the second parameter to get all the values.
print example[-5:] #Leaving the parameter will make it continue until the last.
print example[1:8:2] #Third parameter is by increment.
print example[10::-1] #Count backwards.
