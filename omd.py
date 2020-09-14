def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Сколько бокалов вина выпьем?'
    )
    option = -1
    options_min = 1
    options_max = 10
    while not (options_min <= option <= options_max):
        print('Введите количество от {} до {}'.format(options_min, options_max))
        option = int(input())
    
    if option < 3:
        return step3_umbrella_less()
    return step3_umbrella_more()
    
    
def step2_no_umbrella():
    print(
        'Вся краска растеклась :( '
        'Продолжить путь?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step3_no_umbrella_bar()
    return step3_no_umbrella_home()
    
    
def step3_umbrella_less():
    print(
        'Бар - неплохое место для новых знакомств! '
        'Концовка 1 из 4'
    )
    again()
    return

def step3_umbrella_more():
    print(
        'Завтра будет тяжёлое утро. '
        'Концовка 2 из 4'
    )
    again()
    return

    
def step3_no_umbrella_bar():
    print(
        'Утка-маляр напилась с горя. '
        'Концовка 3 из 4'
    )
    again()
    return
    

def step3_no_umbrella_home():
    print(
        'Единственный безалкогольный исход. '
        'Концовка 4 из 4'
    )
    again()
    return
    
def again():
    print('Начать заново?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step1();
    return


if __name__ == '__main__':
    step1()