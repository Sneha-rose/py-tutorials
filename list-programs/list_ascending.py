num =[]
while True:
    n=input("Enter a no (want to continue(no)):")
    if n =='no':
        break
    num.append(int(n))
print("List:",num)
newli=[n for n in num if n % 2 == 0]
newli.sort()
print("List of even no:",newli)
