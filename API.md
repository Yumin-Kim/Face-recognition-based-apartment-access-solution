# REST API , JSON 설계

## 간단한 메모
PathName vs quryString
PathName = 어떤 데이터의 특정해서 보여줘야 할 경우
querystring = 정렬하거나 필터해서 보여줘야 할 경우

RESTAPI 관련 포스팅
https://digitalbourgeois.tistory.com/53?category=691381
설계 원칙
1. 간략하고 직관적이게 디자인하기(get , set 사용X)
    * GET ,POST ,DELETE , PUT을 사용하여 동사를 대체한다.
    * 조회 - GET
    * 입력 - POST
    * 삭제 - DELETE
    * 수정 - PUT(전체적인 수정)  , PATCH(일부분만 수정)
2. 언더스코어보다는 하이픈 사용 / 소문자만 사용 / 
3. 명시적으로 작성하고 동사는 사용하지 않는쪽으로

---

## REST API
* /api
    * /user
        * 
    * /admin
    * /facility
    * /petitions
    * /voting
    * /pricing
    * /usercar
    * /registering