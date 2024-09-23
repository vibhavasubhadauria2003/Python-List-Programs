l1=[]
print("Enter the list")
while True:
    temp=int(input("  Enter item : "))
    l1.append(temp)
    x=input("    Enter Y to continue or N to exit : ")
    if x=='N'or x=='n':
        break
print(f'Entered list is: {l1}')