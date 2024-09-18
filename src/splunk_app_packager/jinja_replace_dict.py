import toml


def load_config_toml(config_path):
    config_dict = toml.load(config_path)
    return config_dict["package_config"]