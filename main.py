import math

g = 9.8066

print ('Скважина добывающая? (Y/N) ', end=" ")
type_well = input ()
if type_well == "Y" or type_well == "y" or type_well == "да" or type_well == "ДА" or type_well == "Да" or type_well == "lf" or type_well == "Lf" or type_well == "LF":
    print ('Глубина перфорации TVD (m) = ', end=" ")
    tvd = int(input ())

    print ('Диаметр лифта НКТ (m) = ', end=" ")     
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

    p_stat = (density * g * tvd)/100000

    print ('В скважине Ньютоновская жидкость? (Y/N) ', end=" ")
    fluid_type = input ()
    if fluid_type == "Y" or fluid_type == "y":
        velocity = (inj_rate / (math.pi * (pipe_diametr / 2) **2 ))
        dyn_visc = 1
        re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
        relative_roughness = (absolute_pipe_roughness / pipe_diametr)
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * pipe_lenght * density * ((velocity**2)/pipe_diametr)/100000
        pressure_bottom = p_stat - whp - friction

        print ('Скорость потока = ', round(velocity, 4), 'm/sec')
        print ('Число Рейнольдса = ', round(re, 4))
        print ('Относительная шероховатость = ', round(relative_roughness, 4))
        print ('Коэффициент трения = ', round(f, 4))
        print ('Потери на трение = ', round(friction, 4), 'bar')
        print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')
            
    else:
        print ('Показания вискозиметра при 300rpm = ', end=" ")
        mud_visc_300rpm = int(input ())

        print ('Показания вискозиметра при 3rpm = ', end=" ")
        mud_visc_3rpm = int(input ())

        velocity = (inj_rate / (math.pi * (pipe_diametr / 2) **2 ))
        n = 0.5 * math.log (mud_visc_300rpm / mud_visc_3rpm)
        k = (5.11 * mud_visc_300rpm)/(511000000**n)
        dyn_visc = k * 1000 * velocity ** n
        re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
        relative_roughness = (absolute_pipe_roughness / pipe_diametr)
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * pipe_lenght * density * ((velocity**2)/pipe_diametr)/100000
        pressure_bottom = p_stat - whp - friction
                     
        print ('Скорость потока = ', round(velocity, 4), 'm/sec')
        print ('Индекс динамики потока, n = ', round(n, 4))
        print ('Коэффициент вязкости, K = ', round(k, 4))
        print ('Число Рейнольдса = ', round(re, 4))
        print ('Относительная шероховатость = ', round(relative_roughness, 4))
        print ('Коэффициент трения = ', round(f, 4))
        print ('Потери на трение = ', round(friction, 4), 'bar')
        print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')
            
        
else: 
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

    p_stat = (density * g * tvd)/100000

    print ('В скважине Ньютоновская жидкость? (Y/N) ', end=" ")
    fluid_type = input ()
    if fluid_type == "Y" or fluid_type == "y":
        velocity = (inj_rate / (math.pi * (pipe_diametr / 2) **2 ))
        dyn_visc = 1
        re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
        relative_roughness = (absolute_pipe_roughness / pipe_diametr)
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * pipe_lenght * density * ((velocity**2)/pipe_diametr)/100000
        pressure_bottom = p_stat + whp - friction

        print ('Скорость потока = ', round(velocity, 4), 'm/sec')
        print ('Число Рейнольдса = ', round(re, 4))
        print ('Относительная шероховатость = ', round(relative_roughness, 4))
        print ('Коэффициент трения = ', round(f, 4))
        print ('Потери на трение = ', round(friction, 4), 'bar')
        print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')
            
    else:
        print ('Показания вискозиметра при 300rpm = ', end=" ")
        mud_visc_300rpm = int(input ())

        print ('Показания вискозиметра при 3rpm = ', end=" ")
        mud_visc_3rpm = int(input ())

        velocity = (inj_rate / (math.pi * (pipe_diametr / 2) **2 ))
        n = 0.5 * math.log (mud_visc_300rpm / mud_visc_3rpm)
        k = (5.11 * mud_visc_300rpm)/(511000000**n)
        dyn_visc = k * 1000 * velocity ** n
        re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
        relative_roughness = (absolute_pipe_roughness / pipe_diametr)
        f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
        friction = f * pipe_lenght * density * ((velocity**2)/pipe_diametr)/100000
        pressure_bottom = p_stat + whp - friction
                     
        print ('Скорость потока = ', round(velocity, 4), 'm/sec')
        print ('Индекс динамики потока, n = ', round(n, 4))
        print ('Коэффициент вязкости, K = ', round(k, 4))
        print ('Число Рейнольдса = ', round(re, 4))
        print ('Относительная шероховатость = ', round(relative_roughness, 4))
        print ('Коэффициент трения = ', round(f, 4))
        print ('Потери на трение = ', round(friction, 4), 'bar')
        print ('Давление на забое = ', round(pressure_bottom, 4), 'bar')


