#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create an empty to-do list
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to update a task in the list
def update_task(index, new_task):
    if index >= 0 and index < len(todo_list):
        todo_list[index] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index!")

# Function to display the to-do list
def display_list():
    if len(todo_list) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list):
            print(f"{index+1}. {task}")

# Prompt the user for options
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Display the to-do list")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        task = input("Enter the task: ")
        add_task(task)
    elif choice == 2:
        index = int(input("Enter the task index to update: ")) - 1
        new_task = input("Enter the new task: ")
        update_task(index, new_task)
    elif choice == 3:
        display_list()
    elif choice == 4:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice!")


# In[ ]:




