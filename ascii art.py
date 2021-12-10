import time
from PIL import Image
from time import sleep


def initialze_pixelarr(img, width, height):
    """
    produces a 2d list containing image pixel in format (r,g,b)
    goes from left to right and top to bottom covering each pixel

    tuple -> list
    """

    L = []
    for i in range(height):
        M = []
        for j in range(width):
            M.append(img.getpixel((j,i)))
        L.append(M)
    return L

def convert_to_average_brightness_matrix(L, width, height):
    """
        takes a 2d pixel matrix: L[height][width]
        produces a average brightness matrix (brightness = (R + G + B) / 3)
        list -> list
    """
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            average = (L[i][j][0] + L[i][j][1] + L[i][j][2])/3
            W.append(average)
        HW.append(W)

    return HW

def convert_to_luminosity_matrix(L, width, height):
    """
        takes a 2d pixel matrix: L[height][width]
        produces a luminosity matrix (luminosity = 0.21 R + 0.72 G + 0.07 B)
        list -> list
    """
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            luminosity = (0.21*L[i][j][0] + 0.72*L[i][j][1] + 0.07*L[i][j][2])
            W.append(luminosity)
        HW.append(W)

    return HW

def convert_to_lightness_matrix(L, width, height):
    """
        takes a 2d pixel matrix: L[height][width]
        produces a lightness matrix ( (max(R, G, B) + min(R, G, B)) / 2)
        list -> list
    """
    HW = []
    for i in range(height):
        W = []
        for j in range(width):
            lightness = (max(L[i][j][0], L[i][j][1], L[i][j][2]) + max(L[i][j][0], L[i][j][1], L[i][j][2]))/2
            W.append(lightness)
        HW.append(W)

    return HW

def assign_ascii(B, width, height):
    """
        takes a 2d brigtness matrix: B[height][width]
        assigns ascii to each level of brightness and produces a 2d matrix
        list -> list
    """
    ascii_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    # length = 65
    
    A = []
    for i in range(height):
        W = []
        for j in range(width):
            try:
                avg = B[i][j]
                index = int((avg//3.99))
                W.append(ascii_characters[index])
            except:
                print(index)
                break
        A.append(W)

    return A

img = Image.open("cat.jpg")     
w = img.width
h = img.height
wnew = 632
hnew = int(h - ((w-wnew)/w)*h)
print(hnew)
img_resized = img.resize((wnew, hnew))

pixel_matrix = initialze_pixelarr(img_resized, wnew, hnew)

# !!!!!!!uncomment only one of these three!!!!!!!!!

# brightness_matrix = convert_to_average_brightness_matrix(pixel_matrix, wnew, hnew)
# brightness_matrix = convert_to_luminosity_matrix(pixel_matrix, wnew, hnew)
brightness_matrix = convert_to_lightness_matrix(pixel_matrix, wnew, hnew)

ascii_art = assign_ascii(brightness_matrix, wnew, hnew)

#print the ascii art
for elementw in ascii_art:
    for elementh in elementw:
        print(elementh, end="")

#stop the terminal from closing automatically on execution
sleep(100)
