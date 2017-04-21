#uncder construction
import scrape
from bs4 import BeautifulSoup

source=scrape.getSource("http://www.mnemonicdictionary.com/word/recondite")
soup = BeautifulSoup(source, 'html.parser')
print soup.find(id="home-middle-content").p
print soup.find(id="home-middle-content").div
print soup.find(id="home-middle-content").div.find_next_siblings("div")