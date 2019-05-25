from PIL import Image, ImageDraw

def get_bounds():
    x_max = 1
    y_max = 1
    f = open("lines.txt")
    n = int(f.readline())
    for s in f:
        x1, y1, x2, y2 = map(int, s.split())
        x_max = max(x_max, x1, x2)
        y_max = max(y_max, y1, y2)
    f.close()
    return (x_max, y_max)

def main():
    x_max, y_max = get_bounds()
    f = open("lines.txt")
    n = int(f.readline())
    w = h = 600
    img = Image.new('1', (w, h))
    draw = ImageDraw.Draw(img)
    for s in f:
        x1, y1, x2, y2 = map(int, s.split())
        x1 = x1 / x_max * w
        x2 = x2 / x_max * w
        y1 = y1 / y_max * h
        y2 = y2 / y_max * h
        #print(x1, y1, x2, y2)
        draw.line((x1, y1, x2, y2), fill=128)
    img.save("pic.jpg")

main()
