import pandas as pd
import yaml

from validator_missing import validate_missing
from validator_schema import validate_schema

# Load data
df = pd.read_csv("../data/sample_test.csv")

# Load validation rules
with open("../config/validation_rules.yaml", "r") as f:
    rules = yaml.safe_load(f)

# Run validators
missing_result = validate_missing(df, rules["missing_value"])
schema_result = validate_schema(df, rules["schema"])

print("=== MISSING VALIDATION RESULT ===")
print(missing_result)

print("\n=== SCHEMA VALIDATION RESULT ===")
print(schema_result)
