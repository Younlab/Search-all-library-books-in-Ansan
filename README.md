# Status of All Library Book Loans in Ansan City

- 안산시의 모든 도서관에서 책을 검색하고 대출 여부를 확인 할수 있습니다.
- 만일 원하는 도서가 대출중이라면 반납 알림을 이메일로 받아 볼 수 있습니다.

## Install

```bash
pipenv install
pipenv shell
```

## Run ENV

```bash
# dev server run
export DJANGO_SETTINGS_MODULE=config.settings.dev

# production server run
export DJANGO_SETTINGS_MODULE=config.settings.production
```

## Secret Files

아래와 같이 본인의 Secret file 을 세팅해야 합니다.

```json
# app/.secrets/secret.json

{
"SECRET_KEY" : "Your Secret Key",
}
```

## Installed Apps

```bash
# dev
django-debug-toolbar==1.11
django-extensions==2.1.6

# production
djangorestframework==3.9.1
```