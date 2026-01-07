# examples/public_api_case.py

import json
from src.runner import run_engine

if __name__ == "__main__":
    data = run_engine(
        api_config_path="config/api_config.yaml",
        pagination_config_path="config/pagination_rules.yaml",
        fields=["id", "title"]
    )

    with open("data/sample_output.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"Fetched {len(data)} records")
