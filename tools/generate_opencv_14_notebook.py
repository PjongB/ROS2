#!/usr/bin/env python3
"""Generate the OpenCV 14 binary, labeling, and contour notebook."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "opencv" / "notebooks" / "14_Binary_Labeling_Contours.ipynb"


def markdown(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.splitlines(keepends=True)}


def code(source: str) -> dict:
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source.splitlines(keepends=True)}


CELLS = [
    markdown("# 14. 이진화·라벨링·외곽선\n\nOtsu 자동 임계값, 지역 이진화, 연결 요소 라벨링과 외곽선 형상 분석을 실습합니다. 모든 예제 영상을 코드에서 생성하므로 바로 실행할 수 있습니다."),
    code('''import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(images, titles, cmap="gray"):
    fig, axes = plt.subplots(1, len(images), figsize=(5 * len(images), 4))
    axes = np.atleast_1d(axes)
    for ax, image, title in zip(axes, images, titles):
        if image.ndim == 2:
            ax.imshow(image, cmap=cmap, vmin=0, vmax=255)
        else:
            ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis("off")
    plt.tight_layout()
'''),
    markdown("## 전역 임계값과 Otsu 자동 임계값"),
    code('''rng = np.random.default_rng(14)
background = rng.normal(65, 18, (260, 420))
foreground = rng.normal(185, 22, (260, 420))
mask = np.zeros((260, 420), dtype=np.uint8)
cv2.circle(mask, (130, 130), 75, 255, -1)
cv2.rectangle(mask, (250, 60), (380, 210), 255, -1)
gray = np.where(mask > 0, foreground, background)
gray = np.clip(gray, 0, 255).astype(np.uint8)

_, fixed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
otsu_value, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(f"Otsu threshold: {otsu_value:.1f}")
show([gray, fixed, otsu], ["source", "fixed T=127", f"Otsu T={otsu_value:.1f}"])
'''),
    markdown("## 조명이 불균일한 영상과 적응형 이진화"),
    code('''height, width = 300, 500
illumination = np.tile(np.linspace(50, 210, width, dtype=np.float32), (height, 1))
uneven = illumination.copy()
cv2.putText(uneven, "OpenCV", (35, 190), cv2.FONT_HERSHEY_SIMPLEX, 3.0, 20, 12, cv2.LINE_AA)
uneven = np.clip(uneven + rng.normal(0, 6, uneven.shape), 0, 255).astype(np.uint8)

_, global_binary = cv2.threshold(uneven, 115, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(
    uneven, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, blockSize=31, C=8,
)
show([uneven, global_binary, adaptive], ["uneven light", "global", "adaptive Gaussian"])
'''),
    markdown("## 연결 요소 라벨링"),
    code('''components = np.zeros((320, 520), dtype=np.uint8)
cv2.circle(components, (90, 90), 45, 255, -1)
cv2.rectangle(components, (190, 45), (300, 140), 255, -1)
triangle = np.array([[390, 140], [455, 45], [500, 140]], dtype=np.int32)
cv2.fillPoly(components, [triangle], 255)
cv2.ellipse(components, (155, 240), (70, 38), 0, 0, 360, 255, -1)

count, labels, stats, centroids = cv2.connectedComponentsWithStats(components, connectivity=8)
print("objects:", count - 1)
for label in range(1, count):
    x, y, w, h, area = stats[label]
    cx, cy = centroids[label]
    print(f"label={label}: bbox=({x},{y},{w},{h}), area={area}, center=({cx:.1f},{cy:.1f})")

label_view = np.uint8(179 * labels / max(1, labels.max()))
label_view = cv2.applyColorMap(label_view, cv2.COLORMAP_HSV)
label_view[labels == 0] = 0
show([components, label_view], ["binary", "connected labels"])
'''),
    markdown("## 외곽선과 계층"),
    code('''contours, hierarchy = cv2.findContours(components.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_view = cv2.cvtColor(components, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_view, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)
print("contours:", len(contours))
print("hierarchy [next, previous, child, parent]:")
print(hierarchy[0] if hierarchy is not None else None)
show([components, contour_view], ["binary", "contours"])
'''),
    markdown("## 면적·둘레·바운딩 도형·다각형 근사"),
    code('''analysis = cv2.cvtColor(components, cv2.COLOR_GRAY2BGR)
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 100:
        continue
    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    x, y, w, h = cv2.boundingRect(contour)
    (cx, cy), radius = cv2.minEnclosingCircle(contour)
    circularity = 4 * np.pi * area / (perimeter * perimeter) if perimeter else 0

    cv2.rectangle(analysis, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.circle(analysis, (round(cx), round(cy)), round(radius), (0, 255, 0), 2)
    cv2.polylines(analysis, [approximation], True, (0, 0, 255), 2)
    print(f"vertices={len(approximation)}, area={area:.0f}, perimeter={perimeter:.1f}, circularity={circularity:.3f}, convex={cv2.isContourConvex(approximation)}")

show([components, analysis], ["source", "shape analysis"])
'''),
    markdown("## 원 판별 예시"),
    code('''for index, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if area < 100 or perimeter == 0:
        continue
    circularity = 4 * np.pi * area / (perimeter * perimeter)
    print(f"contour {index}: {'circle-like' if circularity > 0.82 else 'not circle'}, score={circularity:.3f}")
'''),
]


def main() -> None:
    from generate_source_aligned_opencv_notebooks import main as aligned_main

    aligned_main()


if __name__ == "__main__":
    main()
