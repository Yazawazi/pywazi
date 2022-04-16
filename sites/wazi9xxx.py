import os
import re
import json
from mods import waziFun
from bs4 import BeautifulSoup
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class wazi9xxx:
    """
    wazi9xxx
    *9 to 5? 0 to 0!*

    A class for crawling https://www.9xxx.net/

    Attributes:
        baseURL: str
            The base url of the website.
            Value: "https://www.9xxx.net/"
        
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
        wazi9xxx.__init__(self)
        *Love It.*

        Initialize this class.

        Parameters:
            None
        """
        super(wazi9xxx, self).__init__()
        self.baseURL = "https://www.9xxx.net/"
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
        wazi9xxx.giveParams(self, params)
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
    
    def returnSoup(self, link):
        """
        wazi9xxx.returnSoup(self, link)
        *88 Keys*

        Request a link and return a BeautifulSoup.

        Parameters:
            link: str
                A link to request.
        
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
            soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取，返回无效 Soup。")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取成功，Soup 返回中。")
            return soup
    
    def sendPost(self, link):
        """
        wazi9xxx.sendPost(self, link)
        *What a lovely day.*

        Send a post request with form data.

        Parameters:
            link: str
                A link to request.
        
        Return:
            Type: dict
            The response of the request but in a dict.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Logs:
                Error:
                    + Cannot get the response.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求 URL，正在请求： {link}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建临时请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 正在更新自定义请求头。")
        tempHeaders.update({
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": link.split("/")[0] + "//" + link.split("/")[2],
            "referer": link.replace("/api/source/", "/v/"),
            "x-requested-with": "XMLHttpRequest"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 更新完毕： {tempHeaders}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理参数。")
        requestParams = self.request.handleParams(tempParams, "fieldsPost", link, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 参数处理完毕，正在填写数据。")
        requestParams["data"] = {
            "r": "",
            "d": link.split("/")[2]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 数据填写完毕，正在发起请求： {requestParams['data']}")
        try:
            temp = self.request.do(requestParams)
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取，返回空字典。")
            return {}
        else:
            try:
                temp = json.loads(temp.data.decode("utf-8"))
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法解析，返回空字典。")
                return {}
            else:
                waziLog.log("info", f"({self.name}.{fuName}) 获取成功： {temp}")
                return temp
    
    def downloadFile(self, url, name, path, video = False):
        isExists = os.path.exists(path)
        if not isExists:
            try:
                os.makedirs(path)
            except:
                return False
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        if video:
            requestParams = self.request.handleParams(tempParams, "download", url, tempHeaders, self.proxies)
        else:
            requestParams = self.request.handleParams(tempParams, "get", url, tempHeaders, self.proxies)
        fileName = os.path.join(path, self.fileName.toRight(name))
        if video:
            requestParams["data"] = fileName
        if not video:
            with open(fileName, "wb") as f:
                try:
                    temp = self.request.do(requestParams)
                except:
                    return False
                else:
                    f.write(temp.data)
        else:
            try:
                self.request.do(requestParams)
            except:
                return False
        return True
    
    def getCommonInfo(self, soup):
        commonInfo = []
        for item in soup:
            commonInfo.append({
                "title": item.text.strip(),
                "link": item.attrs["href"],
                "name": item.attrs["href"].split("/")[-2] if not item.text.strip() == "Home" else None
            })
        return commonInfo
    
    def getVideoDownloadLinks(self, href):
        url = href.replace("/v/", "/api/source/")
        result = wazi9xxx.sendPost(self, url)
        videos = {
            "data": result["data"],
            "posterLink": "https://thumb.fvs.io/asset" + result["player"]["poster_file"]
        }
        return videos

    def getVideosInVideoPage(self, soup):
        videos = []
        items = soup.find_all("a")
        for item in items:
            videos.append({
                "id": item.attrs["href"].split("/")[-3].split("_")[-1],
                "title": item.find("div", {
                    "class": "relpost-block-single-text"
                }).text.strip(),
                "cover": item.find("div", {
                    "class": "relpost-block-single-image"
                }).attrs["style"].split("url(")[1].split(")")[0],
                "link": item.attrs["href"],
                "name": item.attrs["href"].split("/")[-2]
            })
        return videos
    
    def parseVideoPage(self, soup):
        info = soup.find("div", {
            "class": "single-content movie"
        })
        trueVideo = soup.find("div", {
            "class": "single-content video"
        })
        details = soup.find("div", {
            "id": "details"
        })
        container = soup.find("div", {
            "class": "relpost-block-container"
        })
        if not info or not details:
            return {}
        breadCrumb = info.find("div", {
            "class": "Breadcrumb"
        }).find_all("a")
        categories = wazi9xxx.getCommonInfo(self, breadCrumb)
        video = {
            "cover": info.find("div", {
                "class": "poster"
            }).find("img").attrs["src"],
            "views": int(info.find("span", {
                "class": "views-number"
            }).text.strip()
            .split(" ")[0].replace(",", "")),
            "breadCategories": categories,
            "title": info.find("div", {
                "class": "title"
            }).find("h1").text.strip(),
            "categories": wazi9xxx.getCommonInfo(self, info.find("div", {
                "class": "categories"
            }).find_all("a")),
            "directors": wazi9xxx.getCommonInfo(self, info.find("div", {
                "class": "director"
            }).find_all("a")),
            "actors": wazi9xxx.getCommonInfo(self, info.find("div", {
                "class": "actor"
            }).find_all("a")),
            "more": info.find("div", {
                "class": "more"
            }).text.strip(),
            "story": details.find("div", {
                "class": "storyline"
            }).text.strip(),
            "tags": wazi9xxx.getCommonInfo(self, details.find("div", {
                "class": "tags"
            }).find_all("a")),
            "videos": wazi9xxx.getVideosInVideoPage(self, container),
            "downloadLinks": wazi9xxx.getVideoDownloadLinks(self, 
                trueVideo.find("div", {
                    "class": "video-content"
                }).find("iframe").attrs["src"]
            )
        }
        return video
    
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
                "cover": item.find("img").attrs["src"],
                "link": item.find("span", {
                    "class": "movie-title"
                }).find("a").attrs["href"],
                "name": item.find("span", {
                    "class": "movie-title"
                }).find("a").attrs["href"].split("/")[-2],
                "story": item.find("p", {
                    "class": "story"
                }).text.strip(),
                "views": int(item.find("div", {
                    "class": "movie-info"
                }).find("span", {
                    "class": "views"
                }).text.strip()
                .split(" ")[0].replace(",", ""))
            })
        return moviesList
    
    def parseRecentPosts(self, soup):
        div = soup.find("div", id = "recent-posts-2").find("ul")
        if not div:
            return []
        items = div.find_all("li")
        recentPosts = []
        for item in items:
            recentPosts.append({
                "title": item.find("a").text.strip(),
                "link": item.find("a").attrs["href"],
                "name": item.find("a").attrs["href"].split("/")[-2]
            })
        return recentPosts
    
    def parseTagsList(self, soup, tag = False):
        if not tag:
            div = soup.find_all("div", {
                "class": "tags"
            })
        else:
            div = soup.find("div", id = "categories-2").find("ul")
        if not div:
            return []
        if not tag:
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
    
    def parseTagAndMoreSearch(self, soup):
        return (wazi9xxx.parseMoviesList(self, soup), wazi9xxx.parseTagsList(self, soup, True), wazi9xxx.parseRecentPosts(self, soup))
    
    def parseMainAndCategory(self, soup):
        return (wazi9xxx.parseMoviesList(self, soup), wazi9xxx.parseTagsList(self, soup))
    
    def parseVideo(self, soup):
        return wazi9xxx.parseVideoPage(self, soup)
    
    def search(self, keyword, page):
        if page > 1:
            url = f"{self.baseURL}page/{page}/?s={keyword}"
        else:
            url = f"{self.baseURL}?s={keyword}"
        return wazi9xxx.parseSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getVideo(self, videoId, name):
        url = f"{self.baseURL}video_{videoId}/{name}/"
        return wazi9xxx.parseVideo(self, wazi9xxx.returnSoup(self, url))
    
    def downloadVideo(self, videoId, name, path, label):
        url = f"{self.baseURL}video_{videoId}/{name}/"
        video = wazi9xxx.parseVideo(self, wazi9xxx.returnSoup(self, url))
        poster = video["downloadLinks"]["posterLink"]
        data = video["downloadLinks"]["data"]
        cover = re.sub("-\d+x\d+", "", video["cover"])
        title = video["title"]
        coverStatus = wazi9xxx.downloadFile(
            self,
            cover,
            self.fileName.toRight(title + "." + cover.split(".")[-1]),
            os.path.join(path, title)
        )
        posterStatus = wazi9xxx.downloadFile(
            self,
            poster,
            self.fileName.toRight(title + "-poster." + poster.split(".")[-1].split("?")[0]),
            os.path.join(path, title)
        )
        if label:
            for item in data:
                if item["label"] == label:
                    videoStatus = wazi9xxx.downloadFile(
                        self,
                        item["file"],
                        self.fileName.toRight(title + "-" + label + "." + item["type"]),
                        os.path.join(path, title),
                        True
                    )
                    return coverStatus and posterStatus and videoStatus
            return False
        else:
            videoStatuses = []
            for item in data:
                videoStatus = wazi9xxx.downloadFile(
                    self,
                    item["file"],
                    self.fileName.toRight(title + "-" + item["label"] + "." + item["type"]),
                    os.path.join(path, title),
                    True
                )
                videoStatuses.append(videoStatus)
            return coverStatus and posterStatus and all(videoStatuses)
    
    def getCategory(self, category, page, sort = None):
        if page > 1:
            url = f"{self.baseURL}video_category/{category}/page/{page}/"
        else:
            url = f"{self.baseURL}video_category/{category}/"
        if sort:
            url += f"?sort={sort}"
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
    
    def getTag(self, tag, page):
        if page > 1:
            url = f"{self.baseURL}video_tags/{tag}/page/{page}/"
        else:
            url = f"{self.baseURL}video_tags/{tag}/"
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getActor(self, actor, page):
        if page > 1:
            url = f"{self.baseURL}video_stars/{actor}/page/{page}/"
        else:
            url = f"{self.baseURL}video_stars/{actor}/"
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getDirector(self, director, page):
        if page > 1:
            url = f"{self.baseURL}video_director/{director}/page/{page}/"
        else:
            url = f"{self.baseURL}video_director/{director}/"
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getPage(self, page):
        url = f"{self.baseURL}page/{page}/"
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
