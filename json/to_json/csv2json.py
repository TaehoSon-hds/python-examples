#!/usr/bin/env python3
import pandas as pd
import os


def csv2json(PATH_file, name):
    PATH_csv = os.path.join(PATH_file, "{}.csv".format(name))
    PATH_json = os.path.join(PATH_file, "{}.json".format(name))

    df = pd.read_csv(PATH_csv)
    result = df.to_json(PATH_json, orient="records", indent=2)

    return result


if __name__ == "__main__":
    csv2json("./", "SiO2")
