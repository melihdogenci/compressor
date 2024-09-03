import FreeSimpleGUI as sg
from cli import make_archive

label1 = sg.Text('Select files to compress: ')
input1 = sg.Input()
choose_button = sg.FilesBrowse('Choose', key="files", font=("Helvetica", 10))

label2 = sg.Text('Select destination folder: ')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key="folder", font=("Helvetica", 10))

compress_button = sg.Button('Compress')
output = sg.Text(key="output", text_color="green")

window = sg.Window('File Compressor',
                   layout=[[label1, input1, choose_button],
                           [label2, input2, choose_button2],
                           [compress_button, output]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    filepaths = values["files"].split(";")
    folder = values["folder"]

    # Error handling for missing input
    if not filepaths or not filepaths[0]:
        window['output'].update(value="Please select files to compress!", text_color="red")
        continue
    if not folder:
        window['output'].update(value="Please select a destination folder!", text_color="red")
        continue

    name = sg.popup_get_text("ZIP File Name")
    if not name:
        window['output'].update(value="Operation cancelled: No ZIP file name provided.", text_color="red")
        continue

    # Call make_archive function
    try:
        make_archive(filepaths, folder, name)
        window['output'].update(value="Compressing completed!", text_color="green")
    except Exception as e:
        window['output'].update(value=f"Error: {str(e)}", text_color="red")

window.close()





