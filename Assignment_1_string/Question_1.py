
# Python program to capitalize the first and last character of each word in a string (input string should be a statement)

str1=input("Enter An  String:")
j=0
str=list(str1)
str+='\0'

for i in range(len(str)):
    if i==0 or str[i-1]==' ':
        str[i]=str[i].upper()
    elif str[i]==' ' or str[i]=='\0':
        str[i-1] = str[i-1].upper()

print("".join(str))