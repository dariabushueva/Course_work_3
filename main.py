import os
from datetime import datetime
from utils.utils import set_last_operations, encrypted_account

DATA_JSON = os.path.join("data", "operations.json")


def main():

    last_operations = set_last_operations(DATA_JSON)

    for operation in last_operations:

        # дата операции
        date_time = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        unformat_date = date_time.date()
        format_date = unformat_date.strftime('%d.%m.%Y')

        # счет\карта отправителя
        try:
            operation_from = encrypted_account(operation["from"])
        except KeyError:
            operation_from = "Not found"

        # счет\карта получателя
        operation_to = encrypted_account(operation["to"])

        print(f'{format_date} {operation["description"]}\n'
              f'{operation_from} -> {operation_to}\n'
              f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


if __name__ == '__main__':
    main()

