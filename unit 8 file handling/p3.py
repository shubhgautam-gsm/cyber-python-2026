# f=open('file1.txt','r')
with open("file1.txt",'r') as f:
 content = f.read()
#  content = list(f)

 print(content)