import tkinter as tk

def check_entry():
    entered_text = entry.get()
    if entered_text.lower() == "car":
        result_label.config(text="Вы выбрали машину")
        print("Вы выбрали машину")
    else:
        result_label.config(text="Вы выбрали что-то другое")
        print("Вы выбрали что-то другое")

# Главное окно
win = tk.Tk()
win.title("Выбор")
win.geometry("400x400")

# Поле ввода
entry = tk.Entry(win)
entry.pack(pady=10)

# Кнопка
button = tk.Button(win, text="Проверить", command=check_entry)
button.pack(pady=10)

# Label
result_label = tk.Label(win, text="")
result_label.pack(pady=10)

# Старт
win.mainloop()
