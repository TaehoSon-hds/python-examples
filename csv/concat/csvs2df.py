#!/usr/bin/env python3

import pandas as pd
import os
import glob


def csvs2df(PATH_root, element):
    PATH_csv = os.path.join(PATH_root, "{}/".format(element))
    csv_list = glob.glob(PATH_csv + "*.csv")

    csv_sorted_list = sorted(
        csv_list, key=lambda csv: int(csv.split("_")[-1].split(".")[0])
    )

    df = pd.concat(map(pd.read_csv, csv_sorted_list), ignore_index=True)
    return df


if __name__ == "__main__":
    df = csvs2df("./", "C")
    print(df)
