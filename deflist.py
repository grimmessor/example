import datetime

GORGEOUS = '720'
SUPER = '480'


class SMS:
    def __init__(self, number, date, kind, card, value, balance):
        self.number = number
        self.date = date
        self.kind = kind
        self.card = card
        self.value = value
        self.balance = balance


def read_file():
    message = 0
    NUMBER = 0
    DATE = 1
    YEAR = 0
    MONTH = 1
    DAY = 2
    s_b = SMS('480', DATE, 2, 4, 5, 8)
    g_b = SMS('720', DATE, 'none', 2, 3, 6)
    messages = []
    with open('smslist.txt', 'r') as f:
        for line in f:
            parts = line.split()
            if parts[NUMBER] == s_b.number:
                date = list(map(int, parts[DATE].split(':')))
                dates = datetime.date(date[YEAR], date[MONTH], date[DAY])
                message = [parts[NUMBER], dates, parts[s_b.kind], parts[s_b.card], parts[s_b.value], parts[s_b.balance]]
            if parts[NUMBER] == g_b.number:
                date = list(map(int, parts[DATE].split(':')))
                dates = datetime.date(date[YEAR], date[MONTH], date[DAY])
                if parts[g_b.value][0] == '+':
                    message = [parts[NUMBER], dates, 'Transfer:', parts[g_b.card], parts[g_b.value], parts[g_b.balance]]
                else:
                    message = [parts[NUMBER], dates, 'Withdrawal:', parts[g_b.card], parts[g_b.value],
                               parts[g_b.balance]]
            messages.append(message)
    messages.sort()
    return messages


def balance(messages):
    BALANCE = 5
    CARD = 3
    cards = []
    last_tr = {}
    balance = {}
    for sms in messages:
        if sms[CARD] not in cards:
            cards.append(sms[CARD])
    i = 0
    count = 0
    while i < len(cards):
        for sms in messages:
            if sms[CARD] == cards[i]:
                count += 1
        last_tr[cards[i]] = count
        i += 1
        count = 0
    i = 0
    count = 0
    while i < len(cards):
        j = 0
        while j < len(messages):
            if cards[i] == messages[j][CARD]:
                count += 1
            if count == last_tr[cards[i]]:
                balance[cards[i]] = messages[j][BALANCE]
                count = 0
            j += 1
        i += 1
    return balance


def expenses(messages, period, card):
    KIND = 2
    VALUE = 4
    DATE = 1
    CARD = 3
    spents = 0
    profits = 0
    year = int(period[0:4])
    month = int(period[5:7])
    for sms in messages:
        if sms[DATE].year == year and sms[DATE].month == month and sms[CARD] == card:
            if sms[KIND] == 'Transfer:':
                profits += int(sms[VALUE])
            if sms[KIND] == 'Withdrawal:':
                if sms[VALUE][0] == '-':
                    spents -= int(sms[VALUE])
                else:
                    spents += int(sms[VALUE])
    delta = profits - spents

    print(f"money spent in a month: {spents}, money get in a month: {profits}, money inequality: {delta}")


a = read_file()
print(a)
