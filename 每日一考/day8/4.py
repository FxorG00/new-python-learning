PI=3.14
class Shape:
    def area(self):
        pass
class Rectangle(Shape) :
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shape) :
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return PI*self.radius*self.radius
list1=[]
list1.append(Rectangle(10,5))
list1.append(Circle(5))
for x in list1:
    print(x.area())