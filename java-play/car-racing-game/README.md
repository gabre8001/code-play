# 자동차 경주 게임

* 이 게임은 nextstep에서 진행한 교육을 들으면서 작성한 게임이다.
* 자동차 경주게임을 구현했다. 
* 게임의 자세한 설명은 기능 요구 사항과 구현 기능 목록을 참고한다.

## 프로그램 특징

* Event Driven Architecture를 가진다.
* Application에 main 메소드가 있다.
* GameStatus에 이벤트가 정의 되어 있다.
* GameController에 각 이벤트에 수행되어야 할 메소드들이 정의 되어있다.
* ControllerMapper에 event와 수행할 함수를 맵핑한다.
* Method Reference를 위해 Service에 FunctionalInterface로 인터페이스를 정의한다. 여기에서 모든 Exception 처리를 일괄 하도록 한다.
* Test code 를 작성하였다.



## 기능 요구 사항

* 사용자로부터 자동차 이름을 쉼표(,)로 구분하여 입력 받는다.
* 사용자로부터 자동차를 몇 번 이동할 것인지 횟수를 입력 받는다.
* 각 자동차는 매 라운드마다 0~9 사이의 랜덤 숫자를 생성하여, 4 이상인 경우 전진한다.
* 각 라운드가 끝난 후 모든 자동차의 현재 위치를 출력한다.
* 모든 라운드가 종료되면 가장 많이 전진한 자동차를 우승자로 출력한다.
* 우승자가 여러 명일 경우 쉼표(,)로 구분하여 함께 출력한다.


## 구현 기능 목록
* 자동차 이름을 사용자로부터 입력 받아 파싱 후 유효성 체크하고 저장
  * 자동차 리스트를 저장하는 클래스
  * 자동차 하나의 정보를 저장하는 클래스
  * 자동차 이름을 저장하는 래퍼 클래스
* 사용자로부터 자동차가 몇번 움직일 것인지 입력받고 유효성 체크 및 저장
  * 자동차가 움직일 정보를 저장하는 래퍼 클래스 
* 자동차가 랜덤 숫자에 따라 진행하거나 멈추는 기능
* 우승자를 판단하여 출력
* 에러처리
  * 람다를 랩핑하는 클래스
* 위와 같은 동작들을 제어하는 클래스와 게임 상태를 저장하는 클래스



## 게임 실행 예시

```
경주할 자동차 이름을 입력하세요(이름은 쉼표(,)를 기준으로 구분).
pobi,crong,honux
시도할 회수는 몇회인가요?
5

실행 결과
pobi : -
crong : -
honux : -

pobi : --
crong : -
honux : --

pobi : ---
crong : --
honux : ---

pobi : ----
crong : ---
honux : ----

pobi : -----
crong : ----
honux : -----

pobi : -----
crong : ----
honux : -----

pobi, honux가 최종 우승했습니다.
```

## 프로젝트 구조

### 패키지 구성

```
racinggame/
├── Application.java          ← 진입점
├── GamePrint.java            ← 출력 담당
├── Service.java              ← FunctionalInterface
├── car/                      ← 도메인 모델
│   ├── Car.java
│   ├── CarName.java
│   ├── CarProgress.java
│   ├── CarList.java
│   └── GameCount.java
└── control/                  ← 게임 흐름 제어
    ├── GameStatus.java
    ├── CurrentGameInfo.java
    ├── ControllerMapper.java
    └── GameController.java
```

### 게임 상태 흐름

게임 상태(이벤트)를 enum으로 정의하고, 각 상태에 실행할 메서드를 매핑하는 Event Driven 구조이다.

```
INIT → INITCAR → INITCOUNT → INITPROGRESS → PROGRESS → END → EXIT
```

### 제어 클래스 (`control` 패키지)

| 클래스 | 역할 |
|--------|------|
| `GameStatus` | 게임 상태를 enum으로 정의 |
| `ControllerMapper` | `Map<GameStatus, Service>` — 상태와 실행 함수를 매핑 |
| `Service` | `@FunctionalInterface` — 메서드 레퍼런스를 담는 인터페이스 |
| `GameController` | 각 상태별 실행 메서드 정의 및 `run()` 루프 |
| `CurrentGameInfo` | 현재 상태, 자동차 목록, 남은 횟수를 한 곳에서 관리 |

`Application`은 `GameStatus.EXIT`가 될 때까지 `game.run()`을 반복 호출한다.

### 도메인 모델 (`car` 패키지)

| 클래스 | 역할 | 주요 검증 |
|--------|------|----------|
| `CarName` | 자동차 이름 래퍼 | 빈 값 금지, 최대 5글자 |
| `CarProgress` | 전진 거리 래퍼 | `-` 문자열로 시각화 |
| `Car` | 자동차 하나의 정보 | 랜덤값 > 3이면 전진 |
| `CarList` | 자동차 목록 관리 | 전체 전진 처리, 우승자 판별 |
| `GameCount` | 시도 횟수 래퍼 | 숫자 여부, 1~100 범위 |

### 예외 처리

`GameController.run()`에서 모든 예외를 일괄 처리한다. 입력 오류 시 에러 메시지를 출력하고 현재 상태를 유지하여 재입력을 유도하며, `"No line found"` 예외(입력 스트림 종료)는 게임을 즉시 종료한다.


## 과제 제출 과정
* [과제 제출 방법](https://github.com/next-step/nextstep-docs/tree/master/precourse)
