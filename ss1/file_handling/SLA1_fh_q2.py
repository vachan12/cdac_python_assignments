class MyClass:
    def __init__(self, num=0, s=""):
        self.num = num
        self.s = s

    def __add__(self, other):
        # Add numbers + first 3 chars of both strings
        return MyClass(self.num + other.num, self.s[:3] + other.s[:3])

    def __sub__(self, other):
        # Subtract numbers + last 3 chars of both strings
        return MyClass(self.num - other.num, self.s[-3:] + other.s[-3:])

    def __mul__(self, other):
        # Multiply numbers + 1st char repeat logic
        new_s = (self.s[0] * len(self.s)) + (other.s[0] * len(other.s))
        return MyClass(self.num * other.num, new_s)

    def display(self):
        print(f"Result -> Num: {self.num}, String: {self.s}")

# Execution
ob1 = MyClass(12, "abcdserdf")
ob2 = MyClass(13, "bxc")

(ob1 + ob2).display()
(ob1 - ob2).display()
(ob1 * ob2).display()