word = input("enter a word:")
x = len(word)
a = ""
while x > 0:
    a = a + word[x-1]
    x = x - 1   
print (a)
    