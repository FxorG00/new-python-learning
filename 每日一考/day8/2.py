import types

PI=3.14
class Circle:
    def __init__(self,radius):
        self.radius=radius
def calculate_area(self) :
    return PI*(self.radius**2)
c1=Circle(5)
c1.cal=types.MethodType(calculate_area,c1)
print(c1.cal())