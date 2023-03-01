import PySimpleGUI as sg
import main
import os


sg.theme('DarkAmber')

dropDownIcons = main.getFiles()
hasTempImage = False
alphas = None

colorsToChoose = [sg.Text("Select a icon type first!")]

layout = [  [sg.Text('Genarate image with color')],
            [sg.Text('Icon type'), sg.Combo(values = dropDownIcons,key = "iconType")],
            [sg.Text('Background type'), sg.InputText("base",key = "BgType")],
            [ sg.Button("Show me the color options!", key = "show")],
            [sg.Button('Cancel')]]



# Create the Window
window = sg.Window('Icon chooser', layout)
windowColorOpen = False
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        if hasTempImage:
            os.remove(f'icons/temp_temp_icon.PNG')
        break

    if event == "show":
        alphas, num = main.findAlphas(values["iconType"])
        colorsToChoose = [[sg.ColorChooserButton(f'Choose color {i}',target = f'color{i}'), sg.Input(key = f'color{i}')] for i in num]

        layoutColor = [
            [*colorsToChoose],
            [sg.Button('Genarate', key = "gen")],
            [sg.Image(key = "image")],
            [sg.Text('Name'), sg.InputText(key = "name")],
            [sg.FolderBrowse(button_text = "Save destination", target = "saveDest"), sg.InputText("icons",key="saveDest")],
            [sg.Button('Cancel'), sg.Button('Save', key = "save")]
        ]
        windowColor = sg.Window("Color chooser", layoutColor)

        windowColorOpen = True

    while windowColorOpen:
        eventC, valsC = windowColor.read(timeout = 100)
        if eventC == sg.WIN_CLOSED or eventC == "Cancel":
            if hasTempImage:
                os.remove(f'icons/temp_temp_icon.PNG')
            windowColorOpen = False
            hasTempImage = False
            windowColor.close()

        if eventC == "gen":
            colors = []
            for i in range(len(alphas)):
                colors.append(valsC[f'color{i}'])
            RGBs = main.HEXtoRGB(colors)

            main.saveIconSmall(alphas, values["BgType"],values["iconType"], RGBs,"icons", 0.2)
            windowColor["image"].Update('icons/temp_temp_icon.PNG')
            hasTempImage = True
        
        if eventC == "save":
            colors = []
            for i in range(len(alphas)):
                colors.append(valsC[f'color{i}'])
            RGBs = main.HEXtoRGB(colors)

            main.saveIcon(alphas, values["BgType"],values["iconType"], RGBs,valsC["name"],valsC["saveDest"])
            os.remove(f'icons/temp_temp_icon.PNG')
            hasTempImage = False
            windowColorOpen = False


window.close()