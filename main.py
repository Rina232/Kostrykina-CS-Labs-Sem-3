from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from PIL import Image, ImageDraw, ImageFont


def main():
    N = 13

    r = Rectangle(N, N, "синий")
    c = Circle(N, "зеленый")
    s = Square(N)
    s._color = "красный"

    print(r)
    print(c)
    print(s)

    img = Image.new('RGB', (500, 400), color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 200, 150], fill='blue')
    draw.ellipse([50, 200, 120, 270], fill="green")
    draw.rectangle([250, 50, 350, 150], fill='red')

    img.save('shapes.png')
    img.show()


if __name__ == "__main__":
    main()
