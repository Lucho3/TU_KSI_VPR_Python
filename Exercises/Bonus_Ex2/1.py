import random
import string

def Create_List(x,y):
    matrix = [[random.choice(string.ascii_letters) for i in range(y)] for i in range(x)]
    return  matrix

x=int(input("Enter x:"))
y=int(input("Enter y:"))

list=[[0 for i in range(y)] for i in range(x)]
list=Create_List(x,y)
print(list)
