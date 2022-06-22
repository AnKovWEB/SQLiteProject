import tkinter as tk
from database.tools import SQLiteTools
import tkinter.ttk as ttk
from tkinter import *
import os


class SQLiteTest:

    def __init__(self):
        self.database_file = "database.db"
        self.table_name = "Trade"
        self.number_of_columns = 0
        self.column_list = []
        if os.path.exists(self.database_file):
            os.remove(self.database_file)
        self.sqlite = SQLiteTools()
        self.sqlite.createConnection(self.database_file)

    def createTable(self):
        """ Создание таблицы """
        if not self.sqlite.selectTableExists(self.table_name):
            self.sqlite.createTable(self.table_name)

    def addColumn(self):
        """ Создание поля """

        def addColumnInner():
            def closeButton():
                a.destroy()

            def clearFunc():
                self.get_column = name_entry_1.get()
                self.column_list.append(self.get_column)

                name_entry_1.delete(0, END)
                name_entry_3.delete(0, END)

            a = Toplevel()
            a.geometry('250x200')
            a.title("Создание поля")
            a.resizable(False, False)

            name_1 = StringVar()
            name_3 = StringVar()

            name_label_1 = Label(a, text="Столбец:")
            name_label_1.place(x=10, y=10, width=110, height=30)
            name_label_2 = Label(a, text="Тип данных:")
            name_label_2.place(x=10, y=60, width=110, height=30)
            name_label_3 = Label(a, text="Доп. параметры:")
            name_label_3.place(x=10, y=110, width=110, height=30)

            name_entry_1 = Entry(a, textvariable=name_1)
            name_entry_1.place(x=130, y=10, width=110, height=30)
            combobox = ttk.Combobox(a, values=[u'integer',
                                               u'real',
                                               u'text',
                                               u'blob'])
            combobox.current(2)
            combobox.place(x=130, y=60, width=110, height=30)
            name_entry_3 = Entry(a, textvariable=name_3)
            name_entry_3.place(x=130, y=110, width=110, height=30)

            message_button = Button(a, text="Добавить", command=lambda:
                                    (self.sqlite.addColumn(self.table_name,
                                                           name_1.get(),
                                                           combobox.get(),
                                                           name_3.get()),
                                     clearFunc()))
            message_button.place(x=10, y=160, width=100, height=30)

            message_button = Button(a, text="Закрыть окно",
                                    command=closeButton)
            message_button.place(x=140, y=160, width=100, height=30)

        name_label = Label(root, text="<----- Основные функции ----->")
        name_label.place(x=100, y=10, width=300, height=30)

        name_label_header_button = Button(text="Добавить поле",
                                          command=addColumnInner)
        name_label_header_button.place(x=20, y=50, width=125, height=35)

    def addRow(self):
        """ Создание строк(количества) """

        def blockFunc():
            name_label_header['state'] = 'disabled'

        def addRowInner():
            def blockFuncInner():
                message_button['state'] = 'disabled'

            def closeFunc():
                b.destroy()

            def columnID():
                self.number_of_columns = name_entry.get()

            b = Toplevel()
            b.geometry('250x200')
            b.title("Создание строк")
            b.resizable(False, False)

            name = StringVar()

            name_label = Label(b, text="Кол-во строк:")
            name_label.place(x=10, y=10, width=110, height=30)

            name_entry = Entry(b, textvariable=name)
            name_entry.place(x=130, y=10, width=110, height=30)

            message_button = Button(b, text="Добавить", command=lambda:
                                    (columnID(), blockFuncInner(),
                                     self.sqlite.addRow(self.table_name,
                                                        int(name.get()))))
            message_button.place(x=10, y=160, width=100, height=30)

            message_button_closure = Button(b, text="Закрыть окно",
                                            command=closeFunc)
            message_button_closure.place(x=140, y=160, width=100, height=30)

        name_label_header = Button(text="Добавить строки", command=lambda:
                                   (addRowInner(), blockFunc()))
        name_label_header.place(x=185, y=50, width=125, height=35)

    def setValue(self):
        """ Заполнение записи """

        def setValueInner():
            def closeFunc():
                c.destroy()

            def cleareFunc():
                name_entry_3.delete(0, END)

            c = Toplevel()
            c.geometry('250x200')
            c.title("Ввод данных")
            c.resizable(False, False)

            name_3 = StringVar()

            name_label_1 = Label(c, text="Столбец:")
            name_label_1.place(x=10, y=10, width=110, height=30)
            name_label_2 = Label(c, text="ID:")
            name_label_2.place(x=10, y=60, width=110, height=30)
            name_label_3 = Label(c, text="Текст:")
            name_label_3.place(x=10, y=120, width=110, height=30)

            row_list = [str(i) for i in range(1, int(self.number_of_columns)+1)]

            combobox_1 = ttk.Combobox(c, values=self.column_list)
            combobox_1.current(0)
            combobox_1.place(x=130, y=10, width=110, height=30)
            combobox_2 = ttk.Combobox(c, values=row_list)
            combobox_2.current(0)
            combobox_2.place(x=130, y=60, width=110, height=30)
            name_entry_3 = Entry(c, textvariable=name_3)
            name_entry_3.place(x=130, y=110, width=110, height=30)

            message_button = Button(c, text="Добавить", command=lambda:
                                    (self.sqlite.setValue(
                                        self.table_name,
                                        combobox_1.get(),
                                        combobox_2.get(),
                                        name_3.get()),
                                     cleareFunc()))
            message_button.place(x=10, y=160, width=100, height=30)

            message_button = Button(c, text="Закрыть окно",
                                    command=closeFunc)
            message_button.place(x=140, y=160, width=100, height=30)

        name_label_header_button = Button(text="Добавить значение",
                                          command=setValueInner)
        name_label_header_button.place(x=350, y=50, width=125, height=35)

    def clearTable(self):
        """ Очистка таблицы """
        name_label = Label(root, text="<----- Прочие функции ----->")
        name_label.place(x=100, y=100, width=300, height=30)

        message_button = Button(text="Очистить таблицу", command=lambda:
                                self.sqlite.clearTable(self.table_name))
        message_button.place(x=80, y=140, width=125, height=35)

    def delTable(self):
        """ Удаление таблицы """
        message_button = Button(text="Удалить таблицу", command=lambda:
                                self.sqlite.delTable(self.table_name))
        message_button.place(x=290, y=140, width=125, height=35)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x200')
    root.title("Менеджер баз данных")
    root.resizable(False, False)

    win = SQLiteTest()  # Соединение
    win.createTable()  # Создать таблицу

    win.addColumn()  # Создание поля
    win.addRow()  # Создание строк
    win.setValue()  # Заполнение данными
    win.clearTable()  # Очистка таблицы
    win.delTable()  # Удаление таблицы

    root.mainloop()
