No = int(input("Enter the number :"))
sum = 0
temp = abs(No) # -ve to + ve number
while temp > 0 :
        digit = temp % 10 # get last digit 
        sum = sum + digit  # add digit to sum
        temp = temp // 10  # remove last digit
print("number of digits :",sum)
