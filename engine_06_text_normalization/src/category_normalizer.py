from .base_normalizer import BaseTextNormalizer

class CategoryNormalizer(BaseTextNormalizer):
    def normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return text

        text = super().normalize(text)

        mapping = self.rules.get("mapping", {})
        text_key = text.upper().strip()

        if text_key in mapping:
            return mapping[text_key]

        return text
