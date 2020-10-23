# 100moon1ta

> 개발자를 위한 타자 연습 서비스, **백문이불여일타**입니다.



## 목차

- [개요](#개요)
- [기능](#기능)
- [유사 서비스](#유사-서비스)
- [향후 전망](#향후-전망)
- [기술 스택](#기술-스택)
- [기술 설명](#기술-설명)
  - [ERD](#erd)
  - [디렉토리 구조도](#디렉토리-구조도)
  - [아키텍처](#아키텍처)
  - [기타](#기타)
- [테스트 방법](#테스트-방법)



## 개요

> 백문이 불여일견이라고 한다. 백 번 듣는 것이 한 번 보는 것만 못하다는 뜻이다. 개발 또한 마찬가지다. 사람의 뇌는 힘든 상황에서의 기억을 쉽게 떠올린다. 개발자의 덕목인 클린 코드, 알고리즘을 위한 ADT 그리고 다양한 CS 지식을 직접 손으로 따라치면서 향유하는 문화를 만들고자 서비스를 기획하게 되었다.



## 기능

> 프로젝트의 기능들을 설명해주세요  
> 스크린샷이나 gif등으로 한눈에 볼 수 있게 하면 더 좋습니다



## 유사 서비스

### typing.io

- http://typing.io/

### SpeedCoder

- http://www.speedcoder.net/

### 차별점

- 코딩 스타일, 클린 코드, 기술 블로그의 포스팅 제공
- 언어별, 개발 분야별 로드맵 제공



## 향후 전망

> 부득이한 사정으로 프로젝트에 구현하지는 못했지만 보완할 점이나 추가할 점이 있다면 적어주세요



## 기술 스택

> 프로젝트를 구현 할 때 사용한 기술들을 적어주세요



## 기술 설명

### ERD



### 디렉토리 구조도

```
📁100moon1ta
├─📁backend
│   ├─📁l00moon1ta
│   ├─main.py
│   └─requirements.py
└─📁frontend
    ├─📁Components
    ├─App.js
    └─packages.json
```



### 아키텍처



### 기타

> 이외에도 프로젝트를 이해하기 위해 필요한 것들을 적어주세요 (팀별 개발표준, API Documentation 등등...)



## 테스트 방법

> 프로젝트를 배포한 url과 테스트하기 위한 계정 ID/PW를 적어주세요
> 자세한건 localhost:8000/swagger/

### Login

```
POST api/rest-auth/login/

{
    email: string,
    password: string
}
```

### Logout

```
POST api/rest-auth/logout/
```

- jwt 인증방식이기 때문에 로그아웃은 별 효과가 없음, 만료시간을 짧게 하거나 블랙리스트를 사용

### Password

```
Password change

POST api/rest-auth/password/change/

header = { Authorization : JWT {JWT token} }
{
    new_password1: string,
    new_password2: string
}
```

```
Password reset

POST api/rest-auth/password/reset/

{
    email: string,
}
```

### Signup

```
POST api/rest-auth/signup/

{
    username: string,  # 아직 안바꿈
    email: string,
    password1: string,
    password2: string
}

```

### Social

```
POST api/rest-auth/social/

{
    access_token: string
}
```

- github의 경우 access_token만 있으면 됨

### User

```
User 정보

GET api/rest-auth/user/
header = { Authorization : JWT {JWT token} }
```

- token에 해당하는 유저 정보 리턴

```
User 정보 수정

PUT pi/rest-auth/user/
header = { Authorization : JWT {JWT token} }
{
    id: int,
    email: string,
    username: string,
    profile_image,
    comment,
}
```

### Username 중복 검사

```
GET api/rest-auth/nickname-duplicated/?nickname={nickname}

```
