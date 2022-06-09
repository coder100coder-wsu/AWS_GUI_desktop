import json
import PySimpleGUI as sg
from aws_S3_upload_file_only_1 import *
# ASSUMPTION: AWS ACCESS IS SETUP ON THE OS.
# IF NOT, SETUP AWS ACCESS

folder_list = ["videos", "test_images"]
sg.theme('DarkBlue13')  # window color

layout_l = [
    [sg.Text("source folder or files")],
    [sg.HSep()],
    [sg.Text("Paste link to source file"), sg.Text(size=(25, 1),
                                                   key='-path-field-')],
    [sg.InputText(key='source_file_path', size=(100,1))],
    [sg.Button('upload_file')],
]

layout_r = []

layout = [
    # [sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]], p=0)],
    [sg.T('Use Buttons', font='_ 10', justification='l'), sg.VSep(),
     sg.Button('EXIT'), sg.VSep(), sg.VSep()],
    [sg.HSep()],
    [sg.Col(layout_l), sg.VSep(), sg.Col(layout_r)],
    [sg.HSep()],
    [sg.Text("Output of query"), sg.Text(size=(15, 1)), sg.VSep(), sg.Button("CLEAR_OUTPUT")],
    [sg.Output(size=(180, 10), font=('Helvetica 10'), key='-QUERY_OUTPUT-')],
]

# create window
window = sg.Window(finalize=True, title="Desktop GUI for AWS", layout=layout, margins=(10, 10))
# create an Event loop
while True:
    event, values = window.read()
    # print(event, values)
    # End program if user closes window OR presses "OK" button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "CLEAR_OUTPUT":
        window['-QUERY_OUTPUT-'].update("")

    if event == "upload_file":
        print("\n Upload File Event")
        file_path = values['source_file_path']
        file_path = str(file_path).strip("\"")
        # convert single-\ to double-\\; windows to linux path
        file_path = file_path.replace("\\","\\\\")
        print("file_path = ", file_path)
        file_name = os.path.basename(file_path)
        print("file_name = ", file_name)

        print("calling func")
        upload_file_func_return_val = \
            upload_file(file_name= file_path,
                        bucket= 'boto3-bucket-1',
                        object_name=file_name)
        if upload_file_func_return_val == -1:
            print("error, check func")

# close the window
# window.close()
