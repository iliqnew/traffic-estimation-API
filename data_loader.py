from functools import reduce


import polars as pl


def get_opportunity_data(
    country: str | None, browser: str | None, platform: str | None, vertical: str | None
) -> dict:
    null_values = ["", "n/a"]

    countries_df = (
        pl.read_csv("data/countries.csv", null_values=null_values)
        .filter(pl.col("country") == country if country else True)
        .sum()
    )

    browsers_df = (
        pl.read_csv("data/browsername.csv", null_values=null_values)
        .filter(pl.col("browsername") == browser if browser else True)
        .sum()
    )

    platforms_df = (
        pl.read_csv("data/platformname.csv", null_values=null_values)
        .filter(pl.col("platformname") == platform if platform else True)
        .sum()
    )

    verticals_df = (
        pl.read_csv("data/vertical.csv", null_values=null_values)
        .filter(pl.col("publishernewthematic") == vertical if vertical else True)
        .sum()
    )

    return (
        countries_df["opps"][0]
        * browsers_df["opps"][0]
        * platforms_df["opps"][0]
        * verticals_df["opps"][0]
    )
