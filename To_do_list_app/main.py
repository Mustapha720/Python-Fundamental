# Add
# Delete
# Mark as done
# View task
# Exit
from database import my_con
from database import my_cursor

class To_do_list():
    def __init__(self):
        self.items = []
        self.cursor = my_cursor
        self.con = my_con

    def add_task(self):
        add_item = input("Add a To-do item: ")
        self.items.append(add_item)
        # print(self.items)

    def view_task(self):
        print(self.items)

    def mark_done(self):
        pass

    def delete_task(self):
        pass

    def menu(self):
        print("""
            -------To-do-------
            1. Add a To-do item
            2. View all task
            3. Mark task as done
            4. Delete a task
            5. Exit
                """)

    def app(self):
        while True:
            self.menu()
            option = input("Select an option (1-5): ")
            if (option == '1'):
                self.add_task()
            elif (option == '2'):
                self.view_task()
            elif (option == '3'):
                pass
            elif (option == '4'):
                pass
            elif (option == '5'):
                exit()
            else:
                print("Invalid input")
                return
td = To_do_list()
td.app()