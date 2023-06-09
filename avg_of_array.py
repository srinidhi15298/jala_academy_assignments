# 2. Write a function to calculate the average value of an array of integers

list =[1,2,3,4]
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
print("average value of list is ",sum/len(list))