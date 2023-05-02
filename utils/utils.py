import json


def load_data(path):
    """ Загружает данные из файла """

    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
        return data


def set_operation_dates(path):
    """ Возвращает список последних 5-ти дат """

    operations = load_data(path)

    date_list = []

    for operation in operations:
        if len(operation) == 0:
            pass
        elif operation["state"] == "EXECUTED":
            date_in_list = operation["date"]
            date_list.append(date_in_list)
    sorted_list = sorted(date_list)
    last_dates = sorted_list[-5:][::-1]
    return last_dates


def set_last_operations(path):
    """ возвращает список из последних 5-ти операций по дате"""

    operations = load_data(path)
    last_dates = set_operation_dates(path)

    list_operations = []

    for data in last_dates:
        for operation in operations:
            if len(operation) == 0:
                pass
            elif data in operation["date"]:
                list_operations.append(operation)

    return list_operations


def encrypted_account(account):
    """ зашифровывает номер счета/карты """

    list_acc = account.split()

    # это счет
    if len(list_acc) == 2 and len(list_acc[-1]) == 20:
        number = list_acc[-1]
        return f'{list_acc[0]} **{number[-4:]}'

    # это карта
    elif len(list_acc) == 2 and len(list_acc[1]) == 16:
        number = list_acc[1]
        return f'{list_acc[0]} {number[0:4]} {number[4:6]}** **** {number[-4:]}'

    elif len(list_acc) == 3 and len(list_acc[-1]) == 16:
        number = list_acc[-1]
        return f'{list_acc[0]} {list_acc[1]} {number[0:4]} {number[4:6]}** **** {number[-4:]}'









