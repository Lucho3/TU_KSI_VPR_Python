import random

def Create_List(x,y):
    matrix = [[random.randint(1,15) for i in range(y)] for i in range(x)]
    return  matrix

print("Enter dimensions of the list:")
x=int(input("Enter x:"))
y=int(input("Enter y:"))

list=[[0 for i in range(y)] for i in range(x)]
list=Create_List(x,y)
print(list)

row=int(input("Enter row to delete:"))
col=int(input("Enter col to delete:"))

for row_count in range(len(list)):
    if row==row_count:
        del list[row-1]
        break

for col_count in range(len(list[0])):
    if col==col_count:
        for rows in range(len(list)-1,-1,-1):
            del list[rows][col_count-1]
        break
print(list)
