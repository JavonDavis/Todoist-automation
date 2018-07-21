import os, time
from todoist.api import TodoistAPI

API_WAIT_TIME = 3  # seconds

class Project:

    def __init__(self):
        self.token = os.getenv('TOKEN')
        self.api = TodoistAPI(self.token)
        self.api.sync()
        self.project_id = None

    def create_project(self, project_name: str):
        """
        Creates a new project on todoist
        :param project_name: The name of the project
        """
        project = self.api.projects.add(project_name)
        self.api.commit()
        print('Created project:')
        print(project)
        self.project_id = project.data['id']

    def remove_project(self):
        """
        Removes the current project
        """
        if self.project_id is None:
            print('No project Created or project has been deleted')
            return
        project = self.api.projects.get_by_id(self.project_id)
        project.delete()
        self.api.commit()

    def contains_task_with_message(self, message):
        """
        Checks if the current project has a task the given message
        :param message: The message to look for
        :return: True if it does, false otherwise
        """
        print(self.api.items.all())
        print('filtered')
        print(self.project_id)
        print(list(filter(lambda task: task['content'] == message,
                          self.api.items.all())))
        return len(list(filter(lambda task: task['content'] == message,
                               self.api.items.all()))) > 0

    def reopen_task_with_message(self, message):
        """
        Reopens the task with the given message
        :param message: The message to look for, assumes it exists
        """
        item_id = list(filter(lambda task: task['content'] == message and task['project_id'] == self.project_id,
                              self.api.items.all()))[0]['id']

        item = self.api.items.get_by_id(item_id)
        item.uncomplete()
        self.api.commit()

    def sync(self):
        """
        Syncs the API
        """
        self.api.sync()
        time.sleep(API_WAIT_TIME)
