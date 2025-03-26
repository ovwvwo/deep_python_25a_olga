# TODO: Implement
# 01/test_predict_message_mood.py
import unittest
from predict_message_mood import predict_message_mood

class TestPredictMessageMood(unittest.TestCase):
    
    def test_predict_message_mood(self):
        # Тесты для различных порогов
        self.assertEqual(predict_message_mood("Чапаев и пустота"), "отл")
        self.assertEqual(predict_message_mood("Чапаев и пустота", 0.8, 0.99), "норм")
        self.assertEqual(predict_message_mood("Вулкан"), "неуд")

if __name__ == "__main__":
    unittest.main()
