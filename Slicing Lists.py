#
# Tutorial 13
# Slicing Lists
#
# Ross Alejandro A. Bendal
# Monday June 18 2013 - 1:41AM
#
#
#
#####################

example = list('easyhoss') #Slices words by index.
print example

example[4:]=list('baby') #Replaces the words from index 4 onwards with a new list.
print example


example=[7,8,9]
example[1:1] = [3,3,3] #add the list to index one AND TO index one only. 1:1
print example

example[1:4]=[] #delete indexes using list.
print example
