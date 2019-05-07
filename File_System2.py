import os

print('Finding my OS', os.name)

if (os.path.isfile('news.txt')):
    inoutfile = open('news.txt' , 'r', encoding="UTF8")
    
    for line in inoutfile:
        print(line.rstrip())
        inoutfile.close()