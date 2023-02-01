#Саутов Султан 3 курс Computer Science
#2 лабораторная работа

from time import sleep


def game(chislo: int) -> None:

    '''Это текстовая игра "угадайка"'''

    variants = [i for i in range(1, 101)]
    try_counter = 0

    sleep(0.3)

    low = 0
    high = 99

    while True:


        mid = (low + high) // 2
        guess = variants[mid]

        if guess > chislo:
            high = mid - 1
        else:
            low = mid + 1

        print(f'ваше число: {guess}?')
        try_counter += 1

        ans = input('угадал ли число?: y/n -> ').lower()
        if ans == 'y':
            print('супер!')
            print(f'всего потребовалось {try_counter} попыток.')
            break
        else:
            print('окей...')


if __name__ == '__main__':
    digit = int(input('загадай число от 1 до 100... -> '))
    game(digit)
