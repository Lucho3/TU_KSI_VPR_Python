class Travel:
    def __init__(self,id,destination,flight,price):
        self.id=id
        self.destination=destination
        self.flight=flight
        self.price=price

    def Reduce(self):
        if self.price>200:
            self.price-=self.price*0.1

    def Print(self):
        print('''id: {}
                 destination: {}
                 flight: {}
                 price: {}'''.format(self.id, self.destination, self.flight, self.price))

s1 = Travel(1, "Peru", "Fl1", 300)
s1.Reduce()
s1.Print()