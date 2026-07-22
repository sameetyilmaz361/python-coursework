xfile = open('c:/Users/smtty/OneDrive/Belgeler/bme268/lecture5/example.txt')
file = xfile.read()
total = len(file)
print(f"Total characters: {total}")

first50 = file[:50]
print(f"First 50 characters:\n{first50}")