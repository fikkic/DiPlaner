import sys
import json
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate

# Путь к файлу задач
TASKS_FILE = "tasks.json"


class DiPlaner(QtWidgets.QMainWindow):
    def __init__(self):
        super(DiPlaner, self).__init__()
        uic.loadUi("dipla.ui.txt", self)  # Загрузка интерфейса из dipla.ui.txt

        # Привязка виджетов
        self.calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        self.next_month_button = self.findChild(QtWidgets.QPushButton, "nextMonthButton")
        self.tasks_list = self.findChild(QtWidgets.QListWidget, "tasksList")
        self.task_name_input = self.findChild(QtWidgets.QLineEdit, "taskNameInput")
        self.task_desc_input = self.findChild(QtWidgets.QLineEdit, "taskDescInput")
        self.add_task_button = self.findChild(QtWidgets.QPushButton, "addTaskButton")
        self.edit_task_button = self.findChild(QtWidgets.QPushButton, "editTaskButton")
        self.delete_task_button = self.findChild(QtWidgets.QPushButton, "deleteTaskButton")

        # Привязка событий
        self.next_month_button.clicked.connect(self.show_next_month)
        self.add_task_button.clicked.connect(self.add_task)
        self.edit_task_button.clicked.connect(self.edit_task)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.tasks_list.itemClicked.connect(self.show_task_details)

        # Инициализация данных
        self.current_date = self.calendar.selectedDate()
        self.tasks = self.load_tasks()
        self.update_task_list()

    def show_next_month(self):
        """Переход к следующему месяцу."""
        self.current_date = self.current_date.addMonths(1)
        self.calendar.setSelectedDate(self.current_date)

    def add_task(self):
        """Добавление новой задачи."""
        task_name = self.task_name_input.text()
        task_desc = self.task_desc_input.text()

        if not task_name:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Название задачи не может быть пустым.")
            return

        date_str = self.current_date.toString("yyyy-MM-dd")
        if date_str not in self.tasks:
            self.tasks[date_str] = []

        self.tasks[date_str].append({"name": task_name, "desc": task_desc, "done": False})
        self.save_tasks()
        self.update_task_list()

    def edit_task(self):
        """Редактирование выбранной задачи."""
        selected_item = self.tasks_list.currentItem()
        if not selected_item:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите задачу для редактирования.")
            return

        date_str = self.current_date.toString("yyyy-MM-dd")
        task_index = self.tasks_list.row(selected_item)
        task = self.tasks[date_str][task_index]

        task["name"] = self.task_name_input.text()
        task["desc"] = self.task_desc_input.text()
        self.save_tasks()
        self.update_task_list()

    def delete_task(self):
        """Удаление выбранной задачи."""
        selected_item = self.tasks_list.currentItem()
        if not selected_item:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")
            return

        date_str = self.current_date.toString("yyyy-MM-dd")
        task_index = self.tasks_list.row(selected_item)
        self.tasks[date_str].pop(task_index)
        self.save_tasks()
        self.update_task_list()

    def show_task_details(self, item):
        """Отображение деталей выбранной задачи."""
        date_str = self.current_date.toString("yyyy-MM-dd")
        task_index = self.tasks_list.row(item)
        task = self.tasks[date_str][task_index]

        self.task_name_input.setText(task["name"])
        self.task_desc_input.setText(task["desc"])

    def update_task_list(self):
        """Обновление списка задач."""
        self.tasks_list.clear()
        date_str = self.current_date.toString("yyyy-MM-dd")
        if date_str in self.tasks:
            for task in self.tasks[date_str]:
                item_text = f"{task['name']} {'✔' if task['done'] else ''}"
                self.tasks_list.addItem(item_text)

    def load_tasks(self):
        """Загрузка задач из файла."""
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_tasks(self):
        """Сохранение задач в файл."""
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DiPlaner()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
