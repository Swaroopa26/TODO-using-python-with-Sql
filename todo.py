import sqlite3
def create_table():#create new table
    con=sqlite3.connect('todo.db')
    c=con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS  todotasks(id INTEGER PRIMARY KEY,task TEXT NOT NULL , status TEXT NOT NULL)''')
    con.commit()
    con.close()
def add_task(task):#add the list 
    con =sqlite3.connect('todo.db')
    c=con.cursor()
    c.execute("INSERT INTO todotasks(task , status)VALUES (? ,?)",(task,'pending'))
    con.commit()
    con.close()
def view_task():#view the table
    con =sqlite3.connect('todo.db')
    c=con.cursor()
    c.execute("SELECT * FROM todotasks")
    tasks= c.fetchall()
    con.close()
    return tasks
def update_task(task_id,new_status):#update table
    con=sqlite3.connect('todo.db')
    c=con.cursor()
    c.execute("UPDATE todotasks SET status =? WHERE id=?",(new_status,task_id))
def delete_task(task_id):#delete tasks
    con=sqlite3.connect('todo.db')
    c=con.cursor()
    c.execute("DELETE FROM todotasks WHERE id=?",(task_id))
    con.commit()
    con.close()
    #main function
def main():
    create_table()
    while True:
        print("\n1.Add Task\n2.View Task\n3.Update Task\n4.Delete Task\n5.Exit")
        choice=input("Enter your choice")
        if choice=='1':
            task=input("Enter Tasks:")
            add_task(task)
            print("Task Added successfully!")
        elif choice=='2':
             tasks=view_task()
             if not tasks:
                 print("no tasks found")
             else:
                 for task in tasks:
                     print(f"{task[0]}.{task[1]}-{task[2]}")
        elif choice=='3':
            task_id=input("Enter task id:")
            new_status=input("Enter new status :")
            update_task(task_id,new_status)
            print("Task Updated succesfully!")
        elif choice=='4':
            task_id=input("Enter task id:")
            delete_task(task_id)
            print("Task deleted successfully!")
        elif choice=='5':
            print("Exit")
            break
        else:
            print("invalid")
if __name__=="__main__": 
 main()