# 12. Print gender (Male/Female) program according to given M/F using switch

gen =input("enter gender: ")
gen = gen.lower()
if gen =='m':
    print("Male")
elif gen =='f':
    print("Female")
else:
    print("invalid")