# test_api.py
# Run this while uvicorn is running in another terminal

import urllib.request
import json


def call_api(payload: dict) -> dict:
    """Send a POST request to the preprocessing API."""
    url  = "http://localhost:8000/api/preprocess"
    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def print_result(label: str, result: dict):
    print(f"\n{'═' * 50}")
    print(f"  {label}")
    print(f"{'═' * 50}")
    print(f"  Steps  : {' → '.join(result['steps_applied'])}")
    print(f"  Result : {result['result']}")


# ── Test 1: English ───────────────────────────────────────
print_result("English — Full Pipeline", call_api({
    "text":             "The students are running quickly to school",
    "language":        "english",
    "remove_stopwords": True,
    "lemmatize":       True,
    "stemming":        False,
}))

# ── Test 2: Arabic ────────────────────────────────────────
print_result("Arabic — Full Pipeline", call_api({
    "text":             "الْبِنْتُ الجمـــيلة كتَبَتْ رِسَالةً",
    "language":        "arabic",
    "remove_tashkeel": True,
    "normalize":       True,
    "remove_stopwords": True,
    "stemming":        True,
}))

# ── Test 3: Stemming only ─────────────────────────────────
print_result("English — Stemming Only", call_api({
    "text":      "The children are running and swimming",
    "language": "english",
    "stemming":  True,
    "lemmatize": False,
}))

print("\n✅ All API tests passed!")