# djangocrawler

<h3>Do you feel lucky?</h3>

This app is designed to 1) extract data about world population and poverty rates using scrapy, 2) manage the data using django models, 3) express them by means of simple rest framework and ajax-driven webpage and 4) enable a simple drawing function which (a) selects a country each time "a person" "is born", (b) draws whether this "person" lives below or above the poverty rate of $3.10/day and (c) compares this with minimal daily food cost.

<u>Disclaimer:</u>
This is not an exercise in statistics, but in scrapy and django frameworks. The accuracy of collected data relies on the methodology of World Bank and Numbeo.com. Their juxtaposition, on the other hand, is not fully correct, because the data have discrete rather than continuous character. 

<h3>Sources:</h3>

List of countries and population: http://wdi.worldbank.org/table/2.1
Minimum $ amount for daily food ration: https://www.numbeo.com/food-prices/
Poverty thresholds: http://wdi.worldbank.org/table/1.2

The $3.10 poverty index provides a better comparison (in contrast with the usual $1.90 threshold) with food prices which are generally not lower than $3.00/ration/day

<h3>Comments:</h3>

* Scrapyd server running at port 6800 is necessary to run the scrapers from the level of browser.

<h2>TODO:</h2>

* add data concerning ongoing armed conflicts
* reserve the actualization function to logged user with appropriate permission
