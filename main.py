def select_problem():
    while(True):
        print('Выберите задачу: \n1. Конвертор dec -> hex\n'
              '2. Сложение-умножение неправильных дробей)')
        try:
            user_choice = user_input_number('соответствующее номеру задания ')
            user_choice = int(user_choice)
            match user_choice:
                case 1:
                    dec_to_hex_convert()
                    break
                case 2:
                    fractions_calculation()
                    break
                case _:
                    print('Введите корректный номер задачи')
                    continue
        except ValueError:
            print('Введите корректный номер задачи')


def dec_to_hex_convert():
    hex_digits = '0123456789ABCDEF'
    result = ''
    while True:
        try:
            user_num = user_input_number('десятичное ')
            user_num = int(user_num)
            break
        except ValueError:
            print('Введите целое число')
    original_num = user_num
    user_num = abs(user_num)
    while user_num:
        result = hex_digits[user_num % 16] + result
        user_num //= 16
    if original_num > 0:
        print(f'dec: {original_num} --> hex: 0x{result}')
    elif original_num == 0:
        print(f'dec: {original_num} --> hex: 0x0')
    else:
        print(f'dec: {original_num} --> hex: -0x{result}')


def fractions_calculation():
    print('Введите дробное число в формате "a/b"')
    num1 = user_input_fractions('первое ')
    num2 = user_input_fractions('второе ')
    lcm = lcm_usr(num1[1], num2[1])
    sum = ((lcm / num1[1] * num1[0] + lcm / num2[1] * num2[0]), (lcm))
    product = (num1[0] * num2[0], num1[1] * num2[1])
    result_sum = f'{num1[0]}/{num1[1]} + {num2[0]}/{num2[1]} = {int(sum[0] / gcd_usr(sum[0], sum[1]))}'\
                f'/{int(sum[1] / gcd_usr(sum[0], sum[1]))}'
    result_product = f'{num1[0]}/{num1[1]} * {num2[0]}/{num2[1]} = {int(product[0] / gcd_usr(product[0], product[1]))}'\
                f'/{int(product[1] / gcd_usr(product[0], product[1]))}'
    print(f'{result_sum} \n{result_product}')


def gcd_usr(a, b):
    a = abs(a)
    b = abs(b)
    if a >= b:
        greater = a
        lesser = b
    else:
        greater = b
        lesser = a
    remainder = greater % lesser
    while remainder != 0:
        greater = lesser
        lesser = remainder
        remainder = greater % lesser
    return lesser


def lcm_usr(a, b):
    return int(abs(a * b) / gcd_usr(a, b))


def user_input_fractions(message):
    while True:
        user_input = input(f'Введите {message}число:\n')
        user_rat_num = user_input.split('/')
        if len(user_rat_num) > 2:
            continue
        elif len(user_rat_num) == 1:
            if user_rat_num[0] == '':
                continue
            else:
                user_rat_num.append(1)
        try:
            user_rat_num[0], user_rat_num[1] = int(user_rat_num[0]), int(user_rat_num[1])
        except ValueError:
            print('Введите корректное число')
            continue
        try:
            1 / user_rat_num[0]
            1 / user_rat_num[1]
            break
        except ZeroDivisionError:
            print('Знаменатель не может быть нулём. Введите корректное число')

    return tuple(user_rat_num)


def user_input_number(message):
    user_number = input(f'Введите {message}число:\n')
    return user_number


select_problem()