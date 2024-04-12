import cv2
import numpy as np

def translate_image(img, dx, dy, border_type=cv2.BORDER_CONSTANT, border_color=(255, 0, 0)):
    rows, cols = img.shape[0:2]
    
    # Translation matrix
    mtrx = np.float32([[1, 0, dx], [0, 1, dy]])  

    # Translation
    dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy))

    # Handling borders
    dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, border_type, border_color)

    return dst

if __name__ == "__main__":
    img = cv2.imread('../img/fish.jpg')

    dx, dy = 100, 50  # Pixel distances to move

    translated_img = translate_image(img, dx, dy)
    border_constant_img = translate_image(img, dx, dy, cv2.BORDER_CONSTANT, (255, 0, 0))
    border_reflect_img = translate_image(img, dx, dy, cv2.BORDER_REFLECT)

    cv2.imshow('Original', img)
    cv2.imshow('Translated', translated_img)
    cv2.imshow('Border Constant', border_constant_img)
    cv2.imshow('Border Reflect', border_reflect_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
