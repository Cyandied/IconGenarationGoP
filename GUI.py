import PySimpleGUI as sg
import main
import os


sg.theme('DarkAmber')

dropDownIcons = main.getFiles()
hasTempImage = False

layout = [  [sg.Text('Genarate image with color')],
            [sg.Text('Icon type'), sg.Combo(values = dropDownIcons,key = "iconType")],
            [sg.Text('Background type'), sg.InputText("base",key = "BgType")],
            [sg.Text('Color'), sg.ColorChooserButton(target = "color", button_text = "Pick color"), sg.InputText(key="color")],
            [sg.Button('Genarate', key = "gen")],
            [sg.Image(key = "image")],
            [sg.Text('Name'), sg.InputText(key = "name")],
            [sg.FolderBrowse(button_text = "Save destination", target = "saveDest"), sg.InputText("icons",key="saveDest")],
            [sg.Button('Cancel'), sg.Button('Save', key = "save")]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        if hasTempImage:
            os.remove(f'icons/temp_temp_icon.PNG')
        break
    
    if event == "gen":
        RGB = main.HEXtoRGB(values["color"])
        main.saveIconSmall(values["iconType"], values["BgType"], RGB,"temp","icons")
        window["image"].Update(f'icons/temp_temp_icon.PNG')
        hasTempImage = True
    
    if event == "save":
        RGB = main.HEXtoRGB(values["color"])
        main.saveIcon(values["iconType"], values["BgType"], RGB,values["name"],values["saveDest"])
        os.remove(f'icons/temp_temp_icon.PNG')
        hasTempImage = False

window.close()