# Overview

The goal of this project is to analyze the influence of the USA's 2025 tariffs(that includes Liberation Day and June 2025 steel tariffs) on carbon footprint of supply chains for washing machines.
 
It will use Difference-in-Difference method, as well as the Carbon Rerouting index

# Data Cycle

## Obtaining the Data

Here is the data that I need for my project, with links to sources.

[Ember Energy](https://ember-energy.org/latest-insights/global-electricity-review-2025/major-countries-and-regions/) - main source for ton-km data.

[US Census Bureau: State Imports HS6](https://www.census.gov/foreign-trade/data/ISTHSM.html) - data on tonnage/value/origin/destination of imported goods. Contains data on specific states of destination, so the project uses it for inland imports from Mexico.

[US Census Bureau: Port HS6 Imports](https://www.census.gov/foreign-trade/data/PORTHS6MM.html) - data on tonnage/value/origin/destination of imported goods. Contains information on ports of destination, but NOT the destionation states, which makes the project use this dataset for imports from Asian countries(China/South Korea/Vietnam)

[Country list](https://www.census.gov/foreign-trade/schedules/c/country.txt) - list of country codes that the Census Bureau uses in their data.

Office of the President. Executive Order 14326, "Further Modifying the Reciprocal Tariff Rates." Federal Register, vol. 90, no. 149, 6 Aug. 2025, pp. 37963–67, www.federalregister.gov/documents/2025/08/06/2025-15010/further-modifying-the-reciprocal-tariff-rates.
 - information for tariff rates on China, Vietnam, South Korea.

## Cleaning

As usual, cleaning the data will the the most time-consuming part here. For each of two periods(Dec 2024 and Dec 2025), there were two dataframes - one for land-based imports from Mexico(using the "State Imports HS6" dataset), another for naval imports from Asian countries(using the "Port HS6 Imports") dataset. 
+ Deduplicated columns
+ converted necessary columns to numbers

For now, the carbon footprint only includes CO2 emitted by one leg of transportation(port-to-port for Asian countries, land transportation for Mexico). This will be amended later on.

## Data Processing
I began with a simple 2x2 difference-in-difference model that involves only the land-based Mexico data, which is then run through a OLS regression. 

+ Time - pick the proper start and end time in order to see the change over time. Must address the seasonality component of demand
    + Before: Dec 2024
    + After: Dec 2025
+ Treatment group: washing machines
+ Control group: TV sets/monitors

As a result, there has been no change in CO2 emissions of the supply chain. 

## Statistics Analysis
A OLS model, with DiD estimator and HC3 covariance. R²=0 for all trials, regardless of improvements to the model. Given the full pass-through of tariffs(Flaen, et al.), this can be explained by high elasticity of demand.

![alt text](image.png)
Fig. 4 - Fourth revision of the experiment. Mexico's data has been integrated into the port dataset, since port codes also describe land ports. The skew and kurtosis have increased significantly after that. Still R²=0