class User:
    next_id = 1

    def __init__(self, name, email):
        self.id = User.next_id
        User.next_id = User.next_id + 1
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }

    def __str__(self):
        return "User " + str(self.id) + ": " + self.name + " (" + self.email + ")"