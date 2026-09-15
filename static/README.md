# REST.NEXUS

Готовый тёмный футуристичный интерфейс для работы с REST API.

## Запуск

Просто открой `index.html` в браузере или раздай папку через любой статический сервер.

## Подключение своего API

Открой `script.js` и измени:

```js
const API_BASE = "https://jsonplaceholder.typicode.com/users";
```

на endpoint своего API, например:

```js
const API_BASE = "https://api.example.com/users";
```

Страницы:
- `get.html` — GET
- `post.html` — POST
- `put.html` — PUT
- `patch.html` — PATCH
- `delete.html` — DELETE

По умолчанию используется JSONPlaceholder как безопасный демонстрационный API. Для собственного backend убедись, что сервер разрешает CORS-запросы из браузера.
