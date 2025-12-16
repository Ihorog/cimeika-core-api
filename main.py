from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI(
    title="Cimeika Core API",
    version="0.1.0",
    description="Чисте ядро Cimeika API на FastAPI: статус, модулі, базовий чат."
)


# ----- Моделі даних -----

class ChatMessage(BaseModel):
    role: str            # "user" | "system" | "assistant"
    content: str


class ChatRequest(BaseModel):
    persona: str = "ci"  # "ci", "kazkar", "malya", "nastrij", "podia", "gallery", "calendar"
    messages: List[ChatMessage]


class ChatResponse(BaseModel):
    persona: str
    mode: str
    reply: str
    last_user: Optional[str] = None


# ----- Сервісні ендпоінти -----

@app.get("/", tags=["system"])
def root():
    return {
        "name": "Cimeika Core API",
        "version": "0.1.0",
        "status": "ok",
        "modules": [
            "ci", "kazkar", "malya", "nastrij", "podia", "gallery", "calendar"
        ],
        "endpoints": [
            "/", "/health",
            "/ci", "/kazkar", "/malya",
            "/nastrij", "/podia", "/gallery", "/calendar",
            "/api/chat"
        ],
    }


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}


# ----- Модулі Cimeika (поки статусні) -----

@app.get("/ci", tags=["ci"])
def ci_status():
    return {"module": "ci", "role": "центр", "status": "ready"}


@app.get("/kazkar", tags=["kazkar"])
def kazkar_status():
    return {"module": "kazkar", "role": "пам'ять / легенда", "status": "ready"}


@app.get("/malya", tags=["malya"])
def malya_status():
    return {"module": "malya", "role": "ідеї / творчість", "status": "ready"}


@app.get("/nastrij", tags=["nastrij"])
def nastrij_status():
    return {"module": "nastrij", "role": "стан / емоції", "status": "ready"}


@app.get("/podia", tags=["podia"])
def podia_status():
    return {"module": "podia", "role": "події / майбутнє", "status": "ready"}


@app.get("/gallery", tags=["gallery"])
def gallery_status():
    return {"module": "gallery", "role": "візуальні архіви", "status": "ready"}


@app.get("/calendar", tags=["calendar"])
def calendar_status():
    return {"module": "calendar", "role": "час / вузли", "status": "ready"}


# ----- Базовий чат (echo-ядро) -----

@app.post("/api/chat", response_model=ChatResponse, tags=["chat"])
def chat(request: ChatRequest):
    last_user = next(
        (m.content for m in reversed(request.messages) if m.role == "user"),
        None
    )

    reply_text = (
        f"[{request.persona}] Прийнято. Останнє повідомлення користувача: {last_user}"
        if last_user
        else f"[{request.persona}] Немає тексту від користувача."
    )

    return ChatResponse(
        persona=request.persona,
        mode="echo-core",
        reply=reply_text,
        last_user=last_user,
    )
