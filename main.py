from PIL import Image as img
from os import listdir
from os.path import isfile, join

def changeColor(image:str,newColor:tuple):
    picture = img.open(f'alpha/{image}_alpha.png')
    width, height = picture.size
    color = (newColor[0], newColor[1], newColor[2], 255)
    for x in range(width):
        for y in range(height):
            currentColor = picture.getpixel((x,y))
            if currentColor != (0,0,0,0):
                picture.putpixel((x,y), color)
    return picture

def genarateIcon(image:str, backgroundType:str, newColor:tuple):
    alpha = changeColor(image,newColor)
    background = img.open(f'backgrounds/{backgroundType}Background.png')
    glowEffect = img.open(f'backgrounds/glowEffect/{image}_gloweffect.png')
    foreground = img.open(f'foregrounds/{image}_lines.png')
    background = img.alpha_composite(background,glowEffect)
    background = img.alpha_composite(background,alpha)
    background = img.alpha_composite(background,foreground)
    return background

def saveIconSmall(image:str, backgroundType:str, newColor:tuple,color:str,dest:str):
    icon = genarateIcon(image, backgroundType, newColor)
    icon = icon.resize((400, 400))
    icon.save(f'{dest}/temp_{color}_icon.PNG', "PNG")

def saveIcon(image:str, backgroundType:str, newColor:tuple,color:str,dest:str):
    icon = genarateIcon(image, backgroundType, newColor)
    icon.save(f'{dest}/{image}_{color}_icon.PNG', "PNG")

def HEXtoRGB(HEX:str) -> tuple:
        trash, HEX = HEX.split("#")
        RGB = tuple(int(HEX[i:i+2], 16) for i in (0, 2, 4))
        return RGB

def getFiles():
    onlyfilesIconType = [f for f in listdir("alpha") if isfile(join("alpha", f))]
    nameListIconType = []
    for entry in onlyfilesIconType:
        name = entry.split("_")
        nameListIconType.append(name[0])
    return nameListIconType


