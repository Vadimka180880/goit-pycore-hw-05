import os

def main(log_file_path):
    # Відкриття файлу журналу для читання
    with open(log_file_path, "r") as file:
        # Читання рядків з файлу
        for line in file:
            print(line)

    # Файл автоматично закриється при виході з контексту 'with'

if __name__ == "__main__":
    # Отримання повного шляху до поточної директорії
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Формування шляху до файлу журналу в поточній директорії
    log_file_path = os.path.join(current_dir, "logfile.log")

    # Відкриваємо файл журналу у режимі запису
    with open(log_file_path, "w") as file:
        # Записуємо деякі логи
        file.write("INFO: This is an information message\n")
        file.write("DEBUG: This is a debug message\n")
        file.write("ERROR: This is an error message\n")
        file.write("WARNING: This is a warning message\n")

    # Викликаємо функцію main та передаємо їй шлях до файлу журналу
    main(log_file_path)

