from pathlib import Path

from src.loader.config_loader import load_config
from src.excel.excel_reader import extract_data

# ==========================================
# 1. PROJECT PATHS
# ==========================================
# Get root directory of project
PROJECT_ROOT = Path(__file__).resolve().parent

# Configuration file
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"


def main():
    # Load YAML instructions
    config = load_config(path=CONFIG_PATH)

    # Resolve file paths
    excel_path = PROJECT_ROOT / config['files']['excel']
    powerpoint_path = PROJECT_ROOT / config['files']['powerpoint']
    output_path = PROJECT_ROOT / config['files']['output']

    # Go over instructions
    for operation in config['operations']:
        
        # Get excel instructions
        source = operation['source']

        # Extract data
        data = extract_data(file_path=excel_path, sheet_name=source['sheet'], cell_range=source['range'])

        for d in data:
            print(d)


# Call main
main()