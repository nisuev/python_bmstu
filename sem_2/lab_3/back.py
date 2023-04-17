from PIL import Image


# Процедура для шифрования.
def encode(filename: str, message: str):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        return

    length = len(message)
    data = list(image.getdata())
    bin_length = eight_bin(length)

    for i in range(3):
        first_pixel = list(data[i])
        put_element(first_pixel, bin_length[3*i:3 * (i + 1) - (1 if 3 * i == 9 else 0)])
        data[i] = tuple(first_pixel)

    for i in range(1, length + 1):
        char = eight_bin(ord(message[i - 1]))
        for j in range(3):
            pixel = list(data[3 * i + j])
            put_element(pixel, char[3*j:3 * (j + 1) - (1 if 3 * j == 9 else 0)])
            data[3 * i + j] = tuple(pixel)

    image.close()
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(data)
    new_image.save(filename[:-4] + "_code.bmp")


# Процедура для дешифрования.
def decode(filename: str) -> str:
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        return ""

    data = list(image.getdata())
    image.close()

    message = ""
    length = get_element(data[0:3])

    for i in range(1, length + 1):
        message += chr(get_element(data[3*i:3*(i + 1)]))

    return message


# Функция для представления числа в восьмибитном виде.
def eight_bin(number: int):
    return bin(number)[2:].rjust(8, "0")


# Получение элемента из одного пикселя.
def put_element(pixel: list, element: str):
    for i, bites in enumerate(element):
        pixel[i] = int((eight_bin(pixel[i]) + element[i])[1:], 2)


# Упаковка элемента в пиксель.
def get_element(pixels: list) -> int:
    element = ""
    for pixel in pixels:
        for bit in pixel:
            element += eight_bin(bit)[-1]

    return int(element[:-1], 2)
