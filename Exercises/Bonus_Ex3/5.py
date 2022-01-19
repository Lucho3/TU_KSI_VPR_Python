def Max_In_Range(num1,num2):
    list1=[x for x in range(num1,num2)]
    return max(list1)

def Max_By_Reference(func,num1,num2):
    max=func(num1,num2)
    return max

print(Max_By_Reference(Max_In_Range,1,5))

