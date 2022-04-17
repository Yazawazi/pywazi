import os
import re
import json
from mods import waziFun
from bs4 import BeautifulSoup
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziAsianToLick:
    """
    waziAsianToLick
    *HTTP/3 (200)*

    A class for crawling https://asiantolick.com/

    Attributes:
        baseURL: str
            The base url of the website.
            Value: "https://asiantolick.com/"
        
        request: waziRequest
            The request object.
        
        fileName: waziFileName
            The file name object.
        
        headers: dict
            The headers for the request.
            Default: 
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/91.0.4472.164 Safari/537.36"
            }
        
        proxies: dict
            The proxies for the request.
             Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziAsianToLick.__init__(self)
        *Love It.*

        Initialize this class.

        Parameters:
            None
        """
        super(waziAsianToLick, self).__init__()
        self.baseURL = "https://asiantolick.com/"
        self.request = waziRequest()
        self.fileName = waziFileName()
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
        """
        waziAsianToLick.giveParams(self, params)
        *Wake up and sleep.*

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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置信息，正在写入。")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前配置为： {self.params}")
        return self.params
    
    def returnSoup(self, link, xml):
        """
        waziAsianToLick.returnSoup(self, link, xml)
        *Copy from waziNyaa*

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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在获得 Soup： {link}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 需要检查 URL 并进行处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起网络请求。")
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            if xml:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "xml")
            else:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取，返回无效 Soup。")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取成功，Soup 返回中。")
            return soup
    
    def parseXML(self, soup):
        urls = soup.find("urlset").find_all("url")
        urlsList = []
        for url in urls:
            urlsList.append({
                "url": url.find("loc").text.strip(),
                "lastmod": url.find("lastmod").text.strip(),
                "priority": float(url.find("priority").text.strip()),
                "id": url.find("loc").text.strip().split("/")[3].split("-")[1] if url.find("loc").text.strip() != self.baseURL else None,
                "title": url.find("loc").text.strip().split("/")[-1] if url.find("loc").text.strip() != self.baseURL else None
            })
        return urlsList
    
    def getAjaxPosts(self, soup):
        posts = soup.find_all("a")
        if not posts:
            return []
        postsList = []
        for post in posts:
            baseTt = post.find("div", {
                "class": "base_tt"
            })
            spans = baseTt.find_all("span")
            tags = []
            if spans:
                for span in span:
                    if "tt_tag" in span.get("class")[0]:
                        tags.append({
                            "tagClass": span.get("class")[0],
                            "tagName": span.text.strip()
                        })
            postsList.append({
                "url": post.get("href"),
                "hashId": post.get("id"),
                "cover": post.find("div", {
                    "class": "background_miniature"
                }).find("img").get("src"),
                "alt": post.find("div", {
                    "class": "background_miniature"
                }).find("img").get("alt").strip(),
                "pageNum": int(post.find("div", {
                    "class": "contar_imagens"
                }).text.strip()),
                "tags": tags,
                "title": BeautifulSoup(re.sub('<span class="tt_tag_[a-zA-Z]+.*?">[a-zA-Z]+.*?</span>', "", str(baseTt.span)), "lxml").text.strip(),
            })
        return postsList
    
    def getSiteMapPosts(self):
        url = f"{self.baseURL}sitemap/post.xml"
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def getSiteMapCategories(self):
        url = f"{self.baseURL}sitemap/category.xml"
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def getSiteMapTags(self):
        url = f"{self.baseURL}sitemap/tags.xml"
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def get(self, post, cat, tag, search, page, index, ver):
        url = f"{self.baseURL}ajax/buscar_posts.php?post={post}&cat={cat}&tag={tag}&search={search}&page={page}&index={index}&ver={ver}"
        return waziAsianToLick.getAjaxPosts(self, waziAsianToLick.returnSoup(self, url, False))
    
    def getPost(self, postId, name):
        pass
    
    def downloadPostByNative(self, postId, name, path, key = "org"):
        pass

    def downloadPost(self, postId, name, path):
        pass
