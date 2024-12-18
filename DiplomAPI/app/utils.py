import json  # Импортируем модуль для работы с JSON-файлами


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в строку JSON и сохраняет её в файл.
    :param dict_list: Список словарей, которые нужно преобразовать
    :param filename: Имя файла, в который будет сохранён JSON
    :return: Строка JSON, если успешно, иначе None
    """
    try:
        # Преобразование списка словарей в JSON-строку с поддержкой Юникода
        json_str = json.dumps(dict_list, ensure_ascii=False)
        # Запись JSON-строки в файл с кодировкой UTF-8
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str  # Возврат JSON-строки
    except (TypeError, ValueError, IOError) as i:
        # Обработка ошибок при преобразовании или записи в файл
        print(f"Ошибка преобразования списка словарей в JSON или записи в файл: {i}")
        return None


def json_to_dict_list(filename):
    """
    Считывает JSON-данные из файла и преобразует их в список словарей.
    :param filename: Имя файла, из которого будет считан JSON
    :return: Список словарей, если успешно, иначе None
    """
    try:
        # Открытие файла для чтения с кодировкой UTF-8
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()  # Чтение содержимого файла
        # Преобразование JSON-строки в список словарей
        dict_list = json.loads(json_str)
        return dict_list  # Возврат списка словарей
    except (TypeError, ValueError, IOError) as e:
        # Обработка ошибок при чтении файла или преобразовании JSON
        print(f"Ошибка чтения JSON из файла или преобразования в список словарей: {e}")
        return None


'''
В этом коде два метода: один для сохранения списка словарей в формате JSON в файл, 
а другой для чтения JSON-данных из файла и преобразования их обратно в список словарей.
Каждый метод обрабатывает возможные ошибки, чтобы предотвратить сбой выполнения программы.
'''