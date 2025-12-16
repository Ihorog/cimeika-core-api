# CIMEIKA_API_CORE · Cimeika Core API (FastAPI)

## 1. Призначення

Cimeika Core API — чисте ядро Cimeika, яке надає:

- системні ендпоінти (`/`, `/health`);
- статусні ендпоінти 7 модулів (ci, kazkar, malya, nastrij, podia, gallery, calendar);
- базовий чат `/api/chat` як точку підключення до подальшої логіки Ci / GPT.

Цей API використовується як:

- бекенд для Hugging Face Space `cimeika-core-api`;
- точка входу для OpenAI Apps SDK / інструментів;
- основа для майбутнього сайту `cimeika.com.ua`.

---

## 2. Ендпоінти

- `GET /` — статус ядра, перелік модулів, список ключових шляхів.
- `GET /health` — простий healthcheck (для моніторингу / HF).
- `GET /ci` — статус модуля Ci.
- `GET /kazkar` — статус модуля Казкар.
- `GET /malya` — статус модуля Маля.
- `GET /nastrij` — статус модуля Настрій.
- `GET /podia` — статус модуля ПоДія.
- `GET /gallery` — статус модуля Галерея.
- `GET /calendar` — статус модуля Календар.
- `POST /api/chat` — базовий чат (echo) з параметром `persona`.

---

## 3. Формат `/api/chat`

### Запит

```json
{
  "persona": "ci",
  "messages": [
    { "role": "user", "content": "Привіт, Ci." }
  ]
}
