# 10. Write a function to find the duplicate values of an array
list1=[1,2,1,5,7,2,7]
duplicates = [number for number in list1 if list1.count(number) > 1]
unique_duplicates = list(set(duplicates))

print(unique_duplicates)