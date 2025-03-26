# 01/predict_message_mood.py

class SomeModel:
    def predict(self, message: str) -> float:
        # Здесь может быть заглушка или реальная логика
        return 0.9  # Примерный результат

def predict_message_mood(
    message: str,
    bad_threshold: float = 0.3,
    good_threshold: float = 0.8,
) -> str:
    model = SomeModel()
    prediction = model.predict(message)
    
    if prediction < bad_threshold:
        return "неуд"
    elif prediction > good_threshold:
        return "отл"
    else:
        return "норм"

