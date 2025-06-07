# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цера: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."

class HouseholdChemicals(Product):
    """
    Класс для бытовой химии, наследует Product.
    """
    def __init__(self, name, price, application_area, volume_ml):
        super().__init__(name, price)
        self.application_area = application_area  # для чего применяется
        self.volume_ml = volume_ml  # объем в мл

    def get_details(self):
        return f"Бытовая химия: {self.name}, Область применения: {self.application_area}, Объем: {self.volume_ml} мл, Цена: {self.price} руб."
