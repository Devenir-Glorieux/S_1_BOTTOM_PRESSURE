import math

print ('Скважина добывающая? (Y/N) ', end=" ")
type_well = input ()
if type_well == "Y" or type_well == "y":
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

        print ('Плотность флюида (kg/m3) = ', end=" ") 
        density = int(input ())

        print ('Это Ньютоновская жидкость? (Y/N) ', end=" ")
        fluid_type = input ()
        if fluid_type == "Y" or fluid_type == "y":
            velocity = (inj_rate / (math.pi * (pipe_diametr / 2) **2 ))
            dyn_visc = 1
            re = (density * pipe_diametr * velocity) / (dyn_visc / 1000)
            relative_roughness = (absolute_pipe_roughness / pipe_diametr)
            f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
            friction = f * pipe_lenght * density * ((velocity**2)/pipe_diametr)/100000
            print ('Скорость потока = ', round(velocity, 4), 'm/sec')
            print ('Число Рейнольдса = ', round(re, 4))
            print ('Относительная шероховатость = ', round(relative_roughness, 4))
            print ('Коэффициент трения = ', round(f, 4))
            print ('Потери на трение = ', round(friction, 4), 'bar')

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
             
            print ('Скорость потока = ', round(velocity, 4), 'm/sec')
            print ('Индекс динамики потока, n = ', round(n, 4))
            print ('Коэффициент вязкости, K = ', round(k, 4))
            print ('Число Рейнольдса = ', round(re, 4))
            print ('Относительная шероховатость = ', round(relative_roughness, 4))
            print ('Коэффициент трения = ', round(f, 4))
            print ('Потери на трение = ', round(friction, 4), 'bar')
            
        
else: print ('ERROR')
    

