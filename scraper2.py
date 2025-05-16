import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site
   #self.siteインスタンス変数にscraper()引数を代入
   
    def scrape(self):
        r =urllib.request.urlopen(self.site) #urlopen関数、返り値はオブジェクト
        haha = r.read() #readメソッド
   #urllib.requestモジュールを使うのはここまで
   
        parsername = "html.parser" #パース解析器の名前、これじゃないとﾀﾞﾒ
        BSobj = BeautifulSoup(haha,parsername) #BSオブジェクトを作成

        for eachtag in BSobj.find_all("a"): #BSオブジェクトのfindallメソッド、オブジェクトのリストを返す　eachtagには各オブジェクトが代入される
            urlstr = eachtag.get("href")

            full_url = urljoin(self.site,urlstr)
            print(full_url)

site = "https://newsdig.tbs.co.jp/list/tag/%E5%A4%A7%E8%B0%B7%E7%BF%94%E5%B9%B3"
Scraper(site).scrape()

        

        
