# CIMEIKA RESOURCE MOUNT — CORE EDITION

## 1. Призначення

Єдиний консолідований документ, що описує:

- монтаж Cimeika Core API;
- прив’язку зовнішніх сервісів;
- структуру 7 модулів;
- джерела даних;
- зв’язок із доменом `cimeika.com.ua`.

Це — головний ресурс для розгортання ядра Cimeika на GitHub, Hugging Face та OpenAI Apps.

---

## 2. API ENTRY CONFIG

```yaml
CIMEIKA_API_MOUNT:
  version: "0.1.0"
  description: "Базовий монтаж Cimeika Core API"

  gateway:
    primary: "${CIMEIKA_API_BASE_URL:-https://ihorog-cimeika-core.hf.space}"
    mode: "direct"

  healthcheck:
    enabled: true
    interval_sec: 10
    endpoints:
      - "/health"
```

---

## 3. MODULE MAP (7 MODULES)

```yaml
modules:
  ci:
    route: "/ci"
    description: "Центральне сенсове ядро"

  kazkar:
    route: "/kazkar"
    description: "Пам'ять, архіви, легенди, досвід"

  malya:
    route: "/malya"
    description: "Творчість, ідеї, інновації"

  nastrij:
    route: "/nastrij"
    description: "Стан, емоційна основа"

  podia:
    route: "/podia"
    description: "Події, майбутнє, прогнози"

  gallery:
    route: "/gallery"
    description: "Візуальні архіви, слайдери, історії"

  calendar:
    route: "/calendar"
    description: "Час, ритми, вузли, хронос"
```

---

## 4. DATA SOURCES

```yaml
data_sources:
  media_repo: "https://github.com/Ihorog/media"
  core_repo: "https://github.com/Ihorog/cimeika"
  api_repo: "https://github.com/Ihorog/cimeika-core-api"
  realtime_repo: "https://github.com/Ihorog/cimeika-real-time-data-app"

  huggingface:
    core_api: "https://huggingface.co/spaces/Ihorog/cimeika-core-api"
```

---

## 5. SITE MOUNT (ПОДАЛІ)

```yaml
site:
  domain: "https://cimeika.com.ua"
  frontend_framework: "Next.js"
  api_base: "${CIMEIKA_API_BASE_URL}"
  chatgpt_app_support: true
```

---

## 6. SSOT

```yaml
SSOT:
  id: "cimeika_core_api_mount_0_1"
  description: "Офіційна схема монтажу Cimeika Core API"
  repo: "https://github.com/Ihorog/cimeika-core-api"
```
