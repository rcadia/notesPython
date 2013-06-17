#
# Tutorial 14
# Intro to methods
#
# Ross Alejandro A. Bendal
# Monday June 18 2013 - 2:04AM
#
#
# yourface.punch() #the first is the object. what you want to do to it.

face=[21,18,30] #created a simple list.
print face
face.append(45) #append is to add something to the end of the list
print face

apples = ['i','love','apples','apples','now']
print apples
print apples.count('apples') #Returns how many times does the string mentioned.

one = [1,2,3]
two = [4,5,6]
one.extend(two) #Extend connects two list together. object.method.argument
print one
