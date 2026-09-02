#!/usr/bin/env python3
"""Generate OpenCV concept study pages from structured lecture notes."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "learn"


LESSONS = [
    {
        "slug": "opencv-01-setting",
        "num": "01",
        "title": "OpenCV 환경 설정",
        "lead": "가상환경, 패키지, Jupyter 커널이 어떻게 연결되는지 이해하고 재현 가능한 실습 환경을 준비합니다.",
        "source": "../opencv/01_OpenCV_Setting.html", "pdf": "../opencv/01_OpenCV_Setting.pdf", "nb": "../opencv/notebooks/01_OpenCV_Setting.ipynb",
        "concepts": [("가상환경", "프로젝트별 Python과 패키지 버전을 격리하는 독립 실행 공간"), ("패키지", "opencv-python, numpy, matplotlib처럼 실습 기능을 제공하는 모듈 묶음"), ("인터프리터", "VS Code와 터미널이 실제로 실행할 Python 경로"), ("Jupyter 커널", "노트북 셀을 실행하는 Python 프로세스. 가상환경과 일치해야 함")],
        "theory": "Python 코드는 선택된 인터프리터에서 실행되고, import는 그 환경의 site-packages를 탐색합니다. 따라서 설치한 환경과 노트북 커널이 다르면 cv2를 찾지 못합니다.",
        "equation": "terminal / VS Code / Jupyter\n            ↓ interpreter 선택\nPython virtual environment\n            ↓ import\ncv2 + numpy + matplotlib",
        "matrix": None,
        "table": [("python -m venv", "독립 Python 환경 생성"), ("source .../bin/activate", "현재 셸에서 환경 활성화"), ("pip install opencv-python", "OpenCV Python 바인딩 설치"), ("cv2.__version__", "실제로 import된 버전 확인")],
        "flow": ["가상환경 생성", "환경 활성화", "패키지 설치", "커널·버전 확인"],
        "checks": ["터미널의 python 경로와 VS Code 인터프리터가 같은지 확인", "노트북 커널에서 import cv2 실행", "재시작 후에도 같은 환경을 선택할 수 있는지 확인"],
    },
    {
        "slug": "opencv-02-numpy-array",
        "num": "02",
        "title": "NumPy 배열과 OpenCV",
        "lead": "이미지를 숫자 배열로 읽고 높이·너비·채널과 픽셀 연산의 관계를 이해합니다.",
        "source": "../opencv/02_Numpy_array_with_OpenCV.html", "pdf": "../opencv/02_Numpy_array_with_OpenCV.pdf", "nb": "../opencv/notebooks/02_Numpy_array_with_OpenCV.ipynb",
        "concepts": [("픽셀", "영상 좌표 (x, y)에 저장된 밝기 또는 색 값"), ("shape", "그레이는 (H, W), 컬러는 (H, W, C) 구조"), ("채널", "RGB/BGR 색 성분을 분리해 담는 2차원 레이어"), ("dtype", "uint8은 0~255 범위를 갖는 대표적인 영상 자료형")],
        "theory": "그레이 영상은 하나의 행렬, 컬러 영상은 채널 행렬 세 장을 쌓은 3차원 텐서입니다. NumPy 슬라이싱으로 특정 채널이나 관심 영역을 한 번에 읽고 바꿀 수 있습니다.",
        "equation": "gray[y, x] → 밝기 1개\ncolor[y, x] → [R, G, B] 또는 [B, G, R]\nshape = (height, width, channels)",
        "matrix": ([["R00", "R01", "…"], ["R10", "R11", "…"], ["⋮", "⋮", "Rhw"]], "R 채널 행렬 - G와 B도 같은 크기"),
        "table": [("img[y, x]", "한 픽셀 읽기"), ("img[:, :, 0]", "첫 번째 채널 전체"), ("img[y1:y2, x1:x2]", "ROI 영역"), ("img[:, :, 1] = 0", "두 번째 채널 제거")],
        "flow": ["이미지 읽기", "shape·dtype 확인", "채널 분리", "배열 연산·표시"],
        "checks": ["행 인덱스 y가 높이, 열 인덱스 x가 너비임을 구분", "uint8에서 255를 넘는 연산의 overflow 주의", "Matplotlib의 RGB와 OpenCV의 BGR 순서 확인"],
    },
    {
        "slug": "opencv-03-image-read",
        "num": "03",
        "title": "이미지 읽기와 표시",
        "lead": "파일 디코딩부터 BGR↔RGB 변환, 그레이스케일, 크기 변경, 반전, 저장까지의 흐름을 정리합니다.",
        "source": "../opencv/03_Image_read.html", "pdf": "../opencv/03_Image_read.pdf", "nb": "../opencv/notebooks/03_Image_read.ipynb",
        "concepts": [("imread", "파일을 디코딩해 NumPy 배열로 반환. 실패하면 None"), ("BGR/RGB", "OpenCV와 Matplotlib이 사용하는 기본 채널 순서의 차이"), ("그레이스케일", "색 채널을 하나의 밝기 값으로 축약"), ("보간", "resize 시 새 픽셀 값을 주변 값으로 추정하는 방법")],
        "theory": "색상 순서를 바꾸는 것은 공간 좌표가 아니라 마지막 채널 축의 순서를 재배열하는 연산입니다. 그레이 변환은 사람의 밝기 지각을 반영해 G 채널에 더 큰 가중치를 둡니다.",
        "equation": "Y ≈ 0.299R + 0.587G + 0.114B\nRGB = BGR[:, :, [2, 1, 0]]\nresize: (H, W) → (H′, W′)",
        "matrix": ([["B", "G", "R"], ["↓", "↓", "↓"], ["R", "G", "B"]], "색 채널 순서 변환"),
        "table": [("IMREAD_COLOR", "3채널 BGR"), ("IMREAD_GRAYSCALE", "1채널 밝기"), ("flipCode=0", "상하 반전"), ("flipCode=1 / -1", "좌우 / 상하좌우 반전")],
        "flow": ["경로·파일 확인", "imread", "색·크기 변환", "imshow/imwrite"],
        "checks": ["img is None을 먼저 검사", "cv2.resize의 크기 인자는 (width, height)", "저장 전 RGB 배열을 BGR로 되돌릴지 확인"],
    },
    {
        "slug": "opencv-04-drawing",
        "num": "04",
        "title": "기본 도형 그리기",
        "lead": "영상 좌표계와 도형 API의 공통 인자를 이해하고 선·사각형·원·텍스트·다각형을 그립니다.",
        "source": "../opencv/04_Draw_simple_figure.html", "pdf": "../opencv/04_Draw_simple_figure.pdf", "nb": "../opencv/notebooks/04_Draw_simple_figure.ipynb",
        "concepts": [("영상 좌표", "왼쪽 위가 원점, x는 오른쪽, y는 아래쪽으로 증가"), ("색과 두께", "BGR 튜플과 thickness로 외곽선·채우기를 제어"), ("lineType", "LINE_AA로 계단 현상을 줄인 선을 그림"), ("다각형 배열", "꼭짓점을 (N, 1, 2) 형태의 int32 배열로 전달")],
        "theory": "도형 그리기는 연속적인 기하 도형을 이산 픽셀 격자에 기록하는 래스터화입니다. 모든 점은 (x, y)로 입력하지만 배열 접근은 [y, x] 순서입니다.",
        "equation": "image coordinate: origin = (0, 0) at top-left\nx → right, y → down\npoint array shape: (N, 1, 2)",
        "matrix": ([["x₁", "y₁"], ["x₂", "y₂"], ["⋮", "⋮"], ["xₙ", "yₙ"]], "꼭짓점 좌표 행렬 - reshape 후 polylines에 전달"),
        "table": [("rectangle", "두 꼭짓점으로 사각형"), ("circle", "중심과 반지름으로 원"), ("line", "두 점을 잇는 선"), ("polylines / fillPoly", "다각형 외곽선 / 채우기")],
        "flow": ["캔버스 생성", "좌표·색 선택", "도형 래스터화", "RGB 변환·표시"],
        "checks": ["캔버스 dtype을 uint8로 생성", "thickness=-1은 내부 채우기", "좌표가 영상 범위를 벗어나지 않는지 확인"],
    },
    {
        "slug": "opencv-05-callback",
        "num": "05",
        "title": "콜백 함수 활용",
        "lead": "마우스 이벤트가 발생할 때 호출되는 함수를 등록하고, 상태를 유지하며 대화형 그리기를 구현합니다.",
        "source": "../opencv/05_Use_Callback_function.html", "pdf": "../opencv/05_Use_Callback_function.pdf", "nb": "../opencv/notebooks/05_Use_Callback_function.ipynb",
        "concepts": [("이벤트 루프", "waitKey가 창 메시지를 처리하며 입력을 계속 기다리는 구조"), ("콜백", "특정 이벤트가 발생했을 때 OpenCV가 대신 호출하는 함수"), ("event/flags", "발생 사건과 현재 눌린 버튼·보조키 상태"), ("상태", "이전 좌표 oldx, oldy를 저장해 연속적인 선으로 연결")],
        "theory": "프로그램이 마우스를 반복 확인하는 대신 이벤트 시스템이 콜백을 호출합니다. 클릭 시작 좌표를 상태로 저장하고 이동할 때 새 좌표까지 선을 그리면 자유 곡선이 됩니다.",
        "equation": "event → callback(event, x, y, flags, param)\nLBUTTONDOWN: p_old ← (x, y)\nMOUSEMOVE: line(p_old, p_new), p_old ← p_new",
        "matrix": None,
        "table": [("EVENT_LBUTTONDOWN", "왼쪽 버튼 누름"), ("EVENT_LBUTTONUP", "왼쪽 버튼 해제"), ("EVENT_MOUSEMOVE", "포인터 이동"), ("EVENT_FLAG_LBUTTON", "이동 중 왼쪽 버튼 상태")],
        "flow": ["창 생성", "콜백 등록", "이벤트·상태 처리", "waitKey 루프"],
        "checks": ["namedWindow 다음 setMouseCallback 호출", "콜백 안에서 공유 상태를 명확히 관리", "종료 시 destroyAllWindows 호출"],
    },
    {
        "slug": "opencv-06-color-space",
        "num": "06",
        "title": "색 공간",
        "lead": "RGB/BGR과 HSV를 비교하고 가중 합성, ROI, 마스크, 비트 연산으로 워터마크를 만듭니다.",
        "source": "../opencv/06_Color_space.html", "pdf": "../opencv/06_Color_space.pdf", "nb": "../opencv/notebooks/06_Color_space.ipynb",
        "concepts": [("RGB/BGR", "빛의 삼원색을 직접 채널 값으로 표현"), ("HSV", "색조 H, 채도 S, 명도 V로 색과 밝기를 분리"), ("알파 블렌딩", "두 영상의 대응 픽셀을 가중합"), ("마스크·ROI", "연산할 영역과 통과시킬 픽셀을 제한")],
        "theory": "addWeighted는 크기가 같은 두 영상의 대응 원소를 선형 결합합니다. 워터마크는 ROI에서 배경을 마스크로 비우고 전경을 OR/ADD하여 합성합니다.",
        "equation": "dst(x,y) = α·src1(x,y) + β·src2(x,y) + γ\nmask=0 → 차단, mask=255 → 통과\nresult = background ∨ foreground",
        "matrix": ([["R", "G", "B"], ["α", "α", "α"], ["R′", "G′", "B′"]], "채널별 동일한 가중 합성 연산"),
        "table": [("cvtColor", "색 공간 변환"), ("addWeighted", "가중 합성"), ("bitwise_and", "마스크가 켜진 픽셀만 통과"), ("bitwise_not", "0과 255 마스크 반전")],
        "flow": ["두 영상 읽기", "크기·ROI 정렬", "마스크 생성", "전경·배경 합성"],
        "checks": ["합성 전 두 이미지 크기와 채널 수 일치", "OpenCV HSV의 H 범위는 기본적으로 0~179", "ROI shape과 워터마크 shape이 같은지 확인"],
    },
    {
        "slug": "opencv-07-video-capture",
        "num": "07",
        "title": "비디오 캡처",
        "lead": "카메라와 동영상 파일을 프레임 스트림으로 읽고 FPS·해상도·코덱을 이해해 저장합니다.",
        "source": "../opencv/07_Video_capture.html", "pdf": "../opencv/07_Video_capture.pdf", "nb": "../opencv/notebooks/07_Video_capture.ipynb",
        "concepts": [("VideoCapture", "카메라 장치나 동영상 파일을 프레임 단위로 읽는 객체"), ("프레임", "시간축에서 한 시점의 H×W×C 이미지 배열"), ("FPS", "1초 동안 표시·저장되는 프레임 수"), ("FourCC", "저장 스트림에 사용할 영상 코덱을 나타내는 네 문자 코드")],
        "theory": "영상은 이미지 배열의 시간 순서입니다. 읽기 성공 여부 ret를 확인하고, 표시·처리·저장을 한 루프 안에서 수행해야 프레임 순서가 유지됩니다.",
        "equation": "video = { frame₀, frame₁, …, frameₜ }\nduration ≈ frame_count / FPS\nframe shape = (height, width, channels)",
        "matrix": None,
        "table": [("CAP_PROP_FRAME_WIDTH", "프레임 너비"), ("CAP_PROP_FRAME_HEIGHT", "프레임 높이"), ("CAP_PROP_FPS", "초당 프레임 수"), ("VideoWriter", "프레임 배열을 동영상 파일로 인코딩")],
        "flow": ["장치 열기", "ret·frame 읽기", "표시·처리·저장", "release"],
        "checks": ["isOpened와 ret를 모두 검사", "Writer 크기와 실제 frame 크기를 일치", "카메라와 Writer를 종료할 때 release 호출"],
    },
    {
        "slug": "opencv-08-filtering",
        "num": "08",
        "title": "이미지 필터링",
        "lead": "커널을 영상 위로 이동시키는 합성곱에서 출발해 평균·가우시안·샤프닝·메디안·양방향 필터를 비교합니다.",
        "source": "../opencv/08_present_Filtering_.html", "pdf": "../opencv/08_Filtering_.pdf", "nb": "../opencv/notebooks/08_Filtering.ipynb",
        "concepts": [("커널", "주변 픽셀의 가중치를 담은 홀수 크기 행렬"), ("합성곱", "커널과 겹친 픽셀을 곱해 더한 값을 출력 픽셀로 기록"), ("저역 통과", "고주파 변화와 잡음을 줄여 부드럽게 함"), ("고역 강조", "원본에서 저주파 성분을 빼 경계와 세부를 강조")],
        "theory": "평균 필터는 모든 이웃에 같은 가중치를 주고, 가우시안은 중심에 더 큰 가중치를 줍니다. 메디안은 값을 정렬해 중앙값을 택하므로 소금·후추 잡음에 강하며, 양방향 필터는 거리와 색 차이를 함께 고려해 경계를 보존합니다.",
        "equation": "g(x,y) = Σᵢ Σⱼ K(i,j)·f(x-i, y-j)\nmean: ΣK = 1\nunsharp: dst = src + α(src - Gaussian(src))",
        "matrix": ([["1/9", "1/9", "1/9"], ["1/9", "1/9", "1/9"], ["1/9", "1/9", "1/9"]], "3×3 평균값 필터 커널"),
        "table": [("filter2D / blur", "사용자 커널 / 평균 필터"), ("GaussianBlur", "가우시안 가중 블러"), ("medianBlur", "중앙값 기반 잡음 제거"), ("bilateralFilter", "경계를 보존하는 비선형 필터")],
        "flow": ["커널 선택", "주변 픽셀 가중", "경계 처리", "출력·품질 비교"],
        "checks": ["커널 크기는 보통 3, 5, 7 같은 홀수", "샤프닝 결과는 clip 후 uint8 변환", "색 영상 샤프닝은 밝기 채널만 처리하면 색 왜곡 감소"],
    },
    {
        "slug": "opencv-09-geometrical-transform",
        "num": "09",
        "title": "기하학적 변환",
        "lead": "화소값이 아니라 좌표를 바꾸는 이동·전단·크기·회전·어파인·투시 변환의 행렬 구조를 이해합니다.",
        "source": "../opencv/09_present_Geometrical_transfer_.html", "pdf": "../opencv/09_Geometrical_transfer_.pdf", "nb": "../opencv/notebooks/09_Geometrical_transfer.ipynb",
        "concepts": [("동차좌표", "2D 점 (x,y)에 1을 붙여 이동까지 행렬곱으로 표현"), ("역방향 매핑", "출력 좌표가 참조할 입력 좌표를 찾아 빈 구멍을 방지"), ("보간", "실수 좌표의 화소값을 최근접·선형·큐빅 등으로 추정"), ("자유도", "변환을 결정하는 독립 파라미터 수. 이동 2, 어파인 6, 투시 8")],
        "theory": "이동은 위치만, 유클리드는 길이·각도, 닮음은 각도·비율, 어파인은 평행성, 투시는 직선성을 보존합니다. 제약이 적을수록 더 일반적인 변환이 됩니다.",
        "equation": "[x′ y′ 1]ᵀ = H · [x y 1]ᵀ\naffine: 마지막 행 = [0 0 1]\nprojective: w로 나눔 → (x′/w, y′/w)",
        "matrices": [
            ([["1", "0", "tₓ"], ["0", "1", "tᵧ"], ["0", "0", "1"]], "이동"),
            ([["cosθ", "-sinθ", "0"], ["sinθ", "cosθ", "0"], ["0", "0", "1"]], "회전"),
            ([["a", "b", "tₓ"], ["c", "d", "tᵧ"], ["0", "0", "1"]], "어파인"),
            ([["h₁₁", "h₁₂", "h₁₃"], ["h₂₁", "h₂₂", "h₂₃"], ["h₃₁", "h₃₂", "1"]], "투시")],
        "table": [("warpAffine", "2×3 이동·회전·어파인 행렬 적용"), ("getRotationMatrix2D", "중심·각도·배율로 회전 행렬 생성"), ("getAffineTransform", "점 3쌍으로 어파인 행렬 계산"), ("getPerspectiveTransform", "점 4쌍으로 호모그래피 계산")],
        "flow": ["대응점·행렬 정의", "출력 크기 결정", "역매핑·보간", "잘림·경계 확인"],
        "checks": ["점 좌표 dtype을 float32로 맞춤", "cv2 함수의 점 순서를 일관되게 지정", "변환 후 필요한 출력 dsize를 직접 계산"],
    },
    {
        "slug": "opencv-10-brightness-contrast",
        "num": "10",
        "title": "밝기와 명암비",
        "lead": "화소 단위 변환 함수에서 출발해 밝기·명암비 조절, 영상 산술, 히스토그램과 HSV 색상 추출을 연결합니다.",
        "source": "../opencv/10_present_Brightness_Contrast_.html", "pdf": "../opencv/10_Brightness_Contrast_.pdf", "nb": "../opencv/notebooks/10_Brightness_Contrast.ipynb",
        "concepts": [("화소 처리", "출력 화소가 같은 위치의 입력 화소 하나로 결정되는 연산"), ("포화 연산", "계산 결과를 uint8 범위 0~255 안으로 제한"), ("히스토그램", "각 밝기 값에 속하는 화소 개수를 나타내는 분포"), ("색상 마스크", "지정 범위에 포함된 픽셀만 255로 표시한 1채널 영상")],
        "theory": "밝기는 화소값에 상수를 더하고, 명암비는 기준점으로부터의 거리를 확대합니다. OpenCV 산술은 포화 연산을 적용하지만 NumPy uint8 덧셈은 값이 순환하므로 실수 승격과 clip이 필요합니다. 컬러 영상은 YCrCb의 Y 채널만 평활화해야 색 왜곡을 줄일 수 있습니다.",
        "equation": "brightness: dst = saturate(src + n)\ncontrast: dst = src + α(src - 128)\nstretch: dst = (src - Gmin)·255/(Gmax - Gmin)\nblend: dst = α·src1 + β·src2 + γ",
        "matrices": [
            ([["p₁₁", "p₁₂", "…"], ["p₂₁", "p₂₂", "…"], ["⋮", "⋮", "pₕ𝓌"]], "각 행렬 원소에 같은 점 변환 함수 f를 적용"),
            ([["Y", "Cr", "Cb"], ["equalize", "keep", "keep"], ["Y′", "Cr", "Cb"]], "컬러 평활화는 밝기 Y 채널만 처리"),
        ],
        "table": [("cv2.add / subtract", "포화 덧셈·뺄셈"), ("cv2.absdiff / addWeighted", "절대 차이·가중 합성"), ("normalize / equalizeHist", "선형 스트레칭·CDF 기반 평활화"), ("cvtColor / inRange", "색 공간 변환·범위 마스크")],
        "flow": ["입력·dtype 확인", "변환 함수 선택", "포화·색 공간 처리", "히스토그램·마스크 비교"],
        "checks": ["imread 결과가 None인지 resize보다 먼저 검사", "NumPy uint8 산술은 실수 승격 후 clip", "addWeighted 입력의 크기·타입을 일치", "컬러 equalizeHist는 YCrCb의 Y 채널에만 적용"],
    },
]


def matrix_html(values, label):
    cols = len(values[0])
    cells = "".join(f"<span>{escape(str(v))}</span>" for row in values for v in row)
    return f'<div class="matrix-row"><div class="matrix" style="--cols:{cols}">{cells}</div><span class="matrix-label">{escape(label)}</span></div>'


def page(lesson, index):
    concepts = "".join(f'<div class="concept"><b>{escape(k)}</b><span>{escape(v)}</span></div>' for k, v in lesson["concepts"])
    table = "".join(f"<tr><td><span class=\"code-key\">{escape(a)}</span></td><td>{escape(b)}</td></tr>" for a, b in lesson["table"])
    flow = "".join(f"<span>{escape(x)}</span>" for x in lesson["flow"])
    checks = "".join(f"<li>{escape(x)}</li>" for x in lesson["checks"])
    matrices = lesson.get("matrices") or ([lesson["matrix"]] if lesson.get("matrix") else [])
    matrix_section = "".join(matrix_html(*m) for m in matrices) or '<p class="note">이 강의는 행렬 계산보다 실행 환경과 이벤트 흐름을 이해하는 것이 핵심입니다.</p>'
    prev_lesson = LESSONS[index - 1] if index else None
    next_lesson = LESSONS[index + 1] if index + 1 < len(LESSONS) else None
    prev_link = f'<a href="{prev_lesson["slug"]}.html">← {prev_lesson["num"]}</a>' if prev_lesson else '<a href="../index.html">← 전체 목차</a>'
    next_link = f'<a href="{next_lesson["slug"]}.html">{next_lesson["num"]} →</a>' if next_lesson else '<a href="../index.html">전체 목차 →</a>'
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(lesson["title"])} · OpenCV</title><link rel="stylesheet" href="opencv-study.css"></head><body>
<header><div class="shell top"><a class="brand" href="../index.html"><b>ROS</b> FIELD NOTES</a><a class="back" href="../index.html">전체 강의로 돌아가기</a></div></header>
<section class="hero"><div class="shell"><div class="kicker">08.{lesson["num"]} · OPENCV CONCEPT STUDY</div><h1>{escape(lesson["title"])}</h1><p class="lead">{escape(lesson["lead"])}</p><div class="actions"><a class="button primary" target="_blank" rel="noopener" href="{lesson["source"]}">원본 강의</a><a class="button pdf" target="_blank" rel="noopener" href="{lesson["pdf"]}">강의 PDF</a><a class="button nb" download href="{lesson["nb"]}">IPYNB 다운로드</a></div></div></section>
<div class="shell layout"><nav class="toc"><b>이 페이지에서</b><a href="#concepts">핵심 개념</a><a href="#theory">이론과 수식</a><a href="#matrix">행렬로 보기</a><a href="#functions">함수·용어 정리</a><a href="#flow">실습 흐름</a><a href="#check">확인할 점</a></nav><main>
<section><div class="summary"><b>한 줄 정리</b><span>{escape(lesson["theory"])}</span></div></section>
<section id="concepts"><h2>핵심 개념</h2><div class="concepts">{concepts}</div></section>
<section id="theory"><h2>이론과 수식</h2><p>{escape(lesson["theory"])}</p><div class="equation">{escape(lesson["equation"])}</div></section>
<section id="matrix"><h2>행렬로 보기</h2>{matrix_section}</section>
<section id="functions"><h2>함수·용어 정리</h2><table class="study-table"><thead><tr><th>함수·표현</th><th>역할</th></tr></thead><tbody>{table}</tbody></table></section>
<section id="flow"><h2>실습 흐름</h2><div class="flow">{flow}</div></section>
<section id="check"><h2>실습 전후 확인할 점</h2><ul class="checklist">{checks}</ul><p class="note">세부 코드와 실행 예제는 위의 IPYNB 파일에서 셀 단위로 실습할 수 있습니다.</p></section>
<div class="nav-bottom">{prev_link}{next_link}</div></main></div></body></html>'''


def main():
    for i, lesson in enumerate(LESSONS):
        path = OUT / f'{lesson["slug"]}.html'
        path.write_text(page(lesson, i), encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
