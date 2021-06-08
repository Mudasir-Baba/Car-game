car_is_started = False

while True:
    command = input('> ').lower()
    if command == 'start' and car_is_started == False:
        print('Car has been started')
        car_is_started = True

    elif command == 'start' and car_is_started == True:
        print('The car is already started')

    elif command == 'stop' and car_is_started == True:
        print('The car has been stopped')
        car_is_started = False

    elif command == 'stop' and car_is_started == False:
        print('The car has already been stopped')

    elif command == 'quit':
        print('Thanks for playing')
        break
    else:
        print('The is not a valid command')

