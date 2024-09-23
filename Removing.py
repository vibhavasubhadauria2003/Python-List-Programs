l1=[4,6,2,8,1,9]
print(l1)
n=int(input("Enter number to remove : "))
l1.remove(n)
print(l1)
del(l1[0])
print("removing from index 0")
print(l1)

print("poping last item")
l1.pop()
print(l1)