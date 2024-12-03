import json
from typing import Dict, Any

class Task:
    # Класс объекта задачи
    def __init__(
            self,
            id: int,
            title: str,
            description: str,
            category: str,
            due_date: str,
            priority: str,
            status='в ожидании'
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self) -> str:
        result = f'''
        № {self.id}, Название: {self.title},
        Описание: {self.description},
        Категория: {self.category}, Срок выполнения: {self.due_date},
        Приоритет: {self.priority}, Статус: {self.status}'''
        return result


    def to_json(self) -> Dict[str, Any]:
        # Преобразование объект Task в JSON
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status
        }
        return data

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'Task':
        # Создание объекта Task из JSON
        if isinstance(data, str):
            data = json.loads(data)
        return cls(**data)

