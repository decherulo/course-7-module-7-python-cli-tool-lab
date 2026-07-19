import argparse
from models import Task, User

users = {}


def add_task(args):
    user = users.get(args.user)
    if user is None:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)


def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")


def list_tasks(args):
    user = users.get(args.user)
    if user:
        if not user.tasks:
            print(f"{user.name} has no tasks.")
            return
        for task in user.tasks:
            status = "Done" if task.completed else "Not done"
            print(f"- {task.title} ({status})")
    else:
        print("❌ User not found.")


parser = argparse.ArgumentParser(description="Task Manager CLI")
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser("add-task", help="Add a new task")
add_parser.add_argument("user")
add_parser.add_argument("title")
add_parser.set_defaults(func=add_task)

complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
complete_parser.add_argument("user")
complete_parser.add_argument("title")
complete_parser.set_defaults(func=complete_task)

list_parser = subparsers.add_parser("list-tasks", help="List a user's tasks")
list_parser.add_argument("user")
list_parser.set_defaults(func=list_tasks)

if __name__ == "__main__":
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()