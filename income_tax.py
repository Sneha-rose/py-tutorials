#income tax calculation

income=float(input("Enter your annual income"))
tax=0
if(income<=300000):
    tax=0
elif (income<=700000):
    tax=(income-300000)*0.05
elif (income<=1000000):
    tax=(700000 - 300000)*0.05 
    tax += (income-700000)*0.2
else:
    tax = (700000 - 300000) *0.05
    tax += (1000000 - 700000)*0.2
    tax += (income-1000000)*0.3

print("Tax=",tax)
