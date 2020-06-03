Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def acceptuserinput():
    num = input('Please enter an integer and I will tell you if it is odd or even: ')
    check = input('Please enter an integer by which I can check your number: ')
    if num is not None and int(num) != 0:
        if check is None or len(str(check)) == 0 or int(check) <= 1:
            if int(num) % 2 == 0:
                if int(num) % 4 != 0:
                    print('The number :' + str(num) + ' is an even number but not a multiple of 4')
                else:
                    print('The number :' + str(num) + ' is an even number and is a multiple of 4')
            else:
                print('The number :' + str(num) + ' is an odd number')
        else:
            if int(num) % int(check) == 0:
                print('The number you entered: ' + num + 'gets divided evenly by :' + check)
            else:
                print('The number you entered: ' + num + ' is not divided evenly by :' + check)
    else:
        print('Please provide the first non zero argument for the program to function')

acceptuserinput()