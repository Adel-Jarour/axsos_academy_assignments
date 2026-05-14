class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# Testing the class
md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)

# Additional tests
md2 = MathDojo()
print(md2.add(10).add(5, 3, 2).subtract(1, 1).result)

md3 = MathDojo()
print(md3.add(100).subtract(30, 20, 10).add(5, 5).result)