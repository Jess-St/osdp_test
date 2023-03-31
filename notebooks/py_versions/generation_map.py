# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: OSDP
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import plotly.express as px

# import matplotlib.pyplot as plt
import numpy as np

# import seaborn as sns; sns.set(style="ticks", color_codes=True)
import geopandas as gpd
from geopandas import GeoDataFrame
import json
import os

# %%
osdp_folder = os.environ.get("OSDP")
px.set_mapbox_access_token("pk.eyJ1IjoiamVzc2lzdCIsImEiOiJjbGZ3bmt0aWowOGNqM250YThjaHoybDJ5In0.3UL3rcO1IM_Xlr1rPiSTKA")

# %%
df = pd.read_csv(
    os.path.join(osdp_folder, "data", "BMRS", "Final", "Generation_Combined.csv"),
    parse_dates=["localDateTime", "settlementDate"],
)

# %%
df.dtypes


# %%
def animate_map(time_col):
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="commonName",
        size="quantity",
        color="fuel",
        animation_frame=time_col,
        mapbox_style="carto-positron",
        category_orders={time_col: list(np.sort(df[time_col].unique()))},
        width=800,
        height=1000,
        zoom=5,
    )
    fig.show()


animate_map(time_col="localDateTime")

# %%
fig2 = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="commonName",
    size="quantity",
    color="fuel",
    animation_frame="localDateTime",
    mapbox_style="carto-positron",
    category_orders={"localDateTime": list(np.sort(df["localDateTime"].unique()))},
    width=800,
    height=1000,
    zoom=5,
)
fig2.show()

# %%
import plotly.io as pio

pio.write_html(fig2, file="index.html", auto_open=True)
