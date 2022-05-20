

# Program to check if a string contains any special character.

str1=input("Enter a string : ")
special_char = str1.split()
for i in special_char:
    for j in i:
        if j.isalnum() or j==" ":
            n=True
        else:
            n=False
            print("This string is not accepted")
            break
    if n==False:
        break
if n==True:
    print("String is accepted")
