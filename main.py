import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import save_users, load_users


def find_user(users, name):
    for u in users:
        if u.name == name:
            return u
    return None


def find_project(users, title):
    for u in users:
        for p in u.projects:
            if p.title == title:
                return p
    return None


def cmd_add_user(args, users):
    user = User(args.name, args.email)
    users.append(user)
    save_users(users)
    print("Added user: " + str(user))


def cmd_list_users(args, users):
    if not users:
        print("No users yet.")
        return
    for u in users:
        print(u)


def cmd_add_project(args, users):
    user = find_user(users, args.user)
    if user is None:
        print("No user found with name: " + args.user)
        return
    project = Project(args.title, args.description, args.due_date, user)
    save_users(users)
    print("Added project: " + str(project))


def cmd_list_projects(args, users):
    user = find_user(users, args.user)
    if user is None:
        print("No user found with name: " + args.user)
        return
    if not user.projects:
        print(user.name + " has no projects yet.")
        return
    for p in user.projects:
        print(p)


def cmd_add_task(args, users):
    project = find_project(users, args.project)
    if project is None:
        print("No project found with title: " + args.project)
        return
    task = Task(args.title, project, assigned_to=args.assigned_to)
    save_users(users)
    print("Added task: " + str(task))


def cmd_complete_task(args, users):
    project = find_project(users, args.project)
    if project is None:
        print("No project found with title: " + args.project)
        return
    for t in project.tasks:
        if t.title == args.title:
            t.mark_complete()
            save_users(users)
            print("Marked complete: " + str(t))
            return
    print("No task found with title: " + args.title)


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", dest="due_date", required=True)

    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.add_argument("--user", required=True)

    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", dest="assigned_to", default=None)

    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--project", required=True)
    complete_task_parser.add_argument("--title", required=True)

    args = parser.parse_args()
    users = load_users()

    if args.command == "add-user":
        cmd_add_user(args, users)
    elif args.command == "list-users":
        cmd_list_users(args, users)
    elif args.command == "add-project":
        cmd_add_project(args, users)
    elif args.command == "list-projects":
        cmd_list_projects(args, users)
    elif args.command == "add-task":
        cmd_add_task(args, users)
    elif args.command == "complete-task":
        cmd_complete_task(args, users)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()