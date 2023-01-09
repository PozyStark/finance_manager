# Finance manager

***

### Описание сервиса: 
Cервис отвечает за регистрацию и авторизацию пользователя.
Так же предоставляется возможность фиксации всех расходов и создание целей
для накопления, возможность указать денежные поступления и 
регулярные траты для того чтобы можно было вычислить сумму которую 
необходимо отложить для выполнение цели накопления.

***

## Описание API:
***
### Получения токена доступа:
#### http://localhost/api/token/
Тело запроса:
```json
{
    "email": "example@gmail.ru",
    "password": "YourPassword"
}
```
Тело ответа:
```json
{
    "refresh": "refreshToken",
    "access": "accessToken"
}
```

### Обновление токена доступа:
#### http://localhost/api/token/refresh/
Тело запроса:
```json
{
    "refresh": "refreshToken"
}
```
Тело ответа:
```json
{
    "access": "accessToken"
}
```

### Проверка токена на валидность
#### http://localhost/api/token/verify/
Тело запроса:
```json
{
    "token": "accessToken"
}
```
Тело ответа:

В случае успеха пустое тело и код:200

В случае если токен недействителен код 401
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

### Регистрация пользователя
#### http://localhost/api/finance_manager/register/

Тело запроса:
```json
{
    "email": "example@mail.ru",
    "number": "",
    "first_name": "",
    "last_name": "",
    "password": "",
    "confirm_password": ""
}
```

