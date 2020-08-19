import requests
from bs4 import BeautifulSoup

class data_scraper:
    def __init__(self,*args):
        self.pricedata = []
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://secure.runescape.com/m=itemdb_oldschool/results',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        } 
        self._IDlist = [_ID for _ID in args]
        self.get_top100(self)
        for _ID in self._IDlist:
        
            self.pricedata.append(self.get_pricedata(self,_ID))
        
    def get_pricedata(self,master,_ID):
    

        params = (
            ('obj',f'{_ID}'),
            )

        response = requests.get('https://secure.runescape.com/m=itemdb_oldschool/viewitem', headers = master.headers, params=params)
        soup = BeautifulSoup(response.content,'html.parser')
        price = str(soup('h3'))
        price = price[price.find('"'):price.find('">')].replace('"','')   
        name = str(soup('title')).replace('[<title>','').replace('</title>]','').replace(' - Grand Exchange - Old School RuneScape','')
        

        return price,name

    
    def get_top100(self,master):
    
        
        params = (
            ('list', '0'),
        )
        response = requests.get('https://secure.runescape.com/m=itemdb_oldschool/top100',headers = master.headers,params=params)
        soup = BeautifulSoup(response.content,'html.parser')
        print(soup.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://secure.runescape.com/m=itemdb_oldschool/top100?list=0', headers=headers, cookies=cookies)
