""" Created by renat on 07/12/2022"""


def app1():
    def add(lst):
        lst.append(input("Enter todo: "))
        return lst

    def show(lst):
        for count, item in enumerate(lst):
            print(f"{count} - {item}")

    def edit(lst):
        show(lst)
        index_to_edit = int(input("\nWhat is the index of the todo you want to change?").strip())
        lst[index_to_edit] = input(f"New item for index {index_to_edit}: ")
        show(lst)
        return lst

    todos = []
    while True:
        user_action = input("Type add, show, edit or exit: ")
        user_action = (user_action.casefold()).strip()
        match user_action:
            case 'add':
                todos = add(todos)
            case 'show':
                show(todos)
            case 'edit':
                todos = edit(todos)
            case 'exit':
                break



if __name__ == '__main__':
    app1()
