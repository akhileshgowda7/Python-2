class kettle(object):
    def __init__(self,make, price):
        self.make=make
        self.price=price
        self.on=False


kenwood= kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price=12.75
print(kenwood.price)

hamilton=kettle("hamilton",14.55)
print(hamilton.price)
print(hamilton.make)

print("{}={},{}={}".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))

