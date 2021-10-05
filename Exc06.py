import random
# randomlist1 = random.sample(range(10, 30), 5)
# randomlist2 = random.sample(range(10, 20), 7)
randomlist1=[14,1,5,14,2]
randomlist2=[1,5,1,4,14,2,14]
new_list=[]
print(randomlist1)
print(randomlist2)
cnt1 = 0
cnt2 = 0
for num1 in randomlist1:
    for num2 in randomlist2:
        if num1 == num2:
         new_list.append(num1)


print(new_list)







