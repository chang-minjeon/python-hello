import os
f = open("./files/1.txt", 'r')
data = f.read()
f.close()

data = data.replace('12', '1200')

f = open('./files/2.txt', 'w')
f.write(data)
f.close()