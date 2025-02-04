l1 =[]
while True:
    n=input("Enter a number (want to continue(no)):")
    if n =='no':
        break
    l1.append(int(n))
print("List1:",l1)

l2 =[]
while True:
    n=input("Enter a no (want to continue(no)):")
    if n =='no':
        break
    l2.append(int(n))
print("List2:",l2)

com_ele = [n for n in l1 if n in l2]
print("Common elements in both:",com_ele)
