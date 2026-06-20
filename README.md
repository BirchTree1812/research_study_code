# Overview

The goal of this project is to analyze the influence of the USA's 2025 tariffs(that includes Liberation Day and June 2025 steel tariffs) on carbon footprint of supply chains for washing machines.
 
It will use Difference-in-Difference method, as well as the Carbon Rerouting index

# Data Cycle

## Obtaining the Data

Here is the data that I need for my project, with links to sources.

[https://comtradeplus.un.org/](https://comtradeplus.un.org/) - ~~United Nations' international trade database~~ not used, as US Census Bureau is a more comprehensive source for all the necessary data(see below). May be used for a sanity check later on.

[Ember Energy](https://ember-energy.org/latest-insights/global-electricity-review-2025/major-countries-and-regions/) - main source for ton-km data.

[US Census Bureau: State Imports HS6](https://www.census.gov/foreign-trade/data/ISTHSM.html) - data on tonnage/value/origin/destination of imported goods. Contains data on specific states of destination, so the project uses it for inland imports from Mexico.

[US Census Bureau: Port HS6 Imports](https://www.census.gov/foreign-trade/data/PORTHS6MM.html) - data on tonnage/value/origin/destination of imported goods. Contains information on ports of destination, but NOT the destionation states, which makes the project use this dataset for imports from Asian countries(India/China/South Korea/Vietnam)

[Country list](https://www.census.gov/foreign-trade/schedules/c/country.txt) - list of country codes that the Census Bureau uses in their data.

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

First, we must assemble an econometric model.

Let us start with a basic 2x2 regression equation:

$$Y_i = \alpha + \beta*ifTariffShock\_c*\delta*PostTariff\_t+\gamma*(ifTariffShock*PostTariff)+\epsilon_i$$

+ $Y_i$ represents grams of CO2 emissions of supply chains of imports from a particular country $c$ at a certain time $t$
+ ifTariffShock_c is a boolean that represents if a country has been affected by the tariff shock. 1 if it is, 0 if not.
+ PostTariff_t is a boolean that represents if the observation takes place before or after the tariff. 0 if the date is Dec 2024, 1 if it's Dec 2025
+ $\gamma$ is the difference-in-differences estimator.

For the model, we need the following assumptions:
+ Parallel trends
    + Flaaen, Hortaçsu & Tintelnot (2020) did this by comparing the trends of the treatment group(washing machines) with the control group(refrigerators, dishwashes and other un-tariffed appliances) before the tariffs.
    + We do this because we cannot see what the countries would've done WITHOUT tariffs. However, we CAN test whether these groups moved in parallel before the tariff.
    + Pre-trend plot necessary to demonstrate it?
+ Anticipation
    + Expectations shape economics. If the importers already knew that the tariffs would've happened, this would've influenced their behavior compared to if they didn't know about the tariffs beforehand.
    + Announcements come many weeks before the actual tariff, as evidenced by Freund et al. (2024). 
+ Error correlates over time within a country
    + How do we address that?
+ Seasonality
    + We assume that washing machine demand is affected by seasons. To avoid the error caused by that, we compare the same month of a different year(Dec 2024 and Dec 2025) respectively. 
    + The announcement date for Liberation Day Tariffs was Feb 13th 2025, so this covers the "anticipation" assumption
+ Semiconductor tariff exception for TV sets is valid
    + While the language around the tariff exception for semiconductors doesn't clarify(rewrite? how exactly is the ambiguity problematic?) the status of TV sets, we assume that they fall under that exemption, and that every party in the supply chain of TVs recognizes that.