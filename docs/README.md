# 2.Вариативная часть задания 
Выбор тематики. Мной была выбрана тема – «Создание простого текстового редактора на Python с использованием Tkinter».
# 📝 Проект: Простой текстовый редактор на Python с Tkinter

## 📌 Цель проекта
Разработка простого текстового редактора с графическим интерфейсом на языке Python с использованием библиотеки Tkinter, обеспечивающего базовые функции работы с текстом: ввод, редактирование, сохранение, открытие файлов и изменение шрифта.

## 📌 Задачи проекта
- Изучить возможности библиотеки Tkinter для создания графического интерфейса.
- Разработать главное окно приложения с элементами управления.
- Реализовать текстовое поле для ввода и редактирования текста.
- Добавить функциональность сохранения текста в файл.
- Реализовать возможность открытия существующих текстовых файлов.
- Внедрить меню для выбора шрифта текста (например, Courier и Helvetica).
- Обеспечить взаимодействие с файловой системой через диалоговые окна открытия и сохранения файлов.
- Провести тестирование программы на корректность работы всех функций.


## 🔍 Исследование и разработка

### 1. Выбор тематики

Была выбрана тема: **«Создание простого текстового редактора на Python с использованием Tkinter»** — лёгкий старт в разработке GUI-приложений.

### 2. Стек технологий

| Компонент       | Выбор                   |
|-----------------|-------------------------|
| Язык            | Python                  |
| GUI-библиотека  | Tkinter (встроенная)    |
| Графика         | Draw.io / Mermaid (диаграммы) |

---

### 3. Изучение технологии
Мной был изучен сайт и видеоурок из репозитория, а также изучено руководство по Tkinter.
Создан основной файл: `text_editor.py`, в котором реализованы:
- Главное окно (`Tk()`)
- Виджет `Text` для отображения текста
- Кнопки "Сохранить", "Открыть"
- Меню для изменения шрифта (Courier, Helvetica)
- Диалоги работы с файлами через `tkinter.filedialog`

---

## 🛠 Техническое руководство

### Необходимое ПО

- Python 3.x (https://python.org)
- Tkinter (включён в стандартную библиотеку Python)

---

### 🔧 Шаг 1: Импорт библиотек и создание окна

```python
import sys

if sys.version_info[0] == 2:
    from Tkinter import *
    import tkFileDialog
else:
    from tkinter import *
    import tkinter.filedialog as tkFileDialog

root = Tk()
root.title("Простой текстовый редактор")
```
### 🔧 Шаг 2: Добавление текстового поля
```python
text = Text(root)
text.grid()
```

### 🔧 Шаг 3: Кнопка сохранения текста
```python
def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = tkFileDialog.asksaveasfilename()
    with open(save_location, "w+") as file1:
        file1.write(t)

button = Button(root, text="Сохранить", command=save_as)
button.grid()
```
### 🔧 Шаг 4: Кнопка открытия файла
```python
def open_file():
    file_path = tkFileDialog.askopenfilename()
    with open(file_path, "r") as file:
        content = file.read()
        text.delete("1.0", END)
        text.insert(INSERT, content)

open_button = Button(root, text="Открыть", command=open_file)
open_button.grid()
```

### 🔧 Шаг 5: Меню выбора шрифта
```python
def set_font_helvetica():
    global text
    text.config(font="Helvetica")

def set_font_courier():
    global text
    text.config(font="Courier")

font_menu = Menubutton(root, text="Шрифт")
font_menu.grid()
font_menu.menu = Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

helvetica_var = IntVar()
courier_var = IntVar()

font_menu.menu.add_checkbutton(label="Courier", variable=courier_var, command=set_font_courier)
font_menu.menu.add_checkbutton(label="Helvetica", variable=helvetica_var, command=set_font_helvetica)
```
### 🔧 Шаг 6: Модификация — добавление функции открытия существующих файлов
```python
def open_file():
    file_path = tkFileDialog.askopenfilename()
    with open(file_path, "r") as file:
        content = file.read()
        text.delete("1.0", END)
        text.insert(INSERT, content)

open_button = Button(root, text="Открыть", command=open_file)
open_button.grid()
```
### 💻 Код
![Снимок экрана (996)](https://github.com/user-attachments/assets/e747a59a-2556-4b7e-920c-5e7acfc6fb01)

### 💻 Окно текстового редактора
![Снимок экрана (992)](https://github.com/user-attachments/assets/92b34183-8a0a-4cb2-b189-dce45803ff5a)

### 💻 Окно текстового редактора с введённым текстом 
![Снимок экрана (993)](https://github.com/user-attachments/assets/912ca322-b2cf-47de-8780-dbf6e6183838)

### 💻 Выбор шрифта 
![Снимок экрана (994)](https://github.com/user-attachments/assets/1e0014b5-7027-4acc-9fba-35a1f9fa67ad)

### 💻 Отрыть файл 
![Снимок экрана (995)](https://github.com/user-attachments/assets/032f5e62-97f5-426c-9b74-58ba40edf7d3)

### ✍ Подведение итогов и вывод
В рамках данного проекта была успешно реализована цель — создание простого текстового редактора с графическим интерфейсом, позволяющего пользователю вводить, редактировать и сохранять текст, а также изменять его шрифт. Для реализации проекта был выбран язык программирования Python и библиотека Tkinter, что обеспечило простоту разработки и возможность запуска на разных операционных системах. 

Вывод: Проект позволил на практике освоить принципы построения GUI-приложений и модульного программирования в Python. Разработанное приложение можно использовать как основу для дальнейшего расширения — добавления новых функций, работы с форматированием текста, изменением цвета, поддержкой разных кодировок и других улучшений. Таким образом, поставленные задачи выполнены в полном объеме.

### Список литературы
1.	Метанит. Tkinter – создание графических интерфейсов на Python [Электронный ресурс]. – Режим доступа: https://metanit.com/python/tkinter/ (дата обращения: 05.05.2025).
2.	Create a Simple Python Text Editor [Электронный ресурс] // Instructables. – Режим доступа: https://www.instructables.com/Create-a-Simple-Python-Text-Editor/ (дата обращения: 05.05.2025).
3.	Python GUI Text Editor With Tkinter [Видеоресурс] / YouTube, канал Codemy.com. – URL: https://www.youtube.com/watch?v=xqDonHEYPgA (дата обращения: 05.05.2025).
4.	https://online.mospolytech.ru/course/view.php?id=15065
5.	https://sky.pro/wiki/html/osnovy-html-struktura-html-dokumenta/
