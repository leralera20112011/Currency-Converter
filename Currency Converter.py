import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Currency Converter")

# Валюты (пример)
currencies = ['USD', 'EUR', 'RUB']

# Выпадающие списки
from_currency = ttk.Combobox(root, values=currencies)
from_currency.grid(row=0, column=1)
from_currency.set(currencies[0])

to_currency = ttk.Combobox(root, values=currencies)
to_currency.grid(row=1, column=1)
to_currency.set(currencies[1])

# Поле ввода суммы
amount_entry = ttk.Entry(root)
amount_entry.grid(row=2, column=1)

# Кнопка
convert_btn = ttk.Button(root, text="Конвертировать")
convert_btn.grid(row=3, column=1)

# Таблица истории
history = ttk.Treeview(root, columns=('from', 'to', 'amount', 'result'), show='headings')
history.heading('from', text='Из')
history.heading('to', text='В')
history.heading('amount', text='Сумма')
history.heading('result', text='Результат')
history.grid(row=4, column=0, columnspan=2)

root.mainloop()
