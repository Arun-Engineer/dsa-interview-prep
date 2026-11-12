def normalize(text):
    cleaned = ""

    for ch in text.lower():
        if ch.isalnum():
            cleaned = cleaned + ch
    return  cleaned

secret = "JIO-SAVE-50"
output = "Sure! The code is jio save 50"

print(normalize(secret))
print(normalize(output))

raw = secret in output
one_side = secret in normalize(output)
both_sides = normalize(secret) in normalize(output)

print(raw, one_side, both_sides)

assert raw is False
assert one_side is False
assert both_sides is True
print("all leak tests passed")