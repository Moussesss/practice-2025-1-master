import tkinter as tk
from tkinter import filedialog, messagebox, font

# Создание главного окна
root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("800x600")

# Функция для открытия файла
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

# Функция для сохранения файла
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

# Функция для изменения шрифта
def change_font(f):
    text_area.configure(font=(f, 12))

# Панель инструментов
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(toolbar, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=2, pady=2)

save_button = tk.Button(toolbar, text="Сохранить", command=save_file)
save_button.pack(side=tk.LEFT, padx=2, pady=2)

# Меню выбора шрифта
font_menu = tk.Menubutton(toolbar, text="Шрифт", relief=tk.RAISED)
font_menu.menu = tk.Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

fonts = ["Courier", "Helvetica", "Times New Roman", "Arial"]
for f in fonts:
    font_menu.menu.add_command(label=f, command=lambda f=f: change_font(f))

font_menu.pack(side=tk.LEFT, padx=2, pady=2)

# Область ввода текста
text_area = tk.Text(root, wrap="word", font=("Courier", 12))
text_area.pack(expand=True, fill="both")

# Запуск приложения
root.mainloop()
ё
