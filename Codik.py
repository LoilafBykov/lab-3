print('Алексей: Привет Виталик даш денег на колу?')
print('Владислав: Сколько?')
while True:
    try:
        i = int(input('Алексей: Всего-то '))
        if i < 100:
            print('Конечно дружище, держи')
        elif i >= 101 and i <= 250:
             print('Владислав: Хорошо, только жду возврата')
        elif i > 251:
             print('Это много денег, поэтому под проценты')
        break
    except ValueError:
                    print('Владислав: говори понятнее')
input()
