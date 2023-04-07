from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import math
import csv
from tkinter import filedialog
#from tkinter.messagebox import showinfo

window = Tk()
window.title ('Расчет забойного давления и гидравлических потерь на трение')
window.geometry ('575x480+600+100')

bg1='gainsboro' 
bg2='rosybrown'
bg3='grey' 

# Создаю фреймы
up_frame  =  Frame(window,  width=640,  height=  400,  bg=bg1)
up_frame.grid(row=0,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')

right_frame_1 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_1.grid(row=4,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

right_frame_2 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_2.grid(row=5,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

right_frame_3 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_3.grid(row=6,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

down_frame  =  Frame(window,  width=640,  height=  400,  bg=bg2)
down_frame.grid(row=1,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')

type_well = IntVar()
fluid_type = IntVar()

#Затемнение областей ввода данных по реологии
def flag_fluid_type():
    if fluid_type.get() == 1:
        mud_visc_300_entry = ttk.Entry(up_frame, state=DISABLED) 
        mud_visc_300_entry.grid(row=8, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
        mud_visc_3_entry = ttk.Entry(up_frame, state=DISABLED)
        mud_visc_3_entry.grid(row=9, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
    else:
        mud_visc_300_entry = ttk.Entry(up_frame, state=ACTIVE) 
        mud_visc_300_entry.grid(row=8, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
        mud_visc_300_entry.insert(0, "20")
        mud_visc_3_entry = ttk.Entry(up_frame, state=ACTIVE)
        mud_visc_3_entry.grid(row=9, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
        mud_visc_3_entry.insert(0, "3")
    return    

#Функция очистки ячеек
def Clear():
    density_entry.delete(0, END)
    tvd_entry.delete(0, END)
    pipe_diametr_entry.delete(0, END)
    pipe_lenght_entry.delete(0, END)
    absolute_pipe_roughness_entry.delete(0, END)
    inj_rate_entry.delete(0, END)
    whp_entry.delete(0, END)
    mud_visc_3_entry.delete(0, END)
    mud_visc_300_entry.delete(0, END)
    spm_entry.delete(0, END)
    pl_entry.delete(0, END)
    dp_entry.delete(0, END)
    return


#Функция записи результатов расчета
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != " ":
        text = st.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)



#Получение данных из ячеек и вычисления
def Calculate():
    density = float((density_entry.get()))
    tvd = float((tvd_entry.get()))
    pipe_diametr = float(pipe_diametr_entry.get())/1000
    pipe_lenght = float(pipe_lenght_entry.get())
    absolute_pipe_roughness = float(absolute_pipe_roughness_entry.get())
    inj_rate = float(inj_rate_entry.get())
    whp = float(whp_entry.get())
    spm = float(spm_entry.get())
    pl = float(pl_entry.get())
    dp = float(dp_entry.get())

    
# Кострукция вычисления
    if type_well.get() == 1:
        if fluid_type.get() ==1:        #нагнетательная ньютоновская
            p_stat = ((density) * 9.8066 * (tvd))/100000
            velocity = float(inj_rate) / ((math.pi * (float(pipe_diametr) / 2) **2 ))
            dyn_visc = 1
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            kfr = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = (kfr * float(pipe_lenght) * float(density) * (float(velocity)**2)/float(pipe_diametr))/100000
            Np = spm * pl
            Cd = 1.4081*(dp/25.4)**2-0.4214*(dp/25.4)+0.4976
            Pperf = ((0.2369*((inj_rate*375)**2)*(density*0.00834))/((Np**2)*((dp/25.4)**4)*Cd**2))/14.5
            pressure_bottom = p_stat + float(whp) - float(friction)-Pperf
            
            
        else: #нагнетательная НЕньютоновская
            mud_visc_3 = float((mud_visc_3_entry.get()))
            mud_visc_300 = float((mud_visc_300_entry.get()))
            p_stat = (float(density) * 9.8066 * float(tvd))/100000
            velocity = float(inj_rate) / ((math.pi * (float(pipe_diametr) / 2) **2 ))
            n = 0.5 * math.log (float(mud_visc_300) / float(mud_visc_3))
            k = (5.11 * float(mud_visc_300))/(511000000**float(n))
            dyn_visc = float(k) * 1000 * float(velocity) ** float(n)
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            kfr = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = (kfr * float(pipe_lenght) * float(density) * (float(velocity)**2)/float(pipe_diametr))/100000
            Np = spm * pl
            Cd = 1.4081*(dp/25.4)**2-0.4214*(dp/25.4)+0.4976
            Pperf = ((0.2369*((inj_rate*375)**2)*(density*0.00834))/((Np**2)*((dp/25.4)**4)*Cd**2))/14.5
            pressure_bottom = p_stat + float(whp) - float(friction) - Pperf
            
            
    else:
        if fluid_type.get() ==1: #добывающая ньютоновская
            p_stat = (density * 9.8066 * tvd)/100000
            velocity = float(inj_rate) / ((math.pi * (float(pipe_diametr) / 2) **2 ))
            dyn_visc = 1
            re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
            relative_roughness = (absolute_pipe_roughness) / (pipe_diametr)
            kfr = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
            friction = (kfr * float(pipe_lenght) * float(density) * (float(velocity)**2)/float(pipe_diametr))/100000
            Np = spm * pl
            Cd = 1.4081*(dp/25.4)**2-0.4214*(dp/25.4)+0.4976
            Pperf = ((0.2369*((inj_rate*375)**2)*(density*0.00834))/((Np**2)*((dp/25.4)**4)*Cd**2))/14.5
            pressure_bottom = p_stat - whp - friction - Pperf
            
            
            
        else: #нагнетательная НЕньютоновская
            mud_visc_3 = float((mud_visc_3_entry.get()))
            mud_visc_300 = float((mud_visc_300_entry.get()))
            p_stat = (float(density) * 9.8066 * float(tvd))/100000
            velocity = float(inj_rate) / ((math.pi * (float(pipe_diametr) / 2) **2 ))
            n = 0.5 * math.log (float(mud_visc_300) / float(mud_visc_3))
            k = (5.11 * float(mud_visc_300))/(511000000**float(n))
            dyn_visc = float(k) * 1000 * float(velocity) ** float(n)
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            kfr = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = (kfr * float(pipe_lenght) * float(density) * (float(velocity)**2)/float(pipe_diametr))/100000
            Np = spm * pl
            Cd = 1.4081*(dp/25.4)**2-0.4214*(dp/25.4)+0.4976
            Pperf = ((0.2369*((inj_rate*375)**2)*(density*0.00834))/((Np**2)*((dp/25.4)**4)*Cd**2))/14.5
            pressure_bottom = p_stat - float(whp) - float(friction) - Pperf

#Вставляю строки в поле text

    st.insert(END, 'Гидростатическое давление (бар) ' + str(round(p_stat, 4)) + "\n")
    st.insert(END, 'Скорость потока жидкости (м/сек) ' + str(round(velocity, 4)) + "\n")
    st.insert(END, 'Число Рейнольдса ' + str(round(re, 4)) + "\n")
    st.insert(END, 'Коэффициент трения ' + str(round(kfr, 4)) + "\n")
    st.insert(END, 'Потери на трение в трубах (бар) ' + str(round(friction, 4)) + "\n")
    st.insert(END, 'Потери на трение в перфорации (бар) ' + str(round(Pperf, 4)) + "\n")
    st.insert(END, 'Давление на забое (бар) ' + str(round(pressure_bottom, 4)) + "\n")
    st.insert(END, '__________________________________________________________________________' + "\n")

    return
    
     
#Создаю и размещаю виджеты 

Label(up_frame, text='Глубина перфорации TVD (м)', bg=bg1).grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s') 
tvd_entry = ttk.Entry(up_frame) 
tvd_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
tvd_entry.insert(0, "1800")

Label(up_frame, text='Диаметр лифта НКТ (мм)', bg=bg1).grid(row=2, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s') 
pipe_diametr_entry = ttk.Entry(up_frame)
pipe_diametr_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
pipe_diametr_entry.insert(0, "76")

Label(up_frame, text = 'Длина лифта НКТ (м) ', bg=bg1).grid(row=3,column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s') 
pipe_lenght_entry = ttk.Entry(up_frame) 
pipe_lenght_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
pipe_lenght_entry.insert(0, "1800")

Label(up_frame, text = 'Абсолютная шероховатость труб ', bg=bg1).grid(row=4,column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
absolute_pipe_roughness_entry = ttk.Entry(up_frame) 
absolute_pipe_roughness_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
absolute_pipe_roughness_entry.insert(0, "0.00002")

Label(up_frame, text = 'Расход/дебет (м3/сек) ', bg=bg1).grid(row=5, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
inj_rate_entry = ttk.Entry(up_frame) 
inj_rate_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
inj_rate_entry.insert(0, "0.010667")

Label(up_frame, text = 'Устьевое давление (бар) ', bg=bg1).grid(row=6,column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
whp_entry = ttk.Entry(up_frame) 
whp_entry.grid(row=6, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
whp_entry.insert(0, "0")

Label(up_frame, text = 'Плотность флюида (кг/м3) ', bg=bg1).grid(row=7, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
density_entry = ttk.Entry(up_frame) 
density_entry.grid(row=7, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
density_entry.insert(0, "1000")

Label(up_frame, text = 'Показания вискозиметра при 300 (об/мин) ', bg=bg1).grid(row=8, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_300_entry = ttk.Entry(up_frame, state=ACTIVE) 
mud_visc_300_entry.grid(row=8, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_300_entry.insert(0, "20")

Label(up_frame, text = 'Показания вискозиметра при 3 (об/мин) ', bg=bg1).grid(row=9, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_3_entry = ttk.Entry(up_frame, state=ACTIVE) 
mud_visc_3_entry.grid(row=9, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_3_entry.insert(0, "3")

#Блок перфорации
Label(up_frame, text='Параметры перформации', bg=bg1, font='Arial 9').grid(row=3, column=2, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

Label(right_frame_1, text='Количество на метр   ', bg=bg3, font='Arial 8').grid(row=4, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
spm_entry = ttk.Entry(right_frame_1, width=6)
spm_entry.grid(row=4, column=1, padx=1, pady=1, sticky='w'+'e'+'n'+'s')
spm_entry.insert(0, "20")

Label(right_frame_2, text='Мощность интервала (м)  ', bg=bg3, font='Arial 8').grid(row=5, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
pl_entry = ttk.Entry(right_frame_2, width=3)
pl_entry.grid(row=5, column=1, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
pl_entry.insert(0, "0.7")

Label(right_frame_3, text='Ширина / диаметр (мм)   ', bg=bg3, font='Arial 8').grid(row=6, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
dp_entry = ttk.Entry(right_frame_3, width=4)
dp_entry.grid(row=6, column=1, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
dp_entry.insert(0, "8")


Checkbutton(up_frame, text="Нагнетательная скважина", variable=type_well, bg=bg1).grid(row=1, column=2, sticky='w'+'e'+'n'+'s')
Checkbutton(up_frame, text="Ньютоновская жидкость", variable=fluid_type, command=flag_fluid_type, bg=bg1).grid(row=8, column=2, sticky='w'+'e'+'n'+'s')

Button(up_frame, text="Очистить", command=Clear).grid(row=9, column=2, padx=2, pady=2, sticky='w'+'e'+'n'+'s')
Button(down_frame, text="Расчет", command=Calculate, width=30).grid(row=2, column=0, padx=5, pady=5, sticky='w')
Button(down_frame, text="Сохранить", command=save_file).grid(row=2, column=0, padx=5, pady=5, sticky='e')

#окно вывода результатов
st = ScrolledText(down_frame, width=76,  height=8, bd=1.5, font = 'Arial 10')
st.grid(row=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

          

if __name__ == '__main__':
    # Create and run the GUI   
    window.mainloop()
