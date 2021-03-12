# Android에서 얼굴 인식 후 서버 구축 단계

- **<a href = "https://github.com/Yumin-Kim/RTSP_Node.js_Server">해당 링크</a>README를 이어서 작성중이다**

* 개발 기간
  - 진행 기간 : 2021.02.17 ~ 진행중
  - 예상 마감 기간 : 2021.08.01(여름방학전)
  - 서버 개발 기간 : 2021.03.10

---

# Flask 서버 구축 및 관리자 페이지 정리

- Back(Flask)

  - **모듈화** 하여 개발
  - Node.js express와 같은 폴더 구조로 개발
  - DB(mysql - pymysql)을 사용하여 연동
  - 향후 AI개발후 서비스를 개발할때 사용할 가능성이 높기 때문에 template만든다는 생각으로 개발

* 파이썬 관련 메모
  - 해당 명령어를 통해 의존성 있는 Module을 확인 및 다운로드 받을 수 있다
  ```
  # 해당 프로젝트에 있는 requirements.txt 파일에는 테스트로 무분별하게 설치 되어있지만 배포시 정리 예정
  pip freeze > requirements.txt
  ```

---

- Front(React Dashboard Template 활용)
  - SSR 예정 없음
  * 실시간으로 모니터링 가능하게 구현

## RestAPI 설계(간단한 설계)

- /admin(관리자를 위한 URL)

  - 조회
  - 삭제
  - 변경
  - 추가
    - (POST) /Image/:teacher/:group (이미지 추가)
      - teacher : 누구인지 DB 조회
      - group : 원하는 그룹이 있는지 확인후 DB에 기록

- /face(얼굴인식 위한 URL)
  - 얼굴 인식 비교
  - 수정중...
- /user(사용자 정보 조회)
  - 조회 (수업 , 정보)
  - 삭제 (수업 , 정보)
  - 변경 (수업 , 정보)
  - 추가 (수업 , 정보)

## DB 설계(Toy Project로 간단하게 구성)

<!-- ![DB설계]() -->

<img src="/MarkupImage/workspace.jpg" width="40%" height="30%" title="MysqlWorkSpaceImage" alt="MysqlWorkSpaceImage"></img>

---

# TODO List

1. 2021-03-13 **문제점 : 이미지 저장 및 인코딩 요청시점**

- 관리자 페이지에서 이미지 입력(Front) **API-/admin/saveImage**
- 이미지 input으로 입력받고 resize과정(Back) **API-/face/compare**

  - 입력 받은 이미지 기록을 DB에 기록

  - 입력 받은 이미지 학과에 따라 분리후 저장

    - 분리하지 않을시 data<이미지 지정 폴더> 무분별하게 이미지 배치

    ```
    /data
      /multi
        /20121234.png
        /20121234.png
        /2012123123.png
      /computer
        /20123123.png
        /20123123.png
        /20123123.png
      /...
    ```

    - 현재는 서버가 실행됨과 동시에 이미지 인코딩 과정 진행 >> 시간이 많이 소모되며 서버에 많은 무리가 간다.
      - 이부분을 개선하기 위해서 Android(Front)부분에서 UI<학과>를 선정 할 수 있는 UI를 배치하여 통신 하여 인코딩로직을 실행시킬 방법 생각중

  - 향후 보안(이미지 관련) 생각해보기

2. 세부적인 로직 및 고려 사항

   - 출첵후 다시 출첵이 안되도록 부가적인 비즈니스 로직 설계

   - Flask prod모드 변경 방법
   - 실서비스를 위한 AWS >> 이미지 저장을 S3로 할거 고려하기
