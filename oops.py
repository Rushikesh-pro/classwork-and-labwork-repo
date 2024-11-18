class Test:
    def add(self,a,b):
      res = a+b
      return res

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

T=Test()
answer = T.add(a,b)
print("The addition of 2 values is: ",answer)