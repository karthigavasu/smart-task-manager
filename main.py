from rich import print
import database
import auth
import task_manager

print("\n[bold bright_magenta]✨ 🚀 𝗣 𝗥 𝗢 𝗗 𝗨 𝗖 𝗧 𝗜 𝗩 𝗜 𝗧 𝗬   𝗛 𝗨 𝗕 🚀 ✨[/bold bright_magenta]\n")
while True:
    print("\n[bold yellow]1.[/bold yellow] Register")
    print("[bold yellow]2.[/bold yellow] Login")
    print("[bold yellow]3.[/bold yellow] Exit")
    choice = input("\nEnter Choice: ")
    if choice == "1":
        auth.register()

    elif choice == "2":
        username = auth.login()
        
        if username:
            while True:
                print("\n[bold cyan]===== DASHBOARD =====[/bold cyan]")
                print("\n1. Add Task")
                print("2. View Tasks")
                print("3. Complete Task")
                print("4. Delete Task")
                print("5. Logout")
                option = input("\nEnter Choice: ")
                
                if option == "1":
                    task_manager.add_task(username)
                elif option == "2":
                    task_manager.view_tasks(username)
                elif option == "3":
                    task_manager.complete_task(username)
                elif option == "4":
                    task_manager.delete_task(username)
                elif option == "5":
                    break
                
    elif choice == "3":
        print("\n[red]Exiting Application...[/red]")

        break
