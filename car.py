car_is_started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if not car_is_started:
            print('Car has been started...')
            car_is_started = True
        else:
            print('The car has already been staretd!')

    elif command == 'stop':
        if car_is_started:
            print('The car has been stopped...')
            car_is_started = False
        else:
            print('The car has already been stopped')

    elif command == 'quit':
        print('Thanks for playing :)')
        break
    else:
        print('The is not a valid command')

