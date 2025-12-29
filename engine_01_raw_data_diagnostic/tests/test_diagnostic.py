import pytest
import pandas as pd
from src.loader import load_csv
from src.scan_missing import scan_missing
from src.scan_duplicates import scan_duplicates
from src.scan_format import scan_format
from src.scan_schema import scan_schema
import yaml

def test_loader():
    df = load_csv("../data/sample_dirty.csv")
    assert not df.empty

def test_scan_missing():
    df = load_csv("../data/sample_dirty.csv")
    with open("../config/diagnostic_rules.yaml") as f:
        config = yaml.safe_load(f)
    missing = scan_missing(df, config)
    assert isinstance(missing, dict)

def test_scan_duplicates():
    df = load_csv("../data/sample_dirty.csv")
    dup = scan_duplicates(df)
    assert "exact_duplicates_count" in dup

def test_scan_format():
    df = load_csv("../data/sample_dirty.csv")
    with open("../config/diagnostic_rules.yaml") as f:
        config = yaml.safe_load(f)
    fmt = scan_format(df, config)
    assert isinstance(fmt, dict)

def test_scan_schema():
    df = load_csv("../data/sample_dirty.csv")
    schema = scan_schema(df, df.columns.tolist())
    assert "total_columns_expected" in schema
