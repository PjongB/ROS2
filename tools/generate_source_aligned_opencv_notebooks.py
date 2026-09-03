#!/usr/bin/env python3
"""Build course notebooks from the code actually used in the OpenCV lectures.

The source notebooks and scripts are the student's lecture workspace. Outputs
are intentionally removed, while code order and statements are preserved.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "opencv" / "notebooks"
COURSE = Path("/home/whd0199/dev_ws/openCV/08_OpenCV")


def code_cell(source):
    lines = source.rstrip().splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines,
    }


def markdown_cell(source):
    lines = source.rstrip().splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return {"cell_type": "markdown", "metadata": {}, "source": lines}


def notebook_code(path, limit=None):
    data = json.loads(path.read_text(encoding="utf-8"))
    cells = [
        "".join(cell.get("source", []))
        for cell in data["cells"]
        if cell.get("cell_type") == "code" and "".join(cell.get("source", [])).strip()
    ]
    return cells[:limit]


def script_code(path):
    return path.read_text(encoding="utf-8").rstrip()


def write_notebook(filename, title, source_note, sections):
    cells = [
        markdown_cell(
            f"# {title}\n\n"
            f"> {source_note}\n\n"
            "강의 화면의 코드 순서와 파일명을 유지했습니다. 데이터 파일은 "
            "코드에 표시된 `./data` 또는 `../data` 상대 경로에 두세요."
        )
    ]
    for heading, code in sections:
        cells.extend([markdown_cell(f"## {heading}"), code_cell(code)])
    data = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path = OUT / filename
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))


def numbered_sections(codes, labels=None):
    labels = labels or []
    return [
        (labels[index] if index < len(labels) else f"원본 강의 코드 {index + 1:02d}", code)
        for index, code in enumerate(codes)
    ]


def main():
    write_notebook(
        "01_OpenCV_Setting.ipynb",
        "01. OpenCV 환경 설정",
        "강의 터미널 화면의 명령을 순서대로 옮겼습니다.",
        [
            ("홈 폴더 확인", "%%bash\nls\n"),
            ("opencv 가상환경 생성", "%%bash\npython3 -m venv ./venv/opencv\nls ./venv/\n"),
            ("가상환경 활성화", "%%bash\nsource ./venv/opencv/bin/activate\n"),
            ("기본 데이터 패키지 설치", "%%bash\nsource ./venv/opencv/bin/activate\npip3 install pandas matplotlib numpy scikit-learn\n"),
            ("OpenCV 설치", "%%bash\nsource ./venv/opencv/bin/activate\npip3 install opencv-python\n"),
        ],
    )

    numpy_codes = [
        "import numpy as np\nimport matplotlib.pyplot as plt\nfrom PIL import Image\n",
        "pic = Image.open('../data/test.png')\npic\n",
        "type(pic)\n",
        "pic_arr = np.asarray(pic)\ntype(pic_arr)\n",
        "pic_arr.shape\n",
        "plt.imshow(pic_arr)\n",
        "pic_red = pic_arr.copy()\nplt.imshow(pic_red[:, :, 0])\n",
        "pic_red = pic_arr.copy()\nplt.imshow(pic_red[:, :, 0], cmap='gray')\n",
        "pic_red = pic_arr.copy()\nplt.imshow(pic_red[:, :, 1], cmap='gray')\n",
        "pic_red = pic_arr.copy()\nplt.imshow(pic_red[:, :, 2], cmap='gray')\n",
        "pic_red[:, :, 1] = 0\nplt.imshow(pic_red)\n",
        "pic_red[:, :, 2] = 0\nplt.imshow(pic_red)\n",
    ]
    write_notebook(
        "02_Numpy_array_with_OpenCV.ipynb",
        "02. NumPy 배열과 이미지",
        "2번 강의 슬라이드의 PIL·NumPy·채널 실습 코드를 화면 순서대로 옮겼습니다.",
        numbered_sections(
            numpy_codes,
            ["라이브러리 준비", "PIL 이미지 읽기", "PIL 타입", "NumPy 배열 변환", "배열 크기", "전체 이미지 표시", "R 채널과 viridis", "R 채널을 gray로 표시", "G 채널", "B 채널", "G 채널 제거", "B 채널도 제거"],
        ),
    )

    image_read_codes = [
        "import matplotlib.pyplot as plt\nimport cv2\n",
        "img = cv2.imread('../data/lenna.bmp')\ntype(img)\n",
        "tmp = cv2.imread('./dddd.jpg')\ntype(tmp)\n",
        "img.shape\n",
        "fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\nplt.imshow(fix_img)\n",
        "img_gray = cv2.imread('../data/lenna.bmp', cv2.IMREAD_GRAYSCALE)\nplt.imshow(img_gray, cmap='gray')\n",
        "img.shape\n",
        "new_img = cv2.resize(fix_img, (800, 600))\nplt.imshow(new_img)\n",
        "plt.imshow(cv2.flip(fix_img, 0))\n",
        "plt.imshow(cv2.flip(fix_img, 1))\n",
        "plt.imshow(cv2.flip(fix_img, -1))\n",
        "plt.imshow(img_gray, cmap='gray')\n",
        "cv2.imwrite('../data/lenna_gray.jpg', img_gray)\n",
    ]
    write_notebook(
        "03_Image_read.ipynb",
        "03. 이미지 읽기와 표시",
        "3번 강의 슬라이드의 lenna.bmp 예제를 화면 순서대로 옮겼습니다.",
        numbered_sections(
            image_read_codes,
            ["라이브러리 준비", "이미지 읽기", "잘못된 경로 확인", "영상 크기", "BGR을 RGB로 변환", "그레이 영상 읽기", "컬러 영상 크기", "크기 변경", "상하 반전", "좌우 반전", "상하좌우 반전", "그레이 영상 표시", "그레이 영상 저장"],
        ),
    )

    write_notebook(
        "04_Draw_simple_figure.ipynb",
        "04. 기본 도형 그리기",
        "강의 실습 노트북 `imigeshow.ipynb`의 셀을 그대로 정리했습니다.",
        numbered_sections(
            notebook_code(COURSE / "imigeshow.ipynb"),
            ["라이브러리 준비", "빈 영상 만들기", "빈 영상 확인", "사각형·원·선·문자", "다각형 꼭짓점", "꼭짓점 배열 크기", "polylines 입력 형태", "원본 꼭짓점 확인", "변환된 꼭짓점 확인", "다각형 그리기"],
        ),
    )

    callback_codes = [
        '''import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8)

while True:
    cv2.imshow("my_first_drawing", img)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
''',
        '''import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, param):
    pass

cv2.namedWindow(winname="my_first_drawing")
cv2.setMouseCallback("my_first_drawing", draw_circle, img)

while True:
    cv2.imshow("my_first_drawing", img)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
''',
        '''import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x, y)

cv2.namedWindow(winname="my_first_drawing")
cv2.setMouseCallback("my_first_drawing", draw_circle, img)

while True:
    cv2.imshow("my_first_drawing", img)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
''',
        '''def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 30, (50, 50, 200), -1)
''',
        '''def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 30, (50, 50, 200), -1)
    elif event == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img, (x, y), 30, (200, 50, 50), -1)
''',
        '''import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 30, (50, 50, 200), -1)
    elif event == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img, (x, y), 30, (200, 50, 50), -1)

cv2.namedWindow(winname="my_first_drawing")
cv2.setMouseCallback("my_first_drawing", draw_circle, img)

while True:
    cv2.imshow("my_first_drawing", img)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
''',
    ]
    write_notebook(
        "05_Use_Callback_function.ipynb",
        "05. 콜백 함수 활용",
        "5번 강의 슬라이드의 mouse_event.py 변화 과정을 화면 순서대로 옮겼습니다.",
        numbered_sections(
            callback_codes,
            ["창과 waitKey 반복문", "빈 마우스 콜백 등록", "왼쪽 버튼 좌표 출력", "왼쪽 버튼으로 원 그리기", "왼쪽·오른쪽 버튼 분기", "전체 코드"],
        ),
    )

    write_notebook(
        "06_Color_space.ipynb",
        "06. 색 공간·합성·마스크",
        "강의 실습 노트북 `donotcopy.ipynb`의 셀을 그대로 정리했습니다.",
        numbered_sections(
            notebook_code(COURSE / "donotcopy.ipynb"),
            ["라이브러리 준비", "배경 영상 읽기", "워터마크 읽기", "두 영상 크기 확인", "크기 맞추기", "가중 합성", "워터마크 축소", "합성 위치 지정", "ROI에 영상 대입", "단순 합성 결과", "원본 다시 읽기", "오른쪽 아래 오프셋", "ROI 추출", "그레이 마스크", "마스크 반전", "마스크 크기 확인", "OR 마스크", "AND 마스크", "배경과 전경 합성", "결과를 원본 ROI에 기록", "추가 실습 영상", "추가 실습"],
        ),
    )

    write_notebook(
        "07_Video_capture.ipynb",
        "07. 비디오 캡처",
        "강의 작업 파일 `video.py`를 노트북 셀로 옮겼습니다.",
        [("동영상 파일 열기와 프레임 반복", script_code(COURSE.parent / "video.py"))],
    )

    filtering_files = [
        ("사용자 커널과 평균 블러", "filter.py"),
        ("3×3·5×5·7×7 평균 필터", "filter3x5x7.py"),
        ("가우시안 필터", "filter_gaussian.py"),
        ("언샤프 마스크 샤프닝", "filter_sharp.py"),
        ("메디안 필터 잡음 제거", "filter_noise.py"),
        ("카툰·스케치 카메라", "cartooncamera.py"),
    ]
    write_notebook(
        "08_Filtering.ipynb",
        "08. 이미지 필터링",
        "강의에서 작성한 `filter*.py`와 `cartooncamera.py`를 실행 순서대로 담았습니다.",
        [(title, script_code(COURSE / filename)) for title, filename in filtering_files],
    )

    translation = notebook_code(COURSE / "translation.ipynb")
    namecard = [
        code.replace(
            "/home/whd0199/dev_ws/openCV/08_OpenCV/data/pinkwink_namecard.png",
            "./data/pinkwink_namecard.png",
        )
        for code in notebook_code(COURSE / "namecard.ipynb")
    ]
    write_notebook(
        "09_Geometrical_transfer.ipynb",
        "09. 기하학적 변환",
        "강의 실습 노트북 `translation.ipynb`와 `namecard.ipynb`를 합쳤습니다. 명함 파일 경로만 배포용 상대 경로로 바꿨습니다.",
        numbered_sections(
            translation + namecard,
            ["이동 변환", "전단 변환", "확대와 축소", "회전행렬 직접 계산", "중심 기준 회전", "회전 결과 확인", "명함 실습 라이브러리", "명함 이미지 읽기", "원본 크기", "미리보기 축소", "축소 크기", "선택점과 미리보기", "마우스 콜백", "네 점 선택과 투시 변환"],
        ),
    )

    write_notebook(
        "10_Brightness_Contrast.ipynb",
        "10. 밝기와 명암비",
        "강의 실습 노트북 `10_present_prightness.ipynb`의 셀을 그대로 정리했습니다.",
        numbered_sections(
            notebook_code(COURSE / "10_present_prightness.ipynb"),
            ["라이브러리 준비", "가중 합성", "덧셈·뺄셈·곱셈·나눗셈", "절대 차이", "명암비 조절", "히스토그램 스트레칭", "밝기 채널 평활화", "HSV 색상 추출", "마스크 응용"],
        ),
    )

    morphology = notebook_code(COURSE / "11.Morphology_Gradient.ipynb")
    morphology.extend([
        "sobelx = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)\ndisplay_img(sobelx)\n",
        "sobely = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)\ndisplay_img(sobely)\n",
        "laplacian = cv2.Laplacian(img, ddepth=cv2.CV_64F)\ndisplay_img(laplacian)\n",
        "blended = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)\ndisplay_img(blended)\n",
        "ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)\ndisplay_img(th1)\n",
        "kernel = np.ones((4, 4), np.uint8)\ngradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)\ndisplay_img(gradient)\n",
    ])
    write_notebook(
        "11_Morphology_Gradient.ipynb",
        "11. 모폴로지와 그래디언트",
        "강의 실습 노트북의 모폴로지 셀과 강의 슬라이드의 Sobel·Laplacian 셀을 원래 순서로 정리했습니다.",
        numbered_sections(
            morphology,
            ["라이브러리 준비", "테스트 영상 함수", "표시 함수", "테스트 영상", "구조 요소", "침식", "침식 결과", "흰색 잡음", "잡음 영상", "오프닝", "영상 초기화", "검은 잡음", "검은 잡음 합성", "음수값 정리", "클로징", "영상 다시 준비", "형태학적 그래디언트", "x 방향 Sobel", "y 방향 Sobel", "Laplacian", "x·y 결과 합성", "임계값 처리", "합성 결과의 모폴로지 그래디언트"],
        ),
    )

    write_notebook(
        "12_Feature_extraction.ipynb",
        "12. 특징 추출",
        "강의 실습 노트북 `12.feature.ipynb`의 셀을 그대로 정리했습니다.",
        numbered_sections(
            notebook_code(COURSE / "12.feature.ipynb"),
            ["라이브러리 준비", "그레이 영상 읽기", "읽기 검사", "Sobel 크기와 임계값", "Canny 에지", "확률적 Hough 선분", "Hough 원", "동전 원 검출"],
        ),
    )

    write_notebook(
        "13_Image_Thresholding.ipynb",
        "13. 영상 이진화",
        "강의 실습 노트북 `13.image_thresholding.ipynb`에서 13번 강의 범위의 셀을 그대로 정리했습니다.",
        numbered_sections(
            notebook_code(COURSE / "13.image_thresholding.ipynb", limit=15),
            ["컬러 영상 확인", "그레이 변환", "그레이로 직접 읽기", "그레이 표시", "THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV", "불균일 조명 영상", "표시 함수", "원본 확인", "전역 임계값", "적응형 임계값", "두 결과 합성"],
        ),
    )

    binary_sections = [
        ("서로 다른 전역 임계값 비교", '''import sys
import cv2

src = cv2.imread("./data/cells.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
'''),
        ("Otsu 자동 임계값", '''import sys
import cv2

src = cv2.imread("./data/rice.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
'''),
        ("지역 적응형 이진화", '''import sys
import cv2

src = cv2.imread("./data/sudoku.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

bsize = 201
dst = cv2.adaptiveThreshold(
    src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bsize, 5
)

cv2.imshow("dst", dst)
cv2.imshow("srs", src)
cv2.namedWindow("dst")
cv2.waitKey()
cv2.destroyAllWindows()
'''),
        ("작은 행렬의 연결 요소 라벨링", '''import sys
import numpy as np
import cv2

mat = np.array(
    [
        [0, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    np.uint8,
)

cnt, labels = cv2.connectedComponents(mat)
print("sep:", mat, sep="\\n")
print("cnt:", cnt)
print("labels:", labels, sep="\\n")
'''),
        ("라벨별 통계와 바운딩 박스", '''import sys
import cv2

src = cv2.imread("./data/keyboard.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]
    if area < 20:
        continue
    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))
    cv2.putText(dst, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("src", src)
cv2.imshow("src_bin", src_bin)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
'''),
        ("외곽선으로 삼각형·사각형·원 판별", '''import math
import cv2

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def main():
    img = cv2.imread("./data/polygon.jpg", cv2.IMREAD_COLOR)
    if img is None:
        print("Image load failed!")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for pts in contours:
        if cv2.contourArea(pts) < 400:  # 너무 작으면 무시
            continue
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
        vtc = len(approx)
        if vtc == 3:
            setLabel(img, pts, "TRI")
        elif vtc == 4:
            setLabel(img, pts, "RECT")
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4.0 * math.pi * area / (length * length)
            if ratio > 0.85:
                setLabel(img, pts, "CIR")
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''),
    ]
    write_notebook(
        "14_Binary_Labeling_Contours.ipynb",
        "14. 이진화·라벨링·외곽선",
        "14번 강의 슬라이드의 여섯 코드 예제를 화면 순서대로 옮겼습니다.",
        binary_sections,
    )


if __name__ == "__main__":
    main()
