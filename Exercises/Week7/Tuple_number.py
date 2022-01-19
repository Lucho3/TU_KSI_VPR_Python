number=int(input("Enter number: "))

numbers_tuple=tuple(x for x in range(1,number+1))
reversed_numbers_tup=tuple(x for x in range(number,0,-1))

print(numbers_tuple)
print(reversed_numbers_tup)
