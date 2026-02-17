def pert(sci, maths, guj):
    return (sci + maths + guj) / 3

# Input for the first student
name = input('Write your name: ')
sci = int(input('Write marks of Science: '))
maths = int(input('Write marks of Maths: '))
guj = int(input('Write marks of Gujarati: '))

# Calculate percentage
jaydeep = pert(sci, maths, guj)

# Check pass/fail status
if sci >= 40 and maths >= 40 and guj >= 40:
    print(f'{name}  your percentage is {jaydeep:.2f}. You are pass.\n')
else:
    print(f'{name}  your percentage is {jaydeep:.2f}. You are fail.\n')

# Input for the second student
name = input('\nWrite your name: ')
sci = int(input('Write marks of Science: '))
maths = int(input('Write marks of Maths: '))
guj = int(input('Write marks of Gujarati: '))

# Calculate percentage
mithilesh = pert(sci, maths, guj)

# Print result
print(f'{name}, your percentage is {mithilesh:.2f}.\n')
