import os

import yaml


def data(name):

    with open(os.getcwd() + os.sep + "../data" + os.sep + name, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
