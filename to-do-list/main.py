import function as fn
import FreeSimpleGUI as gui
import  time

gui.theme("")
clock = gui.Text("", key="clock")
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button(button_text="Add", size=10)
list_box = gui.Listbox(values=fn.get_todos(), key="todos",
                       enable_events=True, size=(45, 10))
edit_button = gui.Button(button_text="Edit")
complete_button = gui.Button(button_text="Complete")
exit_button = gui.Button(button_text="Exit")
window = gui.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                            font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(values="")
            except IndexError:
                gui.popup("Please select a todo item first", font=('Helvetica', 20))
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = fn.get_todos()
            todos.remove(todo_to_complete)
            fn.write_todos(todos)
            window["todos"].update(values=todos)
        case "Exit":
            break
        case "todos":
            window["todo"].update(values=values["todos"][0])
        case gui.WIN_CLOSED:
            break

window.close()

