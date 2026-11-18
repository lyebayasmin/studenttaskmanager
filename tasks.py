tasks = []

def add_task(task_list, title):
    task = {"id": len(task_list) + 1, "title": title, "done": False}
    task_list.append(task)
    return task

def display_tasks(task_list):
    if not task_list:
        print("No tasks yet.")
    for t in task_list:
        mark = "X" if t["done"] else " "
        print(f'{t["id"]}. [{mark}] {t["title"]}')

def complete_task(task_list, task_id):
    for t in task_list:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False

def delete_task(task_list, task_id):
    for t in task_list:
        if t["id"] == task_id:
            task_list.remove(t)
            return True
    return False