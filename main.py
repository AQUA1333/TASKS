import datetime

class Client:
    def __init__(self, full_name, client_id, status, contacts, age):
        if age < 18:
            raise ValueError("Клиент должен быть совершеннолетним (18+)")

        self.full_name = full_name
        self.client_id = client_id
        self.status = status
        self.contacts = contacts
        self.accounts = []
        self.failed_attempts = 0
        self.is_blocked = False


class Bank:
    def __init__(self):
        self.clients = {}

    def add_client(self, client):
        self.clients[client.client_id] = client
        print(f"Клиент {client.full_name} успешно добавлен.")

    def authenticate_client(self, client_id):
        client = self.clients.get(client_id)
        if not client:
            print("Клиент не найден.")
            return False

        if client.is_blocked:
            print("Доступ запрещен: аккаунт заблокирован.")
            return False

        now = datetime.datetime.now().hour
        if 0 <= now < 5:
            print("Вход в систему запрещен в ночное время (00:00 - 05:00).")
            return False

        password = input(f"Введите пароль для {client.full_name}: ")
        if password == "1234":
            client.failed_attempts = 0
            print("Успешный вход.")
            return True
        else:
            client.failed_attempts += 1
            print(f"Неверный пароль! Попыток: {client.failed_attempts}")
            if client.failed_attempts >= 3:
                client.is_blocked = True
                print("Аккаунт заблокирован из-за превышения попыток входа.")
            return False

    def open_account(self, client_id, account_number):
        if client_id in self.clients:
            self.clients[client_id].accounts.append(account_number)
            print(f"Счет {account_number} открыт для ID {client_id}.")

    def process_transaction(self, amount):
        if amount > 100000:
            print(f"ВНИМАНИЕ: Операция на сумму {amount} помечена как подозрительная!")
        else:
            print(f"Операция на сумму {amount} выполнена успешно.")

my_bank = Bank()

try:
    c1 = Client("Иван Иванов", "ID001", "Active", "ivan@mail.com", 25)
    my_bank.add_client(c1)
except ValueError as e:
    print(e)

my_bank.open_account("ID001", "ACC-777")

for _ in range(3):
    my_bank.authenticate_client("ID001")

my_bank.process_transaction(150000)