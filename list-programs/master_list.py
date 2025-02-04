l1=[]
while True:
    num=int(input("Enter a number:"))
    l1.append(num)
    ch=input("want to continue(y/n):")
    if ch !='y':
        break
print(l1)
newlist=[]
num=int(input("Enter a number to filter:"))
for ele in l1:
    if(ele<num):
        newlist.append(ele)
print("Filtered list:",newlist)
