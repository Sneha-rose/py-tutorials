#income tax calculation

income=float(input("Enter your annual income"))
tax=0
if(income<=250000):
    tax=0
elif (income<=500000):
    tax=(income-250000)*0.05
elif (income<=1000000):
    tax=250000*0.05   
    tax=tax+(income-500000)*0.2
elif (income>1000000):
    tax=250000*0.05
    tax=tax+500000*0.2
    tax=tax+(income-1000000)*0.3

print("Tax=",tax)
