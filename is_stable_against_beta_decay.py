def is_stable_against_beta_decay(A, Z):
    N = A - Z
    # Коэффициент стабильности для легких и тяжелых ядер
    if A <= 40:  # легкие элементы
        stability_ratio = 1.0
    else:  # тяжелые элементы
        stability_ratio = 1.5

    # Проверка стабильности
    if N / Z > stability_ratio:
        return "Неустойчив к β⁻-распаду (избыток нейтронов)"
    elif N / Z < 1 / stability_ratio:
        return "Неустойчив к β⁺-распаду (избыток протонов)"
    else:
        return "Устойчив к β-распаду"

# Пример использования для U-238
A = 238  # массовое число для U-238
Z = 92   # атомный номер урана
stability_U238 = is_stable_against_beta_decay(A, Z)
print(f"U-238: {stability_U238}")