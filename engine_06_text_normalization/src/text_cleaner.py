from .base_normalizer import BaseTextNormalizer

def normalize_text(text: str, rules: dict) -> str:
    normalizer = BaseTextNormalizer(rules)
    return normalizer.normalize(text)
