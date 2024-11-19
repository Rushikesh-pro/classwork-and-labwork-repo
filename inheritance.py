
class plus:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Addition(plus):
    def add(self):
        return self.a + self.b


class Subtraction(plus):
    def sub(self):
        return self.a - self.b



num1 = 5
num2 = 1

addition = Addition(num1, num2)
subtraction = Subtraction(num1, num2)

print(f"Addition of {num1} and {num2} is: {addition.add()}")
print(f"subtraction of {num1} and {num2} is: {subtraction.sub()}")
