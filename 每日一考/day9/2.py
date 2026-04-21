class InvalidAgeError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value
class UnrealisticAgeError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return self.value
def check_age(age):
    if age<0:
        raise InvalidAgeError("年龄为负！")
    elif age>120:
        raise UnrealisticAgeError("能活这么久？")
try:
    check_age(1110)
except (InvalidAgeError,UnrealisticAgeError) as e:
    print(e)
finally:
    print("ok")
