def nuclear_radius(A):
    R0 = 1.2  # в фм
    R = R0 * A**(1/3)
    return R

# Пример использования для U-238
A = 238  # массовое число для U-238
R_U238 = nuclear_radius(A)
print(f"Радиус ядра U-238: {R_U238:.2f} фм")