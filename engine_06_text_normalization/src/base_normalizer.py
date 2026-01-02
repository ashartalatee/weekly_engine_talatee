import re

class BaseTextNormalizer:
    def __init__(self, rules: dict):
        self.rules = rules

    def apply_basic_rules(self, text: str) -> str:
        if not isinstance(text, str):
            return text
        
        if self.rules.get("trim_whitespace"):
            text = text.strip()

        if self.rules.get("collapse_spaces"):
            text = re.sub(r"\s+", " ", text)

        if self.rules.get("lowercase"):
            text = text.lower()

        if self.rules.get("uppercase"):
            text = text.upper()

        return text
    
    def apply_replace_patterns(self, text: str) -> str:
        patterns = self.rules.get("replace_patterns", [])
        for rule in patterns:
            pattern = rule.get("pattern")
            replace = rule.get("replace", "")
            text = re.sub(pattern, replace, text)
        return text
    
    def normalize(self, text: str) -> str:
        if not isinstance(text, str):
            return text
        
        text = self.apply_basic_rules(text)
        text = self.apply_replace_patterns(text)

        return text