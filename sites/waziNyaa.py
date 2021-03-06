"""
sites/waziNyaa.py

class: waziNyaa
"""

from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck
from mods.waziRequest import waziRequest

class waziNyaa:
    """
    waziNyaa
    *My comment format is a mystery.*

    A class for crawling the nyaa.si website. (Support sukebei.nyaa.si)

    Attributes:
        headers: dict
            The headers for the request. A customized header is filled in.
        
        proxies: dict
            The proxy for the request.
            Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.
        
        tempFiles: list
            A list of files in the page.
        
        urls: list
            A list of urls.
            0: https://nyaa.si/
            1: https://sukebei.nyaa.si/
        
        URL: waziURL
            A waziURL object.
        
        check: waziCheck
            A waziCheck object.
        
        request: waziRequest
            A waziRequest object.
        
        name: str
            The name of the class.
    
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziNyaa.__init__(self)
        *I know this is a lie.*

        Parameters:
            None
        """
        super(waziNyaa, self).__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.params = {}
        self.tempFiles = []
        self.urls = ["https://nyaa.si/", "https://sukebei.nyaa.si/"]
        self.URL = waziURL()
        self.check = waziCheck()
        self.request = waziRequest()
        self.name = self.__class__.__name__
    
    def giveParams(self, params):
        """
        waziNyaa.giveParams(self, params)
        *Everywhere.*

        Give params to this class. Controled by user.
        Proxy and headers are controlled by self.params.

        Parameters:
            params: dict
                A dict of params, user given.
        
        Return:
            Type: dict
            The params given.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) ????????????????????????????????? {self.params}")
        return self.params
    
    def getFiles(self, ul):
        """
        waziNyaa.getFiles(self, ul)
        *The Art of Recursion.*

        Get all files in the page.
        Input root ul element, you can get all files in the page.
        Save in self.tempFiles.

        Parameters:
            ul: BeautifulSoup
                The root ul element.
            
        Return:
            None
        
        Errors:
            None
        """
        for i in ul.contents:
            if i != "\n":
                if i.find("a"):
                    self.tempFiles.append(i.find("a").text.strip())
                    waziNyaa.getFiles(self, i.find("ul"))
                elif i.find("li"):
                    waziNyaa.getFiles(self, i)
                else:
                    self.tempFiles.append(i.text.strip())
    
    def returnSoup(self, link, xml):
        """
        waziNyaa.returnSoup(self, link, xml)
        *Reuse, abstract. But I cannot.*

        Request a link and return a BeautifulSoup.

        Parameters:
            link: str
                A link to request.

            xml: bool
                Whether the link is xml or not.
        
        Return:
            soup: BeautifulSoup
                A BeautifulSoup of the requested link.
                If the request failed, return BeautifulSoup("<html></html>", "lxml")
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Logs:
                Error:
                    + Cannot get the response.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL??????????????? Soup??? {link}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL ??????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            if xml:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "xml")
            else:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) ??????????????????????????? Soup???")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) ???????????????Soup ????????????")
            return soup

    def parsePage(self, soup, site):
        """
        waziNyaa.parsePage(self, soup, site)
        *No Heroes.*

        Parse the page to get the information.

        Parameters:
            soup: BeautifulSoup
                A BeautifulSoup of the page.
            
            site: int
                The site of the page.
                0: https://nyaa.si/
                1: https://sukebei.nyaa.si/
        
        Return:
            Type: dict
            A dict of the information.
            Like:
            {
                "type": str,                                        # The type of the torrent.
                "title": str,                                       # The title of the torrent.
                "category": {                                       # The category of the torrent.
                    "fatherCategory": str,                          # The father category of the torrent.
                    "fatherCategoryId": str,                        # The father category ID of the torrent.
                    "subCategory": str,                             # The sub category of the torrent.
                    "subCategoryId": str                            # The sub category ID of the torrent.
                    "category": str,                                # The category of the torrent.
                },
                "time": str,                                        # The time of the torrent.
                "timeStamp": int,                                   # The time stamp of the torrent.
                "uploader": str,                                    # The uploader of the torrent.
                "uploaderLink": str,                                # The uploader link of the torrent.
                "seeders": int,                                     # The seeders number of the torrent.
                "information": str,                                 # The information of the torrent.
                "informationLink": str,                             # The information link of the torrent.
                "leechers": int,                                    # The leechers number of the torrent.
                "size": str,                                        # The size of the torrent.
                "completes": int,                                   # The download completes number of the torrent.
                "hash": str,                                        # The hash of the torrent.
                "torrent": str or None,                             # The torrent link of the torrent.
                "magnet": str,                                      # The magnet link of the torrent.
                "description": str,                                 # The description of the torrent.
                "files": str or list[str],                          # The files of the torrent.
                "comments": [{
                    "name": str,                                    # The name of the commenter.
                    "link": str,                                    # The link of the commenter.
                    "extra": str,                                   # The extra information of the commenter.
                    "time": str,                                    # The time of the commenter.
                    "timeStamp": int,                               # The time stamp of the commenter.
                    "editTime": str,                                # The edit time of the commenter.
                    "editTimeStamp": float,                         # The edit time stamp of the commenter.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup ??? site ????????????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????? {site}")
        itemInfo = {}
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? container???")
        container = soup.find_all("div", class_ = "container")[1]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        classNamesList = container.find(class_ = "panel").attrs["class"]
        if "panel-danger" in classNamesList:
            itemInfo["type"] = self.check.nyaaTranslations["panel-danger"]
        elif "panel-success" in classNamesList:
            itemInfo["type"] = self.check.nyaaTranslations["panel-success"]
        else:
            itemInfo["type"] = self.check.nyaaTranslations["panel-default"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["title"] = soup.find(class_ = "panel-title").text.strip()
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["category"] = {
            "fatherCategory": soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[0].find_all("a")[0].text,
            "fatherCategoryId": soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[0].find_all("a")[0].attrs["href"].split("=")[-1],
            "subCategory": soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[0].find_all("a")[1].text,
            "subCategoryId": soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[0].find_all("a")[1].attrs["href"].split("=")[-1],
        }
        itemInfo["category"]["category"] = itemInfo["category"]["fatherCategory"] + " - " + itemInfo["category"]["subCategory"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["time"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[1].text
        itemInfo["timeStamp"] = int(soup.find(class_ = "panel-body").find_all(class_ = "row")[0].find_all(class_ = "col-md-5")[1].attrs["data-timestamp"])
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
        itemInfo["uploader"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[1].find_all(class_ = "col-md-5")[0].find_all("a")[0].text
        itemInfo["uploaderLink"] = self.urls[int(site)] + "user/" + soup.find(class_ = "panel-body").find_all(class_ = "row")[1].find_all(class_ = "col-md-5")[0].find_all("a")[0].attrs["href"].split("/")[-1]
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        itemInfo["seeders"] = int(soup.find(class_ = "panel-body").find_all(class_ = "row")[1].find_all(class_ = "col-md-5")[1].text)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["information"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[2].find_all(class_ = "col-md-5")[0].text.strip()
        itemInfo["informationLink"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[2].find_all(class_ = "col-md-5")[0].find("a").attrs["href"]
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        itemInfo["leechers"] = int(soup.find(class_ = "panel-body").find_all(class_ = "row")[2].find_all(class_ = "col-md-5")[1].text)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["size"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[3].find_all(class_ = "col-md-5")[0].text
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
        itemInfo["completes"] = int(soup.find(class_ = "panel-body").find_all(class_ = "row")[3].find_all(class_ = "col-md-5")[1].text)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        itemInfo["hash"] = soup.find(class_ = "panel-body").find_all(class_ = "row")[4].find_all(class_ = "col-md-5")[0].text
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        if "magnet:?xt=" in soup.find(class_ = "panel-footer").find_all("a")[0].attrs["href"]:
            itemInfo["torrent"] = None
        else:
            itemInfo["torrent"] = self.urls[int(site)] + "download/" + soup.find(class_ = "panel-footer").find_all("a")[0].attrs["href"].split("/")[-1]
        itemInfo["magnet"] = soup.find(class_ = "panel-footer").find_all("a")[-1].attrs["href"]
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        itemInfo["description"] = soup.find(id = "torrent-description").text
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????????????????????????????????????????????????????")
        try:
            fileList = soup.find(class_ = "torrent-file-list").find("ul")
        except:
            itemInfo["files"] = "File list is not available for this torrent."
        else:
            self.tempFiles = []
            waziNyaa.getFiles(self, fileList)
            itemInfo["files"] = self.tempFiles
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        if soup.find(id = "comments").h3.text.strip() == "Comments - 0":
            itemInfo["comments"] = []
        else:
            comments = []
            for comment in soup.find_all(class_ = "comment-panel"):
                commentInfo = {}
                commentInfo["name"] = comment.find("p").find("a").text
                commentInfo["link"] = self.urls[int(site)] + "user/" + comment.find("p").find("a").attrs["href"].split("/")[-1]
                commentInfo["extra"] = comment.find("p").text.strip().replace(commentInfo["name"], "").strip().replace("(", "").replace(")", "")
                commentInfo["avatar"] = comment.find("img").attrs["src"]
                commentInfo["time"] = comment.find(class_ = "comment-details").find("a").text
                commentInfo["timeStamp"] = int(comment.find(class_ = "comment-details").find("a").find("small").attrs["data-timestamp"])
                if len(comment.find(class_ = "comment-details").find_all("small")) == 2:
                    commentInfo["editTime"] = comment.find(class_ = "comment-details").find_all("small")[1].attrs["title"]
                    commentInfo["editTimeStamp"] = float(comment.find(class_ = "comment-details").find_all("small")[1].attrs["data-timestamp"])
                else:
                    commentInfo["editTime"] = None
                    commentInfo["editTimeStamp"] = None
                commentInfo["comment"] = comment.find(class_ = "comment-content").text
                comments.append(commentInfo)
            itemInfo["comments"] = comments
        waziLog.log("info", f"({self.name}.{fuName}) ??????????????? {itemInfo}")
        return itemInfo

    def parseRSS(self, rss):
        """
        waziNyaa.parseRSS(self, rss)
        *I love you so.*

        Parses the RSS feed and returns a list of items.

        Parameters:
            rss: BeautifulSoup
                The RSS feed.
        
        Return:
            Type: list[dict{}]
            A list of dictionaries containing the item information.
            Like:
            [{
                "type": str,                        # The type of the item.
                "category": str,                    # The category of the item.
                "categoryId": str,                  # The category ID of the item.
                "comments": int,                    # The number of comments of the item.
                "title": str,                       # The title of the item.
                "link": str,                        # The link of the item.
                "id": int,                          # The ID of the item.
                "torrent": str or None,             # The link to the torrent file of the item.
                "magnet": str,                      # The magnet link of the item.
                "size": str,                        # The size of the torrent.
                "time": str,                        # The time of the torrent.
                "seeders": int,                     # The number of seeders of the torrent.
                "leechers": int,                    # The number of leechers of the torrent.
                "completes": int                    # The number of completions of the torrent.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Log:
                Warn:
                    + Cannot get item elements.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? RSS ????????????????????????")
        items = rss.find_all("item")
        if items is None:
            waziLog.log("warn", f"({self.name}.{fuName}) ???????????? RSS ?????? item ???????????????????????????")
            return []
        else:
            waziLog.log("info", f"({self.name}.{fuName}) ????????????????????????????????????")
            result = []
            for item in items:
                itemInfo = {}
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                if item.find("nyaa:trusted").text == "Yes":
                    itemInfo["type"] = self.check.nyaaTranslations["success"]
                elif item.find("nyaa:remake").text == "Yes":
                    itemInfo["type"] = self.check.nyaaTranslations["danger"]
                else:
                    itemInfo["type"] = self.check.nyaaTranslations["default"]
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                itemInfo["category"] = item.find("nyaa:category").text
                itemInfo["categoryId"] = item.find("nyaa:categoryId").text
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                itemInfo["comments"] = int(item.find("nyaa:comments").text)
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                itemInfo["title"] = item.find("title").text
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                itemInfo["link"] = item.find("guid").text
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????? ID???")
                itemInfo["id"] = int(item.find("guid").text.split("/")[-1])
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
                try:
                    itemInfo["torrent"] = item.find("link").text
                except:
                    itemInfo["torrent"] = None
                itemInfo["magnet"] = "magnet:?xt=urn:btih:" + item.find("nyaa:infoHash").text
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                itemInfo["size"] = item.find("nyaa:size").text
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                itemInfo["time"] = item.find("pubDate").text
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
                itemInfo["seeders"] = int(item.find("nyaa:seeders").text)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
                itemInfo["leechers"] = int(item.find("nyaa:leechers").text)
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
                itemInfo["completes"] = int(item.find("nyaa:downloads").text)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {itemInfo}")
                result.append(itemInfo)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????")
            return result

    def parseSearch(self, soup, site):
        """
        waziNyaa.parseSearch(self, soup, site)
        *Cold but warm.*

        Parse the search result.

        Parameters:
            soup: BeautifulSoup
                The soup of the search result.
            
            site: int
                The site of the page.
                0: https://nyaa.si/
                1: https://sukebei.nyaa.si/
        
        Return:
            Type: list[dict{}]
            The parsed result.
            Like:
            [{
                "type": str,                        # The type of the item.
                "typeExtra": str,                   # The extra type of the item. (May have)
                "category": str,                    # The category of the item.
                "categoryId": str,                  # The category ID of the item.
                "comments": int,                    # The number of comments of the item.
                "title": str,                       # The title of the item.
                "link": str,                        # The link of the item.
                "id": int,                          # The ID of the item.
                "torrent": str,                     # The torrent link of the item.
                "magnet": str,                      # The magnet link of the item.
                "size": str,                        # The size of the item.
                "time": str,                        # The time of the item.
                "timeStamp": int,                   # The timestamp of the item.
                "seeders": int,                     # The number of seeders of the item.
                "leechers": int,                    # The number of leechers of the item.
                "completes": int                    # The number of completes of the item.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Log:
                Warn:
                    + Cannot get tbody element.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        table = soup.find("tbody")
        if table is None:
            waziLog.log("warn", f"({self.name}.{fuName}) ??????????????????????????????????????????")
            return []
        else:
            waziLog.log("info", f"({self.name}.{fuName}) ?????????????????????????????????")
            rows = table.find_all("tr")
            waziLog.log("info", f"({self.name}.{fuName}) ?????? tr ???????????? {len(rows)} ??????")
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????? tr???")
            result = []
            for row in rows:
                rowInfo = {}
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                try:
                    rowInfo["type"] = self.check.nyaaTranslations[row.attrs["class"][0]]
                except:
                    waziLog.log("warn", f"({self.name}.{fuName}) ????????????????????????????????? class???")
                    rowInfo["type"] = row.attrs["class"][0]
                    rowInfo["typeExtra"] = "class"
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                rowInfo["category"] = row.find("td").find("a").attrs["title"]
                rowInfo["categoryId"] = row.find("td").find("a").find("img").attrs["src"].split("/")[-1].split(".")[0]
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                comment = row.find("a", class_ = "comments")
                if comment:
                    rowInfo["comments"] = int(comment.text)
                else:
                    rowInfo["comments"] = 0
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                href = row.find_all("td")[1].find_all("a")[-1]
                rowInfo["title"] = href.attrs["title"]
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
                rowInfo["link"] = self.urls[int(site)] + "view/" + href.attrs["href"].split("/")[-1]
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????? ID???")
                rowInfo["id"] = int(href.attrs["href"].split("/")[-1])
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
                if "magnet:?xt=" in row.find_all("td")[2].find("a").attrs["href"]:
                    rowInfo["torrent"] = None
                else:
                    rowInfo["torrent"] = self.urls[int(site)] + "download/" + row.find_all("td")[2].find("a").attrs["href"].split("/")[-1]
                rowInfo["magnet"] = row.find_all("td")[2].find_all("a")[-1].attrs["href"]
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                rowInfo["size"] = row.find_all("td")[3].text
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
                rowInfo["time"] = row.find_all("td")[4].text
                rowInfo["timeStamp"] = int(row.find_all("td")[4].attrs["data-timestamp"])
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
                rowInfo["seeders"] = int(row.find_all("td")[5].text)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
                rowInfo["leechers"] = int(row.find_all("td")[6].text)
                waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
                rowInfo["completes"] = int(row.find_all("td")[7].text)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {rowInfo}")
                result.append(rowInfo)
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????")
            return result

    def search(self, params):
        """
        waziNyaa.search(self, params)
        *Nonfiction ecstasy.*

        Parameters:
            params: dict
                The search parameters.
                {
                    "page": int or str,             # The page number. Start from 1.
                    "keyword": str,                 # The search keyword.
                    "category": str,                # The category.
                    "filter": str,                  # The filter. No / No Remakes / Trusted Only
                    "order": str,                   # The order. Comments / Size / Date / Seeders / Leechers / Completed Downloads,
                    "site": str or int,             # The site. 0 is https://nyaa.si/, 1 is https://sukebei.nyaa.si/
                    "orderBy": str                  # The order by. asc / desc
                }
        
        Return:
            Type: list[dict{}]
            The search result.
            Like:
            [{
                "type": str,                        # The type of the item.
                "typeExtra": str,                   # The extra type of the item. (May have)
                "category": str,                    # The category of the item.
                "categoryId": str,                  # The category ID of the item.
                "comments": int,                    # The number of comments of the item.
                "title": str,                       # The title of the item.
                "link": str,                        # The link of the item.
                "id": int,                          # The ID of the item.
                "torrent": str,                     # The torrent link of the item.
                "magnet": str,                      # The magnet link of the item.
                "size": str,                        # The size of the item.
                "time": str,                        # The time of the item.
                "timeStamp": int,                   # The timestamp of the item.
                "seeders": int,                     # The number of seeders of the item.
                "leechers": int,                    # The number of leechers of the item.
                "completes": int                    # The number of completes of the item.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? Soup???")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {params}")
        searchParams = {
            "f": "0",
            "c": "0_0",
            "q": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        if "page" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["p"] = str(params["page"])
        if "keyword" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????????????????")
            searchParams["q"] = params["keyword"]
        if "category" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["c"] = self.check.nyaaSearch["catgroies"][params["category"]]
        if "filter" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["f"] = self.check.nyaaSearch["filters"][params["filter"]]
        if "order" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams.update(self.check.nyaaSearch["orders"][params["order"]])
            if "orderBy" in params:
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????????????????")
                searchParams["o"] = params["orderBy"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL???")
        url = self.URL.getFullURL(self.urls[int(params["site"])], searchParams)
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? {url}")
        return waziNyaa.parseSearch(self, waziNyaa.returnSoup(self, url, False), int(params["site"]))
        
    def searchRSS(self, params):
        """
        waziNyaa.searchRSS(self, params)
        *Rat.*

        Parameters:
            params: dict
                The search parameters.
                {
                    "page": int or str,             # The page number. Start from 1.
                    "keyword": str,                 # The search keyword.
                    "category": str,                # The category.
                    "filter": str,                  # The filter. No / No Remakes / Trusted Only
                    "order": str,                   # The order. Comments / Size / Date / Seeders / Leechers / Completed Downloads,
                    "site": str or int,             # The site. 0 is https://nyaa.si/, 1 is https://sukebei.nyaa.si/
                    "orderBy": str                  # The order by. asc / desc
                }

        Return:
            Type: list[dict{}]
            The search result.
            Like:
            [{
                "type": str,                        # The type of the item.
                "category": str,                    # The category of the item.
                "categoryId": str,                  # The category ID of the item.
                "comments": int,                    # The number of comments of the item.
                "title": str,                       # The title of the item.
                "link": str,                        # The link of the item.
                "id": int,                          # The ID of the item.
                "torrent": str or None,             # The link to the torrent file of the item.
                "magnet": str,                      # The magnet link of the item.
                "size": str,                        # The size of the torrent.
                "time": str,                        # The time of the torrent.
                "seeders": int,                     # The number of seeders of the torrent.
                "leechers": int,                    # The number of leechers of the torrent.
                "completes": int                    # The number of completions of the torrent.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? XML ?????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {params}")
        searchParams = {
            "page": "rss",
            "f": "0",
            "c": "0_0",
            "q": ""
        }
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        if "page" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["p"] = str(params["page"])
        if "keyword" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????????????????")
            searchParams["q"] = params["keyword"]
        if "category" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["c"] = self.check.nyaaSearch["catgroies"][params["category"]]
        if "filter" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams["f"] = self.check.nyaaSearch["filters"][params["filter"]]
        if "order" in params:
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            searchParams.update(self.check.nyaaSearch["orders"][params["order"]])
            if "orderBy" in params:
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????????????????")
                searchParams["o"] = params["orderBy"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL???")
        url = self.URL.getFullURL(self.urls[int(params["site"])], searchParams)
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? {url}")
        return waziNyaa.parseRSS(self, waziNyaa.returnSoup(self, url, True))
    
    def getViewFromId(self, id, site):
        """
        waziNyaa.getViewFromId(self, id, site)
        *I love CityPop.*

        Parameters:
            id: int or str
                The ID of the item.

            site: int or str
                The site of the item. 0 is https://nyaa.si/, 1 is https://sukebei.nyaa.si/
        
        Return:
            Type: dict
            A dict of the information.
            Like:
            {
                "type": str,                                        # The type of the torrent.
                "title": str,                                       # The title of the torrent.
                "category": {                                       # The category of the torrent.
                    "fatherCategory": str,                          # The father category of the torrent.
                    "fatherCategoryId": str,                        # The father category ID of the torrent.
                    "subCategory": str,                             # The sub category of the torrent.
                    "subCategoryId": str                            # The sub category ID of the torrent.
                    "category": str,                                # The category of the torrent.
                },
                "time": str,                                        # The time of the torrent.
                "timeStamp": int,                                   # The time stamp of the torrent.
                "uploader": str,                                    # The uploader of the torrent.
                "uploaderLink": str,                                # The uploader link of the torrent.
                "seeders": int,                                     # The seeders number of the torrent.
                "information": str,                                 # The information of the torrent.
                "informationLink": str,                             # The information link of the torrent.
                "leechers": int,                                    # The leechers number of the torrent.
                "size": str,                                        # The size of the torrent.
                "completes": int,                                   # The download completes number of the torrent.
                "hash": str,                                        # The hash of the torrent.
                "torrent": str or None,                             # The torrent link of the torrent.
                "magnet": str,                                      # The magnet link of the torrent.
                "description": str,                                 # The description of the torrent.
                "files": str or list[str],                          # The files of the torrent.
                "comments": [{
                    "name": str,                                    # The name of the commenter.
                    "link": str,                                    # The link of the commenter.
                    "extra": str,                                   # The extra information of the commenter.
                    "time": str,                                    # The time of the commenter.
                    "timeStamp": int,                               # The time stamp of the commenter.
                    "editTime": str,                                # The edit time of the commenter.
                    "editTimeStamp": float,                         # The edit time stamp of the commenter.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? ID ??? site ????????????????????? Soup???")
        waziLog.log("debug", f"({self.name}.{fuName}) ID??? {id}??? ????????? {site}")
        url = self.urls[int(site)] + "view/" + str(id)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? Soup??? {url}")
        return waziNyaa.parsePage(self, waziNyaa.returnSoup(self, url, False), int(site))
