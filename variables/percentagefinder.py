def pert(sci, maths, guj):
 if sci >= 40 and sci<=100 and maths >= 40 and maths <=100 and guj >= 40  and  guj<=100:
    peri=(sci + maths + guj) / 3
    return print(f'{name} YOU ARE PASS AND YOU PER IS {peri:.2f}')
 elif sci >= 0 and sci<40 or maths>=0 and maths<40 or guj >= 0  and  guj<40:
    peri=(sci + maths + guj) / 3
    return  print(f'{name} YOU ARE FAIL AND YOU PER IS {peri:.2f}')
 else:
    return print('Invalid marks')


# Input for the first student
name=str(input('Write your name: '))
sci = int(input('Write marks of Science: '))
maths = int(input('Write marks of Maths: '))
guj = int(input('Write marks of Gujarati: '))

# Calculate percentage
jaydeep = pert(sci, maths, guj)

# Input for the second student
name = input('\nWrite your name: ')
sci = int(input('Write marks of Science: '))
maths = int(input('Write marks of Maths: '))
guj = int(input('Write marks of Gujarati: '))

# Calculate percentage
mithilesh = pert(sci, maths, guj)

