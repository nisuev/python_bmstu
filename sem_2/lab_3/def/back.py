def write_right_line(size: list[int, int], pix_mat: list[list[tuple]], color) -> list[list[tuple]]:
    begin = 50
    for i in range(size[1]):
        if begin == -1:
            begin = 49
        for j in range(begin, size[0], 50):
            pix_mat[i][j] = color
        begin -= 1

    return pix_mat


def write_left_line(size: list[int, int], pix_mat: list[list[tuple]], color) -> list[list[tuple]]:
    begin = 0
    for i in range(size[1]):
        if begin == 51:
            begin = 1
        for j in range(begin, size[0], 50):
            pix_mat[i][j] = color
        begin += 1

    return pix_mat


def write_up_line(size: list[int, int], pix_mat: list[list[tuple]], color) -> list[list[tuple]]:
    begin = 50
    for i in range(size[1]):
        for j in range(begin, size[0], 50):
            pix_mat[i][j] = color

    return pix_mat


def write_hor_line(size: list[int, int], pix_mat: list[list[tuple]], color) -> list[list[tuple]]:
    begin = 50
    for i in range(begin, size[1], 50):
        for j in range(size[0]):
            pix_mat[i][j] = color

    return pix_mat


def inverse(size, pixels):
    for i in range(size[0] * size[1]):
        inverse_pixel = []
        for j in pixels[i]:
            inverse_pixel.append(abs(j - 255))
        pixels[i] = tuple(inverse_pixel)

    return pixels
