# 01/filtered_file_reader.py

def filtered_file_reader(file, search_words, stop_words):
    """
    Генератор, который читает строки из файла, фильтруя по словам поиска и стоп-словам.
    """
    for line in file:
        line = line.strip().lower()  # Приводим строку к нижнему регистру
        words = set(line.split())  # Разбиваем строку на слова
        
        if any(word in words for word in search_words) and not any(stop_word in words for stop_word in stop_words):
            yield line

