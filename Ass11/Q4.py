No = int(input("Enter the Number :"))
rev = 0
temp = abs(No)

while temp > 0 :
    digit = temp % 10 
    rev = rev * 10 + digit
    temp = temp // 10

    if No < 0 :
        rev = - rev
print("Reversed number :",rev)