class MyString:

    def __init__(self, s):
        self.s = s

    def __mul__(self, other):
        return self.s * other

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        return self.s + other

    def __radd__(self, other):
        return other + self.s

    def __str__(self):
        return self.s

    def __neg__(self):
        return self.s[::-1]

s = MyString('Python Programmer is Good')
t = s / ' '
print(type(t))
print(t)

print(s + "job")

print(MyString("python") * 3)

print('Hello' + ' ' + MyString('World'))

print(-MyString('python'))

