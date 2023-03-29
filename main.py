import math

print ('Скважина добывающая? (Y/N) ', end=" ")
type_well = input ()
if type_well == "Y":
        print ('Глубина перфорации TVD (м) = ', end=" ")
        tvd = input ()
        tvd_1 = int(tvd)

        print ('Диаметр лифта НКТ (м) = ', end=" ")     
        pipe_diametr = input ()
        pipe_diametr_1 = float(pipe_diametr)

        print ('Длина лифта НКТ (м) = ', end=" ")           
        pipe_lenght = input ()
        pipe_lenght_1 = int(pipe_lenght)

        print ('Абсолютная шероховатость труб (0.00002 по умолчанию) =  ', end=" ")  
        absolute_pipe_roughness = input ()
        absolute_pipe_roughness_1 = float(absolute_pipe_roughness)

        print ('Расход/дебет (м3/сек) = ', end=" ")  
        inj_rate = input ()
        inj_rate_1 = float(inj_rate)

        print ('Плотность флюида (кг/м3) = ', end=" ") 
        density = input ()
        density_1 = int(density)

        print ('Это Ньютоновская жидкость? (Y/N) ', end=" ")
        fluid_type = input ()
        if fluid_type == "Y":
            velocity = (inj_rate_1 / (math.pi * (pipe_diametr_1 / 2) **2 ))
            print ('Скорость потока = ', velocity)
        else: print ('ERROR')
else: print ('ERROR')
    

# mud_visc_300rpm = input ('Значения вискозиметра 300rpm = ')
# mud_visc_3rpm = input ('Значения вискозиметра 3rpm = ')

#print (tvd, pipe_diametr, pipe_lenght, inj_rate, densety, mud_visc_300rpm, mud_visc_3rpm)
#print("Hello World", end=" ")