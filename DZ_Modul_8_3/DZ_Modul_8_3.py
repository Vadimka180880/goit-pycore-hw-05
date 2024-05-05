import argparse
import re

def count_logs(log_file):
    """
    Підраховує кількість записів для кожного рівня логування у файлі журналу.

    Args:
        log_file (str): Шлях до файлу журналу.

    Returns:
        dict: Словник, де ключі - це рівні логування, а значення - кількість записів.
    """
    levels_count = {"INFO": 0, "DEBUG": 0, "ERROR": 0, "WARNING": 0}

    # Відкриваємо файл журналу і зчитуємо його рядок за рядком
    with open(log_file, 'r') as file:
        for line in file:
            # Використовуємо регулярний вираз для знаходження рівня логування у кожному рядку
            match = re.search(r'\b(INFO|DEBUG|ERROR|WARNING)\b', line)
            if match:
                level = match.group()
                levels_count[level] += 1

    return levels_count

def print_log_stats(log_file, log_level=None):
    """
    Виводить статистику про рівні логування та, за потреби, деталізовану інформацію про певний рівень логування.

    Args:
        log_file (str): Шлях до файлу журналу.
        log_level (str, optional): Рівень логування, для якого виводяться деталі. За замовчуванням None.
    """
    # Отримуємо кількість записів для кожного рівня логування
    levels_count = count_logs(log_file)

    # Виводимо заголовок
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    # Виводимо статистику для кожного рівня логування
    for level, count in levels_count.items():
        print(f"{level:<17}| {count}")

    # Якщо вказано рівень логування для деталізації, виводимо його деталі
    if log_level:
        print(f"\nДеталі логів для рівня '{log_level}':")
        with open(log_file, 'r') as file:
            for line in file:
                if log_level in line:
                    print(line.strip())

def main():
    parser = argparse.ArgumentParser(description="Process log files")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("loglevel", nargs="?", default=None, help="Log level")

    args = parser.parse_args()

    log_file = args.logfile
    log_level = args.loglevel

    print(f"Log file path: {log_file}")
    print(f"Log level: {log_level}")

    print_log_stats(log_file, log_level)

if __name__ == "__main__":
    main()
