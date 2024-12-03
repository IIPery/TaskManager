import json
from typing import List
from datetime import datetime

from Task import Task

DATA = 'task_db.json'


class TaskManager:
    # Класс для управления задачами
    def __init__(self) -> None:
        # Инициализация, загрузка данных из JSON
        self.data: str = DATA
        self.tasks: List[Task] = self.get_tasks_from_json()

    def load_db(self) -> List[dict]:
        # Загрузка бд из JSON. Если файла нет - создает пустой JSON
        try:
            with open(self.data, 'r', encoding='utf-8') as file:
                loaded_data = json.load(file)
                return loaded_data
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.data, "w", encoding="utf-8") as file:
                json.dump([], file)
            return []

    def dump_file(self) -> None:
        # Сохраняет текущий список Task в JSON
        with open(self.data, 'w', encoding='utf-8') as file:
            tasks = [task.to_json() for task in self.tasks]
            json.dump(tasks, file, ensure_ascii=False, indent=4)

    def get_tasks_from_json(self) -> List[Task]:
        # Возвращает список Task из JSON
        data = self.load_db()
        tasks = [Task.from_json(item) for item in data]
        return tasks

    def generate_id(self) -> int:
        # Генерация id для новой задачи
        new_id = (max(task.id for task in self.tasks) + 1 if self.tasks else 1)
        return new_id

    def valid_date(self, due_date: str) -> bool:
        # Проверка формы даты
        try:
            date_obj = datetime.strptime(due_date, '%Y-%m-%d')
            if date_obj.date() < datetime.today().date():
                print('ОШИБКА ВВОДА. Дата не может быть раньше чем сегодняшний день')
                return False
            return True
        except ValueError:
            return False



    def show_tasks(self) -> None:
        # Выводит список всех задач
        if len(self.tasks) == 0:
            print('Список задач пуст')
        else:
            for item in self.tasks:
                print(item.__str__())

    def search(self, choice_num: str, search: str) -> List[Task]:
        # Поиск задач по ключевому слову, категории и статусу
        result = []

        for item in self.tasks:
            if choice_num == '1' and (search in item.title or
                                      search in item.description):
                result.append(item)
            if choice_num == '2' and search in item.category:
                result.append(item)
            if choice_num == '3' and search in item.status:
                result.append(item)

        return result

    def edit_task(self, task: 'Task', selected_attr: str, text: str) -> None:
        # Редактирование аттрибутов задачи, выбранной по id
        setattr(task, selected_attr, text)
        self.dump_file()
        return

    def add_task(
            self,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str
    ) -> None:
        # Добавление новой задачи
        new_id = self.generate_id()
        new_task = Task(new_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.dump_file()
        return new_id

    def remove_task(self, selected: int) -> bool:
        # Удаление задачи по id
        for item in self.tasks:
            if item.id == selected:
                self.tasks.remove(item)
                self.dump_file()
                return True
        return False
