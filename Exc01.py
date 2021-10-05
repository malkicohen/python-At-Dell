tryi = 0
cnt = 0
sum = 0
while True:
    mnumber = input('Please enter a number: ')
    if mnumber == 'q':
        break
    try:
            fnumber = float(mnumber)
    except:
            print('Please enter a numeric value input')
            continue
    cnt = cnt + 1
    sum = sum+int(fnumber)
print(cnt," cnt")
print(sum, " sum")
print("The average is: ", sum/cnt)








