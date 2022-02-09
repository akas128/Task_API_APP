def task_serializer(task)->dict:
    return {
        "id":str(task["_id"]),
        "Urgent_task":task["Urgent_task"],
        "Regulat_task":task["Regulat_task"],
        "Normal_task":task["Normal_task"],
    }

def tasks_serializer(tasks)->list:
    return [task_serializer(task) for task in tasks]