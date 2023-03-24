#!/usr/bin/env python3

import pandas as pd
import json

def spectrum2df(PATH_json):
    with open(PATH_json, 'r') as f:
        initial_json = json.load(f)

    df = pd.json_normalize(initial_json)
    df.columns = ['val', 'a', 'p', 'w', 'o']

    return df

if __name__ == "__main__":
    df = spectrum2df('./spectrum.json')
    print (df)
