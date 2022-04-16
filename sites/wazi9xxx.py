from bs4 import BeautifulSoup
from mods.waziRequest import waziRequest

class wazi9xxx:
    def __init__(self):
        super(wazi9xxx, self).__init__()
        self.baseURL = "https://www.9xxx.net/"
        self.request = waziRequest()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.params = {}
        self.name = self.__class__.__name__
    
    def giveParams(self, params):
        self.params = params
        return self.params
    
    def returnSoup(self, link):
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            return BeautifulSoup("<html></html>", "lxml")
        else:
            return soup
    
    def parseMain(self, soup):
        pass
    
    def getPage(self, page):
        url = self.baseURL + "page/" + str(page) + "/"
        soup = self.returnSoup(url)
        return soup

