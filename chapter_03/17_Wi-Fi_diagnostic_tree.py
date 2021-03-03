# Wi-Fi Diagnostic Tree

print(' Please reboot your computer and try to connect.')
answer = input('Did that fix the problem? ')
if answer != 'yes':
    print('Reboot your computer and try to connect.')
    answer = input('Did that fix the problem? ')
    if answer != 'yes':
        print('Make sure the cables between the router and modem are '
              'plugged in firmly.')
        answer = input('Did that fix the problem? ')
        if answer != 'yes':
            print('Move the router to a new location and try to connect.')
            answer = input('Did that fix the problem? ')
            if answer != 'yes':
                print('Get a New router.')
