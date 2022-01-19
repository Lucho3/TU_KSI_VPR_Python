import random

list_numbers=[random.randint(1,50) for x in range(9)]
print(list_numbers)

list_sums=list()

for i in range(len(list_numbers)):
    if i%2==1:
        list_sums.append(list_numbers[i]+list_numbers[i-1])

print(list_sums)

new_list=list()
for i in range(len(list_sums)):
    new_list.append(list_numbers[0])
    list_numbers.pop(0)
    new_list.append(list_numbers[0])
    list_numbers.pop(0)
    new_list.append(list_sums[i])

    if i==len(list_sums)-1 and len(list_numbers)>0:
        new_list.append(list_numbers[0])

print(new_list)
