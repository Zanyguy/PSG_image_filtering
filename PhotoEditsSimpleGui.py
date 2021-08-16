import io
import os
import PySimpleGUI as sg
from PIL import Image


file_types = [("PNG (*.png)", "*.png"),
              ("All files (*.*)", "*.*")]

def main():
    column1 = [[sg.B(image_filename ='cloud-trends.gif',
                     image_subsample=5, key = "-CLOUDS-")],
               [sg.B(image_filename ='USA-Flag.gif',
                     image_subsample=5, key = "-FLAG-")],
               [sg.B(image_filename ='desert.gif',
                     image_subsample=5, key = "-SAND-")],
               [sg.B()],
               [sg.B()],
               [sg.B()]]
    layout = [[sg.Image(key="-IMAGE-"),sg.Column(column1)],
            [sg.Text("Image File"),
             sg.Input(size=(25, 1), key="-FILE-"),
             sg.FileBrowse(file_types=file_types),
             sg.Button("Load Image")],
            [sg.Slider(range=(1,250), orientation='horizontal',)]]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        elif event == "-FLAG-":
           merged = mergeimage('USA-Flag.gif',values["-FILE-"])
           window["-IMAGE-"].update(data=merged)
        elif event == "-CLOUDS-":
           merged = mergeimage('cloud-trends.gif',values["-FILE-"])
           window["-IMAGE-"].update(data=merged)
        elif event == "-SAND-":
           merged = mergeimage('desert.gif',values["-FILE-"])
           window["-IMAGE-"].update(data=merged)
        print(event, values)
           
            
    window.close()

def mergeimage(img_file, background_file):
    background = Image.open(background_file)
    image = Image.open(img_file).convert("RGBA")
    bio = io.BytesIO()
    image.putalpha(150)
    background.paste(image, (0,0), image)
    background.save(bio, "PNG")
    return bio.getvalue()


    
if __name__ == "__main__":
    main()
