import random

def Create_List():
    matrix = [random.randint(1,15) for i in range(10)]
    return  matrix

def Max_In_List(list_of_numbers):
    max=list_of_numbers[0]
    index=0
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i]>max:
            max=list_of_numbers[i]
            index=i
    return list([max,index])

list_of_numbers=Create_List()

print(list_of_numbers)
print(Max_In_List(list_of_numbers))

