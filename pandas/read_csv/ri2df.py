#!/usr/bin/env python3

import pandas as pd
import numpy as np


def ri2df(PATH_csv):
    df = pd.read_csv(PATH_csv, skip_blank_lines=False)

    ind_row_arr, _ = np.where(pd.isnull(df))

    if ind_row_arr.size == 0:
        df["k"] = 0.0
        df["wl"] *= 1000
    else:
        ind_row = ind_row_arr[0]

        df_n = df.iloc[:ind_row, :]
        df_n = df_n.astype("float")

        df_k = df.iloc[(ind_row + 2) :, :]
        df_k = df_k.astype("float")
        df_k.columns = ["wl", "k"]

        df = df_n.merge(df_k, how="left", on="wl")
        df["wl"] *= 1000

    return df


if __name__ == "__main__":
    # From https://refractiveindex.info/

    df = ri2df("./Ghosh-o.csv")
    print(df)
    df = ri2df("./Johnson.csv")
    print(df)
