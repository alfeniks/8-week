def atomic_mass(A, Z):
    # Константы
    m_p = 1.00727646688   # масса протона в а.е.м.
    m_n = 1.00866491588   # масса нейтрона в а.е.м.
    MeV_to_amu = 1.073544e-3  # перевод 1 МэВ в а.е.м.
    
    # Функция для вычисления энергии связи
    def binding_energy(A, Z):
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

        B = (a_v * A 
             - a_s * A**(2/3) 
             - a_c * (Z**2 / A**(1/3)) 
             - a_a * ((A - 2 * Z)**2 / A) 
             + delta)
        return B
    
    # Вычисление энергии связи
    B = binding_energy(A, Z)
    
    # Масса атома
    M_atom = Z * m_p + (A - Z) * m_n - B * MeV_to_amu
    return M_atom

# Пример для U-238
A = 238  
Z = 92   
M_U238 = atomic_mass(A, Z)
print(f"Масса атома U-238: {M_U238:.5f} а.е.м.")