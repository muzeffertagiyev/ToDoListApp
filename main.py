import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgb
import csv
import os

root = tk.Tk()
root.title("To do list app")


# for tkinter messages
def ask_ok_cancel(message):
    return msgb.askokcancel(title='Confirmation',message=message)

def show_warning(message):
    return msgb.showwarning(title='Warning', message=message)


# for buttons
def add_text():
    task = entry.get()
    task_status = status.get()
    if task and not task.isspace():
        tree.insert("", tk.END, values=(task, task_status))
        entry.delete(0, tk.END)
    else:
        show_warning(message='The entry field is empty. Please write a task')

def delete_task():
    task_index = tree.selection()
    if len(task_index) != 0:
        message = 'Do you really want to delete selected task?'
        if len(task_index) != 1:
            message = 'Do you really want to delete all selected tasks?'
        
        if ask_ok_cancel(message=message): 
            for task in task_index:
                tree.delete(task)
    else:
        show_warning(message='Please select at least a task to delete')

def delete_all_tasks():
    all_tasks = tree.get_children()
    if len(all_tasks) != 0:
        if ask_ok_cancel(message='Do you really want to delete all the tasks from to do list?'):
            tree.delete(*all_tasks)
    else:
        show_warning(message="There is not any task to delete. Please first add some tasks")

def load_tasks_by_clicking():
    tasks = tree.get_children()
    if len(tasks) != 0:
        if ask_ok_cancel('Do you really want to do that?'):
            load_tasks()
    else:
        load_tasks()

def load_tasks():
    try:
        tasks = tree.get_children()
        tree.delete(*tasks)
        with open('tasks.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # skip the header
            for row in reader:
                task, status = row
                tree.insert("", tk.END, values=(task, status))
    except:
        show_warning(message='There is not saved tasks for loading. Please first save some tasks')

def save_tasks():
    if len(tree.get_children()) != 0 :
        if ask_ok_cancel(message='Do you want to save all tasks? Be aware that previous saved tasks will disappear'):
            with open('tasks.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Task', 'Status'])
                for task in tree.get_children():
                    task_data = tree.item(task)['values']
                    writer.writerow(task_data)
    else:
        if(os.path.isfile('./tasks.csv')):
            if ask_ok_cancel(message='Please be aware that you try to save empty to do list. All data will be deleted from base'):
                open("tasks.csv", 'w').close()
        show_warning(message='Please add some tasks')


def change_status(event):
    item = tree.identify_row(event.y)
    status_menu.post(event.x_root, event.y_root)

def set_status(new_status):
    item = tree.focus()
    tree.item(item, values=[tree.item(item)["values"][0], new_status])



text_frame = tk.Frame(root)
text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tree = ttk.Treeview(text_frame, columns=("Task", "Status"), show="headings")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tree.column("Task", width=200, anchor="w")
tree.column("Status", width=100, anchor="center")

tree.heading("Task", text="Task")
tree.heading("Status", text="Status")

scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

entry = tk.Entry(root)
entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

status = tk.StringVar()
status.set("To Do")

status_menu = tk.Menu(root, tearoff=0)
status_menu.add_command(label="To Do", command=lambda:set_status("To Do"))
status_menu.add_command(label="Completed", command=lambda:set_status("Completed"))
status_menu.add_command(label="Going On", command=lambda:set_status("Going On"))

tree.bind("<Button-3>", change_status)

add_button = tk.Button(root, text="Add", command=add_text)
add_button.pack(pady=5)

delete_button = tk.Button(root,text='Delete',command=delete_task)
delete_button.pack()

delete_all_button = tk.Button(root,text='Delete All', command=delete_all_tasks)
delete_all_button.pack()

load_button = tk.Button(root,text='Load Tasks', command=load_tasks_by_clicking)
load_button.pack()

save_button = tk.Button(root,text='Save Tasks',command=save_tasks)
save_button.pack()

load_tasks()

root.mainloop()

