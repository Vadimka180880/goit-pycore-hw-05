
def caching_fibonacci(n, cache={}):
    if n <= 0:                                                                          # Базовий випадок: якщо n менше або дорівнює 0, повертаємо 0
        return 0
    elif n == 1:                                                                        # Базовий випадок: якщо n дорівнює 1, повертаємо 1
        return 1
    elif n not in cache:                                                                # Перевіряємо, чи вже є значення n у кеші
        cache[n] = caching_fibonacci(n - 1, cache) + caching_fibonacci(n - 2, cache)    # Якщо немає, рекурсивно обчислюємо n-те число Фібоначчі

    return cache[n]                                                                     # Повертаємо значення n-го числа Фібоначчі

print(caching_fibonacci(10))                                                            # Виводимо 10-те число Фібоначчі
print(caching_fibonacci(15))                                                            # Виводимо 15-те число Фібоначчі