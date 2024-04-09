import cv2
import numpy as np

def translate_image(img, dx, dy, border_type=cv2.BORDER_CONSTANT, border_color=(255, 0, 0)):
    rows, cols = img.shape[0:2]
    
    # 변환 행렬 생성
    mtrx = np.float32([[1, 0, dx], [0, 1, dy]])  

    # 이동
    dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy))

    # 외곽 처리
    if border_type == cv2.BORDER_CONSTANT:
        dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, border_type, border_color)
    elif border_type == cv2.BORDER_REFLECT:
        dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, border_type)

    return dst

if __name__ == "__main__":
    img = cv2.imread('../img/fish.jpg')

    dx, dy = 100, 50  # 이동할 픽셀 거리

    translated_img = translate_image(img, dx, dy)
    border_constant_img = translate_image(img, dx, dy, cv2.BORDER_CONSTANT, (255, 0, 0))
    border_reflect_img = translate_image(img, dx, dy, cv2.BORDER_REFLECT)

    cv2.imshow('original', img)
    cv2.imshow('translated', translated_img)
    cv2.imshow('BORDER_CONSTANT', border_constant_img)
    cv2.imshow('BORDER_REFLECT', border_reflect_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()