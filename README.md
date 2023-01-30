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
## Работа с токенами:
### Получения токена доступа:
#### http://localhost/api/token/
Request POST:
```json
{
    "email": "example@mail.ru",
    "password": "your_password"
}
```
Response
status "200 ok":
```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```
Response
status "401 unauthorized":
```json
{
    "detail": "No active account found with the given credentials"
}
```
### Обновление токена доступа:
#### http://localhost/api/token/refresh/
Request POST:
```json
{
    "refresh": "refresh_token"
}
```
Response status "200 ok":
```json
{
    "access": "access_token"
}
```
Response status "401 unauthorized":
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

### Проверка токена на валидность
#### http://localhost/api/token/verify/
Request POST:
```json
{
    "token": "access_token"
}
```
Response status "200 ok":
```json
{
  
}
```

Response status "401 unauthorized":
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

***
## Работа с пользователем:
### Регистрация пользователя
#### http://localhost/api/finance_manager/register/

Required: [email, password, confirm_password]

Request POST:
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

Response status "201 created":
```json
{
    "detail": "user was created"
}
```

### Смена пароля
#### http://127.0.0.1:8000/api/finance_manager/change-password/

Required: [old_password, new_password, confirm_password]

Authorized: True

Request PUT:
```json
{
    "old_password": "",
    "new_password": "",
    "confirm_password": ""
}
```

Response status "200 ok":
```json
{
    "detail": "password changed"
}
```

### Обновление профиля
#### http://127.0.0.1:8000/api/finance_manager/update-profile/

Required: [email]

Authorized: True

Request PUT:
```json
{
    "email": "",
    "number": "",
    "first_name": "",
    "last_name": ""
}
```

Response status "200 ok":
```json
{
    "detail": "profile was updated"
}
```
***
## Работа с Expenses:
### Получение Expenses
#### http://127.0.0.1:8000/api/finance_manager/expenses/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "expenses": [
        {
            "id": 1,
            "name": "шоколад",
            "amount": 30.0,
            "date": "2023-01-02"
        },
        "..."
    ]
}
```

### Получение Expenses detail
#### http://127.0.0.1:8000/api/finance_manager/expenses/<id:int>/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "expense": {
        "id": 1,
        "name": "шоколад",
        "amount": 30.0,
        "date": "2023-01-02"
    }
}
```

### Добавление Expenses
#### http://127.0.0.1:8000/api/finance_manager/expenses/

Required: [name, amount]

Authorized: True

#### Добавление нескольких записей

Request POST:
```json
{
    "expenses":[
        {
            "name": "",
            "amount": 0,
            "date": ""
        },
        {
            "name": "",
            "amount": 0,
            "date": ""
        }
    ]
}
```
#### Добавление одной записи

Request POST:
```json
{
    "name": "",
    "amount": 0,
    "date": ""
}

```

Response status "201 created":
```json
{
    "detail": "expense create"
}
```

### Изменение Expenses
#### http://127.0.0.1:8000/api/finance_manager/expenses/<id:int>/

Required: [name, amount]

Authorized: True

Request PUT:
```json
{
    "name": "",
    "amount": 0,
    "date": ""
}
```

Response status "200 ok":
```json
{
    "detail": "expense updated"
}
```
### Удаление Expenses
#### http://127.0.0.1:8000/api/finance_manager/expenses/<id:int>/

Authorized: True

Request DELETE:
```json
```

Response status "200 ok":
```json
{
    "detail": "expense id:1 deleted"
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```
***
## Работа с Regular-Expenses:
### Получение Regular-Expenses
#### http://127.0.0.1:8000/api/finance_manager/regular-expenses/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "regular_expenses": [
        {
            "id": 2,
            "name": "кредит",
            "amount": 16000.0
        },
        "..."
    ]
}
```

### Получение Regular-Expenses detail
#### http://127.0.0.1:8000/api/finance_manager/regular-expenses/<id:int>/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "regular_expense": {
        "id": 3,
        "name": "косметика",
        "amount": 1000.0
    }
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```

### Добавление Regular-Expenses
#### http://127.0.0.1:8000/api/finance_manager/expenses/

Required: [name, amount]

Authorized: True

#### Добавление нескольких записей

Request POST:
```json
{
    "regular_expenses":[
        {
            "name": "",
            "amount": 0
        },
        {
            "name": "",
            "amount": 0
        }
    ]
}
```
#### Добавление одной записи

Request POST:
```json
{
    "name": "",
    "amount": 0
}
```

Response status "201 created":
```json
{
    "detail": "regular expense create"
}
```

### Изменение Regular-Expenses
#### http://127.0.0.1:8000/api/finance_manager/regular-expenses/<id:int>/

Required: [name, amount]

Authorized: True

Request PUT:
```json
{
    "name": "",
    "amount": 0
}
```

Response status "200 ok":
```json
{
    "detail": "regular expense updated"
}
```
### Удаление Regular-Expenses
#### http://127.0.0.1:8000/api/finance_manager/regular-expenses/<id:int>/

Authorized: True

Request DELETE:
```json
```

Response status "200 ok":
```json
{
    "detail": "regular expense id:1 deleted"
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```
***
## Работа с Cash-Incomes:
### Получение Cash-Incomes
#### http://127.0.0.1:8000/api/finance_manager/cash-incomes/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "cash_incomes": [
        {
            "id": 1,
            "name": "Зарплата",
            "amount": 95000.0,
            "regular": true,
            "date": "2023-01-05"
        },
        "..."
    ]
}
```

### Получение Cash-Incomes detail
#### http://127.0.0.1:8000/api/finance_manager/cash-incomes/<id:int>/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "cash_income": {
        "id": 1,
        "name": "Зарплата",
        "amount": 95000.0,
        "regular": true,
        "date": "2023-01-05"
    }
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```

### Добавление Cash-Incomes
#### http://127.0.0.1:8000/api/finance_manager/cash-incomes/

Required: [name, amount, regular]

Authorized: True

#### Добавление нескольких записей

Request POST:
```json
{
    "cash_incomes": [
        {
            "name": "Зарплата",
            "amount": 95000,
            "regular": true,
            "date": "2023-01-05"
        },
        {
            "name": "Бизнес",
            "amount": 95000,
            "regular": true,
            "date": "2023-01-06"
        }
    ]
}
```
#### Добавление одной записи

Request POST:
```json
{
    "name": "Бизнес",
    "amount": 95000,
    "regular": true,
    "date": "2023-01-06"
}
```

Response status "201 created":
```json
{
    "detail": "cash income create"
}
```

### Изменение Cash-Income
#### http://127.0.0.1:8000/api/finance_manager/regular-expenses/<id:int>/

Required: [name, amount, regular]

Authorized: True

Request PUT:
```json
{
    "name": "Зарплата-большая",
    "amount": 260000.0,
    "regular": true,
    "date": "2023-01-05"
}
```

Response status "200 ok":
```json
{
    "detail": "cash income updated"
}
```
### Удаление Cash-Incomes
#### http://127.0.0.1:8000/api/finance_manager/cash-incomes/<id:int>/

Authorized: True

Request DELETE:
```json
```

Response status "200 ok":
```json
{
    "detail": "cash income id:1 deleted"
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```
***
## Работа с Banks:
### Получение Banks
#### http://127.0.0.1:8000/api/finance_manager/banks/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "banks": [
        {
            "id": 1,
            "name": "Яхта",
            "required_amount": 30000000.0,
            "available_amount": 500.0
        },
        "..."
    ]
}
```

### Получение Banks detail
#### http://127.0.0.1:8000/api/finance_manager/banks/<id:int>/

Authorized: True

Request GET:
```json
```

Response status "200 ok":
```json
{
    "bank": {
        "id": 1,
        "name": "Яхта",
        "required_amount": 30000000.0,
        "available_amount": 500.0
    }
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```

### Добавление Banks
#### http://127.0.0.1:8000/api/finance_manager/banks/

Required: [name, required_amount, available_amount]

Authorized: True

#### Добавление нескольких записей

Request POST:
```json
{
    "banks": [
        {
            "name": "Яхта",
            "required_amount": 30000000,
            "available_amount": 500
        },
        {
            "name": "Компьютер",
            "required_amount": 60000,
            "available_amount": 2000
        }
    ]
}
```
#### Добавление одной записи

Request POST:
```json
{
    "name": "Компьютер",
    "required_amount": 60000,
    "available_amount": 2000
}
```

Response status "201 created":
```json
{
    "detail": "banks create"
}
```

### Изменение Banks
#### http://127.0.0.1:8000/api/finance_manager/banks/<id:int>/

Required: [name, required_amount, available_amount]

Authorized: True

Request PUT:
```json
{
    "name": "Компьютер-ноутбук",
    "required_amount": 60000,
    "available_amount": 2000
}
```

Response status "200 ok":
```json
{
    "detail": "bank updated"
}
```
### Удаление Banks
#### http://127.0.0.1:8000/api/finance_manager/banks/<id:int>/

Authorized: True

Request DELETE:
```json
```

Response status "200 ok":
```json
{
    "detail": "bank id:4 deleted"
}
```

Response status "404 not found":
```json
{
    "detail": "Not found."
}
```