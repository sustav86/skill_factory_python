import random


# Функция входа
def main():
    number = random.randint(0, 100)
    print("Загадали число {}, отгадали за попыток {}".format(number, guess_number(number)))


# Функция нахождения числа O(logn)
def guess_number(number, tries=0, start=0, stop=100):
    while True:
        current_number = (stop + start) // 2
        tries += 1
        if current_number == number:
            break
        elif current_number > number:
            stop = current_number;
        else:
            start = current_number

    return tries


if __name__ == '__main__':
    main()
