# Add
# Delete
# Mark as done
# View task
# Exit
from database import my_con
from database import my_cursor

class To_do_list():
    def __init__(self):
        self.items = set()
        self.cursor = my_cursor
        self.con = my_con

    def add_task(self):
        count = 0
        print("Please ensure you don't add duplicate items!!!")
        ask = int(input("How many task(s) do you want to add: "))
        for i in range(ask):
            count += 1
            add_item = input("Add a To-do item: ").strip()
            self.items.add(add_item)
            query = "INSERT INTO To_do_list_table (task) VALUES(%s)"
            value = (add_item)
            my_cursor.execute(query, value)
            my_con.commit() #Saving to the database
        print(f"{count}, Items added!")
        # print(self.items)

    def view_task(self):
        count = 0
        # print(self.items)
        my_cursor.execute("SELECT task FROM To_do_list_table")
        # rows = my_cursor.fetchall()
        for row in my_cursor:
            count += 1
            print(f"{count}. {row[0]}")


    def mark_done(self):
        pass

    def task_done(self):
        pass

    def delete_task(self):
        count = 0
        my_cursor.execute("SELECT task FROM To_do_list_table")
        for row in my_cursor:
            count += 1
            print(f"{count}. {row[0]}")
        ask = int(input("How many task(s) do you want to delete: "))
        for i in range(ask):
            count = 0
            count += 1
            delete = input("Which task do you want to delete: ")
            query = "DELETE FROM To_do_list_table WHERE task = %s"
            val = (delete)
            my_cursor.execute(query, val)
            my_con.commit()
        print(f"{count}, Items deleted")

    def menu(self):
        print("""
            -------To-do-------
            1. Add a To-do item
            2. View all task
            3. Mark task as done
            4. Task done
            5. Delete a task
            6. Exit
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
                self.delete_task()
            elif (option == '6'):
                exit()
            else:
                print("Invalid input")
                return
td = To_do_list()
td.app()