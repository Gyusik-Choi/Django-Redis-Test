# Django-Redis-Test

### Redis

```
key-value
in-memory database
```



### 진행 순서

레디스를 설치하지 않다면 레디스부터 설치해야 한다.

프로젝트 생성

- django-admin startproject django_redis_test

앱 생성

- python manage.py startapp posts

장고에서 사용할 레디스 라이브러리 설치

- pip install django-redis

settings.py에 캐시 세팅

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

데이터 모델링(models.py)

db 마이그레이션

- python manage.py makemigrations
- python manage.py migrate

요청할 url을 urls.py에 세팅

url에 맞는 로직을 수행할 views.py 세팅

bulk_create 를 통해서 db에 임의의 데이터 1000개 생성

레디스 캐시를 거치지 않는 요청과 레디스 캐시를 통한 요청을 각각 세팅

비교



### 진행관련 부연정리

#### 윈도우 레디스 설치

레디스는 공식적으로는 Unix 환경에서만 지원하지만 윈도우 환경에서도 사용할 수 있도록 MS에서 지원하고 있다.

윈도우에서 레디스 설치는 https://gofnrk.tistory.com/35 이분의 글을 참조했다.



#### 프로젝트 이름

처음에 프로젝트 이름은 django_redis로 했다가 django_redis_test로 바꿨다.

레디스에 데이터를 캐싱하려는데 오류가 발생했다.

오류는 settings.py에 정의한 django_redis.cache.RedisCache에서 발생했다.



