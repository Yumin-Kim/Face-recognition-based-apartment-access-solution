# OpenCV + Android 연동 후 얼굴인식을 통해 서버의 등록된 사용자 판별

## 설계

## 구현

### 몰랐던 용어 정리

- JDK NDK SDK
  - JDK 자바 개발 도구 - 자바 어플리케이션을 구축하기위한 핵심 플랫폼
    - JVM(Java Virtual machine) 자바 가상 머신
    - JRE(Java Runtime Environment) 자바 런타임 환경
    - JDk(Java Development Kit) 자바 기반 소프트웨어를 개발하기 위한 도구들로 이뤄진 패키지함
      - 패키지 종류
        - Java SE ( Standard Edition )
        - Java EE ( Enterprise Edition ) Java SE + Java Beans , ORM(Object Relational Mapping) 지원
        - Java ME ( Miro Editon ) Java SE + 휴대폰 + PDA , 셋텁박스
  - SDK (Software Developer Kit) 소프트웨어 개발 도구
    - UI 기반으로 특화된 API를 제공하여 Application Level에서 개발이 가능하게 도와준다.
  - NDK ( Native Development Kit) 네이티브 개발 도구
    - C / C++를 이용하여 애플리케이션 , 미들웨어 개발에 사용되는 Framework
    - SDK를 토대로 만든 안드로이드 애플리케이션은 자바를 활용했기 때문에 자바의 한계점을 그대로 가지고 있다
    - 그렇기 때문에 그래픽 처리나 시그널 프로
    - 이런 처리를 위해 구글에서 안드로이드 어플리케이션에서도 C/C++을 활용 할 수 있돌고 제공하는 도구가 바로 NDK라고 한다.
- JNI( Java Native Interface )
  - JVM위에서 실행되고 있는 자바 코드가 네이티브 응용 프로그램(하드웨어와 운영 체제 플랫폼에 종속된 프로그램들) 그리고 C / C++등 다른 언어들로 작성된 라이브러리들을 호출되거나 반대로 호출되는 것을 가능하게 하는 Framework
  - JNI의 원리
    - Java 파일 : 호출되려고 하는 C 함수에 대한 선언문과 호출문 그리고 dll로드문을 작성
    - C/C++ : 파일 Native Call 하려는 C함수에 대한 정의문 및 헤더 파일을 작성
    - 만들어진 C파일을 dll로 빌드
    - 빌드한 dll을 자바 코드에서 호출해서 만든 C함수를 자바에서 사용할 수 있게함  
      ![C 와 Java를 사용하기 위한 JNI](https://miro.medium.com/max/700/1*ATfVpiorbLHwD9bBGp37_A.png)
    - 활용
      - C/C++로 제어가 가능했던 하드웨어 단위의 기능(센서 값 처리 , 터치)등을 JNI을 활용하여 개발할 수 있게 함으로써 다음과 같은 처리가 가능해진다.
        - 영상 처리
        - 게임
        - 센서 처리
        - 물리 시뮬레이션
