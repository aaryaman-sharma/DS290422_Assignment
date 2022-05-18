
# Python program to capitalize the first and last character of each word in a string (input string should be a statement)

def String_Lettercap_f_and_a(str):
      

    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), 
                        s.title().split()))
      
s = input("Enter string : ")
print("String before:", s)
print("String after:", String_Lettercap_f_and_a(str))