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
    
    def parseMoviesList(self, soup):
        div = soup.find("div", {
            "class": "list_items"
        })
        if not div:
            return []
        items = div.find_all("div", {
            "class": "movie-preview"
        })
        moviesList = []
        for item in items:
            moviesList.append({
                "id": item.find("span", {
                    "class": "ribbon"
                }).attrs["data-id"],
                "title": item.find("span", {
                    "class": "movie-title"
                }).text.strip(),
                "link": item.find("span", {
                    "class": "movie-title"
                }).find("a").attrs["href"],
                "name": item.find("span", {
                    "class": "movie-title"
                }).find("a").attrs["href"].split("/")[-2],
            })
        return moviesList
    
    def parseTagsList(self, soup):
        div = soup.find_all("div", {
            "class": "tags"
        })
        if not div:
            return []
        div = div[-1]
        items = div.find_all("li")
        tagsList = []
        for item in items:
            tagsList.append({
                "id": item.get("class")[1].split("-")[-1],
                "title": item.find("a").text.strip(),
                "link": item.find("a").attrs["href"],
                "name": item.find("a").attrs["href"].split("/")[-2]
            })
        return tagsList
    
    def parseSearch(self, soup):
        return wazi9xxx.parseMoviesList(self, soup)
    
    def parseMainAndCategory(self, soup):
        return (wazi9xxx.parseMoviesList(self, soup), wazi9xxx.parseTagsList(self, soup))
    
    def parseVideo(self, soup):
        pass
    
    def search(self, keyword, page):
        if page > 1:
            url = f"{self.baseURL}page/{page}/?s={keyword}"
        else:
            url = f"{self.baseURL}?s={keyword}"
        return wazi9xxx.parseSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getVideo(self, videoId, name):
        url = f"{self.baseURL}video_{videoId}/{name}/"
        return wazi9xxx.parseVideo(self, wazi9xxx.returnSoup(self, url))
    
    def getCategory(self, category, page, sort = None):
        if page > 1:
            url = f"{self.baseURL}video_category/{category}/page/{page}/"
        else:
            url = f"{self.baseURL}video_category/{category}/"
        if sort:
            url += f"?sort={sort}"
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
    
    def getPage(self, page):
        url = f"{self.baseURL}page/{page}/"
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
