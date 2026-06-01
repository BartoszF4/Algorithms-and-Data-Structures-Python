from PIL import Image

def load_image_rgb(filepath):
    img = Image.open(filepath).convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())
    img_2d = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[y * width + x])
        img_2d.append(row)
    return img_2d, width, height

def load_image_grayscale(filepath):
    img = Image.open(filepath).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    img_2d = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[y * width + x])
        img_2d.append(row)
    return img_2d, width, height

def save_image_rgb(img_2d, filepath):
    height = len(img_2d)
    width = len(img_2d[0])
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append(img_2d[y][x])
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    img.save(filepath)

def save_image_grayscale(img_2d, filepath):
    height = len(img_2d)
    width = len(img_2d[0])
    pixels = []
    for y in range(height):
        for x in range(width):
            pixels.append(img_2d[y][x])
    img = Image.new('L', (width, height))
    img.putdata(pixels)
    img.save(filepath)