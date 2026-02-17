# Define the correct password and the user's input
# PASS = 'BCA'
PASS = str(input('ENTER PASS :').upper())
USER = 'AAA'

# List of all 27 possible arrangements
POSSIBILITIES = [
    "AAA", "AAB", "AAC", "ABA", "ABB", "ABC", 
    "ACA", "ACB", "ACC", "BAA", "BAB", "BAC", 
    "BBA", "BBB", "BBC", "BCA", "BCB", "BCC", 
    "CAA", "CAB", "CAC", "CBA", "CBB", "CBC", 
    "CCA", "CCB", "CCC"
]

# Check if the USER's input matches the correct password
for USER in POSSIBILITIES:
    # print(f"Match found: {USER}, breaking out of the loop.")
    if USER == PASS:
        print(f"Match found: {USER}, breaking out of the loop.")
        print(f"PASS AT { POSSIBILITIES.index(USER)+1} TRIES")
        
        break
    
else:
    print(f" {PASS} No match found.")
    print(f"PASS AT {len(POSSIBILITIES)} TRIES")
