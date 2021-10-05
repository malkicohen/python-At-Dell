
def isPolindrom(stringi):
    new_word = ""
    for letter in stringi:
     new_word = letter+new_word
    return new_word == stringi
ustring = input('Please enter a string')
print(isPolindrom(ustring))

# def isPalindrome(w):
#     return s == s[::-1]
#
# s = input("Please enter a word")
# if isPalindrome(s):
#     print("Yes")
# else:
#     print("No")