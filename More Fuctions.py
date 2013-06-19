#
# Tutorial - 15
# More Functions
#
# Ross Alejandro A. Bendal
# Tuesday June 18 2013 - 5:18PM
#
#

say = ['hey','now','brown']
print say.index('brown') # Search for index that will match in the text parameter

say.insert(2,'show') # Inserts a new value. (Index.'string')
print say

say.pop(2) # Removes a value in index. Returns the value
print say

say.remove('brown') # Removes the string on an index completely.
print say

say.reverse() # Reverse the indexes.
print say
