# probabilities
flipcart = ['printer','laptop','mobile','printer laptop','printer mobile',
            'laptop printer','laptop mobile','printer laptop mobile']
search=str(input('choose product name:'))

# Using not to check if the target is not in the list
# if search in flipcart:
#     print(f'{search} is  in the list')
# else:
#     print(f'{search} is not in the list')  # Should print: 3 is in the list


# Using not to check if the target is not in the list
if not search in flipcart:
    print(f'{search} is not in the list')
else:
    print(f'{search} is in the list')  # Should print: 3 is in the list



