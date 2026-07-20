class Project:
    next_id = 1

    def __init__(self, title, description, due_date, user):
        self.id = Project.next_id
        Project.next_id = Project.next_id + 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = user
        self.tasks = []

        user.add_project(self)

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    def __str__(self):
        return "Project " + str(self.id) + ": " + self.title + " (owner: " + self.user.name + ")"