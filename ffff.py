from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog

def save_selection():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Вік машини: {age_car.get()}\n")
            file.write(f"Марка машини: {selected_car.get()}\n")
            file.write(f"Об'єм двигуна: {obiem_car.get()}\n")
            file.write(f"Континент виробник: {contri_car.get()}\n")
            file.write(f"Вид палива: {vud_car.get()}\n")
            file.write(f"Колір машини: {color.get()}\n")
            file.write(f"Покриття машини: {stul_car.get()}\n")
def opus_car():
    a = age_car.get()
    m = selected_car.get()
    o = obiem_car.get()
    c = contri_car.get()
    v = vud_car.get()
    p = stul_car.get()
    s = color.get()
    result_label.delete(1.0, END)
    result_label.insert(END,f"Вік машини: {a}\nМарка машини: {m}\nОб'єм двигуна: {o}\nКонтинент виробник: {c}\nВид палива: {v}\nКолір машини: {s}\nПокриття машини: {p}")
def colors(event):
    f = color.get()
    lab2.config(bg=f)

def deval():
    age_car.set("Стан машини")
    age_car2.set("До 15 років")
    selected_car.set("BMW")
    obiem_car.set("Менше 1200")
    contri_car.set("Західна Європа")
    vud_car.set("Дизель")
    stul_car.set(stul_options[0])
    color.set("red")
    lab2.config(bg="#ff0000")

root = Tk()
root.title("Анкета")
root.geometry('800x600')
root.configure(bg='#e6e6e6')
f1 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f1.place(x=6, y=40, width=150, height=60)
age_car = StringVar()
age_car.set("Стан машини")
age_radios = ['Нова машина', 'Якась ще']
for index, car in enumerate(age_radios):
    rb = Radiobutton(f1, text=car, variable=age_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+1, column=0, sticky=W, pady=2)

f2 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f2.place(x=10, y=160, width=180, height=125)
age_car2 = StringVar()
age_car2.set("До 15 років")
age_radios2 = ['До 15 років', '6-10 років', '11-15 років', 'Більше 15 років']
for index, car in enumerate(age_radios2):
    rb = Radiobutton(f2, text=car, variable=age_car2, value=car,bg='#a6a6a6')
    rb.grid(row=index+6, column=0, sticky=W, pady=2)

f3 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f3.place(x=200, y=160, width=180, height=125)
selected_car = StringVar()
selected_car.set("BMW")
marca_radios = ['BMW', 'Mercedes', 'Wolkevagen','Інша']
for index, car in enumerate(marca_radios):
    rb = Radiobutton(f3, text=car, variable=selected_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+6, column=4, sticky=W)

f4 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f4.place(x=390, y=160, width=180, height=125)
obiem_car = StringVar()
obiem_car.set("Менше 1200")
obiem_radios = ['Менше 1200', '1200-1500', '1501-2200', 'Більше 2200']
for index, car in enumerate(obiem_radios):
    rb = Radiobutton(f4, text=car, variable=obiem_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+6, column=6, sticky=W)

f5 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f5.place(x=10, y=300, width=180, height=125)
contri_car = StringVar()
contri_car.set("Західна Європа")
contri_radios = ['Західна Європа', 'Східна Європа', 'Азія', 'Америка']
for index, car in enumerate(contri_radios):
    rb = Radiobutton(f5, text=car, variable=contri_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+12, column=0, sticky=W)

f6 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f6.place(x=200, y=300, width=180, height=125)
vud_car = StringVar()
vud_car.set("Дизель")
vud_radios = ['Дизель', 'Бензин']
for index, car in enumerate(vud_radios):
    rb = Radiobutton(f6, text=car, variable=vud_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+12, column=2, sticky=W)
f7 = Frame(root,relief="solid", bd=2,bg='#a6a6a6')
f7.place(x=390, y=300, width=180, height=125)
stul_options = ['Мат', 'Глянц']
stul_car = StringVar()
stul_car.set(stul_options[0])
for index, car in enumerate(stul_options):
    rb = Radiobutton(f7, text=car, variable=stul_car, value=car,bg='#a6a6a6')
    rb.grid(row=index+12, column=4, sticky=W)

color = StringVar()
color.set("red")
lab2 = Label(root, text="", width=10, height=2,bg='#ff0000')
lab2.place(x=600, y=180,width=100, height=90)
class_combobox = Combobox(root, textvariable=color, values=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
class_combobox.place(x=600, y=160, width=100, height=40)
class_combobox.bind("<<ComboboxSelected>>", colors)

ggg = Label(root, text="Основні питання:",bg='#cccccc',font=(7))
ggg.place(x=200, y=40,width=155, height=35)

result_label = Text(root)
result_label.place(x=10, y=450,width=500, height=120)

b = Button(root, text="Показати результат",bg='#cccccc', command=opus_car)
b.place(x=550, y=450,width=150, height=30)

onova_button = Button(root, text="Оновити вибір",bg='#cccccc',command=deval)
onova_button.place(x=550, y=500,width=150, height=30)


save_button = Button(root, text="Зберегти вибір", bg='#cccccc', command=save_selection)
save_button.place(x=550, y=550, width=150, height=30)

root.mainloop()