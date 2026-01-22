No = int(input("Enter the number :"))
count = 0
temp = abs(No)
if temp == 0:
    count = 1
else :
    while temp > 0 :
        temp = temp // 10
        count += 1 
print("number of digits :",count)
