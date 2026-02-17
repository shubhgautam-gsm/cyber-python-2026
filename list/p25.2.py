list=set([1,2,3,'jay',15,'meet'])
list.remove('jay') # throw error
print(list)
list.discard('met') # not throw error
print(list)