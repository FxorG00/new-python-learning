class Person:
    home="earth"
    def __init__(self,name):
        self.name=name
class YellowRace(Person):
    color="yellow"
p1=YellowRace("xiaoming")
print(p1.home)