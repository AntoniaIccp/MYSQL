class MathDojo:
    def __init__(self):
        self.result = 0
        
    def suma(self, num, *nums):
            self.result += num
            for n in nums:
                self.result += n
            return self
        
    def resta(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
            return self
    
md = MathDojo()

x = md.suma(2).sumar(2,5,1).resta(3,2).result
print(x)

