m=int(input("Enter rows : "))
n=int(input("Enter columns : "))
def printMatrix(m):
    for item in m:
        for item1 in item:
            print(item1,end=" ")
        print()
def inputMatrix(m,n):
    mat=[]
    for i in range(m):
        m0=[]
        print(f'=>Enter items of row number {i+1}')
        for j in range(n):
            x=int(input("   Enter item : "))
            m0.append(x)
        mat.append(m0)
    return mat
def matrixAdd(m1,m2,n):
    add=[]
    for i in range(n):
        tem=[]
        for j in range(n):
            tem.append(m1[i][j]+m2[i][j])
        add.append(tem)
    return add



print("Enter First matrix")
m1=inputMatrix(m,n)
print("Enter Second matrix")
m2=inputMatrix(m,n)
print("First matrix")
printMatrix(m1)
print("Second matrix")
printMatrix(m2)

# for i in range(m):
#     for j in range(n):
#         temp=m1[i][j]
#         m1[i][j]=m2[i][j]
#         m2[i][j]=temp
temp=m1
m1=m2
m2=temp


print("First matrix")
printMatrix(m1)
print("Second matrix")
printMatrix(m2)