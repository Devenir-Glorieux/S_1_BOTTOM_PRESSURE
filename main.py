import math

print ('Скважина добывающая? (Y/N) ', end=" ")
type_well = input ()
if type_well == "Y":
        print ('Глубина перфорации TVD (m) = ', end=" ")
        tvd = input ()
        tvd_1 = int(tvd)

        print ('Диаметр лифта НКТ (m) = ', end=" ")     
        pipe_diametr = input ()
        pipe_diametr_1 = float(pipe_diametr)

        print ('Длина лифта НКТ (m) = ', end=" ")           
        pipe_lenght = input ()
        pipe_lenght_1 = int(pipe_lenght)

        print ('Абсолютная шероховатость труб (0.00002 по умолчанию) =  ', end=" ")  
        absolute_pipe_roughness = input ()
        absolute_pipe_roughness_1 = float(absolute_pipe_roughness)

        print ('Расход/дебет (m3/sec) = ', end=" ")  
        inj_rate = input ()
        inj_rate_1 = float(inj_rate)

        print ('Плотность флюида (kg/m3) = ', end=" ") 
        density = input ()
        density_1 = int(density)

        print ('Это Ньютоновская жидкость? (Y/N) ', end=" ")
        fluid_type = input ()
        if fluid_type == "Y":
            velocity = (inj_rate_1 / (math.pi * (pipe_diametr_1 / 2) **2 ))
            dyn_visc = 1
            re = (density_1 * pipe_diametr_1 * velocity) / (dyn_visc / 1000)
            relative_roughness = (absolute_pipe_roughness_1 / pipe_diametr_1)
            f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
            friction = f * pipe_lenght_1 * density_1 * ((velocity**2)/pipe_diametr_1)/100000
            print ('Скорость потока = ', velocity, 'm/sec')
            print ('Число Рейнольдса = ', re)
            print ('Относительная шероховатость = ', relative_roughness)
            print ('Коэффициент трения = ', f)
            print ('Потери на трение = ', friction, 'bar')

        else: 
            print ('Показания вискозиметра при 300rpm = ', end=" ")
            mud_visc_300rpm = input ()
            mud_visc_300rpm_1 = int(mud_visc_300rpm)

            print ('Показания вискозиметра при 3rpm = ', end=" ")
            mud_visc_3rpm = input ()
            mud_visc_3rpm_1 = int(mud_visc_3rpm)

            velocity = (inj_rate_1 / (math.pi * (pipe_diametr_1 / 2) **2 ))
            n = 0.5 * math.log (mud_visc_300rpm_1 / mud_visc_3rpm_1)
            k = (5.11 * mud_visc_300rpm_1)/(511000000**n)
            dyn_visc = k * 1000 * velocity ** n
            re = (density_1 * pipe_diametr_1 * velocity) / (dyn_visc / 1000)
            relative_roughness = (absolute_pipe_roughness_1 / pipe_diametr_1)
            f = (-1.8 * math.log10((6.9/re) + (relative_roughness/3.7)**1.11))**-2
            friction = f * pipe_lenght_1 * density_1 * ((velocity**2)/pipe_diametr_1)/100000
             
            print ('Скорость потока = ', velocity, 'm/sec')
            print ('Индекс динамики потока, n = ', n)
            print ('Коэффициент вязкости, K = ', k)
            print ('Число Рейнольдса = ', re)
            print ('Относительная шероховатость = ', relative_roughness)
            print ('Коэффициент трения = ', f)
            print ('Потери на трение = ', friction, 'bar')
            
        
else: print ('ERROR')
    

