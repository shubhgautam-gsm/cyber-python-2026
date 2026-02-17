# characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}|;:,.<>?/`~"
# char=0-9a-zA-Z{sp}
# 8-16
# 3 attempt
# 3 raise 8-16 1lakh  

priya_pass="bca"

list_pss=["abc","bac","acb","bca","cba","cab"]

# for foram in range(0,99999): list_pss[foram]
for foram in list_pss:
    print("try ",list_pss.index(foram)+1," ",foram)
    
    if foram==priya_pass:
        print("Password is crack password is",foram," possible at try ",list_pss.index(foram)+1)
        break