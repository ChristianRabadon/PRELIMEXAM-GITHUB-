class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Student("Christian Rabadon",22)
p2 = Student("Miguel Reyes",55)
print("Name:",p1.name)
print("Name:",p1.age)
print("Name:",p2.name)
print("Name:",p2.age)