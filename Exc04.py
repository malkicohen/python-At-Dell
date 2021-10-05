
# word = input("enter a word")
# x = len(word)
# y = 0
# while y <= x:
#       print(word[0:y])
#       y += 1

st = input("please enter a word")
for letter in st:
    ind = st.index(letter)
    if ind == 0:
        print()
    print(st[0:ind+1])







