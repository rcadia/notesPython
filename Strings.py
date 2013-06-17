#
# Tutorial - 6 
# Strings
#
# Ross Alejandro A. Bendal
# Monday - June 17, 2013 - 4:34
#
# Strings can be "dobule quote" or 'single quote'
# Few exceptions:

print "He's a jerk." #Double qoutes so that we can use the single qoute for display.
print 'He\'s a jerk.' #Backslash means it nullifies the next value.

print "He said, \"You are a jerk!\" to me." #Using backslash so Python will ignore whatever comes next to slash.
print 'He said, "You are a jerk!" to me' # Using single quotes to print the double quote as a sentence.

####################### CONCATINATING A STRING ################################

a = "John " #First name was assigned to variable 'a'.
b = "Doe" #Last name was assigned to variable 'b'.

print a + b #Using + to concatinate a and b to create a seamless line of string.
