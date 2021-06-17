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
    