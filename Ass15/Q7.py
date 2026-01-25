string = list(input("Enter the string separated by space :").split())
len = list(filter(lambda s : len(s) > 5 , string))
print("String having lenght greater than 5 are :",len)