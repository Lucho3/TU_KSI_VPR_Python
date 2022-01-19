def palindrome(number):
    number_str=str(number)
    for i in range(len(number_str)):
        if number_str[i]!=number_str[-i-1]:
            return 0
    return 1

number=int(input("Enter number: "))
print(palindrome(number))