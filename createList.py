from toNumber import to_number

def create_list() -> list:
    list = []

    print('Вводите числа для списка (чтобы прекратить напишите "!"): ')
    
    user_answer = ""
    while True:
        user_answer = input()

        if (user_answer == "!"):
            break

        number = to_number(user_answer)
        list.append(number)

    print("Список сформирован: ")
    print(*list)

    return list