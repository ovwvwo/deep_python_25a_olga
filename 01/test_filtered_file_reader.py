# 01/test_filtered_file_reader.py
import unittest
from filtered_file_reader import filtered_file_reader

class TestFilteredFileReader(unittest.TestCase):
    
    def test_filtered_file_reader(self):
        test_data = [
            "а Роза упала на лапу Азора",
            "Это просто строка для проверки",
            "Вулкан и Роза",
            "Это должно быть проигнорировано Азора"
        ]
        
        # Эмулируем файл с помощью StringIO
        from io import StringIO
        file = StringIO("\n".join(test_data))
        
        search_words = ["роза", "вулкан"]
        stop_words = ["азора"]
        
        result = list(filtered_file_reader(file, search_words, stop_words))
        
        expected = [
            "а Роза упала на лапу Азора",  # Слово "роза" найдено
            "Вулкан и Роза",               # Слово "вулкан" найдено
        ]
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
