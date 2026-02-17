try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print("a / b = %d" % c)

except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Hi, I am the else block")


# finally always run but else run when only there is no error
# finally:
#     print("Hi, I am the else block")
