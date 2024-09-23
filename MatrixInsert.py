l=[]

n=int(input("Enter the limit of : "))
for i in range(n):
    l1=[]
    for j in range(n):
        x=int(input("Enter item : "))
        l1.append(x)
    l.append(l1)
for item in l:
    for item1 in item:
        print(item1,end=" ")
    print()

print('Positive Diagonal')
for i in range(n):
    print(l[i][i])

print ('Negative Diagonal')
j=n-1
for i in range(n):
    print(l[i][j])
    j-=1