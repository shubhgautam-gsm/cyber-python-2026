try:
    a =float(input("Enter a: ")) #4
    b = float(input("Enter b: ")) #'5'
    c = a / b
    print("a / b = %f" % c)

except Exception as e:
    print(e)
else:
    print("Hi, I am the else block")
