import os
from shutil import copy

root = "C:/Users/star/Desktop/json"
out = "C:/Users/star/Desktop/json/classes"
dirs = os.listdir(root)
imgs = []

for dir in dirs:
    if os.path.isdir(os.path.join(root, dir)):
        imgs = os.listdir(os.path.join(root, dir))
    else:
        continue
    for img in imgs:
        if img == "img.png":
            if not os.path.exists(out):
                os.mkdir(out)
            copy(os.path.join(root, dir, img), os.path.join(out, "data", dir + ".png"))
        if img == "label.png":
            if not os.path.exists(out):
                os.mkdir(out)
            copy(os.path.join(root, dir, img), os.path.join(out, "label", dir + ".png"))
