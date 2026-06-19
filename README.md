# Overview

The goal of this project is to analyze the influence of the USA's 2025 tariffs(that includes Liberation Day and June 2025 steel tariffs) on carbon footprint of supply chains for washing machines.
 
It will use Difference-in-Difference method, as well as the Carbon Rerouting index

# Data Cycle

## Obtaining the Data

Here is the data that I need for my project, with links to sources.

[https://comtradeplus.un.org/](https://comtradeplus.un.org/) - ~~United Nations' international trade database~~ not used.

[Ember Energy](https://ember-energy.org/latest-insights/global-electricity-review-2025/major-countries-and-regions/) - main source for ton-km data.

[US Census Bureau: State Imports HS6](https://www.census.gov/foreign-trade/data/ISTHSM.html) - data on tonnage/value/origin/destination of imported goods. Contains data on specific states of destination, so the project uses it for inland imports from Mexico.

[US Census Bureau: Port HS6 Imports](https://www.census.gov/foreign-trade/data/PORTHS6MM.html) - data on tonnage/value/origin/destination of imported goods. Contains information on ports of destination, but NOT the destionation states, which makes the project use this dataset for imports from Asian countries(India/China/South Korea/Vietnam)

[Country list](https://www.census.gov/foreign-trade/schedules/c/country.txt) - list of country codes that the Census Bureau uses in their data.

## Cleaning

As usual, cleaning the data will the the most time-consuming part here. For each of two periods(Dec 2024 and Dec 2025), there were two dataframes - one for land-based imports from Mexico(using the "State Imports HS6" dataset), another for naval imports from Asian countries(using the "Port HS6 Imports") dataset. 
+ Deduplicated columns
+ converted necessary columns to numbers

## Data Processing
I began with a simple 2x2 difference-in-difference model, which is then run through a OLS regression. 

+ Time - pick the proper start and end time in order to see the change over time. Must address the seasonality component of demand
    + Before: Dec 2024
    + After: Dec 2025
+ Treatment group: washing machines
+ Control group: TV sets/monitors

