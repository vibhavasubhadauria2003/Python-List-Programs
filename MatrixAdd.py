n=int(input("Enter limit of squre matrix : "))
def printMatrix(m):
    for item in m:
        for item1 in item:
            print(item1,end=" ")
        print()
def inputMatrix(n):
    m=[]
    for i in range(n):
        m0=[]
        print(f'=>Enter items of row number {i+1}')
        for j in range(n):
            x=int(input("   Enter item : "))
            m0.append(x)
        m.append(m0)
    return m
def matrixAdd(m1,m2,n):
    add=[]
    for i in range(n):
        tem=[]
        for j in range(n):
            tem.append(m1[i][j]+m2[i][j])
        add.append(tem)
    return add



print("Enter First matrix")
m1=inputMatrix(n)
print("Enter Second matrix")
m2=inputMatrix(n)
print("First matrix")
printMatrix(m1)
print("Second matrix")
printMatrix(m2)

mAdd=matrixAdd(m1,m2,n)

print("Added matrix is")
printMatrix(mAdd)
