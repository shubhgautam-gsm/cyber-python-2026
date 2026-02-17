import os
fd = "movies.txt"
# popen() is similar to open()
# file = open(fd, 'w')
# file.write("This is awesome")
# file.close()
# file = open(fd, 'r')
# text = file.read()
# print(text)
# popen() provides gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("This is awesome RRR")
# File not closed, shown in next function.


# new file create and write and open that file (popen)