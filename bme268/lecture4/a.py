str1= input("enter a word:")
str2= input ("enter a character:")
index=0
count=0
while index < len(str1):
    if str1[index]==str2:
        print (index)
        count += 1
    index = index +1
if count == 0:
    print ("not found")
else:
    print ("found", count, "times")