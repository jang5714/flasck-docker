from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse

'''
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
'''

class Bugmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _= 0
        ls = soup.find_all(name='p', attrs={'class':'artist'})
        ls2 = soup.find_all(name='p', attrs={'class':'title'})
        for i, j in zip(ls, ls2):
            _ += 1
            print(str(_) + " Rank" +"\nArtist :" + i.find('a').text + "\nTitle :" + j.find('a').text )
        print('*'*100)

class Melon():
    def __init__(self, url):
        self.url = url
        self.header01 = {'User-Agent':'Mozilla/5.0'}

    def scrap(self):
        x = urllib.request.Request(self.url, headers=self.header01)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'html5lib')
        n_artists = 0
        ls = soup.find_all(name='div', attrs={'class':'ellipsis rank02'})
        ls2 = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in zip(ls, ls2):
            n_artists += 1
            print("Rank " + str(n_artists)+"\nArtisis :"+i.find('a').text+" \nTitle :"+j.find('a').text)


def main():
    Bugmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
                  f'chartdate={"20210720"}&charthour={"16"}').scrap()
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072107').scrap()








