import csv
import yaml
from pathlib import Path

from src.name_normalizer import NameNormalizer
from src.category_normalizer import CategoryNormalizer
from src.address_normalizer import AddressNormalizer


BASE_DIR = Path(__file__).resolve().parent.parent

def load_rules():
    config_path = BASE_DIR / "config" / "normalization_rules.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def run():
    rules = load_rules()

    name_norm = NameNormalizer(rules["name"])
    category_norm = CategoryNormalizer(rules["category"])
    address_norm = AddressNormalizer(rules["address"])

    input_path = BASE_DIR / "data" / "raw_sample.csv"
    output_path = BASE_DIR / "data" / "cleaned_sample.csv"
    report_path = BASE_DIR / "reports" / "normalization_summary.json"

    summary = {
        "total_rows": 0,
        "changed_rows": 0
    }

    with open(input_path, newline="", encoding="utf-8") as infile, \
         open(output_path, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            original = row.copy()

            row["customer_name"] = name_norm.normalize(row["customer_name"])
            row["category"] = category_norm.normalize(row["category"])
            row["address"] = address_norm.normalize(row["address"])

            writer.writerow(row)

            summary["total_rows"] += 1
            if row != original:
                summary["changed_rows"] += 1

    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        import json
        json.dump(summary, f, indent=2)

    print("Normalization completed.")
    print(summary)

if __name__ == "__main__":
    run()
