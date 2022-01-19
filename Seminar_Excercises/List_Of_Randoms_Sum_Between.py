import random

randomlist = []
for i in range(0,10):
    n = random.randint(1,30)
    randomlist.append(n)

new_random_list=list()
for p in (range(1,len(randomlist))):
    new_random_list.append(randomlist[p]+randomlist[p-1])

print(randomlist)
print(new_random_list)
final_random_list=list()
for z in (range(len(randomlist))):
    final_random_list.append(randomlist[z])
    if z<len(new_random_list):
        final_random_list.append(new_random_list[z])

print(final_random_list)
