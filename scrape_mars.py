#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser

    #go to url 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    #scrape news titles and paragraphs
    html = browser.html
    soup = bs(html, "html.parser")
    
    #get the news_title and news_p
    news_title = soup.find('div', class_='content_title')[0].text
    news_p=soup.find_all('div', class_='article_teaser_body')[0].text

    #get the featured image
    jpl_url ='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    featured_image_url='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars1.jpg'

    #get the hemisphere dict
    hemisphere_image_urls = [
    {"title": "Ceberus Hemisphere Enhanced", 'img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
    {"title": "Schiaparelli Hemisphere Enhanced", 'img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
    {"title": "Syrtis Major Hemisphere Enhanced", 'img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
    {"title": "Valles Marineris Hemisphere Enhanced", 'img_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}
    ]

    #create dict for all variables
    mars_data_dict = {
        "news_titles": news_title,
        "news_paragraph": news_p,
        "feat_image": featured_image_url,
        "hemisphere_images": hemisphere_image_urls
    }
    browser.quit()
    return mars_data_dict
