def Power_Of_Two(final_power):
    for i in range(1,final_power+1):
        yield 2**i


for i in Power_Of_Two(6):
    print(i, end=' ')