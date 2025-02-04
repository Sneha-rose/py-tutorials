

num = [3, 1, 7, 9, 2, 8]
if len(num) < 3:
     print("None")
else:
     third_large=sorted(num, reverse=True)[2]
     print("3rd Largest:",third_large)
