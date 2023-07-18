class DecimalToBase:
    def conversion(self, a, b):
        s = ""
        while(a != 0 and a != 1):
            s = str(a % b)+s
            a = a//b
        s = str(a)+s
        return s

a = int(input())
b = int(input())
object = DecimalToBase()
print(object.conversion(a, b))