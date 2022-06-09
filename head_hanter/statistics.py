import sqlite3


class Statistics:

    def __init__(self):
        self.stat = {}
        try:
            conn = sqlite3.connect('hh.db')
            cursor = conn.cursor()
            sqlite_create_table_query = '''CREATE TABLE HH (
                id          INTEGER      PRIMARY KEY AUTOINCREMENT,
                requirement TEXT         (32)
                );'''
            print("База данных подключена к SQLite")
            cursor.execute(sqlite_create_table_query)
            conn.commit()
            print("Таблица SQLite создана")
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (conn):
                conn.close()
                print("Соединение с SQLite закрыто")

    def find(self, requirement):
        try:
            conn = sqlite3.connect('hh.db')
            cursor = conn.cursor()
            # print("База данных подключена к SQLite")
            for item in requirement:
                cursor.execute(f"INSERT INTO HH VALUES (NULL, '{item['name']}');")
                if item['name'] in self.stat:
                    self.stat[item['name']] += 1
                else:
                    self.stat[item['name']] = 1
            conn.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite: ", error)
        finally:
            if (conn):
                conn.close()
                # print("Соединение с SQLite закрыто")
        return 0

    def get_stat(self):
        sorted_list = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        short_list = []
        for i in range(len(sorted_list)):
            if sorted_list[i][1] > 1:
                short_list.append(sorted_list[i])
            else:
                break
        sorted_tuple = tuple(short_list)
        return sorted_tuple
