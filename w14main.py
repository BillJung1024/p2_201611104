class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "My dog name is ",self.name
        
    def talk(self,name):
        print "mung mung"
        
class ShihTzuDog(object):
    def talk(self,name):
        print "si si"

class Maltese(object):
    def talk(self,name):
        print "mal mal"
mydog.getName()
mydog.talk('dog')
Bill=ShihTzuDog()
Bill.talk('ShihTzuDog')
Mike=Maltese()
Mike.talk('Maltese')
raw_input("dogs")