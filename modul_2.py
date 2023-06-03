import sqlite3

class Data:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def additional_data(self):
        # Подключение к базе данных
        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        # Создание таблицы, если её нет
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name text, age integer, gender text)''')

        # Добавление данных в таблицу
        c.execute(f"INSERT INTO users VALUES ('{self.name}', {self.age}, '{self.gender}')")
        rows = c.fetchall()
        for row in rows:
            print(row)
        # Сохранение изменений и закрытие соединения
        conn.commit()
        conn.close()

# Пример использования класса
data = Data('марина', 19, 'женский')
data1=Data('простокол', 79, 'Мужской')
data.additional_data()
data1.additional_data()
