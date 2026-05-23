import json

TASKS_FILE = "tasks.json"


# Read data from JSON file
def load_tasks():

    with open(TASKS_FILE, "r") as file:
        return json.load(file)


# Save data into JSON file
def save_tasks(tasks):

    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


# Create Task
def create_task(task):

    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }

    tasks.append(new_task)

    save_tasks(tasks)

    return new_task


# Get All Tasks
def get_tasks():

    return load_tasks()


# Get Single Task
def get_task_by_id(task_id):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:
            return task

    return None


# Update Task
def update_task(task_id, updated_task):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            if updated_task.title is not None:
                task["title"] = updated_task.title

            if updated_task.description is not None:
                task["description"] = updated_task.description

            if updated_task.status is not None:
                task["status"] = updated_task.status

            save_tasks(tasks)

            return task

    return None


# Delete Task
def delete_task(task_id):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            return {"message": "Task deleted successfully"}

    return None