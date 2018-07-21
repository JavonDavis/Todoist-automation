from api.project import Project

from decorators import login_if_necessary
from pages.landing_page import LandingPage

import time

project_name = 'Alex U, Appium Automation Project'
task_message = 'Complete 3 test cases for Todoist app'


@login_if_necessary
def test_create_project(landing_page: LandingPage):
    """
    Test that a newly created project appears in the app
    :param landing_page: The Landing Page object
    """
    project = Project()
    project.create_project(project_name)
    project.sync()

    landing_page.refresh()
    landing_page.click_drawer()
    landing_page.expand_collapse_projects()

    project_exists = landing_page.has_project(project_name)
    landing_page.expand_collapse_projects()

    project.remove_project()
    project.sync()

    landing_page.click_inbox()
    landing_page.refresh()

    assert project_exists is True


@login_if_necessary
def test_create_task(landing_page: LandingPage):
    """
    Test that creating a task is applied to the API
    :param landing_page: The Landing Page object
    """
    project = Project()
    project.create_project(project_name)
    project.sync()

    landing_page.refresh()
    landing_page.click_drawer()
    landing_page.expand_collapse_projects()

    landing_page.select_project(project_name)

    landing_page.click_add_task_button()

    landing_page.enter_task_message(task_message)
    landing_page.save_task()

    project.sync()

    contains_message = project.contains_task_with_message(task_message)
    project.remove_project()
    project.sync()

    assert contains_message


@login_if_necessary
def test_complete_task(landing_page: LandingPage):
    """
    Test that compelting and reopening a tasks applies the necessary updates
    :param landing_page: The Landing Page object
    """
    project = Project()
    project.create_project(project_name)
    project.sync()

    landing_page.refresh()
    landing_page.click_drawer()
    landing_page.expand_collapse_projects()

    landing_page.select_project(project_name)
    landing_page.click_add_task_button()

    landing_page.enter_task_message(task_message)
    landing_page.save_task()

    project.sync()
    landing_page.refresh()

    landing_page.click_task(task_message)
    landing_page.click_complete()
    project.sync()

    message_visible_before = landing_page.has_task_with_message(task_message)
    project.reopen_task_with_message(task_message)

    landing_page.refresh()
    project.sync()

    message_visible_after = landing_page.has_task_with_message(task_message)

    project.remove_project()
    project.sync()

    assert (not message_visible_before) and message_visible_after
