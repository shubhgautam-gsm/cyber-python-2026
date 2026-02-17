list = ["app", "ban", "man"]
count = 1
ind = 0
for i in list:
    if i == "man":
        print("item matched\n")
        print(i)
        print("found at", count, "location as per Value")
        print("found at", ind, "location as per Index")
        break
    count += 1
    ind += 1
