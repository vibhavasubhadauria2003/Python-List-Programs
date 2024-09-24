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
def matrixTranspose(m,n):
    trans=[]
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(m[j][i])
        trans.append(temp)
    return trans
        


print("Enter matrix")
m=inputMatrix(n)
print("Matrix is")
printMatrix(m)
mTrans=matrixTranspose(m,n)

print("Transposed matrix is")
printMatrix(mTrans)
