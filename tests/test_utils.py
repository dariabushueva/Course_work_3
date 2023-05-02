from utils import utils
import pytest


def test_set_operation_dates():
    assert utils.set_operation_dates("data/operations.json") == ['2019-12-08T22:46:21.935582',
                                                                 '2019-12-07T06:17:14.634890',
                                                                 '2019-11-19T09:22:25.899614',
                                                                 '2019-11-13T17:38:04.800051',
                                                                 '2019-11-05T12:04:13.781725']


def test_set_last_operations():
    assert utils.set_last_operations("data/operations.json") == [{"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582", "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}}, "description": "Открытие вклада", "to": "Счет 90424923579946435907"},
                                                                 {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'},
                                                                 {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
                                                                 {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'},
                                                                 {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
                                                                 ]


@pytest.mark.parametrize('account_number, encrypted_account', [
                        ('Счет 90562872508279542248', 'Счет **2248'),
                        ('Visa Classic 2842878893689012', 'Visa Classic 2842 87** **** 9012'),
                        ('Maestro 7810846596785568', 'Maestro 7810 84** **** 5568'),
                        ('Счет 38611439522855669794', 'Счет **9794'),
                        ('Счет 48943806953649539453', 'Счет **9453'),
                        ('Visa Gold 7756673469642839', 'Visa Gold 7756 67** **** 2839')
                        ])
def test_encrypted_account(account_number, encrypted_account):
    assert utils.encrypted_account(account_number) == encrypted_account


