def lists_division(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    
    return sum_y / sum_x

# Example usage:
x_values = [10, 20, 30]
y_values = [5, 10, 15]
result = lists_division(x_values, y_values)
print("Result:", result)

#Making it object oriented:
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