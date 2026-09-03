#!/usr/bin/env python3
"""Generate the OpenCV 11-13 practice notebooks from reviewed lecture notes."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "opencv" / "notebooks"


def markdown(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code(source: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source.splitlines(keepends=True)}


COMMON = '''from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(name, flags=cv2.IMREAD_COLOR):
    path = Path("data") / name
    image = cv2.imread(str(path), flags)
    if image is None:
        raise FileNotFoundError(path)
    return image

def show(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(5 * len(images), 4))
    axes = np.atleast_1d(axes)
    for ax, image, title in zip(axes, images, titles):
        if image.ndim == 2:
            ax.imshow(image, cmap="gray", vmin=0, vmax=255)
        else:
            ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
'''


NOTEBOOKS = {
    "11_Morphology_Gradient.ipynb": [
        markdown("# 11. 모폴로지와 그래디언트\n\n침식·팽창·열기·닫기와 Sobel·Laplacian 그래디언트를 실습합니다.\n\n> 예제 이미지는 노트북 옆 `data` 폴더에 넣으세요."),
        code(COMMON),
        markdown("## 테스트용 이진 영상과 구조 요소"),
        code('''binary = np.zeros((240, 640), dtype=np.uint8)
cv2.putText(binary, "ABCDE", (20, 170), cv2.FONT_HERSHEY_SIMPLEX, 3.2, 255, 12, cv2.LINE_AA)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
show([binary, kernel * 255], ["binary image", "3x3 kernel"])
'''),
        markdown("## 침식과 팽창"),
        code('''eroded = cv2.erode(binary, kernel, iterations=2)
dilated = cv2.dilate(binary, kernel, iterations=2)
show([binary, eroded, dilated], ["source", "erosion", "dilation"])
'''),
        markdown("## 열기와 닫기"),
        code('''rng = np.random.default_rng(7)
salt = binary.copy()
ys = rng.integers(0, salt.shape[0], 1200)
xs = rng.integers(0, salt.shape[1], 1200)
salt[ys, xs] = 255

pepper = binary.copy()
ys = rng.integers(0, pepper.shape[0], 1200)
xs = rng.integers(0, pepper.shape[1], 1200)
pepper[ys, xs] = 0

opened = cv2.morphologyEx(salt, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(pepper, cv2.MORPH_CLOSE, kernel)
show([salt, opened, pepper, closed], ["salt noise", "opening", "pepper holes", "closing"])
'''),
        markdown("## 형태학적 그래디언트"),
        code('''morph_gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
show([binary, morph_gradient], ["source", "morphological gradient"])
'''),
        markdown("## Sobel과 Laplacian"),
        code('''gray = read_image("sudoku.jpg", cv2.IMREAD_GRAYSCALE)
gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
magnitude = cv2.magnitude(gx, gy)
laplacian = cv2.Laplacian(gray, cv2.CV_32F)

gx_view = cv2.convertScaleAbs(gx)
gy_view = cv2.convertScaleAbs(gy)
mag_view = cv2.convertScaleAbs(magnitude)
lap_view = cv2.convertScaleAbs(laplacian)
show([gray, gx_view, gy_view, mag_view, lap_view], ["source", "Sobel x", "Sobel y", "magnitude", "Laplacian"])
'''),
    ],
    "12_Feature_extraction.ipynb": [
        markdown("# 12. 특징 추출\n\nSobel·Scharr·Canny 에지와 Hough 직선·원 검출을 실습합니다.\n\n> 예제 이미지는 노트북 옆 `data` 폴더에 넣으세요."),
        code(COMMON),
        markdown("## Sobel·Scharr 그래디언트"),
        code('''src = read_image("lenna.bmp")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
scharr_x = cv2.Scharr(gray, cv2.CV_32F, 1, 0)
magnitude, angle = cv2.cartToPolar(sobel_x, sobel_y, angleInDegrees=True)
show([gray, cv2.convertScaleAbs(sobel_x), cv2.convertScaleAbs(sobel_y), cv2.convertScaleAbs(scharr_x), cv2.convertScaleAbs(magnitude)], ["gray", "Sobel x", "Sobel y", "Scharr x", "magnitude"])
'''),
        markdown("## Canny 에지"),
        code('''blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)
canny = cv2.Canny(blurred, 80, 160)
show([gray, blurred, canny], ["gray", "Gaussian blur", "Canny"])
'''),
        markdown("## 확률적 Hough 직선 검출"),
        code('''line_src = read_image("building.jpg")
line_gray = cv2.cvtColor(line_src, cv2.COLOR_BGR2GRAY)
line_edges = cv2.Canny(line_gray, 50, 150)
lines = cv2.HoughLinesP(line_edges, 1, np.pi / 180, threshold=70, minLineLength=50, maxLineGap=10)
line_result = line_src.copy()
if lines is not None:
    for x1, y1, x2, y2 in lines[:, 0]:
        cv2.line(line_result, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)
show([line_src, line_edges, line_result], ["source", "edges", "Hough lines"])
'''),
        markdown("## Hough 원 검출"),
        code('''coin_src = read_image("coins.jpg")
coin_gray = cv2.cvtColor(coin_src, cv2.COLOR_BGR2GRAY)
coin_blur = cv2.GaussianBlur(coin_gray, (0, 0), 1.5)
circles = cv2.HoughCircles(coin_blur, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=120, param2=30, minRadius=10, maxRadius=100)
coin_result = coin_src.copy()
circle_list = [] if circles is None else np.uint16(np.around(circles[0]))
for x, y, radius in circle_list:
    cv2.circle(coin_result, (x, y), radius, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.circle(coin_result, (x, y), 2, (255, 0, 0), 3, cv2.LINE_AA)
print("검출된 동전 수:", len(circle_list))
show([coin_src, coin_result], ["source", "detected circles"])
'''),
        markdown("## 중심 HSV로 동전 종류 분류"),
        code('''hsv = cv2.cvtColor(coin_src, cv2.COLOR_BGR2HSV)
coin_values = []
for x, y, radius in circle_list:
    hue = int(hsv[y, x, 0])
    value = 100 if 5 <= hue <= 25 else 500
    coin_values.append(value)
print("동전 값:", coin_values)
print("합계:", sum(coin_values), "원")
'''),
    ],
    "13_Image_Thresholding.ipynb": [
        markdown("# 13. 영상 이진화\n\n전역 임계값 모드와 평균·가우시안 적응형 이진화를 비교합니다.\n\n> 문서 예제 이미지는 노트북 옆 `data` 폴더에 `crossword.jpg`로 넣으세요."),
        code(COMMON),
        markdown("## 임계값 모드 비교"),
        code('''gradient = np.tile(np.arange(256, dtype=np.uint8), (180, 1))
modes = [
    (cv2.THRESH_BINARY, "BINARY"),
    (cv2.THRESH_BINARY_INV, "BINARY_INV"),
    (cv2.THRESH_TRUNC, "TRUNC"),
    (cv2.THRESH_TOZERO, "TOZERO"),
    (cv2.THRESH_TOZERO_INV, "TOZERO_INV"),
]
results, titles = [gradient], ["source"]
for mode, name in modes:
    _, dst = cv2.threshold(gradient, 127, 255, mode)
    results.append(dst)
    titles.append(name)
show(results, titles)
'''),
        markdown("## 전역 임계값"),
        code('''document = read_image("crossword.jpg", cv2.IMREAD_GRAYSCALE)
_, global_binary = cv2.threshold(document, 127, 255, cv2.THRESH_BINARY)
show([document, global_binary], ["source", "global threshold"])
'''),
        markdown("## 평균 적응형 이진화"),
        code('''adaptive_mean = cv2.adaptiveThreshold(
    document, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, blockSize=21, C=10,
)
show([document, global_binary, adaptive_mean], ["source", "global", "adaptive mean"])
'''),
        markdown("## 가우시안 적응형 이진화"),
        code('''adaptive_gaussian = cv2.adaptiveThreshold(
    document, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, blockSize=21, C=10,
)
comparison = cv2.addWeighted(adaptive_mean, 0.5, adaptive_gaussian, 0.5, 0)
show([adaptive_mean, adaptive_gaussian, comparison], ["adaptive mean", "adaptive Gaussian", "overlay"])
'''),
        markdown("## blockSize와 C 비교"),
        code('''settings = [(11, 5), (21, 10), (41, 15)]
outputs = [cv2.adaptiveThreshold(document, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block, c) for block, c in settings]
show(outputs, [f"block={block}, C={c}" for block, c in settings])
'''),
    ],
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    metadata = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3"},
    }
    for filename, cells in NOTEBOOKS.items():
        document = {"cells": cells, "metadata": metadata, "nbformat": 4, "nbformat_minor": 5}
        path = OUT / filename
        path.write_text(json.dumps(document, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
