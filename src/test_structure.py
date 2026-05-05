

import sys
import os

# Make sure Python finds our modules
sys.path.insert(0, os.path.dirname(__file__))

from src.services.pipeline_service import run_pipeline


def print_result(label: str, result: dict):
    print(f"\n{'═' * 50}")
    print(f"  {label}")
    print(f"{'═' * 50}")
    if "error" in result:
        print(f"  ❌ {result['error']}")
    else:
        print(f"  Steps  : {' → '.join(result['steps_applied'])}")
        print(f"  Result : {result['result']}")


# English test
print_result("English Pipeline", run_pipeline({
    "text":             "The students are running quickly to school",
    "language":        "english",
    "remove_stopwords": True,
    "lemmatize":       True,
}))

# Arabic test
print_result("Arabic Pipeline", run_pipeline({
    "text":             "الْبِنْتُ الجمـــيلة كتَبَتْ رِسَالةً",
    "language":        "arabic",
    "remove_tashkeel": True,
    "normalize":       True,
    "remove_stopwords": True,
    "stemming":        True,
}))

# Mismatch test
print_result("Mismatch Error", run_pipeline({
    "text":     "مرحبا بالعالم",
    "language": "english",
}))

print("\n✅ All imports and pipeline calls succeeded!")