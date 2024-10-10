# Create the root window
import tkinter as tk
import os
import json

root = tk.Tk()
root.title("Home's Manager")

# Create a frame for widgets
frame = tk.Frame(root)
frame.pack()

def remove_all_children(widget):
    # Itera por todos os filhos do widget e os destrói
    for child in widget.winfo_children():
        child.destroy()

def create_object_file():
    ids = os.listdir("objects")
    print(int(sorted(ids,key=int, reverse=True)[0]) + 1)
    id = int(sorted(ids,key=int, reverse=True)[0]) + 1
    with open("objects/" + str(id), "w") as file:
        file.write(open("default.txt", "r").read())

def select_object(id):
    global last_id
    last_id = id
    remove_all_children(parameters_list)
    global entries
    entries = {}  # Limpa o dicionário de entradas

    # Abre e lê o arquivo JSON
    with open("objects/" + str(id), 'r') as file:
        data = json.load(file)

    # Para cada chave e valor no JSON, cria um rótulo e uma textbox
    for key, value in data.items():
        # Cria um rótulo com o nome da chave
        label = tk.Label(parameters_list, text=key)
        label.pack(side=tk.TOP)

        # Cria uma textbox com o valor da chave
        textbox = tk.Entry(parameters_list)
        textbox.insert(0, str(value))  # Insere o valor atual na textbox
        textbox.pack(side=tk.TOP)

        # Armazena a entrada no dicionário para depois salvar
        entries[key] = textbox

def save_parameters(id):
    # Cria um dicionário com os valores atuais das textboxes
    data = {key: entry.get() for key, entry in entries.items()}

    # Salva o dicionário em um arquivo JSON
    with open("objects/" + str(id), 'w') as file:
        json.dump(data, file, indent=4)

def refresh_objects():
    remove_all_children(objects_list)
    objects = sorted(os.listdir("objects"), key=int)
    for object in objects:
        tk.Button(objects_list,width=100,height=1, command=lambda obj=object: select_object(int(obj)), text="Propiedade " + object).pack(side=tk.TOP)

panel = tk.Frame(frame)
panel.pack(side=tk.TOP)

create_object = tk.Button(panel, width=12, height=3, text="Create Object", command=lambda:create_object_file())
create_object.pack(side=tk.TOP)

create_object = tk.Button(panel, width=12, height=3, text="Refresh Objects", command=lambda:refresh_objects())
create_object.pack(side=tk.TOP)

create_object = tk.Button(panel, width=12, height=3, text="Save Object", command=lambda:save_parameters(last_id))
create_object.pack(side=tk.TOP)

objects_list = tk.Frame(frame, height=600)
objects_list.pack(side=tk.TOP)

parameters_list = tk.Frame(panel, width=100, height=600)
parameters_list.pack(side=tk.TOP)

tk.Button(parameters_list, text="Nenhum item selecionado", width=100).pack(side=tk.RIGHT)

root.mainloop()
