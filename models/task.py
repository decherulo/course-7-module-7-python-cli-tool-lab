class Task:
    next_id = 1

    def __init__(self, title, project, assigned_to=None, status="pending"):
        self.id = Task.next_id
        Task.next_id = Task.next_id + 1
        self.title = title
        self.project = project
        self.assigned_to = assigned_to
        self.status = status

        project.add_task(self)

    def mark_complete(self):
        self.status = "complete"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __str__(self):
        assigned = self.assigned_to if self.assigned_to else "unassigned"
        return "Task " + str(self.id) + ": " + self.title + " [" + self.status + "] (assigned to: " + assigned + ")"