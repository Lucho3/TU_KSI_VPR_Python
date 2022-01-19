import random

def Create_List():
    matrix = [random.randint(1,15) for i in range(10)]
    return  matrix

def Bubble_Sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]
    return list
list=Create_List()

print(list)
print(Bubble_Sort(list))
