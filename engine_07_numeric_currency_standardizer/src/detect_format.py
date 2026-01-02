import re

def detect_numeric_format(value: str) -> str:
    if value is None:
        return "INVALID_OR_MISSING"
    
    value = str(value).strip()

    if value == "" or value.upper() in {"N/A", "NA", "NULL"}:
        return "INVALID_OR_MISSING"
    
    if re.match(r"^\(.*\)$", value):
        return "ACCOUNTING_NEGATIVE"
    
    if "%" in value:
        return "PERCENTAGE"
    
    if re.search(r"[KMB]$", value, re.IGNORECASE):
        return "MULTIPLIER_FORMAT"
    
    if re.search(r"[A-Za-z]{2,}", value):
        return "CURRENCY_OR_TEXT"
    
    if "," in value and "." in value:
        if value.find(",") < value.find("."):
            return "US_FORMAT"
        else:
            return "eu_separator"
        
    if " " in value and "," in value:
        return "SPACE_SEPARATOR"
        
    if "," in value:
        return "COMMA_SEPARATOR"
        
    if "." in value:
        return "DOT_SEPARATOR"
        
    return "PLAIN_NUMBER"