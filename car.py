class Carmodel:
    def __init__(self,color,year_manufactured,num_plate):
        self.color=color
        self.year_manufactured=year_manufactured
        self.num_plate=num_plate
ford= Carmodel("red",1945,"KMTC")
honda = Carmodel("black", 1999, "KMTH")
audi = Carmodel("blue", 2000, "KMTM")
print(ford.color, ford.year_manufactured, ford.num_plate)
print(honda.color, ford.year_manufactured, ford.num_plate)
print(audi.color, ford.year_manufactured, ford.num_plate)



