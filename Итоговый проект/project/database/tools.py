import sqlite3


class SQLiteTools:

    def __init__(self):
        pass

    def createConnection(self, database_name):
        """ Создать соединение с базой данных """
        self.db = sqlite3.connect(database_name)
        self.cursor = self.db.cursor()

    def selectTableExists(self, table_name):
        """ Определить, существует ли указанная таблица """
        sql = "SELECT * FROM sqlite_master WHERE type = 'table' AND name = '" + table_name + "';"
        self.cursor.execute(sql)

        cur = self.cursor.fetchall()
        return True if cur else False

    def createTable(self, table_name):
        """ Создать общую таблицу """
        sql = "CREATE TABLE IF NOT EXISTS " + table_name + " (id INTEGER PRIMARY KEY AUTOINCREMENT);"
        self.cursor.execute(sql)

        self.db.commit()

    def addColumn(self, table_name, column_name, data_type, other):
        """ Добавить столбцы указанной таблице """
        sql = "ALTER TABLE " + table_name + " ADD " + column_name + " " + data_type + " " + other + ";"
        self.cursor.execute(sql)

        self.db.commit()

    def addRow(self, table_name, row_num):
        """ Добавить строки указанной таблице """
        number = [(i + 1,) for i in range(row_num)]
        sql = "INSERT INTO " + table_name + " (id) VALUES (?);"
        self.cursor.executemany(sql, number)

        self.db.commit()

    def setValue(self, table_name, column, row, value):
        """ Обновить значение указанной позиции в таблице """
        sql = "UPDATE " + table_name + " SET " + column + " = '" + value + "' WHERE id = " + str(row) + ";"
        self.cursor.execute(sql)

        self.db.commit()

    def clearTable(self, table_name):
        """ Очистить указанную таблицу """
        sql = "DELETE FROM " + table_name + ";"
        self.cursor.execute(sql)

        self.db.commit()

    def delTable(self, table_name):
        """ Удалить указанную таблицу """
        sql = "DROP TABLE " + table_name + ";"
        self.cursor.execute(sql)

        self.db.commit()
