import re
from .base_normalizer import BaseTextNormalizer

class NameNormalizer(BaseTextNormalizer):
    def normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return text

        text = super().normalize(text)

        # Remove numbers if configured
        if self.rules.get("remove_numbers"):
            text = re.sub(r"\d+", "", text)

        # Remove extra symbols
        if self.rules.get("remove_extra_symbols"):
            text = re.sub(r"[^\w\s]", "", text)

        # Remove blocked words
        blocked = self.rules.get("blocked_words", [])
        for word in blocked:
            text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)

        # Title case if configured
        if self.rules.get("title_case"):
            text = text.title()

        return text.strip()
