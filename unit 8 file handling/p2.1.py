fileptr = open("file1.txt","r")

try:
    # Read and print data from the file while it's open
    data = list(fileptr)
    # when we convert 'LIST' not need to use Read() function
    print("Data from file:", data)

finally:
    # The file is not being closed here, so data is still accessible
    print("Data from file again in finally block:", data)


print("Data from file again in finally block:", data)


# ambani=600

# ambani=600+60
# ambani=660+60

# ambani=600
# ambani=ambani+(ambani/10) = #600 + (600/10) =600+60
# ambani=ambani+(ambani/10) #660 +(660/10) =660+66
# ambani=ambani+(ambani/10)


