# tests/test_cold_rebuild.py

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

def test_chat_fake_llm_cold():
    response = client.post("/chat", json = {"question": "where is my order?"})
    assert response.status_code == 200
    assert response.json()["answer"] == "Cold fake"

# i have written these lines but now my question is how these fake functions pass to main and then to real llm_client functions and how the answer is show cased here
# based on this fake call answers?
# to be more specific which line calls with file and once again which file calls the llm_client and uses these pytest functions?