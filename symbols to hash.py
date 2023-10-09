import hashlib
import secrets
import string

while True:
    # Задаем строку
    hwid = input("Введите строку: ")

    # Проверяем, является ли введенная строка пустой или равной "0"
    if hwid == "" or hwid == "0":
        # Генерируем случайную строку из 65 символов
        random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(65))
        combined_string = random_string

        # Выводим в случае 0 или пустоты
        print("Сгенерированное значение:", combined_string)
    else:
        # Вооплащаем
        combined_string = hwid + "71QNzN7t8v"

    # Создаем
    sha1_hash = hashlib.sha1(combined_string.encode("utf-8")).hexdigest().upper()

    # Выводим
    print("Хэш строки:", sha1_hash)
