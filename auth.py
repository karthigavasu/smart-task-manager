import sqlite3
from rich import print

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()
def register():
    print("[bold cyan]🌸 Create Account 🌸[/bold cyan]")
    while True:
        username = input("Username: ").strip()
        if username == "":
            print("[bold red]Username cannot be empty![/bold red]")
        else:
            break
    while True:
        password = input("Password: ").strip()
        if password == "":
            print("[bold red]Password cannot be empty![/bold red]")
        else:
            break
    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        connection.commit()
        print("[bold green]✨ Registration Successful ✨[/bold green]")
    except:
        print("[bold red]Username already exists![/bold red]")

def login():
    print("[bold cyan]💖 Welcome Back 💖[/bold cyan]")
    while True:
        username = input("Username: ").strip()
        if username == "":
            print("[bold red]Username cannot be empty![/bold red]")
        else:
            break
    while True:
        password = input("Password: ").strip()
        if password == "":
            print("[bold red]Password cannot be empty![/bold red]")
        else:
            break
        
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cursor.fetchone()
    if user:
        print("[bold green]✨ Login Successful ✨[/bold green]")
        return username
    else:
        print("[bold red]Invalid Credentials![/bold red]")
        return None
