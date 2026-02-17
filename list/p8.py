list1=[1,2,3]
list=['ram','shyam','jay','rakesh']
# Products=({"proname":"shoes","id":"1"},{"proname":"laptop","id":"2"})
Products=[{
   "proname":"shoes",
   "id":"1"
   }
    ,{
   "proname":"laptop",
   "id":"2"
   }]

# dropdown

# product_list ={'cat':'shoes','name':'reebok','price':'2000rs'} 
# product_list ={'cat':'shoes','name':'nike','price':'1000rs'} 

# product = {
#    "proname":"shoes",
#    "id":"1"
#    }
# product =  {
#    "proname":"laptop",
#    "id":"2"
#    }  overiding so show all products and their associated keys


for product in Products:print(product)
for product in Products:print(product['proname'])

for i in list:print(i)

print(len(list))
print(len(list1))


list1=[1,2,3]
list=['ram','shyam','jay','rakesh']


# for i in list[int(input('give index 1:')):int(input('give index 2 :'))]:
#     print(i)
