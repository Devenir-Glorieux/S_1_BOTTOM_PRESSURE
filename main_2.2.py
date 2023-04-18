from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import math
import csv
from tkinter import filedialog
import os
#from tkinter.messagebox import showinfo

window = Tk()
window.title ('Calculate well pressure and frictional losses')
window.geometry ('500x515+600+100')

bg1='gainsboro' 
bg2='rosybrown'
bg3='darkgray' 

# Создаю фреймы
up_frame  =  Frame(window,  width=300,  height=  400,  bg=bg1)
up_frame.grid(row=0,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')

right_frame_1 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_1.grid(row=3,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

right_frame_2 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_2.grid(row=4,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

right_frame_3 = Frame(up_frame, width=50,  height=  10,  bg=bg3)
right_frame_3.grid(row=5,  column=2,  padx=0,  pady=0, sticky='w'+'e'+'n'+'s')

down_frame  =  Frame(window,  width=300,  height= 420,  bg=bg2)
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

#Затемнение переключателя насоса
def injection_well_flag():
    if type_well.get() == 0:
        switch_btn = Button(up_frame, image=switch_off_img, command=toggle_switch, border=0, bg=bg1, activebackground=bg1, height=30, state=ACTIVE)
        switch_btn.grid(row=7, column=2, sticky='e')
    else:
        switch_btn = Button(up_frame, image=switch_off_img, command=toggle_switch, border=0, bg=bg1, activebackground=bg1, height=30, state=DISABLED)
        switch_btn.grid(row=7, column=2, sticky='e')
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

#Функция сохранения результатов расчета
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != " ":
        text = st.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)

#Функция переключателя
def toggle_switch():
    global switch_state
    switch_state = not switch_state
    if switch_state:
        switch_btn.config(image=switch_on_img)
    else:
        switch_btn.config(image=switch_off_img)

#Получение данных из ячеек и вычисления
def Calculate():
    
    tvd = float(tvd_entry.get())
    if tvd_units.get() == 'm':
        tvd = tvd    
    else: 
        tvd = tvd*0.3048
    #---------------------------------------------
    pipe_diametr = float(pipe_diametr_entry.get())
    if pipe_diametr_units.get() == 'mm':
        pipe_diametr = pipe_diametr/1000    
    else: 
        pipe_diametr = pipe_diametr*0.0254
    #--------------------------------------------
    pipe_lenght = float(pipe_lenght_entry.get())
    if pipe_lenght_units.get() == 'm':
        pipe_lenght = pipe_lenght    
    else: 
        pipe_lenght = pipe_lenght*0.3048
    #--------------------------------------------
    absolute_pipe_roughness = float(absolute_pipe_roughness_entry.get())
    #--------------------------------------------   
    inj_rate = float(inj_rate_entry.get())
    if injr_units.get() == 'm3/s':
        inj_rate = inj_rate
    elif injr_units.get() == 'm3/h':
        inj_rate = inj_rate*3600
    elif injr_units.get() == 'm3/d':
        inj_rate = inj_rate/86400
    elif injr_units.get() == 'l/s':
        inj_rate = inj_rate/1000
    elif injr_units.get() == 'ft3/s':
        inj_rate = inj_rate/35.315   
    elif injr_units.get() == 'gal/s':
        inj_rate = inj_rate/264.2 
    elif injr_units.get() == 'bbl/h':
        inj_rate = inj_rate/22640
    elif injr_units.get() == 'bbl/d':
        inj_rate = ((inj_rate*0.26205)/86400)           
            
    #--------------------------------------------
    whp = float(whp_entry.get())
    if whp_units.get() == 'bar':
        whp = whp    
    elif whp_units.get() == 'psi': 
        whp = whp*0.0689476
    else:
        whp = whp*0.01
    #--------------------------------------------
    density = float(density_entry.get())
    if density_units.get() == 'kg/m3':
        density = density    
    elif density_units.get() == 'g/cm3': 
        density = density * 0.001
    elif density_units.get() == 'lb/gal': 
        density = density * 119.8
    else:
        density = density * 16.02       
    # проверка на ввод цифр
    # if density.isdecimal() !=True:
    #     st.insert(END, 'Wrong value, enter digits' + '\n')
    #     st.insert(END, '_________________________________________________________' + '\n')
    # density = float(density)


    spm = float(spm_entry.get())
    #--------------------------------------------
    pl = float(pl_entry.get())
    if pl_units.get() == 'm':
        pl = pl   
    else: 
        pl = pl*0.3048
    #--------------------------------------------
    dp = float(dp_entry.get())
    if dp_units.get() == 'mm':
        dp = dp    
    else: 
        dp = dp*25.4
    #--------------------------------------------

    
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
            if switch_state:
                pressure_bottom = p_stat + whp + friction + Pperf
            else: pressure_bottom = p_stat - whp - friction - Pperf
                
            
            
            
        else: #добывающая НЕньютоновская
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
            if switch_state:
                pressure_bottom = p_stat + whp + friction + Pperf
            else: pressure_bottom = p_stat - whp - friction - Pperf

#Вставляю строки в поле text

    st.insert(END, 'Hydrostatic pressure (bar)  ' + str(round(p_stat, 4)) + '\n')
    st.insert(END, 'Fluid flow speed (m/sec) ' + str(round(velocity, 4)) + '\n')
    st.insert(END, 'Reynolds number ' + str(round(re, 4)) + '\n')
    st.insert(END, 'friction coefficient  ' + str(round(kfr, 4)) + '\n')
    st.insert(END, 'Friction loss in pipes (bar)  ' + str(round(friction, 4)) + '\n')
    st.insert(END, 'Friction loss in perforations (bar)  ' + str(round(Pperf, 4)) + '\n')
    st.insert(END, 'Bottom hole pressure (bar)  ' + str(round(pressure_bottom, 4)) + '\n')
    st.insert(END, '_________________________________________________________' + '\n')
    # st.insert(END, str(tvd) + ' ,')
    # st.insert(END, str(pipe_diametr) + ' ,')
    # st.insert(END, str(pipe_lenght) + ' ,')
    # st.insert(END, str(inj_rate) + ' ,')              #проверка ввода
    # st.insert(END, str(whp) + ' ,')
    # st.insert(END, str(density) + ' ,')
    # st.insert(END, str(pl) + ' ,')
    # st.insert(END, str(dp) + ' ,')
    st.see('end')

    return
    
     
#Создаю и размещаю виджеты 

Label(up_frame, text='Perforation depth (TVD) ', bg=bg1).grid(row=1, column=0, padx=5, pady=5, sticky='w') 
tvd_entry = ttk.Entry(up_frame) 
tvd_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
tvd_entry.insert(0, "1800")

# создаю выпадающий список
options_tvd = ["m", "ft"]
tvd_units = StringVar(value=options_tvd[0])
tvd_units_combobox = ttk.Combobox (up_frame, textvariable = tvd_units, values=options_tvd, width=3)
tvd_units_combobox.grid(row=1, column=0,  padx=5, pady=5, sticky='e')

#_______________________________________________________________________________________________________________

Label(up_frame, text='Pipe diameter ', bg=bg1).grid(row=2, column=0, padx=5, pady=5, sticky='w') 
pipe_diametr_entry = ttk.Entry(up_frame)
pipe_diametr_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
pipe_diametr_entry.insert(0, "76")

options_pipd = ["mm", "in"]
pipe_diametr_units = StringVar(value=options_pipd[0])
pipe_diametr_combobox = ttk.Combobox (up_frame, textvariable = pipe_diametr_units, values=options_pipd, width=4)
pipe_diametr_combobox.grid(row=2, column=0,  padx=5, pady=5, sticky='e')

# # создаю выпадающий список V2
# pipe_diametr_units = OptionMenu(up_frame, pipe_diametr_units, *options_pipd,)
# pipe_diametr_units.grid(row=2, column=0, padx=5, pady=5, sticky='e')
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'Pipe length ', bg=bg1).grid(row=3,column=0, padx=5, pady=5, sticky='w') 
pipe_lenght_entry = ttk.Entry(up_frame) 
pipe_lenght_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
pipe_lenght_entry.insert(0, "1800")

options_pipl = ["m", "ft"]
pipe_lenght_units = StringVar(value=options_pipl[0])
pipe_lenght_combobox = ttk.Combobox (up_frame, textvariable = pipe_lenght_units, values=options_pipl, width=3,)
pipe_lenght_combobox.grid(row=3, column=0,  padx=5, pady=5, sticky='e')
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'Absolute pipe roughness ', bg=bg1).grid(row=4,column=0, padx=5, pady=5, sticky='w')
absolute_pipe_roughness_entry = ttk.Entry(up_frame) 
absolute_pipe_roughness_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
absolute_pipe_roughness_entry.insert(0, "0.00002")
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'Well rate ', bg=bg1).grid(row=5, column=0, padx=5, pady=5, sticky='w')
inj_rate_entry = ttk.Entry(up_frame) 
inj_rate_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
inj_rate_entry.insert(0, "0.010667")

options_injr = ["m3/s", "m3/h", "m3/d", "l/s", "ft3/s", "gal/s", "bbl/h", "bbl/d"]
injr_units = StringVar(value=options_injr[0])
injr_combobox = ttk.Combobox (up_frame, textvariable = injr_units, values=options_injr, width=8,)
injr_combobox.grid(row=5, column=0,  padx=5, pady=5, sticky='e')
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'WHP ', bg=bg1).grid(row=6,column=0, padx=5, pady=5, sticky='w')
whp_entry = ttk.Entry(up_frame) 
whp_entry.grid(row=6, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
whp_entry.insert(0, "0")

options_whp = ["bar", "psi", "kPa"]
whp_units = StringVar(value=options_whp[0])
whp_combobox = ttk.Combobox (up_frame, textvariable = whp_units, values=options_whp, width=3,)
whp_combobox.grid(row=6, column=0,  padx=5, pady=5, sticky='e')
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'Fluid density ', bg=bg1).grid(row=7, column=0, padx=5, pady=5, sticky='w')
density_entry = ttk.Entry(up_frame) 
density_entry.grid(row=7, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
density_entry.insert(0, "1000")

options_den = ["kg/m3", "g/cm3", "lb/ft3", "lb/gal"]
density_units = StringVar(value=options_den[0])
den_combobox = ttk.Combobox (up_frame, textvariable = density_units, values=options_den, width=6,)
den_combobox.grid(row=7, column=0,  padx=5, pady=5, sticky='e')
#_______________________________________________________________________________________________________________
Label(up_frame, text = 'Viscosity at 300rpm ', bg=bg1).grid(row=8, column=0, padx=5, pady=5, sticky='w')
mud_visc_300_entry = ttk.Entry(up_frame, state=ACTIVE) 
mud_visc_300_entry.grid(row=8, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_300_entry.insert(0, "20")

Label(up_frame, text = 'Viscosity at 3rpm ', bg=bg1).grid(row=9, column=0, padx=5, pady=5, sticky='w')
mud_visc_3_entry = ttk.Entry(up_frame, state=ACTIVE) 
mud_visc_3_entry.grid(row=9, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
mud_visc_3_entry.insert(0, "3")

#_______________________________________________________________________________________________________________

#Блок перфорации
Label(up_frame, text='Perforation parameters', bg=bg1, font='Arial 9 bold').grid(row=2, column=2, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

Label(right_frame_1, text='Number of perforations (SPM) ', bg=bg3, font='Arial 8').grid(row=3, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
spm_entry = ttk.Entry(right_frame_1, width=6)
spm_entry.grid(row=3, column=1, padx=1, pady=1, sticky='w'+'e'+'n'+'s')
spm_entry.insert(0, "20")

Label(right_frame_2, text='Length ', bg=bg3, font='Arial 8').grid(row=4, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
pl_entry = ttk.Entry(right_frame_2, width=3)
pl_entry.grid(row=4, column=2, padx=10, pady=0, sticky='e')
pl_entry.insert(0, "0.7")

options_pl = ["m", "ft"]
pl_units = StringVar(value=options_pl[0])
pl_combobox = ttk.Combobox (right_frame_2, textvariable = pl_units, values=options_pl, width=2, font='Arial 8')
pl_combobox.grid(row=4, column=1,  padx=0, pady=0, sticky='w')


Label(right_frame_3, text='Hole size ', bg=bg3, font='Arial 8').grid(row=5, column=0, padx=0, pady=0, sticky='w'+'e'+'n'+'s')
dp_entry = ttk.Entry(right_frame_3, width=4)
dp_entry.grid(row=5, column=3, padx=10, pady=0, sticky='e')
dp_entry.insert(0, "8")

options_dp = ["mm", "in"]
dp_units = StringVar(value=options_pipd[0])
dp_combobox = ttk.Combobox (right_frame_3, textvariable = dp_units, values=options_dp, width=4, font='Arial 8')
dp_combobox.grid(row=5, column=1,  padx=0, pady=0, sticky='w')

#_______________________________________________________________________________________________________________
Checkbutton(up_frame, text="Injection well", variable=type_well, bg=bg1, activebackground=bg1, command=injection_well_flag).grid(row=1, column=2, sticky='w'+'e'+'n'+'s')
Checkbutton(up_frame, text="Newtonian fluid", variable=fluid_type, command=flag_fluid_type, bg=bg1, activebackground=bg1).grid(row=8, column=2, sticky='w'+'e'+'n'+'s')

Button(up_frame, text="Clear", command=Clear).grid(row=9, column=2, padx=2, pady=2, sticky='w'+'e'+'n'+'s')
Button(down_frame, text="Calculate", command=Calculate, width=30).grid(row=2, column=0, padx=5, pady=5, sticky='w')
Button(down_frame, text="Save", command=save_file).grid(row=2, column=0, padx=5, pady=5, sticky='e')

# Загрузка изображений кнопки
switch_on_img = PhotoImage(file="img_elements\switch_on.png")
switch_off_img = PhotoImage(file="img_elements\switch_off.png")
# Привязка переменной
switch_state = False
# Создаю переключатель и надпись
switch_btn = Button(up_frame, image=switch_off_img, command=toggle_switch, border=0, bg=bg1, activebackground=bg1, height=30)
switch_btn.grid(row=7, column=2, sticky='e')
Label(up_frame, text='Electrical Submersible Pump ', bg=bg1, font='Arial 8').grid(row=7, column=2, sticky='w')
Label(up_frame, text='OFF | ON', bg=bg1, font='Arial 6').grid(row=6, column=2, sticky='se', padx=0, pady=0)

#окно вывода результатов
st = ScrolledText(down_frame, width=65,  height=10, bd=1.5, font = 'Arial 10')
st.grid(row=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

#----------------------------------------------------------------------------------------------------------
def calculator():
    os.system("C:/WINDOWS/System32/calc.exe")
    return

#меню
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Сохранить", command=save_file)
# file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
# edit_menu.add_command(label="Копировать")
edit_menu.add_command(label="Calculator", command=calculator)

menu_bar.add_cascade(label="Options", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About...")
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)




          

if __name__ == '__main__':
    # Create and run the GUI   
    window.mainloop()
