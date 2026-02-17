

# characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}|;:,.<>?/`~"
# char=0-9a-zA-Z{sp}
# 8-16
# 3 attempts
user_pass="bca"

list_pss=["abc","bac","acb","bca","cba","cab"]


for avin in list_pss:
    print("try ",list_pss.index(avin)+1," ",avin)
    if avin==user_pass:
        print("Password is crack password is",avin," possible at try ",list_pss.index(avin)+1)
        break