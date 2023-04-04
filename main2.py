from tkinter import *
from tkinter import ttk
import math
from tkinter.messagebox import showinfo

window = Tk()
window.title ('Расчет забойного давления и гидравлических потерь на трение')
window.geometry ('580x500+600+100')

type_well = IntVar()
fluid_type = IntVar()

#Затемнение областей ввода данных по реологии
def flag_fluid_type():
    if fluid_type.get() == 1:
        mud_visc_300_entry = ttk.Entry(state=DISABLED) 
        mud_visc_300_entry.grid(row=14, column=1, padx=5, pady=5, sticky="W")
        mud_visc_3_entry = ttk.Entry(state=DISABLED)
        mud_visc_3_entry.grid(row=15, column=1, padx=5, pady=5, sticky="W")
    else:
        mud_visc_300_entry = ttk.Entry(state=ACTIVE) 
        mud_visc_300_entry.grid(row=14, column=1, padx=5, pady=5, sticky="W")
        mud_visc_3_entry = ttk.Entry(state=ACTIVE)
        mud_visc_3_entry.grid(row=15, column=1, padx=5, pady=5, sticky="W")

#Функция очистки ячеек
def Clear():
    density_entry.delete(0, END)
    tvd_entry.delete(0, END)
    pipe_diametr_entry.delete(0, END)
    pipe_lenght_entry.delete(0, END)
    #absolute_pipe_roughness_entry.delete(0, END)
    inj_rate_entry.delete(0, END)
    whp_entry.delete(0, END)
    mud_visc_3_entry.delete(0, END)
    mud_visc_300_entry.delete(0, END)
               

#Получение данных из ячеек и вычисления
def Calculate():
    density = float((density_entry.get()))
    tvd = float((tvd_entry.get()))
    pipe_diametr = float((pipe_diametr_entry.get()))
    pipe_lenght = (pipe_diametr_entry.get())
    absolute_pipe_roughness = float((absolute_pipe_roughness_entry.get()))
    inj_rate = float((inj_rate_entry.get()))
    whp = float((whp_entry.get()))
    
#Вывод результатов
    def results_print():
        p_stat_n_label = ttk.Label(text='Гидростатическое давление (бар) ')
        p_stat_n_label.grid(row=17, column=0, padx=5, pady=5, sticky="W")
        p_stat_label = ttk.Label(text=round(p_stat, 4))
        p_stat_label.grid(row=17, column=1, padx=5, pady=5, sticky="W")

        velocity_n_label = ttk.Label(text='Скорость потока жидкости (м/сек) ')
        velocity_n_label.grid(row=18, column=0, padx=5, pady=5, sticky="W")
        velocity_label = ttk.Label(text=round(velocity, 4))
        velocity_label.grid(row=18, column=1, padx=5, pady=5, sticky="W")

        re_n_label = ttk.Label(text='Число Рейнольдса ')
        re_n_label.grid(row=19, column=0, padx=5, pady=5, sticky="W")
        re_label = ttk.Label(text=round(re, 4))
        re_label.grid(row=19, column=1, padx=5, pady=5, sticky="W")

        relative_roughness_n_label = ttk.Label(text='Относительная шероховатость ')
        relative_roughness_n_label.grid(row=19, column=0, padx=5, pady=5, sticky="W")
        relative_roughness_label = ttk.Label(text=round(relative_roughness, 4))
        relative_roughness_label.grid(row=19, column=1, padx=5, pady=5, sticky="W")

        f_n_label = ttk.Label(text='Коэффициент трения ')
        f_n_label.grid(row=20, column=0, padx=5, pady=5, sticky="W")
        f_label = ttk.Label(text=round(f, 4))
        f_label.grid(row=20, column=1, padx=5, pady=5, sticky="W")

        friction_n_label = ttk.Label(text='Потери на трение (бар) ')
        friction_n_label.grid(row=21, column=0, padx=5, pady=5, sticky="W")
        friction_label = ttk.Label(text=round(friction, 4))
        friction_label.grid(row=21, column=1, padx=5, pady=5, sticky="W")

        friction_n_label = ttk.Label(text='Давление на забое (бар) ')
        friction_n_label.grid(row=22, column=0, padx=5, pady=5, sticky="W")
        friction_label = ttk.Label(text=round(pressure_bottom, 4))
        friction_label.grid(row=22, column=1, padx=5, pady=5, sticky="W")
   
#Кострукция вычисления
    if type_well.get() == 1:
        if fluid_type.get() ==1:
            p_stat = ((density) * 9.8066 * (tvd))/100000
            velocity = ((float(inj_rate) / (math.pi * float(pipe_diametr) / 2) **2 ))
            dyn_visc = 1
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            f = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = float(f) * float(pipe_lenght) * float(density) * ((float(velocity)**2)/float(pipe_diametr))/100000
            pressure_bottom = p_stat + float(whp) - float(friction)
            results_print()
        else:
            mud_visc_3 = float((mud_visc_3_entry.get()))
            mud_visc_300 = float((mud_visc_300_entry.get()))
            p_stat = (float(density) * 9.8066 * float(tvd))/100000
            velocity = ((float(inj_rate) / (math.pi * float(pipe_diametr) / 2) **2 ))
            n = 0.5 * math.log (float(mud_visc_300) / float(mud_visc_3))
            k = (5.11 * float(mud_visc_300))/(511000000**float(n))
            dyn_visc = float(k) * 1000 * float(velocity) ** float(n)
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            f = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = float(f) * float(pipe_lenght) * float(density) * ((float(velocity)**2)/float(pipe_diametr))/100000
            pressure_bottom = p_stat + float(whp) - float(friction)
            results_print()  
    else:
        if fluid_type.get() ==1:
            p_stat = (float(density) * 9.8066 * float(tvd))/100000
            velocity = (float(inj_rate) / (math.pi * float(pipe_diametr) / 2) **2 )
            dyn_visc = 1
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            f = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = float(f) * float(pipe_lenght) * float(density) * ((float(velocity)**2)/float(pipe_diametr))/100000
            pressure_bottom = p_stat - float(whp) - float(friction)
            results_print()
        else:
            mud_visc_3 = float((mud_visc_3_entry.get()))
            mud_visc_300 = float((mud_visc_300_entry.get()))
            p_stat = (float(density) * 9.8066 * float(tvd))/100000
            velocity = ((float(inj_rate) / (math.pi * float(pipe_diametr) / 2) **2 ))
            n = 0.5 * math.log (float(mud_visc_300) / float(mud_visc_3))
            k = (5.11 * float(mud_visc_300))/(511000000**float(n))
            dyn_visc = float(k) * 1000 * float(velocity) ** float(n)
            re = (float(density) * float(pipe_diametr) * float(velocity)) / (float(dyn_visc) / 1000)
            relative_roughness = (float(absolute_pipe_roughness) / float(pipe_diametr))
            f = (-1.8 * math.log10((6.9/float(re)) + (float(relative_roughness)/3.7)**1.11))**-2
            friction = float(f) * float(pipe_lenght) * float(density) * ((float(velocity)**2)/float(pipe_diametr))/100000
            pressure_bottom = p_stat - float(whp) - float(friction)
            results_print()     




    

    




#Создаю и размещаю виджеты 
tvd_label = ttk.Label(text='Глубина перфорации TVD (м)')
tvd_label.grid(row=1, column=0, padx=5, pady=5, sticky="W") 
tvd_entry = ttk.Entry() 
tvd_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

pipe_diametr_label = ttk.Label(text='Диаметр лифта НКТ (м)')
pipe_diametr_label.grid(row=3,column=0, padx=5, pady=5, sticky="W") 
pipe_diametr_entry = ttk.Entry()
pipe_diametr_entry.grid(row=3,column=1, padx=5, pady=5, sticky="W")

pipe_lenght_label = ttk.Label(text = 'Длина лифта НКТ (м) ')
pipe_lenght_label.grid(row=5,column=0, padx=5, pady=5, sticky="W") 
pipe_lenght_entry = ttk.Entry() 
pipe_lenght_entry.grid(row=5, column=1, padx=5, pady=5, sticky="W")

absolute_pipe_roughness_label = ttk.Label(text = 'Абсолютная шероховатость труб ')
absolute_pipe_roughness_label.grid(row=7,column=0, padx=5, pady=5, sticky="W")
absolute_pipe_roughness_entry = ttk.Entry() 
absolute_pipe_roughness_entry.grid(row=7, column=1, padx=5, pady=5, sticky="W")
absolute_pipe_roughness_entry.insert(0, "0.00002")

inj_rate_label = ttk.Label(text = 'Расход/дебет (м3/сек) ')
inj_rate_label.grid(row=9, column=0, padx=5, pady=5, sticky="W")
inj_rate_entry = ttk.Entry() 
inj_rate_entry.grid(row=9, column=1, padx=5, pady=5, sticky="W")

whp_entry_label = ttk.Label (text = 'Устьевое давление (бар) ')
whp_entry_label.grid(row=11,column=0, padx=5, pady=5, sticky="W")
whp_entry = ttk.Entry() 
whp_entry.grid(row=11, column=1, padx=5, pady=5, sticky="W")

density_entry_label = ttk.Label (text = 'Плотность флюида (кг/м3) ')
density_entry_label.grid(row=13, column=0, padx=5, pady=5, sticky="W")
density_entry = ttk.Entry() 
density_entry.grid(row=13, column=1, padx=5, pady=5, sticky="W")

mud_visc_300_entry_label = ttk.Label (text = 'Показания вискозиметра при 300 (об/мин) ')
mud_visc_300_entry_label.grid(row=14, column=0, padx=5, pady=5, sticky="W")
mud_visc_300_entry = ttk.Entry(state=ACTIVE) 
mud_visc_300_entry.grid(row=14, column=1, padx=5, pady=5, sticky="W")

mud_visc_3_entry_label = ttk.Label (text = 'Показания вискозиметра при 3 (об/мин) ')
mud_visc_3_entry_label.grid(row=15, column=0, padx=5, pady=5, sticky="W")
mud_visc_3_entry = ttk.Entry(state=ACTIVE) 
mud_visc_3_entry.grid(row=15, column=1, padx=5, pady=5, sticky="W")

type_well_checkbutton = ttk.Checkbutton(text="Нагнетательная скважина", variable=type_well)
type_well_checkbutton.grid(row=1, column=2, sticky="E")
         
fluid_type_checkbutton = ttk.Checkbutton(text="Ньютоновская жидкость", variable=fluid_type, command=flag_fluid_type)
fluid_type_checkbutton.grid(row=14, column=2, sticky="E")

# Создаю кнопки

calc_button = ttk.Button(text="Calculate", command=Calculate)
calc_button.grid(row=16, column=0, padx=5, pady=5, sticky="W")

clear_button = ttk.Button(text="Clear", command=Clear)
clear_button.grid(row=16, column=1, padx=5, pady=5, sticky="W")





if __name__ == '__main__':
    # Create and run the GUI   
    window.mainloop()

