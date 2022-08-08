import pickle
from datetime import *

class Tasks:
    def __init__(self, number, priority, description):
        self.data = datetime.now()
        self.number = number
        self.priority = priority
        self.description = description

    def __str__(self):
        creation_date = datetime.strftime(self.data, '%Y-%m-%d')
        days_ago = (datetime.now() - self.data).days
        return f'Task: {self.number}, priority: {self.priority}, description: {self.description}, date: {creation_date}, days ago: {days_ago}'

class List:
    tasks_list = []
    number = 0

    def __init__(self, file):
        self.file = file
        try:
            with open(self.file, 'rb') as f:
                self.tasks_list = pickle.load(f)
                self.number = max(z.number for z in self.tasks_list)
        except FileNotFoundError:
            pass

    def add(self, task_priority, task_description):
        self.number += 1
        task = Tasks(self.number, task_priority, task_description)
        self.tasks_list.append(task)

    def delete(self, delete_task):
        for index, a in enumerate(self.tasks_list):
            if a.number == delete_task:
                del self.tasks_list[index]
                return

    def display(self):
        for z in self.tasks_list:
            print(z)
    
    def save(self):
        with open(self.file, 'wb') as f:
            pickle.dump(self.tasks_list, f)

def ToDo():
    list = List('C:/Users/omen/Desktop/2/plik.pickle')

    while True:
        print()
        print('1 - add task\n2 - delete task\n3 - display Tasks\n0 - Exit')
        print()
        user_choice = int(input('What option do you choose: '))

        if user_choice == 1:
            task_priority = input("Priority: ")
            task_description = input('Description: ')
            list.add(task_priority, task_description)
            
        if user_choice == 2:
            list.display()
            delete_task = int(input('Which task do you want to delete: '))
            list.delete(delete_task)

        if user_choice == 3:
            list.display()

        if user_choice == 0:
            list.save()
            break

if __name__ == '__main__':
    ToDo()





