# todo list

## About the project
It is used for the person to organize his/her todo list 

## Tech stack
- Backend technologies : 
    - Python v3.10.x or higher
    - Libraries
        - tk
        - ttk
        - tkinter.messagebox
        - csv
        - os

## About application

- we initialized the GUI with the following elemenets :

    - root
    - add button
    - delete button
    - delete all button
    - load tasks button
    - save tasks button 
    - frame 
    - tree view 
    - text box
    - menu with commands
        
- We used the following functions for the commands: 
    - add_text:
        we check if the task title is empty then we show a warning message. 
        If there is text then we take it and insert it inside the tree. 

    - delete_task: 
        we get the selected task, then we make sure that the user wants to delete this task.
        If yes we continue with the deleting.
        If there is nothing is selected, we show a warning message to the user.

    - load_tasks_by_clicking: 
        we are getting the tasks and check if there is no tasks then we are loading the tasks from a specific file. 
        Otherwise, we show ask the user if he/her sure to load the tasks and remove the current tasls.

    - load_tasks: 
        we make sure that the tree is empty, then import the tasks from the file.
        if there is anything happened, we show them a warning message.

    - save_tasks:
        we check if there is any task in the tree, then we write them on a specific file.
        If not, then we empty the current file to make sure that it does not contain any tasks, and we show a warning message.

    - change_status:
        when we click on the right botton on the tree item, then we are showing the status menu to the user to let him/her pick a status.


    - set_status: 
        we get the selected task and then change the status depends on the selected status in the status menu.

