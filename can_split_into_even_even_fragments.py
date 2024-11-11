def can_split_into_even_even_fragments(A, Z):
    N = A - Z  # число нейтронов

    # Проверяем, что A, Z и N все четные
    if A % 2 == 0 and Z % 2 == 0 and N % 2 == 0:
        return "Можно разделить на два одинаковых четно-четных осколка"
    else:
        return "Невозможно разделить на два одинаковых четно-четных осколка"

# Пример использования для U-238
A = 238  # массовое число для U-238
Z = 92   # атомный номер урана
split_U238 = can_split_into_even_even_fragments(A, Z)
print(f"U-238: {split_U238}") 