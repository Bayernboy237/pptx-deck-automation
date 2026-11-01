import yaml

# Returns yaml file
def load_config(path):
    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config