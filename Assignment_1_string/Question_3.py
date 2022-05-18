
# Program to check if a string contains any special character.

import re

def find(string):
    special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    
    if special_char.search(string) == None:
        return ("string is accepted")
    else:
        return ("string not accepted")
   

str1 = input("Enter string : ")
print(str1)
print(find(str1))
