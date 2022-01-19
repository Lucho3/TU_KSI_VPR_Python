number=int(input("Enter new number: "))
list_of_numbers=list()

for i in range(1,number+1):
    list_of_numbers.append(i)

dict_of_numbers=dict()

for p in range(len(list_of_numbers)):
    dict_of_numbers[list_of_numbers[p]]=list_of_numbers[(-1-p)]

print(dict_of_numbers)
