# Add
# Delete
# Mark as done
# View task
# Exit
from colorama import init, Fore, Style
from database import my_con
from database import my_cursor

class To_do_list():
    def __init__(self):
        self.items = set()
        self.cursor = my_cursor
        self.con = my_con

    def add_task(self):
        count = 0
        num = 0
        print(Style.BRIGHT + Fore.RED + "Please ensure you don't add duplicate items!!!")
        ask = int(input("How many task(s) do you want to add: "))
        for i in range(ask):
            num += 1
            add_item = input(f"Add {num} To-do item: ").strip()
            query_check = "SELECT * FROM To_do_list_table WHERE task = %s"
            my_cursor.execute(query_check, (add_item,))
            exists = my_cursor.fetchone()
            if exists:
                print(Fore.RED + f"'{add_item}' already exists!")
                continue
            if add_item not in self.items:
                count += 1
                self.items.add(add_item)
                query = "INSERT INTO To_do_list_table (task) VALUES (%s)"
                my_cursor.execute(query, (add_item,))
                my_con.commit() #Saving to the database
        print(Fore.GREEN + f"{count}, Item(s) added!")
        # print(self.items)

    def view_task(self):
        count = 0
        # print(self.items)
        my_cursor.execute("SELECT task FROM To_do_list_table")
        rows = my_cursor.fetchall()
        if not rows:
            print(Fore.RED + "No task!!")
        else:
            for row in rows:
                count += 1
                print(Fore.GREEN + f"{count}. {row[0]}")


    def mark_done(self):
        count = 0
        my_cursor.execute("SELECT task FROM To_do_list_table")
        tasks = my_cursor.fetchall()
        if not tasks:
            print(Fore.RED + "No task has been mark as done!!")
        else:
            for row in my_cursor:
                count += 1
                print(Fore.BLUE + "Here are your the items:")
                print(Fore.GREEN + f"{count}. {row[0]}")
            ask = int(input("How many task(s) do you want to mark as done: "))
            mark_done_count = 0
            for i in range(ask):
                mark_done_count += 1
                mark_done = input("Input the name of the task you want to mark as done: ")
                query = "INSERT INTO Mark_done_table (mark_done) VALUES (%s)"
                my_cursor.execute(query, (mark_done, ))
                my_con.commit()
                
                query_delete = "DELETE FROM To_do_list_table WHERE task = %s"
                my_cursor.execute(query_delete, (mark_done, ))
                my_con.commit()
                
                if mark_done in self.items:
                    self.items.remove(mark_done)
            print(Fore.GREEN + f"{mark_done_count} task(s) marked as done!")

    def task_done(self):
        count = 0
        my_cursor.execute("SELECT mark_done FROM Mark_done_table")
        rows = my_cursor.fetchall()
        if not rows:
            print(Fore.RED + "No task has been done!!")
        else:
            for row in rows:
                count += 1
                print(Fore.GREEN + f"{count}. {row[0]}")

    def delete_task(self):
        count = 0
        my_cursor.execute("SELECT task FROM To_do_list_table")
        for row in my_cursor:
            count += 1
            print(Fore.BLUE + "Here are your the items:")
            print(Fore.GREEN + f"{count}. {row[0]}")
            print(Style.BRIGHT + Fore.RED + "Once deleted, it can't be restored!!")
        ask = int(input("How many task(s) do you want to delete: "))
        deleted_count = 0
        for i in range(ask):
            # count = 0
            delete = input("Which task do you want to delete: ")
            query = "DELETE FROM To_do_list_table WHERE task = %s"
            # val = (delete)
            my_cursor.execute(query, (delete,))
            my_con.commit()
            if delete in self.items:
                self.items.remove(delete)
            deleted_count += 1
        print(Fore.RED + f"{deleted_count}, Items deleted")

    def menu(self):
        print(Style.BRIGHT + Fore.CYAN + """
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
                self.mark_done()
            elif (option == '4'):
                self.task_done()
            elif (option == '5'):
                self.delete_task()
            elif (option == '6'):
                exit()
            else:
                print("Invalid input")
                return
td = To_do_list()
td.app()