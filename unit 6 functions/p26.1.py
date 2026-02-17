x= 'a=3\nb=4\nprint(a+b)'
file=compile(x,'p1.py','exec')
exec(file)
# print(file)