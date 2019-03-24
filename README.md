# Status of All Library Book Loans in Ansan City

- 안산시의 모든 도서관에서 책을 검색하고 대출 여부를 확인 할수 있습니다.
- 만일 원하는 도서가 대출중이라면 반납 알림을 이메일로 받아 볼 수 있습니다.

## Install

```bash
pipenv install
pipenv shell
```

## Installed Apps

```bash
# dev
django-debug-toolbar==1.11
django-extensions==2.1.6

# base
djangorestframework==3.9.1
djangorestframework-jwt==1.11.0
lxml==4.3.2
bs4==0.0.1
Pillow==5.4.1
redis==3.2.1
requests==2.21.0
django-celery-beat==1.4.0
```

## Secret Files

아래와 같이 본인의 Secret file 을 세팅해야 합니다.

```json
# app/.secrets/secret.json

{
"SECRET_KEY" : "Your Secret Key",
"EMAIL_HOST_USER": "your@gmail.com",
"EMAIL_HOST_PASSWORD": "passworld",
"SERVER_EMAIL": "your@gmail.com",
"DEFAULT_FROM_MAIL": "your"
}
```

## Run ENV

```bash
# dev server run
export DJANGO_SETTINGS_MODULE=config.settings.dev

# production server run
export DJANGO_SETTINGS_MODULE=config.settings.production
```

## Run Redis docker server
celery send email task server

```bash
docker run -d -p 6379:6379 redis
```

## Run Celery
- send-email-process : 10, 14, 16, 18 시 마다 알림요청이 있는지 검사하고 있으면 이메일 발송

```bash
celery -A config worker -l info -B
```



## API Document's
- [GitBook](https://ansan-library-search.gitbook.io/project/)