from Menu import MenuVariants, print_menu
from Database import Database, File
from Editor import Editor


def choose_variant(menu: MenuVariants) -> int:
    variant = 0
    print_menu(menu)
    try:
        variant = int(input('Choose one: '))
    except Exception as e:
        print(e)
        print('Sorry, that variant is unavailable')
    finally:
        return variant


def load_file():
    print('\nLoad File:\n')
    print_menu(MenuVariants.OPEN)
    filename = input('Choose file: ')
    if filename == '0':
        return
    file = Database().load(filename)
    return file


def work_with_editor(file):
    progressing = True
    Editor().load_project(file)

    while progressing:
        print('\nEditor:\n')
        result = choose_variant(MenuVariants.PROJECT)
        if result:
            match_variant_file(result)
        else:
            progressing = False


def match_variant_file(variant: int) -> None:
    match variant:
        case 1:
            Editor().save_project()
        case 2:
            Editor().show_project_settings()
        case 3:
            Editor().print_entities()
        case 5:
            Editor().render_models()
        case 6:
            Editor().render_all_models()
        case _:
            return


def create_new_project():
    filename = input('enter filename: ')
    file = File(filename, [0, 0, 0], [1, 1, 1], [2, 2, 2])
    Editor().load_project(file)
    Editor().save_project()


def match_variant_menu(variant: int) -> None:
    assert 0 < variant < 7, 'should be valid variant'
    match variant:
        case 1:
            file = load_file()
            if file:
                work_with_editor(file)
        case 2:
            print("Available projects: ", *Database().view_projects(), sep='\n ---> ')
        case 3:
            create_new_project()
        case _:
            return


def main():
    progressing = True
    while progressing:
        print('\nMain Menu\n')
        result = choose_variant(MenuVariants.BASE)
        if 0 < result < 8:
            print(result)
            match_variant_menu(result)
        else:
            print_menu()
            progressing = False


if __name__ == '__main__':
    Database()
    main()
