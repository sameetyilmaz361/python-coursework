handle = open('c:/Users/smtty/OneDrive/Belgeler/bme268/lecture5/mails.txt')
count = 0
for line in handle:
    if line.startswith('From:'):
        count = count + 1
        print(line)
print('Total mails found:', count)