# Boats_Project_repo

## Business problem
The goal of the project was to scrape, mine and analyse information about various boats available for sale online. Using this information we could determine the most popular boat features, boat models and boat type. Finally, looking at it from the customers perspective, the goal was to look at the prices ranges for various boats and try to make a regression model which could predict the boat price from these features.

## Data source
This is a standalone dataset collected by scraping the boat24.com website using Scrapy. The code for the web scraper is avaliable here, as well as the original csv file of the data.

## Data description
The original data contains the following columns:
* **Year Built** - The year in which the boat was built
* **Condition** - The condition of the boat at the time of sale
* **Length x Width** - Both the length and the width of the boat in meters. This was later transformed into two seperate columns
* **Material** - The material which the boat is made of
* **Certified No. of Persons** - The number of persons for which the boat is registered
* **No. of Cabins** - The total number of sleeping cabins in the boat
* **Propulsion** - The propulsion of the boat, not to be confused with the engine
* **Engine** - The engine brand in the boat
* **Engine Performance** - The power of the boat's engine, defined as horsepower
* **Engine Hours** - The number of hours made by the engine, though this columns was dropped due to hue % of null values
* **Model** - The brand of the boat, typically the manifacturer
* **Type** - The boat type, such as a sailing yacht or a motor yacht
* **Location** - The location of the boat the the moment. Originally this column contained the regions and subregions as well but only the countries were used in the final data
* **Price** - The boat's price in british pounds
