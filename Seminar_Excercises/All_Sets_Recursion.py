def Recursion_sets(list,final,clone=[],i=0):
    if i==len(list):
        final.append(clone)
        i=0 
        return 1
    copyclone=clone.copy()
    copyclone1=clone.copy()
    copyclone1.append(list[i])

    Recursion_sets(list,final,copyclone,i+1)
    Recursion_sets(list,final,copyclone1,i+1)

list1=[1,2,3]
final=[]
Recursion_sets(list1,final)
print(final)


