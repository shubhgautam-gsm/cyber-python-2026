list = ["app", "ban", "man"]

for i in list:
    if i == "ban":
        print("item matched")
        print(i)
        print("found at", list.index(i), "location")
        print("total items is ", list.index(i)+1)
        break

