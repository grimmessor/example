from deflist import read_file, balance, expenses


while True:
    print('1 - Show current funds')
    print('2 - Expenses per month')
    print('3 - Exit')
    print('')
    a = input('Choose an option: ')
    if a not in ['1', '2', '3']:
        print('Ops, something went wrong, please try again')
    else:
        messages = read_file()
    if a == '1':
        balance = balance(messages)
        for key in balance:
            print(f'{key} {balance[key]} EUR')
    if a == '2':
        cards = []
        for sms in messages:
            if sms[3] not in cards:
                cards.append(sms[3])
        i = 1
        for card in cards:
            print(f'{i} - {card}')
            i += 1
        try:
            a = int(input('Choose a card: '))
            if a < 0 or a > i + 1:
                print('Oops, something went wrong, please try again')
        except ValueError:
            print('Ooops, something went wrong, please try again')
            continue
        card = cards[a - 1]
        period = str(input('Enter date in format YYYY-MM: '))
        if len(period) == 7:
            if period[4:5] == '-':
                try:
                    int(period[:4])
                    int(period[5:])
                except ValueError:
                    print('Oooops, something went wrong, please try again')
                if int(period[5:]) > 12 or int(period[5:]) <= 0:
                    print('There only 12 month in year :^)')
                    continue
                e = expenses(messages, period, card)
        else:
            print('Ooooops, something went wrong, please try again')
    else:
        pass








