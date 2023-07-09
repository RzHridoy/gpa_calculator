bengali = int(input('Number in Bengali: '))
english = int(input('Number in English: '))
math = int(input('Number in Math: '))
science = int(input('Number in Science: '))

total_number = bengali + english + math + science
avg_number = total_number / 4

if(avg_number < 0 or avg_number > 100):
    print('Some problems with your inputs')
elif(avg_number <= 100 and avg_number >= 91):
    print(f'You have got A+ grade with {avg_number}% marks')
elif(avg_number == 90 and avg_number >= 81):
    print(f'You have got A grade with {avg_number}% marks')
elif(avg_number == 80 and avg_number >= 71):
    print(f'You have got B grade with {avg_number}% marks')
elif(avg_number == 70 and avg_number >= 61):
    print(f'You have got C grade with {avg_number}% marks')
elif(avg_number == 60 and avg_number >= 41):
    print(f'You have got D grade with {avg_number}% marks')
elif(avg_number <= 40):
    print(f'You have got F grade with {avg_number}% marks')