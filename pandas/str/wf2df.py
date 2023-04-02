#!/usr/bin/env python3
import pandas as pd
import requests
from dateutil import parser
from bs4 import BeautifulSoup


def wf2df(area):
    session = requests.Session()
    url = "https://www.windfinder.com/forecast/" + area
    req = session.get(url)
    bsObj = BeautifulSoup(req.content, "html.parser")

    bs_date = bsObj.findAll("h3", {"class": "weathertable__headline"})
    bs_time = bsObj.findAll("div", {"class": "cell-timespan"})
    bs_windspeed = bsObj.findAll("div", {"class": "speed"})
    bs_winddir = bsObj.findAll("span", {"class": "units-wd-deg"})
    bs_waveheight = bsObj.findAll("div", {"class": "data-waveheight"})
    bs_wavedir = bsObj.findAll("span", {"class": "units-wad-deg"})
    bs_waveperiod = bsObj.findAll("div", {"class": "data-wavefreq"})

    f = lambda x: x.get_text().strip()

    times = list(map(f, bs_time))
    dates = sorted(len(set(times)) * list(map(parser.parse, map(f, bs_date))))
    wind_speed = map(f, bs_windspeed)
    wind_dir = map(f, bs_winddir)
    wave_height = map(f, bs_waveheight)
    wave_dir = map(f, bs_wavedir)
    wave_period = map(f, bs_waveperiod)

    df = pd.DataFrame(
        {
            "Local_date": dates[: len(times)],
            "Local_time": times,
            "Wind_speed": wind_speed,
            "Wind_direction": wind_dir,
            "Wave_height": wave_height,
            "Wave_direction": wave_dir,
            "Wave_period": wave_period,
        }
    )
    # print(df)

    df["Wind_direction"] = df["Wind_direction"].str.replace("°", "").astype(int)
    df["Wave_direction"] = df["Wave_direction"].str.replace("°", "").astype(int)
    df["Local_time"] = df["Local_time"].str.replace("h", "").astype(int)
    df["Wave_height"] = df["Wave_height"].str.replace("m", "").astype(float)
    df["Wind_speed"] = df["Wind_speed"].str.replace("kts", "").astype(int)
    df["Wave_period"] = df["Wave_period"].str.replace("s", "").astype(int)

    return df


if __name__ == "__main__":
    df = wf2df("Jeju")
    print(df)
