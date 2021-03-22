# REST API , JSON 설계

## 간단한 메모

- PathName vs quryString

  - PathName = 어떤 데이터의 특정해서 보여줘야 할 경우
  - querystring = 정렬하거나 필터해서 보여줘야 할 경우

- RESTAPI 관련 포스팅
- https://digitalbourgeois.tistory.com/53?category=691381
- 설계 원칙

  1. 간략하고 직관적이게 디자인하기(get , set 사용X)
     - GET ,POST ,DELETE , PUT을 사용하여 동사를 대체한다.
     - 조회 - GET
     - 입력 - POST
     - 삭제 - DELETE
     - 수정 - PUT(전체적인 수정) , PATCH(일부분만 수정)
  2. 언더스코어보다는 하이픈 사용 / 소문자만 사용 /
  3. 명시적으로 작성하고 동사는 사용하지 않는쪽으로

- ORM 포스팅 https://blog.dork94.com/194
- 동적 querystring 처리 https://pythonise.com/series/learning-flask/flask-query-strings

---

## 프론트 엔드

- 인원 조회 페이지
  - 방정보를 통한 인원 조회
    - 면적(Group)
    - 동(Group) / 호(groupByGroup)
    - 방갯수(Group)
    - 가격(Group)
    - 입주 날짜(groupByGroup)
  - 유저 정보 조회
    - 세대주
    - 구성원수
    - 전화번호

---

## DTO

```
Interface IUserBasicInfo{
  user.name : string;
  group.name : int;
  groupByGroup.name : int;
}

interface IUser_adminBasic extends IUserBasicInfo{
  admin.name : string;
}

interface ITableBasicInfo{
  title: string;
  description : string;
  createdAt : Date;
  updatedAt? : Null | Date;
  deletedAt? : NULL | Date;
}

interface IPetitionsTable extends ITableBasicInfo {
  stage : string;
}

interface IUserCarTable{
  kind : string;
  carCode : string;
}

interface IVotingInfoTable extends ITableBasicInfo{
  user.count(총인원수) : int;
  agreementCount : int;
  oppositionCount : int;
}

```

---

## REST API(100명 기준)

- /api

  - /user (인원 관리 카테고리) 이미지 관련 로직 여기서 처리

    - GET /?offset={}&limit={}
      - 전반적인 회원 정보 가지고옴
      - Business Logic
        - querystring 값을 통해 User 정보를 상한선을 지키며 groups,groupByGroup을 조인후 가지고 온다.(model)
        - offset = 기준점
        - limit = 출력할 행 숫자
      - return Array<{ id: int , name : string , host : boolean , createdAt : Date , updatedAt : Date , deletedAt:Date , birth:Date , phoneNumber : string ,group.name:int,groupBygroup.name:int , groupBygroup.createdAt:Date }>
    - GET /filter/human
      - 인원의 정보를 세밀하게 조회 할 수 있는 기능 , 조회는 누적으로 개발에 주의!!
      - querystring [("host",boolean) , ("memberIndex",int) , ("phoneNumber",string) , ("offset",int) , ("limit",int)]
      - Business Logic
        - querystring에 담긴 데이터의 값을 기반으로 db조인
      - return {}
    - GET /filter/room/< detail:string>
      - 방에 대한 정보를 통해 인원들 정보 조회
      - (self,detail) detail을 통해 테이블 명 전송
      - querystring Groups >> {("minWeight",int),("name",int),("pricing",int),("roomCount",int),("offset",int) , ("limit",int)}
      - querystring GroupsByGroup >> {("name",int),("createdAt",int),("pricing",int),("offset",int) , ("limit",int)}
      - Business Logic
        - pathName을 통한 분리후 서로 다른 querystring을 통해 id 값 찾은 후 users와 join
    - GET /filter/info/< human:string>/< room:string>
      - 동 또는 호 , 인원 세부정보 조회를 동시에 실행 할 시
      - Business Logic
        - human 과 room을 확인후 table명을 분석 >> querystring >> columns값을 알아낸다
        - querystring Groups {("minWeight",int),("name",int),("pricing",int),("roomCount",int),("offset",int) , ("limit",int)}
        - querystring GroupByGroup {("name",int),("createdAt",int),("pricing",int),("offset",int) , ("limit",int)}
        - querystring users [("host",boolean) , ("memberIndex",int) , ("phoneNumber",string) , ("offset",int) , ("limit",int)]
      - return
    - PATCH /changed
      - 특정 정보를 선택하여 특정 부분을 수정 전 URL 기억후 다시 요청하여
      - querystring { ("id",int),("변경할 항목",그에 해당하는 값) }
      - return {}
    - DELETE /deleted
      - 특정 정보 row 선택하여 삭제
      - querystring {"id":int} id
      - Business Logic
        - 해당 id값을 통해 컬럼 삭제
        - 삭제 후 한 row 선택하여
    - GET /outter
      - 외부 출입자 조회
      - querystring (("offset",int),("limit",int))
      - group 과 groupBygroup ,admin 테이블을 통해서 조인을 한 정보 전달
      - return Array{name : string , description : string , createdAt : Date , phoneNumber : string , group.name:int , groupByGroup.name:int }
    - GET /exit
      - 웹 소켓 활용 예정

  ***

  - /admin
    - GET /
      - 메인 페이지 정보 조회 >> 메인 페이지에 어떤 페이지에 어떤 정보가 보일지 생각후 설계
      - return {}
    - GET /dashboard
      - 공지사항 정보
      - return {id:int , title : string , desciption : string , createdAt : Date , updatedAt : Date | NULL, deletedAt :Date | NULL , admin.name : string , admin.email:string}
    - POST /login
      - 로그인
      - body(form) {email : string , password : string}
      - return { message:string , data: { name : string , email:string , day.id:[1,2,3] }}
    - POST /siginup
      - 회원가입 프론트에서 담당 동 선택할 수 있도록
      - body(form) {name: string , password : string, email:string , groupId:int }
      - return {message : string}
    - POST /logout
      - 로그아웃
      - return { message:string }
    - /registering
      - POST /inner
        - 신규 회원 등록
        - body(form) {name : string , memberIndex : int , host: boolean , createdAt : Date , birth: Date , groupId : int , groupById:int,files:images }
        - Business Logic은 아래와 동일하명 테이블만 다르다
        - return {message : string}
      - POST /outter
        - 외부인 등록 프론트에서 동 호 선택할 수 있게 리스트 보여줌
        - body(form) { name:string ,description : string , createdAt : DateTime , phoneNumber:int , groupId: int , groupById : int ,files:images}
        - Business Logic
          - users 테이블에서 groupId groupById name를 통해 조회후 id 찾은후 outterUsers 저장
          - 이미지 저장은 동별로 한다.
          ```
          /static
              /101(groupId)
                  호_이름.jpg >> {groupById}_{name}.jpg
                  호_이름.jpg
              /102
          ```
          - OutterImages 테이블 저장 >><a href ="https://stackoverflow.com/questions/8589674/sqlalchemy-getting-the-id-of-the-last-record-inserted/8590301">result.inserted_primary_key</a>을 통해 id값 얻기
          - outterUser_images 테이블 저장
        - return { message : string }

  ***

  - /voting (주민 투표 카테고리)

    - POST /registed

      - 주민 투표 정보 등록 (동 , 호는 selectBox를 통해서 전달)
      - body(form) {title : string , description : string , createdAt : string , user.name : string , group.id :int , groupByGroup: int , }
      - Business Logic
        - user.name을 select name from users where name = user.name , groupid = group.id 등으로 user.id값을 조회한후 db에 저장한다
        - agreementCount , oppsitionCount 값은 0으로 votingInfo에 저장한다.
      - return { message : string }

    - GET /progress

      - 진행중인 주민 투표 정보 조회
      - querystring [("limit" , string),("offset",string)]
      - Business Logic

        - 현재 날짜와 비교하여 큰값을 가지고 오되 limit , offset값을 준수하여 데이터 조회를 한다.
        - select count(\*) from users를 통해 총인원수 찾기
        - Voting 테이블을 통해 users.name , admin.name , group.name , groupByGroup.name

      - return Array< IUserBasicInfo extends IvotingUsers>

    - GET /deadline
      - 마감된 주민 투표 조회
      - querystring {("limit",int) , ("offset" , int)}
      - Business Logic
        - 현재 날짜와 비교하여 현재날짜보다 지난 데이터를 가지고 온다.
        - querystring을 통해 조회
      - return Array<-IvotingUsers>

  ***

  - /petitions (민원 관리 센터 카테고리)

    - GET /
      - querystring에 따라서 종류에 따라서 처리(시설 , 신고 , 기타)
      - querystring ("kind",string)
      - return Array< IUserBasicInfo extends IPetitionsTable>

    * PATCH /stage/<-stage:string>
      - 단계 버튼 클릭시 단계 변경
      - Business Logic
        - stage pathname과 비교하여 ["접수" ,"서류 검토" , "검토 완료" , "처리중" , "처리완료"] 다음 값을 알아낼
      * return < IUserBasicInfo extends IPetitionsTable>

  ***

  - /facility (시설관리 카테고리)

  ***

  - /pricing (관리비 고지 관리 카테고리) - 간략하게 마무리
    - GET /
      - 단순히 정보 조회만 가능하게 구현
      - querystring {limit : int } ,{ offset : int }
      - return Array < IUserBasicInfo extends { kindName : string , pricing : int , createdAt : Date , deletedAt : Date }>

  ***

  - /usercar (차량 및 주차 관리)
    - GET /
      - 인원간 차량 조회
      - querystring {("limit":string , "offset":string) }
      - return Array< IUserBasicInfo extends IUserCarTable>
    - GET /filter
      - querystring을 통한 하나 조건으로 정보 조회(차량 번호 , 입력 날짜 , 차종 , 동 , 호 , 이름 )
      - querystring (("carCode",string) , ("createdAt":stirng -> Date), ("kind",string) , ("group",string) , ("groupByGroup",string) , ("user" : string))
      - Business Logic
        - 테이블 명에 해당하는 querystring을 통해 분기 처리
        - if querystring 특정 테이블 명이라면 Join 이나 select사용
      - return Array< IUserBasicInfo extends IUserCarTable>
    - GET /filter/multi
      - 차량정보 조회와 인원정보 동시 조회( /filter에 처리해도 괜찮지만 로직의 깊이가 깊어 질거 같아 분리)
      - querystring [("carCode",string) , ("createdAt":stirng -> Date), ("kind",string) , ("group",string) , ("groupByGroup",string) , ("user" : string)]
      - Business Logic
        - 테이블 명 조회 후 테이블 join후에 정보를 전달 해주는 방식으로 진행한다.
      * return Array< IUserBasicInfo extends IUserCarTable>
    * WebSocket을 활용하여 주차 정보 제공(실시간 영상 처리한 데이터가 배열로 전송 될것으로 예상된다.)

  ### WebSocket

  - 출입 여부 실시간 모니터링
