const Q=[
["명령·통신","실행 중인 ROS 2 노드 목록을 보는 명령은?","ros2 node list",["ros2 node list","ros2 topic list","ros2 run list"],"node list는 현재 ROS 그래프에서 발견되는 노드를 보여줍니다."],
["명령·통신","노드 하나의 publisher, subscriber, service 정보를 확인하려면?","ros2 node info /노드명",["ros2 node show /노드명","ros2 node info /노드명","ros2 info node /노드명"],"ros2 node info 뒤에 전체 노드 이름을 지정합니다."],
["명령·통신","연속적인 센서 데이터 전달에 가장 적합한 통신은?","Topic",["Service","Topic","Action"],"Topic은 비동기 발행·구독 스트림에 적합합니다."],
["명령·통신","한 번 요청하고 한 번 응답받는 작업에 적합한 통신은?","Service",["Topic","Service","Parameter"],"Service는 Request와 Response로 구성되는 단발 통신입니다."],
["명령·통신","진행 피드백과 취소가 필요한 장시간 작업에 적합한 통신은?","Action",["Action","Topic","Logging"],"Action은 Goal, Feedback, Result와 취소 기능을 제공합니다."],
["명령·통신","토픽의 메시지 타입까지 함께 나열하는 명령은?","ros2 topic list -t",["ros2 topic list -t","ros2 topic echo -t","ros2 interface list -v"],"-t 옵션은 토픽명과 타입을 함께 표시합니다."],
["명령·통신","메시지 필드 구조를 확인하는 명령은?","ros2 interface show",["ros2 message open","ros2 interface show","ros2 topic fields"],"값을 발행하기 전에 interface show로 필드를 확인하는 습관이 중요합니다."],
["명령·통신","토픽으로 들어오는 값을 실시간 확인하는 명령은?","ros2 topic echo",["ros2 topic watch","ros2 topic echo","ros2 topic info"],"topic echo는 구독자가 되어 메시지를 출력합니다."],
["명령·통신","노드와 토픽 연결 구조를 시각화하는 도구는?","rqt_graph",["rviz2","rqt_graph","ros2 bag"],"rqt_graph는 ROS 그래프의 노드·토픽 연결을 보여줍니다."],
["명령·통신","ROS 2 Jazzy 환경을 현재 셸에 활성화하는 명령은?","source /opt/ros/jazzy/setup.bash",["source /opt/ros/jazzy/setup.bash","ros2 start jazzy","colcon source jazzy"],"새 터미널마다 설치 공간의 setup.bash를 source해야 합니다."],
["Python 토픽·서비스","Python ROS 2 클라이언트 라이브러리는?","rclpy",["rospy","rclpy","roscpp"],"rclpy는 ROS 2의 Python 클라이언트 라이브러리입니다."],
["Python 토픽·서비스","구독 메시지가 도착했을 때 실행되는 함수는?","Callback",["Executor","Callback","Parameter"],"Subscriber는 메시지를 받으면 등록된 callback을 호출합니다."],
["Python 토픽·서비스","콜백을 계속 처리하는 함수는?","rclpy.spin(node)",["rclpy.wait(node)","rclpy.spin(node)","node.loop()"],"spin은 executor가 콜백을 계속 처리하도록 합니다."],
["Python 토픽·서비스","콜백을 한 번만 처리하고 반환하는 함수는?","rclpy.spin_once(node)",["rclpy.spin_once(node)","rclpy.spin(node)","node.callback_once()"],"spin_once는 준비된 작업을 한 차례 처리할 때 씁니다."],
["Python 토픽·서비스","Publisher를 생성하는 Node 메서드는?","create_publisher()",["create_topic()","create_publisher()","publish_create()"],"메시지 타입, 토픽 이름, QoS를 전달합니다."],
["Python 토픽·서비스","주기적으로 메시지를 발행할 때 유용한 기능은?","create_timer()",["create_timer()","wait_for_service()","declare_parameter()"],"타이머 콜백에서 메시지를 생성하고 publish하면 됩니다."],
["Python 토픽·서비스","Publisher와 Subscriber가 통신하기 위한 필수 조건은?","토픽명과 메시지 타입이 일치",["노드명이 일치","토픽명과 메시지 타입이 일치","타이머 주기가 일치"],"토픽 이름과 타입이 호환되어야 연결됩니다."],
["Python 토픽·서비스","서비스 서버가 준비될 때까지 기다리는 메서드는?","wait_for_service()",["spin_once()","wait_for_service()","wait_for_topic()"],"호출 전에 서버 발견 여부를 확인하면 실패를 안전하게 다룰 수 있습니다."],
["Python 토픽·서비스","call_async()가 반환하는 객체는?","Future",["Response","Future","Timer"],"Future에는 비동기 호출이 완료된 뒤 결과가 담깁니다."],
["Python 토픽·서비스","Future 완료까지 노드 콜백을 처리하며 기다리는 함수는?","spin_until_future_complete()",["spin_until_future_complete()","wait_result()","future.spin()"],"이 함수는 executor를 돌려 응답 콜백이 처리되게 합니다."],
["패키지·인터페이스","ROS 2 패키지가 들어가는 워크스페이스 하위 폴더는?","src",["bin","src","share"],"소스 패키지는 워크스페이스의 src 폴더에 둡니다."],
["패키지·인터페이스","ROS 2 워크스페이스 빌드 도구는?","colcon",["cmake만 사용","colcon","pipenv"],"colcon은 패키지 의존 순서에 따라 워크스페이스를 빌드합니다."],
["패키지·인터페이스","Python 패키지의 ros2 run 실행 이름을 등록하는 곳은?","setup.py의 console_scripts",["README.md","setup.py의 console_scripts","package.xml의 description"],"console_scripts가 실행 이름을 Python main 함수와 연결합니다."],
["패키지·인터페이스","빌드 후 현재 셸에서 패키지를 찾게 하는 명령은?","source install/setup.bash",["source install/setup.bash","ros2 pkg refresh","colcon activate"],"빌드 결과가 있는 install 공간을 source해야 합니다."],
["패키지·인터페이스","특정 패키지만 빌드하는 옵션은?","--packages-select",["--only-package","--packages-select","--target-package"],"colcon build --packages-select 패키지명 형식입니다."],
["패키지·인터페이스","커스텀 토픽 데이터 구조를 정의하는 확장자는?",".msg",[".srv",".action",".msg"],"토픽 메시지 구조는 .msg 파일로 정의합니다."],
["패키지·인터페이스",".srv 파일에서 요청과 응답을 구분하는 표시는?","---",["---","===","###"],"구분선 위가 Request, 아래가 Response입니다."],
["패키지·인터페이스",".action 파일의 올바른 구성 순서는?","Goal → Result → Feedback",["Goal → Result → Feedback","Request → Feedback → Response","Topic → Service → Action"],".action은 두 개의 ---로 Goal, Result, Feedback을 나눕니다."],
["패키지·인터페이스","생성된 커스텀 인터페이스를 확인하는 명령은?","ros2 interface show",["ros2 interface show","ros2 pkg fields","colcon interface"],"빌드와 source 후 패키지/종류/타입 경로로 확인합니다."],
["패키지·인터페이스","인터페이스 정의를 변경한 뒤 필요한 과정은?","재빌드하고 source",["노드 이름만 변경","재빌드하고 source","rqt만 새로고침"],"언어별 코드가 다시 생성되어야 하므로 build와 source를 반복합니다."],
["액션·파라미터·도구","액션의 중간 진행 상태를 뜻하는 것은?","Feedback",["Goal","Feedback","Result"],"서버는 작업 중 Feedback을 여러 번 발행할 수 있습니다."],
["액션·파라미터·도구","액션 서버 작업 완료를 클라이언트에 반환하는 것은?","Result",["Result","Goal","QoS"],"Result는 성공 여부나 최종 계산값을 담습니다."],
["액션·파라미터·도구","액션 콜백 중 다른 콜백도 병렬 처리하려면?","MultiThreadedExecutor",["SingleThreadedExecutor","MultiThreadedExecutor","타이머 제거"],"재진입 콜백 그룹과 MultiThreadedExecutor 조합을 사용합니다."],
["액션·파라미터·도구","노드 실행 중 동작을 조정하는 설정값은?","Parameter",["Topic","Parameter","Frame"],"파라미터는 코드를 다시 빌드하지 않고 설정을 바꿀 수 있게 합니다."],
["액션·파라미터·도구","코드에서 파라미터를 외부에 노출하는 메서드는?","declare_parameter()",["get_parameter()","declare_parameter()","publish_parameter()"],"먼저 선언한 뒤 get_parameter로 값을 읽습니다."],
["액션·파라미터·도구","param set 후 내부 동작도 즉시 바꾸려면 필요한 것은?","파라미터 변경 콜백",["파라미터 변경 콜백","새 서비스","새 워크스페이스"],"변경 콜백에서 값을 검증하고 내부 변수에 반영해야 합니다."],
["액션·파라미터·도구","파라미터를 YAML로 저장하는 명령은?","ros2 param dump",["ros2 param save","ros2 param dump","ros2 bag record"],"dump 결과는 나중에 ros2 param load로 불러올 수 있습니다."],
["액션·파라미터·도구","토픽 데이터를 기록하고 재생하는 도구는?","rosbag",["rqt_console","rosbag","tf2"],"rosbag은 실제 입력을 보존하여 버그를 재현하는 데 유용합니다."],
["액션·파라미터·도구","여러 노드와 파라미터를 한 번에 실행하는 방식은?","Launch",["Launch","Topic echo","Interface show"],"launch 파일은 시스템 실행 구성을 코드로 관리합니다."],
["액션·파라미터·도구","print보다 ROS logger가 좋은 이유는?","레벨과 필터를 사용할 수 있어서",["항상 더 빠르기 때문에","레벨과 필터를 사용할 수 있어서","토픽을 자동 생성해서"],"debug/info/warn/error 레벨과 rqt_console 필터를 활용할 수 있습니다."],
["TF·좌표계","로봇에서 위치와 방향을 해석하는 기준축은?","Frame",["Node","Frame","Action"],"좌표계 또는 frame은 위치·방향의 기준입니다."],
["TF·좌표계","ROS 2에서 좌표계 변환을 관리하는 라이브러리는?","tf2",["rqt","tf2","colcon"],"tf2는 시간에 따른 프레임 사이 변환을 버퍼링하고 합성합니다."],
["TF·좌표계","TransformStamped의 header.frame_id는 무엇인가?","부모 프레임",["부모 프레임","자식 프레임","노드 이름"],"변환을 표현하는 기준, 즉 parent frame입니다."],
["TF·좌표계","TransformStamped의 child_frame_id는 무엇인가?","자식 프레임",["토픽 이름","자식 프레임","패키지 이름"],"부모 기준 변환이 적용될 대상 frame입니다."],
["TF·좌표계","TF 메시지에 현재 시간 stamp가 중요한 이유는?","시간에 맞는 변환을 조회하기 위해",["파일명을 만들기 위해","시간에 맞는 변환을 조회하기 위해","노드 수를 세기 위해"],"센서 데이터 시각과 맞는 변환을 찾으려면 정확한 timestamp가 필요합니다."],
["TF·좌표계","ROS 2에서 3차원 회전을 표현하는 표준 방식은?","Quaternion",["Degree만 사용","Quaternion","RGB"],"Quaternion은 4개 값으로 회전을 표현하며 짐벌락을 피합니다."],
["TF·좌표계","Euler 각의 대표적인 문제는?","Gimbal lock",["Deadlock","Gimbal lock","Packet loss"],"회전 순서에 따라 축이 겹쳐 자유도를 잃을 수 있습니다."],
["TF·좌표계","world → moving_frame → child_frame 구조는 무엇인가?","TF Tree",["Topic chain","TF Tree","Service queue"],"각 자식은 부모에 대한 상대 변환으로 연결됩니다."],
["TF·좌표계","child_frame의 전역 위치를 직접 계산하지 않아도 되는 이유는?","tf2가 변환 체인을 합성해서",["항상 원점에 있어서","tf2가 변환 체인을 합성해서","RViz가 좌표를 삭제해서"],"tf2가 world→moving→child 변환을 순서대로 합성합니다."],
["TF·좌표계","RViz에서 world 기준 TF를 보려면 우선 설정할 것은?","Fixed Frame을 world로 설정",["배경을 흰색으로 변경","Fixed Frame을 world로 설정","토픽 이름을 world로 변경"],"Global Options의 Fixed Frame이 시각화 기준 좌표계입니다."],
["TF·좌표계","수신한 TF 데이터를 일정 시간 보관하는 객체는?","Buffer",["Marker","Buffer","Path"],"TransformListener가 수신한 변환은 Buffer에 저장됩니다."],
["TF·좌표계","/tf와 /tf_static을 구독해 Buffer를 채우는 객체는?","TransformListener",["TransformBroadcaster","TransformListener","PoseStamped"],"Listener는 TF 토픽을 자동으로 구독합니다."],
["TF·좌표계","lookup_transform의 인자 순서는?","target, source, time",["source, target, node","target, source, time","time, child, parent"],"target은 기준 프레임이고 source는 위치를 알고 싶은 프레임입니다."],
["TF·좌표계","rclpy.time.Time()을 lookup_transform에 전달하면 의미하는 것은?","가장 최신 변환",["가장 최신 변환","정확히 1초 전 변환","정적 변환만"],"시간 0은 Buffer에 있는 가장 최신 변환을 요청합니다."],
["TF·좌표계","두 프레임 사이 3차원 거리를 계산하는 식은?","sqrt(x²+y²+z²)",["x+y+z","sqrt(x²+y²+z²)","x*y*z"],"translation의 세 축에 유클리드 거리 공식을 적용합니다."],
["RViz 시각화","점들을 순서대로 연결해 선을 만드는 Marker 타입은?","LINE_STRIP",["TEXT_VIEW_FACING","LINE_STRIP","CUBE"],"LINE_STRIP은 marker.points 순서대로 선분을 연결합니다."],
["RViz 시각화","Path 메시지의 poses 배열에 들어가는 타입은?","PoseStamped",["Point","PoseStamped","Float32"],"Path는 Header와 PoseStamped 배열로 구성됩니다."],
["RViz 시각화","Marker와 Path의 핵심 차이로 올바른 것은?","Path는 위치와 방향을 함께 담을 수 있다",["Marker만 RViz에서 보인다","Path는 위치와 방향을 함께 담을 수 있다","Path에는 frame_id가 없다"],"PoseStamped 기반 Path는 position과 orientation을 함께 보존합니다."],
["RViz 시각화","오래된 경로를 제거하고 최근 N개만 남기는 패턴은?","Sliding window",["Dead reckoning","Sliding window","Goal cancel"],"리스트가 제한을 넘으면 pop(0)으로 가장 오래된 값을 제거합니다."],
["RViz 시각화","카메라 방향을 향하는 3D 텍스트 Marker 타입은?","TEXT_VIEW_FACING",["TEXT_VIEW_FACING","LINE_LIST","SPHERE"],"거리나 상태 문자열을 읽기 좋게 표시할 때 사용합니다."],
["DDS·도메인","같은 네트워크에서 ROS 2 노드의 발견 범위를 논리적으로 분리하는 값은?","ROS_DOMAIN_ID",["ROS_DOMAIN_ID","ROS_NAMESPACE","ROS_DISTRO"],"같은 ROS_DOMAIN_ID를 가진 노드끼리 DDS discovery와 통신이 이루어집니다."],
["DDS·도메인","ROS_DOMAIN_ID의 기본값은?","0",["0","1","232"],"환경변수를 지정하지 않으면 기본 도메인 0을 사용합니다."],
["DDS·도메인","ROS 2 통신을 현재 컴퓨터 안으로 제한하는 설정은?","ROS_LOCALHOST_ONLY=1",["ROS_LOCALHOST_ONLY=1","ROS_DOMAIN_ID=0","RMW_LOCAL=1"],"localhost 제한은 외부 컴퓨터의 노드와 DDS 통신하지 않게 합니다."],
["DDS·도메인","한 Python 스크립트에서 여러 도메인을 동시에 다룰 때 적절한 방식은?","도메인별 multiprocessing",["하나의 rclpy 스레드","도메인별 multiprocessing","노드 이름만 변경"],"각 자식 프로세스가 독립적으로 rclpy.init(domain_id=...)을 호출해야 합니다."],
["DDS·도메인","Domain 1과 Domain 2에서 같은 /id_test 토픽을 사용하면 어떻게 되는가?","서로 격리되어 통신하지 않는다",["자동으로 합쳐진다","서로 격리되어 통신하지 않는다","토픽 이름 충돌로 둘 다 종료된다"],"토픽 이름이 같아도 DDS 도메인이 다르면 서로 발견하거나 메시지를 주고받지 않습니다."]
];
const LESSON03=[
["03-01 · TF 발행",[
["TF의 frame이 뜻하는 것은?","위치와 방향의 기준 좌표계"],["TransformStamped.header.frame_id는?","부모 frame"],["TransformStamped.child_frame_id는?","자식 frame"],["반지름 r의 원운동 좌표식은?","x=r cosθ, y=r sinθ"],["목표점을 바라보는 yaw 계산은?","atan2(dy, dx)"],["움직이는 TF에 timestamp가 필요한 이유는?","측정 시각의 변환을 조회하기 위해"],["Euler 회전의 대표 문제는?","Gimbal lock"],["평면 yaw ψ의 Quaternion qz는?","sin(ψ/2)"],["회전 Quaternion의 정규화 조건은?","x²+y²+z²+w²=1"],["TF를 발행하는 객체는?","TransformBroadcaster"]]],
["03-02 · Child frame",[
["Child pose는 무엇을 기준으로 하는가?","Parent frame"],["world→parent와 parent→child의 합성은?","world→child"],["같은 child를 두 노드가 발행하면?","TF 권한 충돌"],["관련 TF를 함께 발행할 때 권장 timestamp는?","동일 timestamp"],["별도 broadcaster 노드의 장점은?","기능 분리와 장애 격리"],["통합 broadcaster의 장점은?","시간과 실행 관리 단순화"],["TF tree에서 child가 가질 수 있는 parent 수는?","하나"],["Parent가 움직이면 고정 child의 world pose는?","Parent와 함께 변함"],["TF tree를 파일로 확인하는 도구는?","view_frames"],["Transform 생성 중복을 줄이는 방법은?","공통 send_tf 함수"]]],
["03-03 · TF Listener",[
["수신 TF 이력을 저장하는 객체는?","Buffer"],["/tf와 /tf_static을 구독하는 객체는?","TransformListener"],["lookup_transform 인자 순서는?","target, source, time"],["rclpy.time.Time() 조회의 일반적 의미는?","최신 변환"],["시작 직후 lookup이 실패하는 이유는?","Buffer에 TF가 아직 없어서"],["TransformException의 적절한 처리는?","로그 후 다음 주기에 재시도"],["평면 두 frame의 거리식은?","sqrt(x²+y²)"],["센서와 TF를 정확히 맞추는 방법은?","센서 timestamp의 TF 조회"],["Broadcaster와 Listener의 차이는?","관계 발행과 관계 조회"],["TF 조회에서 긴 blocking의 문제는?","다른 callback 지연"]]],
["03-04 · RViz 시각화",[
["점을 순서대로 잇는 Marker 타입은?","LINE_STRIP"],["Path.poses의 원소 타입은?","PoseStamped"],["Marker가 투명할 때 확인할 값은?","color.a"],["같은 namespace와 id를 재발행하면?","기존 Marker 갱신"],["경로 배열을 무한히 늘릴 때 문제는?","메시지와 렌더링 비용 증가"],["카메라를 향하는 문자 Marker는?","TEXT_VIEW_FACING"],["Path와 Marker의 핵심 차이는?","Path는 PoseStamped 경로 의미"],["회전 없는 Pose의 Quaternion은?","w=1인 단위 Quaternion"],["RViz Transform 오류 시 먼저 볼 것은?","frame_id와 Fixed Frame 연결"],["최근 N개만 유지하는 패턴은?","Sliding window"]]],
["03-05 · Domain ID",[
["ROS_DOMAIN_ID의 역할은?","DDS discovery 영역 분리"],["기본 ROS_DOMAIN_ID는?","0"],["실행 후 export 변경이 기존 노드에 반영되는가?","반영되지 않음"],["여러 Domain을 동시에 다루는 권장 방식은?","Domain별 multiprocessing"],["rclpy.init의 Domain 지정 인자는?","domain_id"],["Domain 분리는 완전한 보안 경계인가?","아닌 논리적 격리"],["터미널 Domain 실수를 줄이는 방법은?","프롬프트에 ID 표시"],["다른 Domain의 같은 Topic 이름은?","서로 독립"],["Process 분리의 장점은?","독립 Context와 장애 격리"],["LOCALHOST discovery 설정 목적은?","통신을 현재 PC로 제한"]]],
["03-06 · 다중 Domain 제어",[
["같은 cmd_vel이 다른 거북이를 제어하는 이유는?","Domain별 Graph 격리"],["지속 속도 명령에 적합한 통신은?","Topic"],["TeleportAbsolute의 통신 방식은?","Service"],["RotateAbsolute의 통신 방식은?","Action"],["Action 서버 대기 메서드는?","wait_for_server"],["Goal Future와 Result Future의 관계는?","서로 다른 단계"],["부모가 자식 Process 종료를 기다리는 메서드는?","join"],["자식 종료 시 ROS 정리는?","destroy_node와 shutdown"],["angular.z 부호를 바꾸면?","회전 방향 반전"],["Thread보다 Process를 쓴 핵심 이유는?","독립 rclpy Context"]]],
["03-07 · Domain Bridge",[
["Domain Bridge의 기본 동작은?","Source 구독 후 Target 발행"],["Bridge YAML의 핵심 정보는?","출발·도착 Domain과 Topic 타입"],["Source Subscriber와 QoS가 맞아야 할 대상은?","Source Publisher"],["Best Effort 센서를 Reliable로 가정할 때 문제는?","QoS 비호환"],["A→B와 B→A 동시 중계의 위험은?","메시지 순환"],["Bridge 전후 검증 명령은?","각 Domain의 topic echo"],["Bridge가 공유하는 범위는?","설정한 Interface"],["대상 Topic 이름 변경 방식은?","Remap"],["Jazzy Bridge 패키지는?","ros-jazzy-domain-bridge"],["실행 전 터미널별 확인 환경은?","Domain과 discovery 범위"]]],
["03-08 · Description",[
["URDF의 기본 구성은?","Link와 Joint"],["Xacro의 목적은?","변수·매크로·조건으로 URDF 재사용"],["Visual과 Collision의 차이는?","표시 형상과 충돌 형상"],["Inertial이 담는 것은?","질량·무게중심·관성"],["robot_state_publisher 역할은?","URDF와 joint state로 TF 발행"],["Movable Joint TF에 필요한 입력은?","joint_states"],["URDF OK인데 caster TF만 없을 때 확인할 것은?","해당 Joint state"],["package:// URI 기준은?","설치된 Package share"],["view_robot Launch 용도는?","RViz 모델 검증"],["upload Launch 용도는?","robot_description 제공"]]],
["03-09 · Gazebo",[
["Gazebo에 Robot Entity를 만드는 과정은?","Spawn"],["ros_gz_bridge 역할은?","Gazebo와 ROS 메시지 변환"],["Simulation clock 사용 설정은?","use_sim_time=true"],["cmd_vel의 일반 Bridge 방향은?","ROS→Gazebo"],["scan과 odom의 일반 Bridge 방향은?","Gazebo→ROS"],["wheel separation 오류의 영향은?","회전 Odometry 오류"],["바퀴 마찰이 너무 작을 때 현상은?","Wheel slip"],["중복 Simulator 확인 명령은?","pgrep -a -f gz sim"],["cmd_vel 후 점검 계층 순서는?","Bridge→Drive plugin→Wheel joint"],["Gazebo 센서가 ROS에 없을 때 확인할 것은?","Bridge mapping과 방향"]]],
["03-10 · SLAM",[
["SLAM의 뜻은?","위치추정과 지도작성 동시 수행"],["Front-end 역할은?","Scan matching과 상대 제약"],["Back-end 역할은?","Pose graph 최적화"],["Loop Closure 효과는?","재방문으로 누적 오차 보정"],["Resolution을 작게 할 때 변화는?","정밀도와 계산량 증가"],["빠른 회전의 지도 문제는?","Scan 왜곡과 이중 벽"],["Map 저장 도구는?","map_saver_cli"],["Map resolution 단위는?","m/cell"],["휘어진 복도의 가능 원인은?","Odom과 Loop Closure 오차"],["SLAM 전에 먼저 검증할 것은?","Scan·Odom·TF·Timestamp"]]],
["03-11 · Localization",[
["Localization과 SLAM의 차이는?","저장 지도에서 Pose만 추정"],["Map Server 역할은?","정적 Occupancy Grid 제공"],["AMCL Particle의 의미는?","가능한 Robot Pose 가설"],["Particle Weight의 의미는?","Scan과 Map 일치 가능성"],["Resampling 목적은?","높은 Weight 가설에 집중"],["AMCL의 주요 TF 출력은?","map→odom"],["초기 Pose 지정 RViz 도구는?","2D Pose Estimate"],["Map·Scan 불일치 때 지도를 회전해야 하는가?","아니며 Initial Pose와 TF 점검"],["Particle 수가 해결 못 하는 것은?","잘못된 Sensor TF"],["Lifecycle Manager 역할은?","Map Server와 AMCL 상태 관리"]]],
["03-12 · PID Navigation",[
["PID 출력 구성은?","P+I+D 항의 합"],["P가 너무 클 때 현상은?","진동과 Overshoot"],["I 항의 목적은?","정상상태 오차 제거"],["Integral Windup은?","적분값 과도 누적"],["D가 너무 클 때 현상은?","Noise 민감과 출력 떨림"],["각도 정규화 범위는?","-π~π"],["상태 머신 순서는?","회전→직진→최종 회전"],["거리 PID 출력 축은?","linear.x"],["각도 PID 출력 축은?","angular.z"],["단순 PID Navigator 한계는?","장애물 회피와 재계획 부재"]]],
["03-13 · Navigation",[
["Global Plan은?","전체 지도상의 큰 경로"],["Local Controller 출력은?","cmd_vel"],["Costmap은?","이동 위험과 비용 지도"],["inflation_radius 증가 효과는?","벽 주변 비용 영역 확대"],["좁은 통로에서 먼저 확인할 것은?","실제 Footprint"],["Global과 Local Costmap 관계는?","별도 설정 가능"],["rqt 변경 후 확인 명령은?","ros2 param get"],["안전한 Tuning 방법은?","한 번에 한 항목 변경"],["Costmap에 길이 보이면 항상 안전한가?","아님"],["Goal 전 우선 조건은?","Map과 Scan 정렬"]]],
["03-14 · Python Nav2",[
["Nav2 Python 편의 API는?","BasicNavigator"],["Global Goal의 일반 frame은?","map"],["Nav2 Active 대기 메서드는?","waitUntilNav2Active"],["Goal 이동 시작 메서드는?","goToPose"],["Task 완료 확인 메서드는?","isTaskComplete"],["남은 거리는 어디에서 얻는가?","Navigation Feedback"],["Cancel 직후 UNKNOWN 이유는?","결과 미확정"],["올바른 Cancel 처리 순서는?","Cancel→완료 대기→Result"],["goal_pose Topic 방식의 단점은?","Feedback·Result 직접 수신 어려움"],["get_subscription_count 의미는?","Subscriber discovery 참고값"]]],
["03-15 · Nav2 설정",[
["bringup_launch 역할은?","Localization과 Navigation 조립"],["Lifecycle active 상태는?","실제 Service 수행 상태"],["Composable Node 장점은?","Process 수와 복사 비용 감소"],["AMCL alpha 파라미터는?","Odometry Motion Noise"],["RPP lookahead가 너무 작을 때는?","민감한 추종과 좌우 진동"],["Progress Checker 목적은?","일정 시간 이동량 판정"],["Velocity Smoother 목적은?","속도 변화 제한"],["A*와 Dijkstra 차이는?","A*는 Heuristic 추가"],["Behavior Server와 BT Navigator 차이는?","행동 제공과 실행 정책"],["권장 Tuning 순서는?","TF→Costmap→Planner→Controller"]]]
,
["04-01 · PinkyPro 소개",[
["PinkyPro가 교육용으로 연결하는 핵심 기술은?","ROS 2 센서·SLAM·Nav2"],["PinkyPro의 구동 방식은?","차동 구동 모바일 로봇"],["PinkyPro의 상차 가능 무게는 약 얼마인가?","약 50g"],["PC의 주요 역할은?","개발·RViz·상위 명령"],["로봇의 주요 역할은?","센서·모터·TF 제공"],["PC와 로봇 노드 발견에 중요한 것은?","같은 DDS Domain"],["지도 작성 다음 학습 단계는?","Localization"],["Localization 다음 자율주행 단계는?","Nav2"],["여러 로봇 토픽 충돌 방지에 쓰는 것은?","Namespace와 Domain 설계"],["LLM 행동 전에 필요한 것은?","실행 가능성과 안전 검증"]]],
["04-02 · 환경 설정",[
["SD 이미지 기록 도구는?","Raspberry Pi Imager"],["Custom 이미지를 고르는 메뉴는?","Use custom"],["워크스페이스 소스 폴더는?","~/pinky_/src"],["ROS 의존성 설치 도구는?","rosdep"],["워크스페이스 빌드 도구는?","colcon"],["빌드 후 패키지 검색에 필요한 것은?","install setup source"],["기본 Pinky SSH 주소는?","pinky@192.168.4.1"],["주변 Wi-Fi 확인 명령은?","nmcli device wifi list"],["PC와 로봇에서 같아야 하는 값은?","ROS_DOMAIN_ID"],["첫 구동 전 안전 조치는?","바퀴를 바닥에서 들기"]]],
["04-03 · 맵 작성",[
["실제 로봇 SLAM 전 먼저 실행할 것은?","Robot Bringup"],["SLAM 지도 확인 도구는?","RViz"],["키보드 주행 패키지는?","teleop_twist_keyboard"],["지도 저장 명령 도구는?","map_saver_cli"],["저장되는 두 지도 파일은?","PGM과 YAML"],["PGM이 표현하는 것은?","점유 격자 이미지"],["YAML resolution 의미는?","픽셀당 실제 거리"],["급회전이 만드는 문제는?","Scan matching 오차"],["재방문이 돕는 SLAM 기능은?","Loop Closure"],["SLAM 필수 입력은?","Scan·Odometry·TF"]]],
["04-04 · Nav2 주행",[
["저장 지도를 지정하는 launch 인자는?","map"],["초기 위치를 맞추는 RViz 도구는?","2D Pose Estimate"],["목표 위치와 방향을 지정하는 도구는?","Nav2 Goal"],["클릭한 지도 좌표 토픽은?","/clicked_point"],["AMCL 현재 자세 토픽은?","/amcl_pose"],["Goal 화살표 방향의 의미는?","도착 후 목표 yaw"],["Nav2 경로를 만드는 서버는?","Planner"],["경로를 속도 명령으로 바꾸는 서버는?","Controller"],["여러 목표 순차 실행 기능은?","Waypoint Following"],["초기화 후 확인할 정렬은?","Map과 LaserScan 일치"]]],
["04-05 · Jupyter 내비게이션",[
["Notebook이 Nav2를 찾으려면 먼저 필요한 것은?","ROS 환경 source"],["Jupyter 실행 명령은?","jupyter notebook"],["전역 설치 정책 우회 옵션은?","--break-system-packages"],["각도를 Quaternion으로 바꾸기 전 단위는?","Radian"],["평면 yaw Quaternion의 qz는?","sin(yaw/2)"],["현재 위치를 얻는 토픽은?","/amcl_pose"],["주행 중 상태 정보는?","Feedback"],["최종 성공·취소·실패 정보는?","Result"],["과도한 polling을 줄이는 방법은?","Timeout 간격 사용"],["다중 목표를 담는 것은?","Waypoint Pose 목록"]]],
["04-06 · LCD",[
["LCD 화면에 보내는 기본 데이터 형태는?","Pillow Image"],["LCD 객체 클래스는?","pinky_lcd.LCD"],["이미지 출력 메서드는?","img_show"],["텍스트 크기 계산 메서드는?","textbbox"],["한글 폰트를 여는 메서드는?","ImageFont.truetype"],["밝기 조절 메서드는?","set_backlight"],["GIF 프레임 순회 도구는?","ImageSequence.Iterator"],["Picamera 배열 획득 메서드는?","capture_array"],["OpenCV 기본 색 순서는?","BGR"],["사용 후 LCD 정리 메서드는?","close"]]]
,
["04-07 · LCD·LED ROS 2 제어",[
["LCD 감정 표현 서버 실행 명령은?","ros2 run pinky_emotion emotion_server"],["감정 설정 서비스 이름은?","/set_emotion"],["감정 서비스 타입은?","pinky_interfaces/srv/Emotion"],["happy 표정을 요청하는 필드는?","emotion"],["LED 서버 실행 명령은?","ros2 run pinky_led led_server"],["LED 전체 채우기 command는?","fill"],["일부 pixel만 바꾸는 command는?","set_pixel"],["LED를 모두 끄는 command는?","clear"],["RGB 빨간색 값은?","r=255, g=0, b=0"],["밝기 설정 서비스 이름은?","/set_brightness"]]],
["05-00 · GPU·CUDA·cuDNN 설정",[
["NVIDIA GPU가 PCI 장치로 보이는지 확인하는 명령은?","lspci"],["설치된 NVIDIA 드라이버와 GPU 상태 확인 명령은?","nvidia-smi"],["Ubuntu가 권장 드라이버를 표시할 때 쓰는 명령은?","ubuntu-drivers devices"],["CUDA compiler 버전 확인 명령은?","nvcc --version"],["CUDA 설치 전에 가장 먼저 맞춰야 하는 것은?","드라이버·CUDA·cuDNN 호환 조합"],["cuda-keyring 패키지의 역할은?","NVIDIA CUDA 저장소와 인증 키 등록"],["새 저장소 등록 뒤 실행할 명령은?","sudo apt update"],["CUDA 실행 파일 경로에 추가할 환경 변수는?","PATH"],["CUDA library 경로에 사용하는 환경 변수는?","LD_LIBRARY_PATH"],["TensorFlow에서 GPU 인식을 확인하는 API는?","tf.config.list_physical_devices('GPU')"]]],
["05-01 · Ollama",[
["Ollama의 주된 역할은?","로컬 LLM 실행과 관리"],["모델을 다운로드하며 실행하는 명령은?","ollama run"],["모델만 미리 받는 명령은?","ollama pull"],["설치된 모델 목록 확인 명령은?","ollama list"],["모델 삭제 명령은?","ollama rm"],["GGUF 기반 사용자 모델 생성 명령은?","ollama create"],["Modelfile에서 기반 모델을 지정하는 항목은?","FROM"],["응답 무작위성을 조절하는 옵션은?","temperature"],["대화형 실행을 종료하는 입력은?","/bye"],["여러 모델 결과를 공정하게 비교할 때 기록할 것은?","응답 시간·성공 여부·품질"]],
["05-02 · OpenAI API Python",[
["API Key를 코드에 직접 쓰면 안 되는 이유는?","개인 인증 정보 노출 위험"],["비밀값을 보관하는 파일은?",".env"],[".env를 Git에서 제외하는 파일은?",".gitignore"],["환경 변수를 불러오는 패키지는?","python-dotenv"],["OpenAI Python client 생성 클래스는?","OpenAI"],["Responses API 호출 메서드는?","client.responses.create"],["생성된 텍스트를 읽는 속성은?","response.output_text"],["VLM의 뜻은?","Vision-Language Model"],["로컬 이미지를 data URL로 보낼 때 쓰는 인코딩은?","Base64"],["모델의 JSON 문자열을 Python 객체로 바꾸는 함수는?","json.loads"]],
["05-03 · my_petbot",[
["프로젝트가 다루는 핵심 시스템은?","감정 기반 대화 시스템"],["다루는 감정 수는?","6개"],["LED가 표현하는 것은?","감정별 색상"],["LCD가 표현하는 것은?","감정별 표정 GIF"],["모터 행동의 예시는?","좌우·앞뒤 흔들기와 움찔"],["카메라 한 frame을 얻는 목적은?","VLM 이미지 입력"],["대화 함수가 함께 관리하는 것은?","사용자 text와 대화 history"],["LLM 응답에서 반드시 추론할 값은?","감정"],["Vision API에 이미지 binary를 직접 넣지 않고 쓰는 것은?","Base64 문자열"],["로봇 행동 전 검증할 것은?","감정 값과 안전 조건"]]
];
for(const [cat,items] of LESSON03){const answers=items.map(x=>x[1]);items.forEach(([question,answer],i)=>{const wrong=[answers[(i+3)%10],answers[(i+7)%10]];Q.push([cat,question,answer,[answer,...wrong],`${answer} — ${question.replace(/\?$/,'')}의 핵심 개념입니다.`])})}
document.querySelector('.kicker').textContent=`${Q.length} QUESTIONS · INSTANT FEEDBACK`;
document.querySelector('.intro p').textContent='03·04 과정은 강의자료별로 10문제씩 준비했습니다. 학습한 강의 번호만 선택해서 풀 수 있습니다.';
document.querySelector('#count').innerHTML='<option value="10">10문제</option><option value="20">20문제</option><option value="30">30문제</option><option value="50">50문제</option><option value="100">100문제</option><option value="9999">선택 범위 전체</option>';

const categoryNames=[...new Set(Q.map(q=>q[0]))].sort((a,b)=>{
 const a03=a.startsWith('03-'),b03=b.startsWith('03-');
 return a03!==b03?(a03?-1:1):a.localeCompare(b,'ko');
}),catBox=document.querySelector("#categories");
catBox.innerHTML=categoryNames.map(c=>`<label><input type="checkbox" value="${c}" checked> ${c} <small>(${Q.filter(q=>q[0]===c).length})</small></label>`).join("");
const requestedLesson=new URLSearchParams(location.search).get('lesson');
if(requestedLesson){
 const inputs=[...catBox.querySelectorAll('input')];
 inputs.forEach(input=>input.checked=input.value.startsWith(requestedLesson+' ·'));
 const selected=inputs.find(input=>input.checked);
 if(selected){
  document.querySelector('.intro p').textContent=`${selected.value} 강의에서 출제한 10문제입니다.`;
  document.querySelector('#count').value='10';
  selected.closest('label').scrollIntoView({block:'center'});
 }
}
let run=[],wrong=[],index=0,score=0,locked=false;
const shuffle=a=>[...a].sort(()=>Math.random()-.5);
document.querySelector("#start").onclick=()=>{const cats=[...catBox.querySelectorAll("input:checked")].map(x=>x.value);if(!cats.length)return alert("출제 범위를 하나 이상 선택하세요.");const pool=shuffle(Q.filter(q=>cats.includes(q[0])));run=pool.slice(0,Math.min(+document.querySelector("#count").value,pool.length));wrong=[];index=0;score=0;document.querySelector("#setup").classList.add("hidden");document.querySelector("#finish").classList.add("hidden");document.querySelector("#quiz").classList.remove("hidden");show()};
function show(){locked=false;const q=run[index];document.querySelector("#position").textContent=`${index+1} / ${run.length}`;document.querySelector("#scoreText").textContent=`정답 ${score}`;document.querySelector("#bar").style.width=`${index/run.length*100}%`;document.querySelector("#tag").textContent=q[0];document.querySelector("#question").textContent=q[1];document.querySelector("#explain").textContent="답을 선택하세요.";document.querySelector("#next").classList.add("hidden");const box=document.querySelector("#answers");box.innerHTML="";shuffle(q[3]).forEach(a=>{const b=document.createElement("button");b.textContent=a;b.onclick=()=>answer(b,a,q);box.append(b)})}
function answer(btn,a,q){if(locked)return;locked=true;const ok=a===q[2];if(ok)score++;else wrong.push(q);[...document.querySelector("#answers").children].forEach(b=>{if(b.textContent===q[2])b.classList.add("good");else if(b===btn)b.classList.add("bad")});document.querySelector("#explain").textContent=(ok?"정답! ":"오답. 정답은 ‘"+q[2]+"’. ")+q[4];document.querySelector("#scoreText").textContent=`정답 ${score}`;document.querySelector("#next").classList.remove("hidden")}
document.querySelector("#next").onclick=()=>{index++;index<run.length?show():finish()};
function finish(){document.querySelector("#quiz").classList.add("hidden");document.querySelector("#finish").classList.remove("hidden");const pct=Math.round(score/run.length*100);document.querySelector("#finalScore").textContent=pct+"점";document.querySelector("#finalTitle").textContent=pct>=90?"탄탄합니다!":pct>=70?"좋은 흐름이에요.":"오답을 복습해볼까요?";document.querySelector("#finalText").textContent=`${run.length}문제 중 ${score}개 정답 · 오답 ${wrong.length}개`;document.querySelector("#retryWrong").style.display=wrong.length?"inline-block":"none";localStorage.setItem("ros2-quiz-last",JSON.stringify({score,all:run.length,date:new Date().toISOString()}))}
document.querySelector("#retryWrong").onclick=()=>{run=shuffle(wrong);wrong=[];index=0;score=0;document.querySelector("#finish").classList.add("hidden");document.querySelector("#quiz").classList.remove("hidden");show()};
document.querySelector("#restart").onclick=()=>{document.querySelector("#finish").classList.add("hidden");document.querySelector("#setup").classList.remove("hidden")};
