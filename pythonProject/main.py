from tkinter import *
from tkinter import ttk
i=0
mape={}
mape2={}
def clicked():
    i=0
    print("Проверка")
    print(len(mape))
    while (i<len(mape)):
        if (mape.get("chk_state_" + str(i)).get()==True):

            print("chk_state_" + str(i)+str(mape.get("chk_state_" + str(i)).get()))
        i=i+1
def a():
    i=0
    root = Toplevel()

    container = ttk.Frame(root)
    canvas = Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(width=400, height=500,
                                   scrollregion=canvas.bbox("all")
                                   )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    while (i < 100):
        chk_state = BooleanVar()
        chk_state.set(False)  # задайте проверку состояния чекбокса
        mape["chk_state_" + str(i)] = chk_state
        # print()
        # print(mape.get("chk_state_" + str(i)).get())
        mape2["ch_" + str(i)] = Checkbutton(scrollable_frame, text='Выбрать', var=mape.get("chk_state_" + str(i)))
        mape2.get("ch_" + str(i)).grid(column=0, row=i)
        btn = Button(scrollable_frame, text="Проверить", command=clicked)
        btn.grid(column=1, row=0)

        i = i + 1
    print(mape)
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')





btn1 = Button(window, text="Список", command=a)
btn1.grid(column=1, row=0)
btn = Button(window, text="Проверка!", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()



