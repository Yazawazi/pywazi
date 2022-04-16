import json
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
    
    def sendPost(self, link):
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        tempHeaders.update({
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": link.split("/")[0] + "//" + link.split("/")[2],
            "referer": link.replace("/api/source/", "/v/"),
            "x-requested-with": "XMLHttpRequest"
        })
        requestParams = self.request.handleParams(tempParams, "fieldsPost", link, tempHeaders, self.proxies)
        requestParams["data"] = {
            "r": "",
            "d": link.split("/")[2]
        }
        try:
            soup = json.loads(self.request.do(requestParams).data.decode("utf-8"))
        except:
            return {}
        else:
            return soup
    
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
