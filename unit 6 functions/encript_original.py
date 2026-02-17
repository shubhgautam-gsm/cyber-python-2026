# characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}|;:,.<>?/`~"
# char=0-9a-zA-Z{sp}


# user_message="iant3434"
user_message=input('Enter your message: ')  



user_message=user_message.replace('i', 'x$%^')
user_message=user_message.replace('a', 'm#^^$$')
user_message=user_message.replace('n', '#@@@@')

# encript
print('my bank account number is 1234567890 and pass is ',user_message)

# DARSHIL WHATSAPP DECRIPT CODE
user_message=user_message.replace( 'x$%^', 'i')
user_message=user_message.replace('m#^^$$', 'a')
user_message=user_message.replace('#@@@@', 'n')

# decript
print('my bank account number is 1234567890 and pass is ',user_message)