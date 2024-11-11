def binding_energy_per_nucleon(A, Z):
    # константы в формуле
    a_v = 15.8
    a_s = 18.3
    a_c = 0.714
    a_a = 23.2
    
    if A % 2 == 0 and Z % 2 == 0:
        delta = 12
    elif A % 2 == 1 and Z % 2 == 1:
        delta = -12
    else:
        delta = 0

    # формула
    B = (a_v * A 
         - a_s * A**(2/3) 
         - a_c * (Z**2 / A**(1/3)) 
         - a_a * ((A - 2 * Z)**2 / A) 
         + delta)
    
    # энергия нуклона
    E_b = B / A
    return E_b

# пример на U-238
A = 238  
Z = 92  
E_b_U238 = binding_energy_per_nucleon(A, Z)
print(f"Удельная энергия связи для U-238: {E_b_U238:.2f} МэВ/нуклон")
