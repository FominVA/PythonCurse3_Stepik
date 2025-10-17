def sandwich(func):
    def wrapper(*args, **kwargs):
        return '---- Верхний ломтик хлеба ----' + str(func(*args, **kwargs)) + "/n" + '---- Нижний ломтик хлеба ----'
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])