#Exercise 2 - object oriented
#first: making the function object oriented.
class ListCalculator:
    def __init__(self, x, y): #this is the constructor.
        self.x = x
        self.y = y
    
    def division(self):
        result = sum(self.y) / sum(self.x)
        return result

lists1 = ListCalculator([10, 20, 30], [5, 10, 15])
print(lists1.division())