import math
from tkinter import *
from tkinter import ttk
 
 
# root = Tk()
# root.title("РАЧЕТ ЗАБОЙНОГО ДАВЛЕНИЯ")
# root.geometry("650x800")

def new_fl():
    print ('Скорость потока = ', round(velocity, 4), 'm/sec')
    print ('Число Рейнольдса = ', round(re, 4))
    print ('Относительная шероховатость = ', round(relative_roughness, 4))
    print ('Коэффициент трения = ', round(f, 4))
    print ('Потери на трение = ', round(friction, 4), 'bar')
    print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')

def non_fl():
    print ('Скорость потока = ', round(velocity, 4), 'm/sec')
    print ('Индекс динамики потока, n = ', round(n, 4))
    print ('Коэффициент вязкости, K = ', round(k, 4))
    print ('Число Рейнольдса = ', round(re, 4))
    print ('Относительная шероховатость = ', round(relative_roughness, 4))
    print ('Коэффициент трения = ', round(f, 4))
    print ('Потери на трение = ', round(friction, 4), 'bar')
    print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')    

g = 9.8066

# entry = ttk.Entry()
# entry.pack(anchor=NW, padx=50, pady=10)
  
# btn = ttk.Button(text="Расчет", command=new_fl)
# btn.pack(anchor=NW, padx=6, pady=6)
 
# label = ttk.Label()
# label.pack(anchor=NW, padx=6, pady=6)

print ('Глубина перфорации TVD (m) = ', end=" ")
tvd = int(input ())

print ('Внутренний диаметр НКТ (m) = ', end=" ")     
pipe_diametr = float(input ())

print ('Длина лифта НКТ (m) = ', end=" ")           
pipe_lenght = int(input ())

print ('Абсолютная шероховатость труб (0.00002 по умолчанию) =  ', end=" ")  
absolute_pipe_roughness = float(input ())

print ('Расход/дебет (m3/sec) = ', end=" ")  
inj_rate = float(input ())

print ('Устьевое давление (bar) = ', end=" ")  
whp = float(input ())

print ('Плотность флюида (kg/m3) = ', end=" ") 
density = int(input ())

data_entry = {
     "tvd_key": tvd,
     "pipe_diametr_key": pipe_diametr,
     "pipe_lenght_key": pipe_lenght,
     "absolute_pipe_roughness_key": absolute_pipe_roughness,
     "inj_rate_key": inj_rate,
     "whp_key": whp,
     "density_key": density  
}

p_stat = (data_entry["density_key"] * g * data_entry["tvd_key"])/100000

print ('Скважина добывающая? (Y/N) ', end=" ")
type_well = input ()
if type_well == "Y" or type_well == "y" or type_well == "да" or type_well == "ДА" or type_well == "Да" or type_well == "lf" or type_well == "Lf" or type_well == "LF":

    print ('В скважине Ньютоновская жидкость? (Y/N) ', end=" ")
    fluid_type = input ()
    if fluid_type == "Y" or fluid_type == "y" or fluid_type == "да" or fluid_type == "ДА" or fluid_type == "Да" or fluid_type == "lf" or fluid_type == "Lf" or fluid_type == "LF":
        velocity = (data_entry["inj_rate_key"] / (math.pi * ( data_entry["pipe_diametr_key"] / 2) **2 ))
        dyn_visc = 1
        re = (data_entry["density_key"] * data_entry["pipe_diametr_key"] * velocity) / (dyn_visc / 1000)
        relative_roughness = (data_entry["absolute_pipe_roughness_key"] / data_entry["pipe_diametr_key"])
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * data_entry["pipe_lenght_key"] * data_entry["density_key"] * ((velocity**2)/data_entry["pipe_diametr_key"])/100000
        pressure_bottom = p_stat - data_entry["whp_key"] - friction

        new_fl()
            
    else:
        print ('Показания вискозиметра при 300rpm = ', end=" ")
        mud_visc_300rpm = int(input ())

        print ('Показания вискозиметра при 3rpm = ', end=" ")
        mud_visc_3rpm = int(input ())

        data_entry_2 = {"mud_visc_300": mud_visc_300rpm, "mud_visc_3": mud_visc_3rpm}
        data_entry.update(data_entry_2)

        velocity = (data_entry["inj_rate_key"] / (math.pi * ( data_entry["pipe_diametr_key"] / 2) **2 ))
        n = 0.5 * math.log (data_entry["mud_visc_300"] / data_entry["mud_visc_3"])
        k = (5.11 * data_entry["mud_visc_300"])/(511000000**n)
        dyn_visc = k * 1000 * velocity ** n
        re = (data_entry["density_key"] * data_entry["pipe_diametr_key"] * velocity) / (dyn_visc / 1000)
        relative_roughness = (data_entry["absolute_pipe_roughness_key"] / data_entry["pipe_diametr_key"])
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * data_entry["pipe_lenght_key"] * data_entry["density_key"] * ((velocity**2)/data_entry["pipe_diametr_key"])/100000
        pressure_bottom = p_stat - data_entry["whp_key"] - friction
                     
        non_fl()
            
        
else: 
    print ('В скважине Ньютоновская жидкость? (Y/N) ', end=" ")
    fluid_type = input ()
    if fluid_type == "Y" or fluid_type == "y" or fluid_type == "да" or fluid_type == "ДА" or fluid_type == "Да" or fluid_type == "lf" or fluid_type == "Lf" or fluid_type == "LF":
        velocity = (data_entry["inj_rate_key"] / (math.pi * ( data_entry["pipe_diametr_key"] / 2) **2 ))
        dyn_visc = 1
        re = (data_entry["density_key"] * data_entry["pipe_diametr_key"] * velocity) / (dyn_visc / 1000)
        relative_roughness = (data_entry["absolute_pipe_roughness_key"] / data_entry["pipe_diametr_key"])
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * data_entry["pipe_lenght_key"] * data_entry["density_key"] * ((velocity**2)/data_entry["pipe_diametr_key"])/100000
        pressure_bottom = p_stat + data_entry["whp_key"] - friction

        new_fl()
            
    else:
        print ('Показания вискозиметра при 300rpm = ', end=" ")
        mud_visc_300rpm = int(input ())

        print ('Показания вискозиметра при 3rpm = ', end=" ")
        mud_visc_3rpm = int(input ())

        data_entry_2 = {"mud_visc_300": mud_visc_300rpm, "mud_visc_3": mud_visc_3rpm}
        data_entry.update(data_entry_2)

        velocity = (data_entry["inj_rate_key"] / (math.pi * ( data_entry["pipe_diametr_key"] / 2) **2 ))
        n = 0.5 * math.log (data_entry["mud_visc_300"] / data_entry["mud_visc_3"])
        k = (5.11 * data_entry["mud_visc_300"])/(511000000**n)
        dyn_visc = k * 1000 * velocity ** n
        re = (data_entry["density_key"] * data_entry["pipe_diametr_key"] * velocity) / (dyn_visc / 1000)
        relative_roughness = (data_entry["absolute_pipe_roughness_key"] / data_entry["pipe_diametr_key"])
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * data_entry["pipe_lenght_key"] * data_entry["density_key"] * ((velocity**2)/data_entry["pipe_diametr_key"])/100000
        pressure_bottom = p_stat + data_entry["whp_key"] - friction
                     
        non_fl()

#root.mainloop()
