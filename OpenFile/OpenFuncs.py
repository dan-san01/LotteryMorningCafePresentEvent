import json

def openConfig():
    config_path = 'config/config.json'
    with open(config_path) as f:
        config_dir = json.load(f)
    return config_dir


if __name__ == "__main__":
    print(openConfig())