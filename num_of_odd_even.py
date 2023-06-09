# 15. Write a method to find number of even number and odd numbers in an array
l1=[45,78,76,63,90]
o,e=0,0
for i in range(0,len(l1)):
    if l1[i]%2==0:
        e=e+1
    else:
        o=o+1
print("number of odd numbers in list is ",o)
print("number of even numbers in list is ",e)
