#
# Hands on #4
# Object Oriented Programming
#
# Ross Alejandro A. Bendal
# Thursday - June 20 2013 - 9:08
#
#
class pet: # Like a struct in C.
    numberofLegs = 0
    def sleep(self): # Self is user defined and not a python constant.
        print 'zzzzz'
    def countLegs(self):
        print "I have %s legs." %self.numberofLegs # Used self to be transparent as to what the object is; dog/nemo etc.

#dog = pet()
#dog.numberofLegs = 4
#dog.sleep()
#dog.countLegs()

#nemo = pet()
#nemo.numberofLegs = 0
#nemo.sleep()
#nemo.countLegs()

class dog(pet): #Inheritance
    def bark(self):
        print 'woof!'

dog = dog()
dog.bark()
dog.numberofLegs = 4
dog.countLegs() #Has access to both class pet and class dog because pet is inherited.
