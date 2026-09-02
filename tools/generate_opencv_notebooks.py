#!/usr/bin/env python3
"""Generate the downloadable OpenCV lecture notebooks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "opencv" / "notebooks"


def lines(text: str) -> list[str]:
    text = text.strip("\n") + "\n"
    return text.splitlines(keepends=True)


def markdown(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": lines(text)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines(text),
    }


def notebook(title: str, summary: str, cells: list[dict]) -> dict:
    intro = f"""# {title}

{summary}

강의 슬라이드의 코드를 실행 순서에 맞게 정리한 실습 노트북입니다.

> 이미지 예제는 노트북과 같은 위치에 `data` 폴더를 만들고 강의에서 사용하는 파일을 넣어 실행하세요.  
> `cv2.imshow()`와 카메라·마우스 예제는 데스크톱 Jupyter/VS Code 환경에서 실행하는 것을 권장합니다.
"""
    return {
        "cells": [markdown(intro), *cells],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


NOTEBOOKS = {
    "01_OpenCV_Setting.ipynb": notebook(
        "01. OpenCV 환경 설정",
        "Python 가상환경에 OpenCV와 Jupyter 실습 도구를 설치하고 버전을 확인합니다.",
        [
            markdown("## 1. 패키지 설치\n\n아래 셀은 현재 Jupyter 커널의 Python 환경에 패키지를 설치합니다."),
            code("""%pip install --upgrade pip
%pip install opencv-python numpy matplotlib pillow"""),
            markdown("## 2. 설치 확인"),
            code("""import sys
import cv2
import numpy as np
import matplotlib

print("Python:", sys.version.split()[0])
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Matplotlib:", matplotlib.__version__)"""),
            markdown("## 3. 첫 OpenCV 이미지 만들기"),
            code("""import matplotlib.pyplot as plt

img = np.zeros((240, 400, 3), dtype=np.uint8)
cv2.putText(img, "Hello OpenCV", (45, 130),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 230, 120), 2, cv2.LINE_AA)

plt.figure(figsize=(8, 4))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()"""),
        ],
    ),
    "02_Numpy_array_with_OpenCV.ipynb": notebook(
        "02. NumPy 배열과 OpenCV",
        "이미지가 NumPy 배열로 표현되는 원리와 RGB 채널별 픽셀 연산을 익힙니다.",
        [
            code("""from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt"""),
            markdown("## 1. 이미지 읽기\n\n`sample.jpg`가 없으면 실습용 컬러 이미지를 자동으로 만듭니다."),
            code("""path = Path("data/sample.jpg")
if path.exists():
    bgr = cv2.imread(str(path))
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
else:
    x = np.linspace(0, 255, 640, dtype=np.uint8)
    y = np.linspace(0, 255, 360, dtype=np.uint8)[:, None]
    rgb = np.dstack((np.tile(x, (360, 1)), np.tile(y, (1, 640)), np.full((360, 640), 128, np.uint8)))

print(type(rgb), rgb.shape, rgb.dtype)
plt.imshow(rgb)
plt.axis("off");"""),
            markdown("## 2. 채널별 값 관찰"),
            code("""fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for axis, channel, name in zip(axes, range(3), ["Red", "Green", "Blue"]):
    axis.imshow(rgb[:, :, channel], cmap="gray", vmin=0, vmax=255)
    axis.set_title(name)
    axis.axis("off")
plt.show()"""),
            markdown("## 3. 특정 채널 제거"),
            code("""without_green = rgb.copy()
without_green[:, :, 1] = 0

plt.imshow(without_green)
plt.title("Green channel = 0")
plt.axis("off");"""),
            markdown("## 4. 픽셀과 영역 수정"),
            code("""edited = rgb.copy()
edited[40:140, 40:220] = (255, 80, 80)
edited[180:300, 360:580, 2] = 255

plt.imshow(edited)
plt.axis("off");"""),
        ],
    ),
    "03_Image_read.ipynb": notebook(
        "03. 이미지 읽기와 표시",
        "`imread`, 색상 변환, 크기 변경, 반전, 저장 방법을 실습합니다.",
        [
            code("""from pathlib import Path
import cv2
import matplotlib.pyplot as plt

path = Path("data/sample.jpg")
if not path.exists():
    raise FileNotFoundError("data/sample.jpg 파일을 준비하세요.")

img_bgr = cv2.imread(str(path))
if img_bgr is None:
    raise RuntimeError("이미지를 읽지 못했습니다.")

print("shape:", img_bgr.shape, "dtype:", img_bgr.dtype)"""),
            markdown("## BGR을 RGB로 변환하여 표시"),
            code("""img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis("off");"""),
            markdown("## 그레이스케일로 읽기"),
            code("""gray = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
print("gray shape:", gray.shape)
plt.imshow(gray, cmap="gray")
plt.axis("off");"""),
            markdown("## 크기 변경과 반전"),
            code("""small = cv2.resize(img_rgb, (320, 240))
flip_vertical = cv2.flip(small, 0)
flip_horizontal = cv2.flip(small, 1)
flip_both = cv2.flip(small, -1)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for ax, image, title in zip(axes,
    [small, flip_vertical, flip_horizontal, flip_both],
    ["resize", "vertical", "horizontal", "both"]):
    ax.imshow(image); ax.set_title(title); ax.axis("off")
plt.show()"""),
            markdown("## 이미지 저장"),
            code("""output = Path("output")
output.mkdir(exist_ok=True)
cv2.imwrite(str(output / "gray.png"), gray)
cv2.imwrite(str(output / "flipped.jpg"), cv2.cvtColor(flip_both, cv2.COLOR_RGB2BGR))
print("저장 완료:", output.resolve())"""),
        ],
    ),
    "04_Draw_simple_figure.ipynb": notebook(
        "04. 기본 도형 그리기",
        "빈 캔버스에 사각형, 원, 선, 텍스트, 다각형을 그립니다.",
        [
            code("""import cv2
import numpy as np
import matplotlib.pyplot as plt

canvas = np.zeros((512, 512, 3), dtype=np.uint8)"""),
            markdown("## 사각형·원·선·텍스트"),
            code("""cv2.rectangle(canvas, (30, 30), (220, 160), (0, 255, 0), 6)
cv2.rectangle(canvas, (300, 30), (480, 160), (255, 0, 0), -1)
cv2.circle(canvas, (256, 285), 70, (0, 0, 255), 6)
cv2.circle(canvas, (100, 290), 45, (255, 0, 255), -1)
cv2.line(canvas, (0, 0), (511, 511), (180, 180, 180), 3, cv2.LINE_AA)
cv2.putText(canvas, "OpenCV", (145, 475), cv2.FONT_HERSHEY_TRIPLEX,
            1.4, (255, 255, 255), 2, cv2.LINE_AA)

plt.figure(figsize=(7, 7))
plt.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
plt.axis("off");"""),
            markdown("## 다각형"),
            code("""polygon_img = np.zeros((512, 512, 3), dtype=np.uint8)
vertices = np.array([[100, 300], [200, 120], [420, 260], [260, 430]], dtype=np.int32)
points = vertices.reshape((-1, 1, 2))

cv2.polylines(polygon_img, [points], isClosed=True,
              color=(0, 255, 0), thickness=5, lineType=cv2.LINE_AA)
cv2.fillPoly(polygon_img, [points], color=(40, 90, 180))

plt.imshow(cv2.cvtColor(polygon_img, cv2.COLOR_BGR2RGB))
plt.axis("off");"""),
        ],
    ),
    "05_Use_Callback_function.ipynb": notebook(
        "05. 콜백 함수 활용",
        "OpenCV 창에 마우스 콜백을 연결하여 자유롭게 선을 그립니다.",
        [
            markdown("## 마우스 이벤트 확인\n\n아래 예제는 데스크톱 OpenCV 창을 사용합니다. ESC를 누르면 종료됩니다."),
            code("""import cv2
import numpy as np

old_x = old_y = -1
image = np.ones((480, 640, 3), dtype=np.uint8) * 255

def on_mouse(event, x, y, flags, param):
    global old_x, old_y
    if event == cv2.EVENT_LBUTTONDOWN:
        old_x, old_y = x, y
        print(f"LBUTTON DOWN: {x}, {y}")
    elif event == cv2.EVENT_LBUTTONUP:
        print(f"LBUTTON UP: {x}, {y}")
    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        cv2.line(param, (old_x, old_y), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
        old_x, old_y = x, y

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse, image)

while True:
    cv2.imshow("image", image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()"""),
            markdown("## 콜백 핵심\n\n- 콜백 함수 형식: `callback(event, x, y, flags, param)`\n- `event`: 클릭·이동 같은 사건\n- `flags`: 버튼이 눌린 상태\n- `param`: 콜백에 전달할 사용자 데이터"),
        ],
    ),
    "06_Color_space.ipynb": notebook(
        "06. 색 공간",
        "BGR·RGB·HSV 변환, 이미지 합성, ROI와 마스크를 이용한 워터마크를 실습합니다.",
        [
            code("""from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_rgb(path):
    image = cv2.imread(str(path))
    if image is None:
        raise FileNotFoundError(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)"""),
            markdown("## BGR·RGB·HSV 변환"),
            code("""image = read_rgb(Path("data/sample.jpg"))
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
axes[0].imshow(image); axes[0].set_title("RGB")
for ax, channel, title in zip(axes[1:], cv2.split(hsv), ["Hue", "Saturation", "Value"]):
    ax.imshow(channel, cmap="gray"); ax.set_title(title)
for ax in axes: ax.axis("off")
plt.show()"""),
            markdown("## 크기를 맞춘 뒤 가중 합성"),
            code("""overlay = read_rgb(Path("data/watermark_no_copy.png"))
overlay = cv2.resize(overlay, (image.shape[1], image.shape[0]))
blended = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)

plt.imshow(blended)
plt.axis("off");"""),
            markdown("## ROI와 마스크로 워터마크 합성"),
            code("""base = image.copy()
logo = read_rgb(Path("data/watermark_no_copy.png"))
logo = cv2.resize(logo, (min(320, base.shape[1] // 3), min(180, base.shape[0] // 3)))

y0 = base.shape[0] - logo.shape[0]
x0 = base.shape[1] - logo.shape[1]
roi = base[y0:, x0:]

gray = cv2.cvtColor(logo, cv2.COLOR_RGB2GRAY)
_, mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY_INV)
background = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
foreground = cv2.bitwise_and(logo, logo, mask=mask)
base[y0:, x0:] = cv2.add(background, foreground)

plt.imshow(base)
plt.axis("off");"""),
        ],
    ),
    "07_Video_capture.ipynb": notebook(
        "07. 비디오 캡처",
        "카메라 프레임을 읽고 속성을 확인하며 동영상 파일로 저장합니다.",
        [
            markdown("## 카메라 장치 확인\n\nLinux 터미널에서는 `ls /dev/video*`로 카메라 장치를 확인할 수 있습니다."),
            code("""import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("카메라를 열 수 없습니다.")

print("width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("fps:", cap.get(cv2.CAP_PROP_FPS))

while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF in (27, ord("q")):
        break

cap.release()
cv2.destroyAllWindows()"""),
            markdown("## 카메라 영상 저장\n\n`q` 또는 ESC를 누르면 저장을 마칩니다."),
            code("""cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("카메라를 열 수 없습니다.")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

while True:
    ok, frame = cap.read()
    if not ok:
        break
    writer.write(frame)
    cv2.imshow("recording", frame)
    if cv2.waitKey(1) & 0xFF in (27, ord("q")):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
print("output.mp4 저장 완료")"""),
        ],
    ),
    "08_Filtering.ipynb": notebook(
        "08. 이미지 필터링",
        "평균·가우시안·샤프닝·메디안·양방향 필터와 카툰 카메라를 실습합니다.",
        [
            code("""from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(name, mode=cv2.IMREAD_COLOR):
    image = cv2.imread(str(Path("data") / name), mode)
    if image is None:
        raise FileNotFoundError(f"data/{name}")
    return image

def show(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(5 * len(images), 4))
    axes = np.atleast_1d(axes)
    for ax, image, title in zip(axes, images, titles):
        ax.imshow(image if image.ndim == 2 else cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
                  cmap="gray" if image.ndim == 2 else None)
        ax.set_title(title); ax.axis("off")
    plt.show()"""),
            markdown("## 평균값 필터"),
            code("""src = read_image("rose.bmp", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), dtype=np.float32) / 25
filtered = cv2.filter2D(src, -1, kernel)
blurred = cv2.blur(src, (5, 5))
show([src, filtered, blurred], ["source", "filter2D", "blur"])

sizes = [3, 5, 7]
results = [cv2.blur(src, (size, size)) for size in sizes]
show(results, [f"mean {size}x{size}" for size in sizes])"""),
            markdown("## 가우시안 필터와 언샤프 마스크"),
            code("""gaussians = [cv2.GaussianBlur(src, (0, 0), sigma) for sigma in range(1, 6)]
show(gaussians, [f"sigma={sigma}" for sigma in range(1, 6)])

smooth = cv2.GaussianBlur(src, (0, 0), 2)
sharp = np.clip(2.0 * src - smooth, 0, 255).astype(np.uint8)
show([src, smooth, sharp], ["source", "gaussian", "sharp"])
"""),
            markdown("## 메디안·양방향 필터"),
            code("""noise = read_image("noise.bmp", cv2.IMREAD_GRAYSCALE)
median = cv2.medianBlur(noise, 3)
show([noise, median], ["noise", "median"])

color = read_image("lenna.bmp")
bilateral = cv2.bilateralFilter(color, -1, 10, 5)
show([color, bilateral], ["source", "bilateral"])
"""),
            markdown("## 카툰·연필 스케치 필터"),
            code("""def cartoon_filter(image):
    h, w = image.shape[:2]
    small = cv2.resize(image, (w // 2, h // 2))
    smooth = cv2.bilateralFilter(small, -1, 20, 7)
    edge = 255 - cv2.Canny(small, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    result = cv2.bitwise_and(smooth, edge)
    return cv2.resize(result, (w, h), interpolation=cv2.INTER_NEAREST)

def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (0, 0), 3)
    return cv2.divide(gray, blur, scale=255)

sample = read_image("lenna.bmp")
show([sample, cartoon_filter(sample), pencil_sketch(sample)],
     ["source", "cartoon", "pencil"])
"""),
            markdown("## 실시간 필터 카메라\n\nSpace로 일반·카툰·연필 모드를 바꾸고 ESC로 종료합니다."),
            code("""cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("카메라를 열 수 없습니다.")

mode = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    if mode == 1:
        frame = cartoon_filter(frame)
    elif mode == 2:
        frame = cv2.cvtColor(pencil_sketch(frame), cv2.COLOR_GRAY2BGR)
    cv2.imshow("filter camera", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == ord(" "):
        mode = (mode + 1) % 3

cap.release()
cv2.destroyAllWindows()"""),
        ],
    ),
    "09_Geometrical_transfer.ipynb": notebook(
        "09. 기하학적 변환",
        "이동·전단·크기·회전·어파인·투시 변환과 문서 스캔 원리를 실습합니다.",
        [
            code("""from pathlib import Path
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(name):
    image = cv2.imread(str(Path("data") / name))
    if image is None:
        raise FileNotFoundError(f"data/{name}")
    return image

def show(images, titles):
    fig, axes = plt.subplots(1, len(images), figsize=(6 * len(images), 5))
    axes = np.atleast_1d(axes)
    for ax, image, title in zip(axes, images, titles):
        ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(title); ax.axis("off")
    plt.show()"""),
            markdown("## 이동과 전단"),
            code("""src = read_image("tekapo.bmp")
h, w = src.shape[:2]

translation = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32)
moved = cv2.warpAffine(src, translation, (w + 200, h + 100))

shear = np.array([[1, 0.5, 0], [0, 1, 0]], dtype=np.float32)
sheared = cv2.warpAffine(src, shear, (w + int(h * 0.5), h))
show([src, moved, sheared], ["source", "translation", "shear"])
"""),
            markdown("## 크기 변경과 보간"),
            code("""rose = read_image("rose.bmp")
nearest = cv2.resize(rose, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
linear = cv2.resize(rose, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cubic = cv2.resize(rose, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
lanczos = cv2.resize(rose, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)
show([nearest, linear, cubic, lanczos], ["nearest", "linear", "cubic", "lanczos"])
"""),
            markdown("## 중심 기준 회전"),
            code("""center = (w / 2, h / 2)
rotation = cv2.getRotationMatrix2D(center, 20, 0.7)
rotated = cv2.warpAffine(src, rotation, (w, h))
show([src, rotated], ["source", "rotate 20°, scale 0.7"])
"""),
            markdown("## 어파인 변환"),
            code("""src_points = np.float32([[0, 0], [w - 1, 0], [0, h - 1]])
dst_points = np.float32([[80, 80], [w - 120, 30], [40, h - 70]])
matrix = cv2.getAffineTransform(src_points, dst_points)
affine = cv2.warpAffine(src, matrix, (w, h))
show([src, affine], ["source", "affine"])
"""),
            markdown("## 투시 변환으로 명함 펴기"),
            code("""card = read_image("pinkwink_namecard.png")
out_w, out_h = 720, 400
src_quad = np.array([[360, 345], [879, 404], [895, 664], [254, 573]], np.float32)
dst_quad = np.array([[0, 0], [out_w - 1, 0],
                     [out_w - 1, out_h - 1], [0, out_h - 1]], np.float32)

perspective = cv2.getPerspectiveTransform(src_quad, dst_quad)
flattened = cv2.warpPerspective(card, perspective, (out_w, out_h))
show([card, flattened], ["source", "perspective corrected"])
"""),
            markdown("## 문서 스캔 기본 함수\n\n선택한 네 모서리를 A4 비율의 평면으로 변환합니다."),
            code("""def scan_document(image, corners, output_width=500):
    output_height = round(output_width * 297 / 210)
    source = np.asarray(corners, dtype=np.float32)
    target = np.array([
        [0, 0], [0, output_height - 1],
        [output_width - 1, output_height - 1], [output_width - 1, 0]
    ], dtype=np.float32)
    matrix = cv2.getPerspectiveTransform(source, target)
    return cv2.warpPerspective(image, matrix, (output_width, output_height),
                               flags=cv2.INTER_CUBIC)

document = read_image("scanned.jpg")
dh, dw = document.shape[:2]
corners = [[30, 30], [30, dh - 30], [dw - 30, dh - 30], [dw - 30, 30]]
scanned = scan_document(document, corners)
show([document, scanned], ["document", "scanned"])
"""),
        ],
    ),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for filename, content in NOTEBOOKS.items():
        path = OUT / filename
        path.write_text(json.dumps(content, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
