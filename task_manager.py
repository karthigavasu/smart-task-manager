import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()
TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(username):
    print("\n[bold magenta]🌸 Add New Task 🌸[/bold magenta]\n")
    title = input("Task Title: ")
    category = input("Category: ")

    while True:
        priority = input("Priority (High/Medium/Low): ").capitalize()

        if priority in ["High", "Medium", "Low"]:
            break
        else:
            print("\n[bold red]Invalid Priority![/bold red]")

    while True:
        deadline = input("Deadline (DD-MM-YYYY): ")
        
        try:
            deadline_date = datetime.strptime(
                deadline,
                "%d-%m-%Y"
            )
            today = datetime.now()

            if deadline_date.date() < today.date():
                print(
                    "\n[bold red]Deadline cannot be in the past![/bold red]"
                )
            else:
                break
        except:
            print(
                "\n[bold red]Invalid Date Format![/bold red]"
            )
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "username": username,
        "title": title,
        "category": category,
        "priority": priority,
        "deadline": deadline,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\n[bold green]✨ Task Added Successfully ✨[/bold green]" )

def view_tasks(username):

    tasks = load_tasks()

    # SORT TASKS BASED ON PRIORITY
    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    tasks.sort(
        key=lambda task:
        priority_order[task["priority"]]
    )

    table = Table(
        title="[bold bright_magenta]💖 My Task Planner 💖[/bold bright_magenta]"
    )

    table.add_column(
        "ID",
        style="bright_cyan",
        justify="center"
    )

    table.add_column(
        "Title",
        style="bright_green"
    )

    table.add_column(
        "Category",
        style="bright_yellow"
    )

    table.add_column(
        "Priority",
        justify="center"
    )

    table.add_column(
        "Deadline",
        style="bright_magenta"
    )

    table.add_column(
        "Status",
        justify="center"
    )

    today = datetime.now().date()

    for task in tasks:
        if task["username"] != username:
            continue
        deadline_date = datetime.strptime(
            task["deadline"],
            "%d-%m-%Y"
        ).date()

        status = task["status"]

        if (
            deadline_date < today
            and status != "Completed"
        ):

            status = "[bold red]OVERDUE[/bold red]"

        if task["priority"] == "High":

            priority_color = (
                "[bold red]HIGH[/bold red]"
            )

        elif task["priority"] == "Medium":

            priority_color = (
                "[bold yellow]MEDIUM[/bold yellow]"
            )

        else:

            priority_color = (
                "[bold green]LOW[/bold green]"
            )

        if status == "Completed":

            status_color = (
                "[bold green]Completed[/bold green]"
            )

        elif "OVERDUE" in status:

            status_color = (
                "[bold red]OVERDUE[/bold red]"
            )

        else:

            status_color = (
                "[bold yellow]Pending[/bold yellow]"
            )

        table.add_row(
            str(task["id"]),
            task["title"],
            task["category"],
            priority_color,
            task["deadline"],
            status_color
        )

    console.print(table)
def complete_task():
    tasks = load_tasks()
    task_id = input("\nEnter Task ID: ")
    found = False
    for task in tasks:
        if str(task["id"]) == task_id:
            task["status"] = "Completed"
            found = True
    save_tasks(tasks)

    if found:
        print("\n[bold green]🎉 Task Completed 🎉[/bold green]")
        
    else:
        print("\n[bold red]Invalid Task ID![/bold red]")

def delete_task():
    tasks = load_tasks()
    task_id = input("\nEnter Task ID: ")
    new_tasks = []
    found = False

    for task in tasks:
        if str(task["id"]) != task_id:
            new_tasks.append(task)

        else:
            found = True
    save_tasks(new_tasks)

    if found:
        print("\n[bold red]🗑  Task Removed 🗑[/bold red]")

    else:
        print("\n[bold red]Invalid Task ID![/bold red]")
