print('Car game........')
print('''Command for game
start -> start the Car
stop -> stop the Car''')
command = ""
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car Started')
    elif command == 'stop':
        if not started:
            print('Car is already stoped')
        else:
            started = False
            print('Car Stoped')
    elif command == 'quit':
        print('game over')
        break
    else:
        print('Command not found')
