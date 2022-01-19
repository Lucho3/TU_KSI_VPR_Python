import  math

def isPrime(n):
    if n<=2:
        return True;
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return  False
        return  True

for i in range(25,51):
    if isPrime(i)==True:
        print(i)
