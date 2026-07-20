import json
import os
from models.user import User
from models.project import Project
from models.task import Task

DATA_FILE = "data/data.json"

def save_users(users):
    data = [u.to_dict() for u in users]
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_users():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            raw_data = json.load(file)
    except (json.JSONDecodeError, ValueError):
        print("Warning: data file is empty or corrupted. Starting fresh.")
        return []

    users = []
    max_user_id = 0
    max_project_id = 0
    max_task_id = 0

    for user_dict in raw_data:
        user = User(user_dict["name"], user_dict["email"])
        user.id = user_dict["id"]
        if user.id > max_user_id:
            max_user_id = user.id

        for project_dict in user_dict["projects"]:
            project = Project(project_dict["title"], project_dict["description"], project_dict["due_date"], user)
            project.id = project_dict["id"]
            if project.id > max_project_id:
                max_project_id = project.id

            for task_dict in project_dict["tasks"]:
                task = Task(task_dict["title"], project, task_dict["assigned_to"], task_dict["status"])
                task.id = task_dict["id"]
                if task.id > max_task_id:
                    max_task_id = task.id

        users.append(user)

    User.next_id = max_user_id + 1
    Project.next_id = max_project_id + 1
    Task.next_id = max_task_id + 1

    return users
    