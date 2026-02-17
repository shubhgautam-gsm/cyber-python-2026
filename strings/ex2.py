str='imgs/nature world.jpg'
#print (str.lstrip('imgs/'))
#print (str.rstrip('.jpg'))
#print('finally\n')

# method 1
# store=str.lstrip('imgs/')
# store2=store.rstrip('.jpg')

# method 2
str=str.lstrip('imgs/') #overide imgs/nature world.jpg override natures world.jpg
str=str.rstrip('.jpg') #overide nature world.jpg override natures world 
# need to use from first or from last
print(str)


# ***important using this method no need to store title instead titles get from 'img urls' ***