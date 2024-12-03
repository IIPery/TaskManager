import pytest
from TaskManager import TaskManager, Task


@pytest.fixture
def task_manager():
    manager = TaskManager()
    manager.tasks = []
    return manager

def test_add_task(task_manager):
    task_manager.add_task(
        'test title',
        'description',
        'category',
        '3000-06-15',
        'priority'
    )
    assert len(task_manager.tasks) == 1
    task = task_manager.tasks[0]
    assert task.id == 1
    assert task.title == 'test title'
    assert task.due_date == '3000-06-15'
    assert task.status == 'в ожидании'

def test_search_keyword_and_category(task_manager):
    task_manager.add_task('task', 'desc', 'cat', '3000-06-15', 'pri')
    task_manager.add_task('задача', 'описание', 'cat', '3000-06-15', 'при')

    result = task_manager.search('1', 'desc')
    assert len(result) == 1

    cat_result = task_manager.search('2', 'cat')
    assert len(cat_result) == 2

def test_task_edit(task_manager):
    task_manager.add_task('task', 'desc', 'cat', '3000-06-15', 'pri')
    task = task_manager.tasks[0]

    task_manager.edit_task(task, 'title', 'new task')
    task_manager.edit_task(task, 'status', 'в работе')
    assert task.title == 'new task'
    assert task.status == 'в работе'

def test_remove_task(task_manager):
    task_manager.add_task('task', 'desc', 'cat', '3000-06-15', 'pri')
    assert len(task_manager.tasks) == 1

    task_removed = task_manager.remove_task(1)
    assert task_removed is True
    assert len(task_manager.tasks) == 0

    tsk_removed = task_manager.remove_task(999)
    assert tsk_removed is False



