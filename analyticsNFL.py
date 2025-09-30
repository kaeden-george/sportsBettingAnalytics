import numpy as np
import pandas as pd
import requests

#import the data scraper
from nfl_scraper import NFLDataScraper


#Create an instance of the NFLDataScraper class
nfl_scraper = NFLDataScraper()

#Parameters

#TODO: Check if I can actually pull 2025 stats
nfl_scraper.season = "2025"

#Get current season data
for level in ["player", "team"]:
    nfl_scraper.get_stats(level)

#get historic data

# Create a liPst of years as strings since 1970
seasons = [str(year) for year in range(1970, nfl_scraper.current_season - 1)]

# Loop through seasons and levels to retrieve historical data
for season in seasons:
    for level in ["player", "team"]:
        nfl_scraper.season = season  # Set the season for scraping
        nfl_scraper.get_stats(level)
