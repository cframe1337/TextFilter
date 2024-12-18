# TextFilter
![License](https://img.shields.io/github/license/cframe1337/TextFilter)
![GitHub Repo stars](https://img.shields.io/github/stars/cframe1337/TextFilter)
![Repository Size](https://img.shields.io/github/repo-size/cframe1337/TextFilter)
![GitHub last commit](https://img.shields.io/github/last-commit/cframe1337/TextFilter)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/cframe1337/TextFilter/total)

### TextFilter - это инструмент для фильтрации и поиска слов в тексте с учетом различных форм транслитерации. Он позволяет конвертировать текст из транслитерации в кириллицу и искать заданные слова в преобразованном тексте.

## 🌟 Особенности

- [x] Конвертация текста из различных форм транслитерации в кириллицу
- [x] Поиск заданных слов в преобразованном тексте
- [x] Поддержка различных символов и их комбинаций для каждой буквы кириллицы
- [x] Измерение времени выполнения операций

## Требования

- Python 3.6+

## 🚀 Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cframe1337/TextFilter.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd TextFilter
   ```

## 💻 Использование
1. Подготовьте txt файл со списком ключевых слов для поиска.
2. Запустите скрипт:
   ```bash
   python main.py <input_text> <file_with_words>
   ```
3. Введите текст для фильтрации вместо `<input_text>` и название файла с словами вместо `<file_with_words>`.

## 📁 Структура проекта

- `main.py`: Основной скрипт для выполнения фильтрации и поиска
- `utils/filter_util.py`: Модуль с утилитами для фильтрации и преобразования текста
- `README.md`: Документация проекта

## 🛠️ Как это работает

1. Скрипт принимает входной текст и путь к файлу со словами.
2. Текст конвертируется из транслитерации в кириллицу с использованием предопределенного словаря соответствий.
3. В преобразованном тексте выполняется поиск слов из указанного файла.
4. Результаты поиска и время выполнения выводятся на экран.

## 🤝 Вклад в проект

Приветствуются pull request'ы. Пожалуйста, ознакомьтесь с [руководством по внесению изменений](https://github.com/cframe1337/TextFilter/blob/main/CONTRIBUTING.md) перед тем, как отправить pull request. Для крупных изменений, пожалуйста, сначала откройте issue для обсуждения предлагаемых изменений.

## 📄 Лицензия
Этот проект распространяется под лицензией [MIT](https://choosealicense.com/licenses/mit/). Подробности смотрите в файле [LICENSE](https://github.com/cframe1337/TextFilter/blob/main/LICENSE).
