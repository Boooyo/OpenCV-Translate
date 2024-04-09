## Open CV - Translate

![title](https://viso.ai/wp-content/uploads/2022/04/opencv-wallpaper.png)   

안녕하세요, 이미지를 이동을 하는 방법에 대해 알아보겠습니다. 이번 포스팅 역시 **'파이썬으로 만드는 OpenCV 프로젝트(이세우 저)'** 를 정리한 것임을 밝힙니다.

<br>

### translate_image 함수
- translate_image 함수는 이미지를 이동하고 외곽을 처리하는 함수입니다.
함수는 다음 매개변수를 가집니다:
- img: 이동할 이미지입니다.
- dx: x축 방향으로 이동할 픽셀 수입니다.
- dy: y축 방향으로 이동할 픽셀 수입니다.
- border_type: 외곽 처리 유형을 지정하는 매개변수입니다. 기본값은 cv2.BORDER_CONSTANT로 설정되어 있습니다.
- border_color: cv2.BORDER_CONSTANT를 선택한 경우에만 사용되는 외곽 픽셀의 색상을 지정하는 매개변수입니다. 기본값은 파란색(255, 0, 0)입니다.

### 함수는 다음 작업을 수행합니다
- 이미지의 크기를 가져옵니다.
- 이동을 위한 변환 행렬을 생성합니다.
- cv2.warpAffine 함수를 사용하여 이미지를 이동시킵니다.
- 선택한 외곽 처리 방법에 따라 외곽을 처리합니다.

<br>

### if __name__ == "__main__": 블록:
이 부분은 스크립트가 직접 실행될 때 실행되는 부분입니다.
<br>
- ../img/fish.jpg에서 이미지를 읽어옵니다.
- 이동할 픽셀 거리를 설정합니다.
- translate_image 함수를 사용하여 이미지를 이동시키고 외곽 처리된 이미지를 얻습니다.
- cv2.imshow 함수를 사용하여 원본 이미지와 이동된 이미지를 화면에 표시합니다.
- cv2.waitKey 함수를 사용하여 사용자의 키 입력을 기다립니다.
- cv2.destroyAllWindows 함수를 사용하여 모든 창을 닫습니다.
