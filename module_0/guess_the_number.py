import random
import numpy as np


# Функция входа
def main():
    number = random.randint(0, 100)
    print("Загадали число {}, отгадали за попыток {}".format(number, guess_number(number)))
    print("Загадали число {}, отгадали за попыток {} (рекурсия)".format(number, guess_number_recursion(number)))


# Функция нахождения числа O(logn)
def guess_number(number, tries=0, start=0, stop=100):
    while True:
        current_number = (stop + start) // 2
        tries += 1
        if current_number == number:
            break
        elif current_number > number:
            stop = current_number
        else:
            start = current_number

    return tries


# Функция нахождения числа рекурсия O(logn)
def guess_number_recursion(number, tries=0, start=0, stop=100):
        current_number = (stop + start) // 2
        tries += 1
        if current_number == number:
            return tries
        elif current_number > number:
            return guess_number_recursion(number, tries, start, current_number)
        else:
            return guess_number_recursion(number, tries, current_number, stop)


# Функция теста алгоритма
def score_game(game_core_v1):
    """Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print("Ваш алгоритм угадывает число в среднем за {} попыток".format(score))

    return(score)


if __name__ == '__main__':
    main()
    score_game(guess_number_recursion)

