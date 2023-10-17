import os

from PIL import Image, ImageEnhance,ImageFilter

path = "./imgs"
pathOut = "/editedImgs"


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}").convert("L")

    clean_name = os.path.splitext(filename)[0]

    edit = img.filter(ImageFilter.SHARPEN)

    edit.save(f"./{pathOut}/{clean_name}_edited.jpg")



