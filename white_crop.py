from PIL import Image
import os

for root, dirs, files in os.walk('.'):
    for f in files:
        try:
            image = Image.open(f)
            image = image.convert('RGB')
            w, h = image.size
            for x in range(w):
                r, g, b = image.getpixel((x, 0))
                if r + g + b == 3 * 255:
                    DW = x
                    break
            for y in range(h):
                r, g, b = image.getpixel((0, y))
                if r + g + b == 3 * 255:
                    DH = y
                    break
            img = image.crop((0, 0, x, y))
            name, ext = f.split('.')
            name = name + 'new'
            img.save(name + '.' + ext)
        except Exception as e:
            print(str(e))
        else:
            print("Image Done!")
