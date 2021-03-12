# Android에서 얼굴 인식 후

# Flask 서버 구축

- 모듈화 하여 개발
- Node.js express와 같은 폴더 구조로 개발
- DB(mysql - pymysql)을 사용하여 연동
- 향후 AI개발후 서비스를 개발할때 사용할 가능성이 높기 때문에 template만든다는 생각으로 개발

# TODO List

- 관리자 페이지에서 이미지 입력
  - 이미지 input으로 입력받고 resize과정
  - 입력 받은 이미지 기록을 DB에 기록
  - 입력 받은 이미지 학과에 따라 분리
    - 분리하지 않을시 data<이미지 지정 폴더> 무분별하게 이미지 배치
    * 현재는 서버가 실행됨과 동시에

* Flask prod모드 변경 방법
* 실서비스를 위한 AWS
