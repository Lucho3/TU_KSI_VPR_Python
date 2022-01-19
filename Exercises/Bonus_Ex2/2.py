def Create_List(x,y):
    matrix = [[-1 for i in range(y)] for i in range(x)]
    return  matrix

def Snake_Fill(matrix):
    ctr=1
    row,col=0,0
    while(True):

        #Дъно на цикъла
        if not any(-1 in x for x in matrix):
            break

        #Местене надясно
        if row<len(matrix)//2 and row<len(matrix):
            for y in range(len(matrix[0])):
                if matrix[row][y]==-1:
                    matrix[row][y]=ctr
                    ctr+=1
                    col=y
            row+=1

        #Движение надолу 
        if col>len(matrix[0])//2 and col>=0:
            for x in range(len(matrix)):
                if matrix[x][col]==-1:
                    matrix[x][col]=ctr
                    ctr+=1
                    row=x
            col-=1
            
        #Движение наляво
        if row>=len(matrix)//2 and row>=0:
            for y in range(len(matrix[0])-1,-1,-1):
                if matrix[row][y]==-1:
                    matrix[row][y]=ctr
                    ctr+=1
                    col=y
            row-=1

        #Движение нагоре
        if col<=len(matrix[0])//2 and col<len(matrix[0]):
            for x in range(len(matrix)-1,-1,-1):
                if matrix[x][col]==-1:
                    matrix[x][col]=ctr
                    ctr+=1
                    row=x
            col+=1

    return matrix

def Print_2D_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


x=int(input("Enter x:"))
y=int(input("Enter y:"))

list_of_numbers=Create_List(x,y)
list_of_numbers=Snake_Fill(list_of_numbers)

print(Print_2D_list(list_of_numbers))
