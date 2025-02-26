# pyinstall --onefile --windowed --clean gui.py
# platypus

# streamlit
# terminal streamlit run your_file
# pip freeze > requirements.txt packages

FILEPATH = "todos_item.txt"

def get_todos(file_path=FILEPATH):
    with open(file_path, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos, file_path=FILEPATH):
    with open(file_path, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    get_todos()