'''without constructor'''


class Supermarket:
    pass


product1 = Supermarket()
product2 = Supermarket()

product1.name = "soap"
product2.name = "oil"

print(product1.name)
print(product2.name)

'''with constructor'''
class Supermarket:
    def __init__(self, name):
        self.name = name

product1 = Supermarket("heloo")

print(product1.name)

'''with methods(fun)'''

class Supermarket:
  def __init__(self, name):
    self.name = name


  def myfunc(self):
    print("Hello my name is " + self.name)

product1 = Supermarket("gold")
product1.myfunc()

# Inheritance
'''Has Relationship of inheritance'''
class AC:
    def aircool(self):
        print("cooling")
class Speaker:
    def sound(self):
        print("hearing")
class car:

    def __init__(self):
        self.volats = AC()
        self.sony = Speaker()

'''Nano has AC , Nano has Sepaker'''
nano = car()
print(nano.sony.sound())
print(nano.volats.aircool())

'''IS Relationship of inheritance'''





