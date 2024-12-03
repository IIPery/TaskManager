from TaskManager import TaskManager



MANAGER = TaskManager()

edit_attr = {
    '1': 'title',
    '2': 'description',
    '3': 'category',
    '4': 'due_date',
    '5': 'priority',
    '6': 'status'
}

def main() -> None:
    # Основной метод запуска программы
    while True:
        input('Нажмите Enter чтобы продолжить')

        print('\n### Меню TaskManager ###')
        print('[1] - Список текущих задач')
        print('[2] - Поиск задач')
        print('[3] - Редактирование задач')
        print('[4] - Добавление задачи')
        print('[5] - Удаление задачи')
        print('[6] - Выход')


        choice = input('\nВведите номер пункта: ')


        if choice == '1':
            # [1] - Список текущих задач
            MANAGER.show_tasks()

        elif choice == '2':
            # [2] - Поиск задач
            print('\n[1] - Поиск по ключевому слову')
            print('[2] - Поиск по категориям')
            print('[3] - Поиск по статусу')

            choice_num = input('Введите номер пункта: ')  # вывод инпутов и подсказок
            if choice_num == '2':
                categories = set(task.category for task in MANAGER.tasks)
                print(f'Используемые категории: {", ".join(categories)}')
            if choice_num == '3':
                print('Используемые статусы: в ожидании, в работе, выполнен')
            search = input('Поиск: ').lower()

            if choice_num not in '123':
                print('\nОШИБКА ВВОДА. Неверный номер пункта')
                continue
            if not search:
                print('\nОШИБКА ВВОДА. Поиск не может быть пустым')
                continue

            result = MANAGER.search(choice_num, search)
            if result:
                for item in result:
                    print(item.__str__())
            else:
                print('Ничего не найдено')

        elif choice == '3':
            # [3] - Редактирование задач
            selected = int(input('Введите номер задачи: '))
            task = next((item for item in MANAGER.tasks if item.id == selected), None)
            if not task:
                print('Ничего не найдено')
                continue

            print('[1] - Название   [4] - Срок выполнения')
            print('[2] - Описание   [5] - Приоритет')
            print('[3] - Категория  [6] - Статус')

            num_attr = input('Введите номер аттрибута который хотите изменить: ')
            if num_attr == '6':
                print("в ожидании -> в работе -> выполнен")
            if num_attr == '4':
                print("Форма даты: гггг-мм-дд")
            text = input('Введите новое значение: ').lower()


            if num_attr not in edit_attr:
                print('ОШИБКА ВВОДА. Неверный номер аттрибута')
                continue
            elif num_attr == '4':
                if MANAGER.valid_date(text):
                    pass
                else:
                    print('ОШИБКА ВВОДА. Неверная форма даты')
                    continue
            elif num_attr == '6':
                if text in ('в ожидании', 'в работе', 'выполнен'):
                    pass
                else:
                    print("ОШИБКА ВВОДА. Неверный статус")
                    continue


            selected_attr = edit_attr[num_attr]
            MANAGER.edit_task(task, selected_attr, text)
            print('Задача обновлена')

        elif choice == '4':
            # [4] - Добавление задачи
            try:
                title = input('\nНазвание: ').lower()
                description = input('Описание: ').lower()
                category = input('Категория: ').lower()
                due_date = input('Срок выполнения(гггг-мм-дд): ')
                priority = input('Приоритет(низкий, средний, высокий): ').lower()

                if MANAGER.valid_date(due_date):
                    pass
                else:
                    print('ОШИБКА ВВОДА. Неверная форма даты')
                    continue
                if title and description and category and due_date and priority:
                    get_id = MANAGER.add_task(title, description, category, due_date, priority)
                    print(f'Задача № {get_id} успешно добавлена')
                else:
                    print('ОШИБКА ВВОДА. Все поля должны быть заполнены')
            except ValueError:
                print('ОШИБКА ВВОДА. Срок выполнения должно быть числом')

        elif choice == '5':
            # [5] - Удаление задачи
            try:
                selected = int(input('Введите номер задачи: '))
                task_removed = MANAGER.remove_task(selected)
                if task_removed:
                    print(f'Задача № {selected} успешно удалена')
                else:
                    print('Ничего не найдено')
            except ValueError:
                print('ОШИБКА ВВОДА. Номер должен быть числом')

        elif choice == '6':
            # [6] - Выход
            print('\nВсего хорошего!')
            exit()

        else:
            print('ОШИБКА ВВОДА. Введите номер пункта')


if __name__ == '__main__':
    main()
