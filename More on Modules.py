#
# Hands on exercises # 4
# More on Modules - built in.
#
# Ross Alejandro A. Bendal
# Wednesday - June 19 2013 - 9:38
#
#
############################ RANDOM ###########################
import random
random.randint(0, 10) #randint picks two parameters one being the lowest and the second being the highest.

randomFloat = random.random() * 100 #random float, multiply by 100 to get the decimals up to the first.

userList = ['ross','doby','unix']
randomList = random.choice(userList) #picks random index on a list.
print randomList

############################ MATHS ############################
print'maths function'

import math
math.pi
math.sin(20)
math.degrees(3)
math.factorial(5)
math.sqrt(49)
math.exp(5)

############################# URL ###########################
print 'url'

import urllib2
url = urllib2.urlopen("http://google.com").read(100) #gets the first 100 characters of that website.
print url

############################# DATE TIME #####################
print 'date and time'

import datetime
from datetime import date
import time
time = date.fromtimestamp(time.time()) #converts the time.time() to a more readable
print time
newDate = time.strftime("%d/%m/%y") #changes the date format with strftume
print newDate
ad = date.fromordinal(10000) # gets the year after 1 ad. wtf.
print ad

############################# OPERATING SYSTEM ###############
print 'operating system'

import os
from os import path
path2 = path.exists("C:") #checks if a direcotry exists.
print path2
pathTime = path.getatime("C:") #checks the time it was  modified
print pathTime
#pathBytes = path.getsize{"C:"} #shows the size of a directory in bytes.
pathJoin = path.join("C:", "users")
print pathJoin

############################### LAST TIPS ###########################
#assign the modules and functions in variables.
#random.random() will be:
ran = random.random #parenthesis will be in the variable
print ran() #parenthesis here
square = math.sqrt
print square(2)
