# model scraping for themodelbot

import cfscrape
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://imgsrc.ru/'

scraper = cfscrape.create_scraper()

# download page for parsing
page = scraper.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with images
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = scraper.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(scraper.get(url).content)
                f.close()
                x += 1
    except:
        pass

