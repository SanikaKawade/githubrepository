No = int(input("Enter the Number :"))
rev = 0
temp = abs(No)

while temp > 0 :
    digit = temp % 10 
    rev = rev * 10 + digit
    temp = temp // 10

    if rev == abs(No) :
        print("number is palindrome ")
    else :
        print("number is not palindrome")