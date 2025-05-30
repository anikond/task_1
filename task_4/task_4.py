def g(n):
    x = n
    # Удаляем нули на конце
    while n % 10 == 0:
        n //= 10
    return n / x

unique_values = set()

for k in range(0, 30):
    n = 43 * 10**k
    unique_values.add(g(n))

print("Уникальные значения g(n):", sorted(unique_values))
print("Количество:", len(unique_values))
