import tasks

def main():
    while True:
        print("\n1. Add  2. Show  3. Complete  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                tasks.add_task(tasks.tasks, input("Title: "))
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            tasks.display_tasks(tasks.tasks)
        elif choice == "3":
            tasks.complete_task(tasks.tasks, int(input("Task ID: ")))
        elif choice == "4":
            tasks.delete_task(tasks.tasks, int(input("Task ID: ")))
        elif choice == "5":
            break

if __name__ == "__main__":
    main()