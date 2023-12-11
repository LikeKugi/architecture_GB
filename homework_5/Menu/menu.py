from .Menu_Variants import MenuVariants

_T = [MenuVariants | None]


def print_menu(type_of_menu: _T = None):
    match type_of_menu:
        case MenuVariants.BASE:
            print("1. Открыть проект")
            print("2. Посмотреть доступные проекты")
            print("3. Создать новый проект")
            print("0. ЗАВЕРШЕНИЕ РАБОТЫ ПРИЛОЖЕНИЯ")
        case MenuVariants.OPEN:
            print("1. Введите имя проекта")
            print("0. ОТМЕНА")
        case MenuVariants.PROJECT:
            print("1. Сохранить проект")
            print("2. Отобразить параметры проекта")
            print("3. Отобразить все модели проекта")
            print("4. Отобразить все текстуры проекта")
            print("5. Выполнить рендер всех моделей")
            print("6. Выполнить рендер модели")
            print("0. ОТМЕНА")
        case _:
            print("Goodbye")
