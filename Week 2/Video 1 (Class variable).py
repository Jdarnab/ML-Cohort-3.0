# class Point:
#     def move (self):
#         print ('move')
#     def draw (self):
#         print("draw")
# point= Point()
# point.x=100
# point.move()
# print(point.x)
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area (self):
        print( "The Area is:", self.x*self.y)
D= Rectangle(5,10)
D.area()
class Average :
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def average (self):
        print( "The Average is :", (self.a+self.b)/2 )
        """return  (self.a+self.b)/2"""
Avg= Average (10,105)
Avg.average()
    
# class Average:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y

#     def average(self):
#         print('The Average is :', (self.a + self.b) / 2)

# # # Creating an instance of Average
# avg = Average(10, 105)
# avg.average()






