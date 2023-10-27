from tkinter import *
from tkinter import ttk

# Задаем функцию пересчета. обратите внимание, что к feet и meters мы обращаемся как к глобальным переменным, в общем случае так делать нехорошо
# *args означает, что функция может принимать любое количество переменных. здесь они не используется, поэтому для общности написали так
def calculate(*args):
    try:
        weight = float(weight1.get())
        height = float(height1.get())
        imt.set("{0:.3f}".format(float(weight/(height**2/10000))))
        if float(imt.get())<=16:
            imtresult.set("Выраженный дефицит массы тела")
        elif float(imt.get())>16 and float(imt.get())<=18.5:
            imtresult.set("Дефицит массы тела")
        elif float(imt.get())>18.5 and float(imt.get())<=25:
            imtresult.set("Норма")
        elif float(imt.get())>25 and float(imt.get())<=30:
            imtresult.set("Избыточная масса тела")
        elif float(imt.get()>30 and float(imt.get()))<=35:
            imtresult.set("Ожирение 1 степени")
        elif float(imt.get())>35 and float(imt.get())<=40:
            imtresult.set("Ожирение 2 степени")
        elif float(imt.get())>40:
            imtresult.set("Ожирение 3 степени")
    
    except ValueError:
        print(1)
        pass

root = Tk()
root.title("IMT Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

'''
Первый виджет Entry должен принимать количество футов.

Когда мы создаем виджет, нам нужно указать его родителя.
Это виджет, внутри которого будет размещен новый виджет.
Наша запись и другие виджеты, которые мы вскоре создадим, считаются дочерними элементами mainframe.
Родительский элемент передается в качестве первого параметра при создании экземпляра объекта виджета.

Также мы задали, что наше окно ввода должно иметь ширину под 7 символов.

Также мы создали глобальную переменную feet как textvariable для Entry. 
Когда ввод поменяется, Tkinter автоматически обновит feet. 
Для задания feet используется конструктор по умолчанию для таких переменных -- StringVar()

When widgets are created, they don't automatically appear on the screen; 
Tkinter должен знать куда вы хотите поместить виджеты относительно друг друга. 
За это отвечает функция grid. Она помещает содержимое в column (1, 2, or 3) и row (also 1, 2, or 3) окна.
sticky отвечает за то, по какой стороне будет выравнивание. W (west) означает запад, то есть левую сторону ячейки
W,E (west-east) означает и левую и правую сторону одновременно, то есть выравнивание посередине.
В Python определены константы для направлений компаса, поэтому вы можете писать просто W или (W, E).
'''
weight1 = StringVar()
weight1_entry = ttk.Entry(mainframe, width=10, textvariable=weight1)
weight1_entry.grid(column=2, row=1, sticky=(W, E))

height1 = StringVar()
height1_entry = ttk.Entry(mainframe, width=10, textvariable=height1)
height1_entry.grid(column=2, row=2, sticky=(W, E))

imt = StringVar()
ttk.Label(mainframe, textvariable=imt).grid(column=2, row=3, sticky=(W, E))

imtresult = StringVar()
ttk.Label(mainframe, textvariable=imtresult).grid(column=3, row=4, sticky=(W, E))

'''
По нажатии на кнопку будем выполнять функцию calculate. Поскольку в ней уже прописаны операции напрямую с feet и meters,
то нам не нужно задавать какие-либо аргументы, функция автоматически положит нужное значение в meters и значение в 
определенном выше Label обновится.
'''
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=5, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="weight (kg)").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="height (cm)").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="imt").grid(column=3, row=3, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", calculate)

# циклим наше окно
root.mainloop()