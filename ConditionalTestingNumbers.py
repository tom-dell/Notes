numbers = [1, 2, 3]

num = int(input('enter a number '))

if num in numbers:
    print('in list')
elif num < 10:
    print('you are close')
else:
    print('number not in list, you are way off')
