import random



class Helpers:

    @staticmethod
    def generate_email():
        """Генерирует email"""
        return f"test{random.randint(1000000, 9999999)}@example.com"
