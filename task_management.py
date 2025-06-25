class TaskList:
    def __init__(self):
        self.__task_list = []

    def __is_task_in_list(self, task):
        for t in self.__task_list:
            if t['name'] == task:
                return True
        return False  

    def add_task(self, task):
        if not self.__is_task_in_list(task):
            self.__task_list.append({'name': task, 'done': False})
            print(f'Задача "{task}" добавлена в списко')
        else:
            print(f'Задача "{task}" уже есть в списке')

    def remove_task(self, task_name):
        if self.__is_task_in_list(task_name):
            self.__task_list.remove(task_name)
            print(f'Задача "{task_name}" удалена из списка')
        else:
            print(f'Задачи "{task_name}" нет в списке')

task_list = TaskList()
task_list.add_task("Task 1")
print(task_list._TaskList__task_list)

# Проверяем добавление новой задачи в пустой список с помощью метода add_task()
task_list = TaskList()
task_list.add_task("Task 1")
print(task_list._TaskList__task_list)

# Проверяем добавление дублирующихся задач в список при работе метода add_task()
task_list = TaskList()
task_list.add_task("Task 1")
task_list.add_task("Task 2")
task_list.add_task("Task 2")
task_list.add_task("Task 3")
print(task_list._TaskList__task_list)

# Проверяем работу приватного метода __is_task_in_list()
task_list = TaskList()
task_list.add_task("Task 1")
task_list.add_task("Task 2")
print(task_list._TaskList__is_task_in_list("Task 2"))