from config_loader import load_config
from extractor import extract_data_from_config
from writer import write_output


if __name__ == "__main__":
    config = load_config("config/scraper_config.yaml")

    data = extract_data_from_config(config)
    write_output(data, config["output"])

    print(f"Saved {len(data)} records to {config['output']['path']}")
