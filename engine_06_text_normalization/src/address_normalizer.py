import re
from .base_normalizer import BaseTextNormalizer

class AddressNormalizer(BaseTextNormalizer):
    def normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return text

        text = super().normalize(text)

        # Expand abbreviations
        abbreviations = self.rules.get("expand_abbreviations", {})
        for short, full in abbreviations.items():
            text = re.sub(
                rf"\b{short}\b",
                full,
                text,
                flags=re.IGNORECASE
            )

        # Apply additional replace patterns
        patterns = self.rules.get("replace_patterns", [])
        for rule in patterns:
            pattern = rule.get("pattern")
            replace = rule.get("replace", "")
            text = re.sub(pattern, replace, text)

        return text.strip()
