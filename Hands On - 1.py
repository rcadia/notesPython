#
# Hands on Exercises - Variables and Data Types
# Tuesday - June 18, 2013 - 7:08PM 
#
#

twelve = 12
print twelve

greeting = 'Hello World'
print greeting

# Python is True or False
isMale = True
print isMale

myList = [1,2,3]
print myList

myList = [1,'Hello',False] #Lists or array in other language. Can hold any data types on alist.
print myList

myList = [1,[1,2,3],True] #Theoretically you can use nested lists as needed.
print myList

######################## DECLARING VARIABLES ##############
#Traditional:
a = 1
b = 2
c = 3

#In python/can be in linear:
a, b, c = 1, 2, 3 #a gets 1, b gets 2, c gets 3

a = b = c = 1 # a b and c will get the value of 1

######################### OPERATORS #######################
# + = operators
# numbers being operated are called operands

Hello = 'hello'*10+'end'
print Hello

######################### CONTROL STRUCTURES ##############
#Conditionals and loops.

#Conditionals - decide between one thing or another.

isAlive = False
if isAlive:         #if will run if True
    print 'Congrats!'
else:
    print 'Sorry about that!'

a = 3
if a == 3:
    print 'Equals to three!'
elif a <= 3:
    print 'still equal'
else:
    print 'im sorry about that'

b = 17
if a == 3 and b == 17: #TRUE AND TRUE = TRUE
    print 'both correct!'
if a == 3 or b == 17:
    print 'still correct!'


x = 'happy'
if 'a' in x:    #check if there is a letter a on that string.
    print 'there\'s an A on that string'

#print myList[1][1] #accessing list within a list
myList = [1,2,3]
for a in range(10):
    print a
x, y = 100, 200
while x <= y: # while x is less than y, repeat
    print x
    x += 1 #increment by 1
