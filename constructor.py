# class Vehicle:
#    def __init__(self,color,cc):
#       self.color=color
#       self.cc=cc
# toyota=Vehicle('white',1300)
# nissan = Vehicle('red', 1500)
# mazda = Vehicle('blue', 1800)
# print(toyota.color)
# print(mazda.cc)
class Vehicle:
   def __init__(self, toyota, nissan, mazda):
      self.toyota=toyota
      self.nissan=nissan
      self.mazda=mazda
color=Vehicle("white","red","blue")
cc=Vehicle(1300,1500,1800)
print(color.nissan)
print(cc.mazda)