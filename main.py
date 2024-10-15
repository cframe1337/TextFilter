"""
TextFilter: Модуль для фильтрации и преобразования транслитерированного текста.

Этот модуль предоставляет функциональность для преобразования текста из транслита
в обычный текст и поиска ключевых слов из заданного списка. Он может быть использован
для модерации контента в социальных сетях или для поиска по ключевым словам.
"""

import re
import sys
import time

from utils.filter_util import Filters as f


abc_db = [
    {"а": [
        "A", "a", "2", "0", "а", "А", "𝕒", "𝔸"
    ]},
    {"б": [
        "B", "b", "8", "6", "Б", "б", "𝕓", "𝔹"
    ]},
    {"в": [
        "B", "8", "V", "v", "В", "в", "𝕧", "𝕍"
    ]},
    {"г": [
        "G", "g", "7", "Г", "г", "𝕘", "𝔾"
    ]},
    {"д": [
        "D", "d", "Д", "д", "𝕕", "𝔻"
    ]},
    {"е": [
        "E", "e", "3", "Е", "е", "𝕖", "𝔼"
    ]},
    {"ё": [
        "Е", "е", "E", "e", "3", "𝕖", "𝔼"
    ]},
    {"ж": {
        "ZH", "zh", "Ж", "ж", "𝕫𝕙", "ℤℍ"
    }},
    {"з": [
        "Z", "z", "3", "З", "З", "𝕫", "ℤ"
    ]},
    {"и": [
        "N", "u", "U", "i", "II", "И", "и", "𝕚", "𝕀"
    ]},
    {"й": [
        "N", "u", "U", "i", "II", "й", "й", "ьи", "ЬИ", "𝕚", "𝕀"
    ]},
    {"к": [
        "K", "к", "К", "к", "𝕜", "𝕂"
    ]},
    {"л": [
        "L", "l", "Il", "il", "Л", "л", "𝕝", "𝕃"
    ]},
    {"м": [
        "M", "m", "М", "м", "𝕞", "𝕄"
    ]},
    {"н": [
        "N", "n", "H", "Н", "н", "𝕟", "ℕ"
    ]},
    {"о": [
        "O", "o", "0", "О", "о", "𝕠", "𝕆"
    ]},
    {"п": [
        "P", "p", "5", "П", "п", "𝕡", "ℙ"
    ]},
    {"р": [
        "P", "p", "Р", "р", "𝕡", "𝕣", "r", "R", "ℙ", "ℝ", "𝕣"
    ]},
    {"с": [
        "S", "s", "3", "С", "с", "𝕤", "𝕊"
    ]},
    {"т": [
        "T", "t", "2", "Т", "т", "𝕥", "𝕋"
    ]},
    {"у": [
        "Y", "y", "U", "u", "У", "У", "𝕪", "𝕐"
    ]},
    {"ф": [
        "F", "f", "Ф", "ф", "𝕗", "𝔽"
    ]},
    {"х": [
        "X", "x", "h", "H", "Х", "х", "𝕙", "ℍ"
    ]},
    {"ц": [
        "Ц", "ц"
    ]},
    {"ч": [
        "CH", "ch", "4", "Ч", "ч", "𝕔𝕙", "ℂℍ"
    ]},
    {"ш": [
        "SH", "sh", "6", "ш", "Ш", "W", "w", "𝕤𝕙", "𝕨", "𝕎"
    ]},
    {"щ": [
        "SH", "sh", "Щ", "щ", "𝕤𝕙", "𝕊ℍ"
    ]},
    {"ь": [
        "b", "Ь", "ь", "6"
    ]},
    {"ы": {
        "bI", "bl", "Ы", "𝕓𝕝", "𝕓𝕀"
    }},
    {"ъ": [
        "ъ", "Ъ"
    ]},
    {"э": [
        "E", "e", "3", "э", "Э", "𝔼", "𝕖"
    ]},
    {"ю": [
        "YU", "yu", "ю", "Ю", "U", "u", "𝕪𝕦", "𝕐𝕌"
    ]},
    {"я": [
        "Я", "я", "YA", "ya", "Z", "z", "𝕫", "ℤ"
    ]}
]


def find_word(inp_msg: str, file: str) -> any:
    """
    Основная функция для конвертации и нахождения слов из списка.

    :param inp_msg:
    :param file:
    :return:
    """
    with open(f'{file}', 'r', encoding='utf-8') as _f:
        _bl = re.split(r'[,\s]+', _f.read())
        print(f"ConvertedToRu: {f.convert_to_ru(inp_msg, abc_db)}\n")
        for _w in _bl:
            if _w in f.convert_to_ru(inp_msg, abc_db):
                print(f"Found: {_w}")
                return True
        return False


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(f"Line: {sys.argv[1]}")
    print(f"File: {sys.argv[2]}")
    print(f"Result: {str(find_word(sys.argv[1], sys.argv[2]))}")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.3f} seconds")
