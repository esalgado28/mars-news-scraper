# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Browser setup
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Nasa Mars News
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')

    results = soup.find_all('div', class_='content_title')
    news_titles = [res.text for res in results]

    results = soup.find_all('div', class_='article_teaser_body')
    news_ps = [res.text for res in results]

    # JPL Mars Space Images - Featured Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    soup = bs(browser.html, 'html.parser')
    featured_img_url = url + soup.find('img', 'headerimage fade-in')['src']

    # Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url, header=0, index_col=0)
    df = tables[0]
    table_html = df.to_html(classes='table table-striped text-center', justify='center')

    # Mars Hemispheres
    urls = ['https://marshemispheres.com/cerberus.html',
        'https://marshemispheres.com/schiaparelli.html',
        'https://marshemispheres.com/syrtis.html',
        'https://marshemispheres.com/valles.html']

    hemisphere_image_urls = []

    for url in urls:
        browser.visit(url)
        soup = bs(browser.html, 'html.parser')
        img_url = 'https://marshemispheres.com/' + soup.find('img', 'wide-image')['src']
        title = soup.find('h2', 'title').text
        
        hemisphere_image_urls.append({"title": title, "img_url": img_url})

    browser.quit()
    
    # Put results in dictionary
    results = {
        "news_titles": news_titles,
        "news_ps": news_ps,
        "featured_img_url": featured_img_url,
        "table_html": table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    return results