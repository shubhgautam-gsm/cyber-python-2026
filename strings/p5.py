flipcart=['iphone', 'ipad', 'mobile','laptop']
user=str(input('write product name '))

if user in flipcart:
 print(f'yes product {user} in flipcart at location {flipcart.index(user)+1}')
else:
 print(f'no product {user} not in flipcart ')

#another way to solve this problem
