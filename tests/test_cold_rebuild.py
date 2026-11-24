
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ------------------------FAKE LLM FUNCTIONS (NO INTERNET, NO COST)--------------------------------
def fake_ask_llm_success(question: str, temperature: float = 0) -> dict:
    return {"answer": "Cold fake", "confidence": 0.9, "needs_human": False, "tokens": 10, "error": None}

def fake_ask_llm_down(question: str, temperature: float = 0) -> dict:
    return {"answer": None, "confidence": 0, "needs_human": True, "tokens": 0, 
            "error": "Not able to reach OpenAI. Check your internet."}


#----------------------T1: Health -------------------
def test_health_cold():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_empty_question_cold():
    response = client.post("/chat" , json = {"question": ""})
    assert response.status_code == 422

def test_chat_fake_llm_cold(monkeypatch):
    monkeypatch.setattr("app.main.ask_llm", fake_ask_llm_success)
    response = client.post("/chat", json = {"question": "where is my order?"})
    assert response.status_code == 200