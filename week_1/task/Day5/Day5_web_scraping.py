from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from time import sleep

url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
poster_url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

divs = soup.find_all("div", {'class':"tit3"})

codes = [div.a.attrs["href"].split('=')[1] for div in divs[:5]]

for code in codes:
    poster_page = urlopen(poster_url + code)
    poster_soup = BeautifulSoup(poster_page, 'html.parser')
    img_url = poster_soup.find("img").attrs['src']
    urlretrieve(img_url, "./movie"+code+'.jpg')
    sleep(2)
