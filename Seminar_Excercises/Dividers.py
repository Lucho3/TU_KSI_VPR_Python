def find_dividers(number_input):
    listOfDividers = []
    for i in range(1,number_input//2+1):
        if number_input%i == 0:
            listOfDividers.append(i)
    print(listOfDividers)

number_input=int(input("Enter your number:"))
find_dividers(number_input)

for i in range(1, number_input // 2 + 1):
    if number_input % i == 0:
        print(i)