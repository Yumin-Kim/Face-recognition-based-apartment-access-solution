# REST API , JSON 설계

## 간단한 메모

- PathName vs quryString

  - PathName = 어떤 데이터의 특정해서 보여줘야 할 경우 ex) path/page
  - querystring = 정렬하거나 필터해서 보여줘야 할 경우?pv=v1&v2=px

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

interface ITableBasicInfo{
  id: int;
  title: string;
  description : string;
  createdAt : Date;
  updatedAt? : Null | Date;
  deletedAt? : NULL | Date;
}

  interface IGroupTable{
    minWeight : int;
    maxWeight : int;
    roomCount : int;
    pricing : int;
  }

  interface IGroupByGroupTable_mapping extends IGroupTable{
    repairCount : int;
    createdAt:Date; // 입주 날짜
    updatedAt:Null|Date;
    deletedAt:Null|Date;
    housePassword:string;
    pricing:int;
  }

  interface IUser_ReturnData extends IGroupByGroupTable_mapping{
    memberIndex:int;
    host : boolean;
    birth:Date;
    phoneNumber : string;
  }


interface IUser_adminBasic extends IUserBasicInfo{
  admin.name : string;
}

interface IPetitionsTable extends ITableBasicInfo {
  stage : string;
  sucessedAt? : Date;
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

  ```

  Interface IUserBasicInfo{
    user.name : string;
    group.name : int;
    groupByGroup.name : int;
  }

  ```

  - GET /?offset={}&limit={}
    - 전반적인 회원 정보 가지고옴
    - Business Logic
      - querystring 값을 통해 User 정보를 상한선을 지키며 groups,groupByGroup을 조인후 가지고 온다.(model)
      - offset = 기준점
      - limit = 출력할 행 숫자
    - return Array< IUserBasicInfo extends IUser_ReturnData>
  - GET /filter/human
    - 인원의 정보를 세밀하게 조회 할 수 있는 기능 , 조회는 누적으로 개발에 주의!!
    - querystring [("host",boolean) , ("memberIndex",int) , ("phoneNumber",string) , ("offset",int) , ("limit",int)]
    - Business Logic
      - querystring에 담긴 데이터의 값을 기반으로 db조인
    - return Array< IUserBasicInfo extends IUser_ReturnData>
  - GET /filter/room/< detail:string>
    - 방에 대한 정보를 통해 인원들 정보 조회
    - (self,detail) detail을 통해 테이블 명 전송
    - querystring Groups >> {("minWeight",int),("name",int),("pricing",int),("roomCount",int),("offset",int) , ("limit",int)}
    - querystring GroupsByGroup >> {("name",int),("createdAt",int),("pricing",int),("offset",int) , ("limit",int)}
    - Business Logic
      - pathName을 통한 분리후 서로 다른 querystring을 통해 id 값 찾은 후 users와 join
    * return Array< IUserBasicInfo extends IUser_ReturnData>
  - GET /filter/info/< human:string>/< room:string>
    - 동 또는 호 , 인원 세부정보 조회를 동시에 실행 할 시
    - Business Logic
      - human 과 room을 확인후 table명을 분석 >> querystring >> columns값을 알아낸다
      - querystring Groups {("minWeight",int),("name",int),("pricing",int),("roomCount",int),("offset",int) , ("limit",int)}
      - querystring GroupByGroup {("name",int),("createdAt",int),("pricing",int),("offset",int) , ("limit",int)}
      - querystring users [("host",boolean) , ("memberIndex",int) , ("phoneNumber",string) , ("offset",int) , ("limit",int)]
    - return Array< IUserBasicInfo extends IUser_ReturnData
  - PATCH /changed/< id:string>
    - 특정 정보를 선택하여 특정 부분을 수정 전 URL 기억후 다시 요청하여
    - pathname { ("id",int) } , body(form) 변경된 부분만 전송하여 sql문도 그에 따라 작성
    - return IUserBasicInfo extends IUser_ReturnData
  - DELETE /deleted
    - 특정 정보 row 선택하여 삭제
    - querystring {"id":int} , offset값을 통해서 삭제후 offset+1의 row데이터를 가지고온다
    - Business Logic
      - 해당 id값을 통해 컬럼 삭제
      - 삭제 후 한 row 선택하여
    * return IUserBasicInfo extends IUser_ReturnData
  - GET /outter
    - 외부 출입자 조회
    - querystring (("offset",int),("limit",int))
    - group 과 groupBygroup ,admin 테이블을 통해서 조인을 한 정보 전달
    - return Array < IUserBasicInfo extends { description : string , createdAt : Date , phoneNumber : string} >
  - GET /exit
    - 웹 소켓 활용 예정

  ***

  - /admin
    - GET /dashboard
      - 공지사항 정보
      * return Array< ITableBasicInfo extends { admin.name : string , admin.email:string} >
    * PATCH /dashboard
      - form(body) { id : int , Title? : string , description? : string , createdAt? : Date , updatedAt? : Date , deletedAt?: Date }
      - Business Logic
        - request.form을 통해 key value 확인후 테이블 수정 하는 방법
      - return ITableBasicInfo extends { admin.name : string , admin.email:string} >> return값이 배열이 아니기 떄문에 프론트에서는 불변성을 지키며 코딩 기존 배열에 [ 19 ]값을 변경해야한다.
    * DELETE /dashboard/< id:string>&?offset={}
      - 원하는 row를 지우는 기능 제공
      * querystring offset , pathname id
      * Business Logic
        - (self , id) >> id 값을 통해서 adminDashBoard를 제거 한다.
        * offset값을 통해서 지운데이터를 매꿔주는 역할을 한다.
        * 추가적으로 auto Increment를 해야한다.
      * return ITableBasicInfo extends { admin.name : string , admin.email:string} >> return값이 배열이 아니기 때문에 프론트에서 불별성을 지키며 코딩 >> 기존배열에[ 0 ]값을 변경해야한다.
    * POST /dashboard
      - 공지사항을 등록 할 수 있는 기능
      - body form { adminId : int , groupId: string , title : string , description : string , createdAt : Date}
      - return ITableBasicInfo extends { admin.name : string , admin.email:string}
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
      * /chart
        - GET /user&group={}
          - 각 동 인원 / 해당하는 인원수
          * querystring group
          - Business Logic
            - querystring을 통해서 users테이블에 groupid을 조인후 count하여 전송해준다.
            * 총인원 카운트 , 동마다
          * return {totalUser : int , groupCount : int}
        - GET /parking
          - 각 동 마다 주차 공간 이용 내역
          * querystring group
          - Business Logic
            - querystring을 통해서 users테이블에 groupid을 조인후 count하여 전송해준다.
          * return {totalparking : int , groupCount : int}
        - GET /exituser
          - 출입 현황 날짜별 제공
          * return Array<{createdAt : Date , : accessMemberConut : int}>
      * GET /totalcount
        - 총인원수 , 민원내역 총수 , 주민 투표 총수
        - Business Logic
          - users , votingInfo , petitions 테이블 각각 count해서 return
        - return {totalCount : int , votingInfoConut : int , petitions : int}

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
      - return Array< IvotingUsers>

  ***

  - /petitions (민원 관리 센터 카테고리)

    - GET /
      - querystring에 따라서 종류에 따라서 처리(시설 , 신고 , 기타)
      - querystring ("kind",string)
      - return Array< IUserBasicInfo extends IPetitionsTable>

    * PATCH /stage/< id:int>?stage={}
      - 단계 버튼 클릭시 단계 변경
      * querystring ("stage","") pathname으로 table의 id값을 알아낸다
      - Business Logic
        - stage pathname과 비교하여 배열로 선언 ["접수" ,"서류 검토" , "검토 완료" , "처리중" , "처리완료"] 다음 값을 알아낼
        * 해당 단계가 처리완료 단계 이면 수정이 안됨이라고 프론트에서 처리
        * 해당 index가 검토완료의 index를 가지면 해당 row 테이블 에서 succesdAt현재 날짜를 수정해준다.
      * return < IUserBasicInfo extends IPetitionsTable> >> 불변성 지키기

  ***

  ```
  interface IFacilityInfoTable {
    user.name : string;
    group.name : int;
    groupByGroup.name : int;
    petitions.stage : string;
    petitions.kind : string;
    facility_List.admins.name : string;

    createdAt : Date;
    updatedAt : Date | Null;
    deletedAt : Date | Null;
    description : string;
    quarity: int;
  }

  interface IFacilityToolsListTable{
    name : string;
    pricing : int;
    createdAt : Date;
    updatedAt : Date | Null;
    deletedAt : Date | Null;
    stock? : int;
  }

  interface IFacilityRoomsListsTable extends IFacilityToolsListTable{
    title : string;
    capacity : int
    employment : int;
  }

  ```

  - /facility (시설관리 카테고리)
    - GET /Toollog
      - 전반적인 이용내역확인
      - querystring ("limit" , string) , ("offset",string)
      - return Array< IFacilityInfoTable extends {facilityToolsListTable.name : string , facilityToolsListTable.stock : string }>
    * GET /Toollog/toolslist
      - 항목만 조회(시설 기자재)
      - querystring ("limit" , string) , ("offset",string)
      - return Array< IFacilityToolsListTable>
    - GET /rommslog/
      - 전반적인 이용 내역확인
      - querystring ("limit" , string) , ("offset",string)
      - return Array< IFacilityInfoTable extends {facilityRoomsListsTable.name : title , facilityToolsListTable.capacity : int , facilityToolsListTable.employment:int }>
    * GET /rommslog/roomslist
      - 항목만 조회(시설 물)
      - querystring ("limit",string ) , ("offset", string)
      - return Array< IFacilityRoomsListsTable>

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
