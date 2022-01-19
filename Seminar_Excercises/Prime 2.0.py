import  math

def isPrime(n):
    if n<=2:
        return True;
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return  False
        return  True

number=int(input("Enter number:"))
print(("{0} is prime: {1}".format(number,str(isPrime((number))))))

