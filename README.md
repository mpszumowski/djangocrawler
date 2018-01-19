# djangocrawler

<h3>Do you feel lucky?</h3>

http://mpszumowski.pythonanywhere.com/index.html

A django-rest app which gathers and updates data via scrapy framework

<h3>How does it work?</h3>

This app is designed to 1) extract data about world population and poverty rates using scrapy, 2) manage the data using django models, 3) express them by means of simple rest framework and ajax-driven webpage and 4) enable a simple drawing function which (a) selects a country each time "a person" "is born", (b) draws whether this "person" lives below or above the poverty rate of $3.10/day and (c) compares this with minimal daily food cost.

[screenshot](https://github.com/mpszumowski/djangocrawler/blob/master/screens/Screenshot.jpg)

The button at the top-left edge of the page draws a random country in the world based on its population. The marker highlights yellow if the data is incomplete, blue if it hit the segment of population above - and red if below the threshold of $3.10/day. If the daily food cost is higher than $3.10 the random function works normally, but if it is lower, there is a modificator introduced to lower the probability of finding oneself in the starving part of population.

In a word, the marker indicates whether you surely starve. If it turns blue it is still probable that the whole of your budget would be spent on food if you chose to eat the minimal 2,400kcal ration, but it is indeterminable by the nature of scraped data.

<b><u>Disclaimer:</u></b>
This is not an exercise in statistics, but in scrapy and django frameworks. The accuracy of collected data relies on the methodology of World Bank and Numbeo.com. Their juxtaposition, on the other hand, is not fully correct, because the data have discrete rather than continuous character.


<h3>Sources:</h3>

List of countries and population: http://wdi.worldbank.org/table/2.1 <br>
Minimum $ amount for daily food ration: https://www.numbeo.com/food-prices/ <br>
Poverty thresholds: http://wdi.worldbank.org/table/1.2 <br>

The $3.10 poverty index provides a better comparison (in contrast with the usual $1.90 threshold) with food prices which are generally not lower than $3.00/ration/day

<h3>Implementation:</h3>

* ./manage.py runserver --> open index.html
* Scrapyd server running at port 6800 is necessary to run the scrapers from the level of browser.

<h2>TODO:</h2>

* add data concerning ongoing armed conflicts
* reserve the actualization function to logged user with appropriate permission
