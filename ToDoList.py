# Copy the code and paste it in PyCharm
class Person:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.pronoun = None
        self.height = height
        self.weight = weight
        self.age = age

    def __sub__(self, other: "Person"):
        return self.age - other.age

    def __str__(self):
        return f"{self.name} is {self.height}cm\n{self.pronoun} is {self.age} and {self.weight}Kg"

    def bmr(self) -> float:
        raise NotImplementedError("Not Implemented!")


class Male(Person):
    def __init__(self, name, height, weight, age):
        Person.__init__(self, name, height, weight, age)
        self.pronoun = "He"

    def bmr(self):
        self.bmr = 13.397 * self.weight + 4.799 * self.height - 5.677 * self.age + 88.362



class Female(Person):
    def __init__(self, name, height, weight, age):
        Person.__init__(self, name, height, weight, age)
        self.pronoun = "She"

    def bmr(self):
        self.bmr = 13.397 * self.weight + 4.799 * self.height - 5.677 * self.age + 88.362


class Gym:
    def __init__(self):
        self.member = []

    def add_member(self, m: Person):
        self.member.append(m)

    def total_bmr(self):
        pass


boy = Male("Nasir", 180, 80, 20)
girl1 = Female("Lina", 180, 70, 19)
girl2 = girl1
girl1.bmr()
print(girl1.bmr)

gym = Gym()
gym.add_member(boy)
gym.add_member(girl1)
print(gym.total_bmr())

print(girl1)

# Does Person, Female and Male classes represent an MVC design pattern? -> Answer: False
# Gym class "is-a" list. -> Answer: True
# 'add_member method' in Gym class overrides 'append method' of built-in class list. -> Answer: False
# The instance variables of boy are -> Answer: self.name, self.height, self.weight, self.age, self.pronoun
# Female is a _______ of Person Class -> Answer: subclass
# What is the output if we write print(boy - girl1) at the end of the program? -> Answer: 1

# What is the output if we write print(girl1) at the end of the program? -> Answer:
'''
# Lina is 180cm.
# She is 19 and 70Kg
'''

# Implement a method that overrides the 'bmr method' of Person class in Male, Female subclasses. -> Answer:
# BMR for Male = (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years) + 88.362
# BMR for Female = (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years) + 447.593
'''
# For Male class:
    def bmr(self) -> float:
        bmr = (13.397 * self.weight) + (4.799 * self.height) – (5.677 * self.age) + 88.362
        return bmr

# For female class:
    def bmr(self) -> float:
        bmr = (9.247 * self.weight) + (3.098 * self.height) – (4.330 * self.age) + 88.362
        return bmr
'''

# Implement the 'total_bmr method' in Gym class. -> Answer:
'''
     def total_bmr(self):
        sum_total = 0
        for i in self.member:
            sum_total += i.bmr()
        return sum_total
'''
