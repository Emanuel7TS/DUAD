import FreeSimpleGUI as sg

layout = [
    [sg.Text("Digite su edad", key = "type")],
    [sg.Input(key = "edad")],
    [sg.Button("Show edad")],
    [sg.Text(key="result")],]

window = sg.Window("Example", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    try:
        data = int(values["edad"]) 
        if event == "Show edad":
            if values["edad"] != "":
                age = values["edad"]
            else:
                print("edad invalida")
                window["edad"].update("")
        window["result"].Update(f"Su edad es: {age}")

    except ValueError:
        window["result"].Update(f"Edad invalida")

window.close()