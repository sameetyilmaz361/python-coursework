handle = open('c:/Users/smtty/OneDrive/Belgeler/bme268/lecture5/mails.txt')
for line in handle:
    line = line.rstrip()
    if not '@' in line:
        continue
    print(line)

    