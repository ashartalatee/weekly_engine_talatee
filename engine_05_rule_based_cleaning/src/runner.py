import pandas as pd
from rule_loader import load_rules
from dispatcher import dispatch_cleaning


def run_cleaning(
    input_path: str,
    output_path: str,
    rule_path: str
):
    # Load rules
    rules = load_rules(rule_path)
    columns_rules = rules["columns"]

    # Load data
    df = pd.read_csv(input_path)

    # Apply cleaning per column
    for col_name, col_rule in columns_rules.items():
        if col_name not in df.columns:
            raise ValueError(f"Column '{col_name}' not found in dataset")

        column_type = col_rule["type"]
        actions = col_rule["actions"]

        df[col_name] = dispatch_cleaning(
            df[col_name],
            column_type,
            actions
        )

    # Save output
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    run_cleaning(
        input_path="data/sample_dirty.csv",
        output_path="output/cleaned_sample.csv",
        rule_path="config/cleaning_rules.yaml"
    )
