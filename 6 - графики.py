import matplotlib.pyplot as plt
import numpy as np

# изотопы
isotopes = [
    {"A": 238, "Z": 92, "name": "U-238"},
    {"A": 239, "Z": 94, "name": "Pu-239"},
    {"A": 252, "Z": 98, "name": "Cf-252"},
    {"A": 135, "Z": 52, "name": "Te-135"},
    {"A": 60, "Z": 28, "name": "Ni-60"},
    {"A": 16, "Z": 8, "name": "O-16"},
]

# функции
def nuclear_radius(A):
    R0 = 1.2  # в ферми
    return R0 * A**(1/3)

def binding_energy_per_nucleon(A, Z):
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
    B = (a_v * A - a_s * A**(2/3) - a_c * (Z**2 / A**(1/3)) - a_a * ((A - 2 * Z)**2 / A) + delta)
    return B / A

# данные для графиков
Z_values = [iso["Z"] for iso in isotopes]
radii = [nuclear_radius(iso["A"]) for iso in isotopes]
binding_energies = [binding_energy_per_nucleon(iso["A"], iso["Z"]) for iso in isotopes]
A_values = [iso["A"] for iso in isotopes]

# 1. График радиуса ядра в зависимости от Z
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(Z_values, radii, marker='o', linestyle='-', color='b')
plt.xlabel("Число протонов (Z)")
plt.ylabel("Радиус ядра (фм)")
plt.title("Радиус ядра в зависимости от числа протонов (Z)")
plt.grid(True)

# 2. График удельной энергии связи в зависимости от массового числа A
plt.subplot(1, 2, 2)
plt.plot(A_values, binding_energies, marker='o', linestyle='-', color='r')
plt.xlabel("Массовое число (A)")
plt.ylabel("Удельная энергия связи (МэВ/нуклон)")
plt.title("Удельная энергия связи в зависимости от массового числа (A)")
plt.grid(True)

plt.tight_layout()
plt.show()