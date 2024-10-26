class LowFuelError(Exception):
    """Исключение, если низкий уровень топлива"""
    pass

class NotEnoughFuel(Exception):
    """Исключение, если топлива недостаточно"""
    pass

# Объявляем исключение для перегруза груза
class CargoOverload(Exception):
    """Исключение, если слишком большой вес"""
    pass