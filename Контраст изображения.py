from PIL import Image


def image_filter(pixels_: list, i: int, j: int, n_: int, flag: bool, image) -> None:
    """КОНТРАСТ по высчитываему коэффиценту k через n_, делаем более светлые пиксели светлее, более тёмные темнее """
    k = (101 - n_) / 100
    if not flag:
        im2 = Image.new('RGB', (i, j), 'black')
        B = im2.load()
        for row in range(i):
            for col in range(j):
                r, g, b = pixels[row, col]
                if r + g + b < int(256 * 1.5):
                    B[row, col] = int(r * k), int(b * k), int(g * k)
                else:
                    if int(r / k) < 256:
                        r = int(r / k)
                    else:
                        r = 255
                    if int(g / k) < 256:
                        g = int(g / k)
                    else:
                        g = 255
                    if int(b / k) < 256:
                        b = int(b / k)
                    else:
                        b = 255
                    B[row, col] = r, g, b
        im2.save('1.png')
    else:
        for row in range(i):
            for col in range(j):
                r, g, b = pixels[row, col]
                if r + g + b < int(256 * 1.5):
                    pixels[row, col] = int(r * k), int(b * k), int(g * k)
                else:
                    if int(r / k) < 256:
                        r = int(r / k)
                    else:
                        r = 255
                    if int(g / k) < 256:
                        g = int(g / k)
                    else:
                        g = 255
                    if int(b / k) < 256:
                        b = int(b / k)
                    else:
                        b = 255
                    pixels[row, col] = r, g, b
        image.save('image.jpg')


n = input('На сколько баллов от 1 до 100 включительно вы хотите повысить контрасность? ')
while not (n.isdigit() and abs(int(n)) < 101):
    print('Некорректный ввод')
    n = input('На сколько баллов от 1 до 100 включительно вы хотите повысить контрасность? ')
n = int(n)
im = Image.open('image.jpg')
x, y = im.size
pixels = im.load()
q = input('Сохранить результат в новом файле или заменить существующий файл с изображением? 1 или 2? ')
while q != '1' and q != '2':
    print('Некорректный ввод')
    q = input('Сохранить результат в новом файле или заменить существующий файл с изображением? 1 или 2? ')
image_filter(pixels, x, y, n, bool(int(q) - 1), im)
