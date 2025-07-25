import pyautogui
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import keyboard


def send_message():
    try:
        x = int(entry.get())
        message = entry2.get()
        iterations = int(entry1.get())
        k = int(entry3.get())

        for j in range(x):
            if keyboard.is_pressed('esc'):
                st.config(state='normal')
                st.insert(END, "Атака остановлена по ESC!\n")
                st.see(END)
                st.config(state='disabled')
                return

            x -= 1
            st.config(state='normal')
            st.insert(END, f"{x} - секунд до начала\n")
            st.see(END)
            st.config(state='disabled')
            root.update()
            time.sleep(1)

        st.config(state='normal')
        st.insert(END, "Начало атаки\n")
        st.see(END)
        st.config(state='disabled')
        root.update()

        time.sleep(0.01)

        for i in range(iterations):
            if keyboard.is_pressed('esc'):
                st.config(state='normal')
                st.insert(END, "Атака остановлена по ESC!\n")
                st.see(END)
                st.config(state='disabled')
                return

            pyautogui.typewrite(message)
            pyautogui.press('enter')

            st.config(state='normal')
            st.insert(END, f"Отправлено {i + 1}/{iterations}\n")
            st.see(END)
            st.config(state='disabled')
            root.update()

            time.sleep(k)

        st.config(state='normal')
        st.insert(END, "Вся обойма попала в нашу жертву!\n")
        st.see(END)
        st.config(state='disabled')

    except ValueError as e:
        st.config(state='normal', foreground='red')
        st.insert(END, f"Ошибка - {e}\n")
        st.see(END)
        st.config(state='disabled', foreground='#00FF00')


root = tk.Tk()
root.geometry('700x920')
root.title('Spam-Bot (Version - 2.0)')
root.configure(bg='black')
root.resizable(False, False)

heading = tk.Label(text="Spam-Bot (Version - 2.0)", font=("Arial", 20, "bold"), background="black",
                   foreground="#00FF00", width=50, height=1)
heading1 = tk.Label(text="Программа для спама сообщениями", font=("Arial", 15), background="black",
                    foreground="#00FF00", width=100, height=2)
heading2 = tk.Label(
    text="\nУстанавливайте нужные значения в полях для ввода (рекомендуется) по-больше времени \n поставить в начале таймера перед начало времени), нажимаете кнопку 'Начать' и\n переключаетесь на нужное окно мессенджера и ждёте полного окончания работы программы.\n Лучше не переходить на другие окна, иначе в окне, которое открыто в данный момент,\n то там и продолжится спам сообщениями. Чтобы завершить атаку нажмите клавишу 'Esc'",
    font=("Arial", 12), background="black", foreground="#00FF00", width=100, )

entry = tk.Entry(font=("Arial", 18, "bold"), width=37, background="#006400", foreground="#00FF00")
entry1 = tk.Entry(font=("Arial", 18, "bold"), width=37, background="#006400", foreground="#00FF00")
entry2 = tk.Entry(font=("Arial", 18, "bold"), width=37, background="#006400", foreground="#00FF00")
entry3 = tk.Entry(font=("Arial", 18, "bold"), width=37, background="#006400", foreground="#00FF00")

label = tk.Label(text="Таймер перед \n запуском:", font=("Arial", 15, "bold"), background="black", foreground="#00FF00")
label1 = tk.Label(text="Количество \nсообщений: ", font=("Arial", 15, "bold"), background="black", foreground="#00FF00")
label2 = tk.Label(text="Текст \nсообщения \n(до 35 сим.): ", font=("Arial", 15, "bold"), background="black",
                  foreground="#00FF00")
label3 = tk.Label(text="Задержка \nмежду \nотправками: ", font=("Arial", 15, "bold"), background="black",
                  foreground="#00FF00")

st = ScrolledText(root, width=78, height=10, font=("Arial", 15, "bold"), background="black", foreground="#00FF00",
                  state='disabled')

start_button = tk.Button(text="Начать атаку >>>", font=("Arial", 15, "bold"), background="#006400",
                         foreground="#00FF00", width=53, command=send_message)

heading.pack()
heading1.pack()
heading2.pack()

entry.place(x=200, y=250)
entry1.place(x=200, y=320)
entry2.place(x=200, y=390)
entry3.place(x=200, y=490)

label.place(x=30, y=250)
label1.place(x=30, y=320)
label2.place(x=30, y=390)
label3.place(x=30, y=490)

start_button.place(x=30, y=585)
st.place(x=30, y=650)

root.mainloop()