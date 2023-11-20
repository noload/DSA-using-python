def setZero(arrMatrix,m,n):
    row=[0]*m
    col=[0]*n
    for i in range(m):
        for j in range(n):
            if arrMatrix[i][j] == 0:
                print("*")
                row[i]=1
                col[j]=1
        

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    arrMatrix[i][j] = 0
        
        return arrMatrix



matrix =[[1,0,1],[1,1,1],[1,1,1]]
m=len(matrix)
n=len(matrix[0])
ans = setZero(matrix,m,n)
for row in ans:
    for ele in row:
        print(ele, end=" ")
    print()
