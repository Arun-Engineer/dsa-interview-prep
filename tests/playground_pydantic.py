from pydantic import ValidationError
from app.models import SupportAnswer

# Experiment 1: valid data
good = SupportAnswer(answer = "Delivery takes 10-20 minutes.", confidence = 0.9, needs_human = False)
print("1: ", good)
print("1 field: ", good.confidence)

# Experiment 2: Confidence out of range
try:
    SupportAnswer(answer = "Hi", confidence = 1.5, needs_human = False)
except ValidationError as error:
    print("2: ", error)

# Experiment 3: missing field
try:
    SupportAnswer(answer = "Hi", confidence = 1.5, needs_human = False)
except ValidationError as error:
    print("3: ", error)

# Experiment 4: from a JSON string(this is what the LLM will send us in Block 3)
json_text = '{"answer": "Refunds take 3-5 days.", "confidence": 0.8, "needs_human": false}'
parsed = SupportAnswer.model_validate_json(json_text)
print("4: ", parsed.answer)

# Experiment 5: back to a plain dict
print("5: ", parsed.model_dump())

# Experiment 6: Confidence = "0.8" written as text in quotes it falls under lax mode so pydantic converts it into 0.8 then verifies and passes
try:
    SupportAnswer(answer = "Hi", confidence = "0.8", needs_human = False)
except ValidationError as error:
    print("2: ", error)

# Experiment 7: a JSON string where "answer" is missing
try:
    json_text = '{"confidence": 0.8, "needs_human": false}'
    parsed = SupportAnswer.model_validate_json(json_text)
    print("4: ", parsed.answer)
except ValidationError as error:
    print("7: ", error)