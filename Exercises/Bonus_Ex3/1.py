def Add_In_List(list,size):
    for i in range(0,size):
        list.append(list[i])

def List_Sum(list1,list2):
    if len(list1) > len(list2):
        Add_In_List(list2,len(list1) - len(list2))
    elif len(list1) < len(list2):
        Add_In_List(list1,len(list2) - len(list1))

    sum=0
    for i in range(len(list1)):
        sum+=list1[i]*list2[i]

    return sum


list1=[1,2,3,4]#1,2,3,1
list2=[1,2,3]

print(List_Sum(list1,list2))
