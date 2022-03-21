# Mission to Mars
Eddy's folder for web scraping homework.

## Background
In this assignment, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following sites are scraped:
- [Mars News Site](https://redplanetscience.com/)
- [JPL Space Images](https://spaceimages-mars.com)
- [Mars Facts](https://galaxyfacts-mars.com)
- [Mars Hemispheres](https://marshemispheres.com/)

## Part 1
Initial scraping is done using Jupyter Notebook along with the BeautifulSoup, Pandas, and Splinter libraries. This code can be found in *mission_to_mars.ipynb*

## Part 2
The code from the Jupyter notebook is converted to a python script *scrape_mars.py* which defines a function that scrapes the websites and returns the data as a dictionary. Then, using MongoDB and Flask templating, an HTML page is created that displays the scraped data.
