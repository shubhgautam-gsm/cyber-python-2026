# the pop() method 
# will always remove the last item but the set is unordered, we can't determine which 
# element will be popped from set
YoutubePremiumUsers = ["jay","meet", "ram", "shayam", "jeet", "jiya"]


# 1 dec  1 jan  dec-jan   monthcomplete=dec-jan 31-31 ans 0
# monthcomplete==0
# username can change in insta after more than 14 days 
for user in YoutubePremiumUsers:
 time=int(input("Time"))
 if(time>30): 
    YoutubePremiumUsers.pop()

print(YoutubePremiumUsers)

print("\nPrinting the modified set...")
