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
        """
        wazi9xxx.downloadFile(self, url, name, path, video = False)
        *Panda*

        Download a file.

        Parameters:
            url: str
                A link to download.
            
            name: str
                The name of the file.
            
            path: str
                The path to save the file.
            
            video: bool
                Whether the file is a video.
                If True, will use waziDownload to download the video.
                Default: False
            
        Return:
            Type: bool
            If the download is successful, return True, else return False.
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Cannot save the file may cause the program to crash.)
            
            Logs:
                Error:
                    + Cannot get the response.
                    + Cannot create the path.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，文件名和路径，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 文件名： {name}， 路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取路径是否存在。")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) 路径是否存在： {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到路径不存在，准备创建。")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 创建失败。")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 成功创建，继续执行。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完毕： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
        if video:
            requestParams = self.request.handleParams(tempParams, "download", url, tempHeaders, self.proxies)
        else:
            requestParams = self.request.handleParams(tempParams, "get", url, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完毕，正在修正文件名。")
        fileName = os.path.join(path, self.fileName.toRight(name))
        if video:
            requestParams["data"] = fileName
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名修正完成： {fileName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {url}")
        if not video:
            with open(fileName, "wb") as f:
                try:
                    temp = self.request.do(requestParams)
                except:
                    waziLog.log("error", f"({self.name}.{fuName}) 该文件无法下载！")
                    return False
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在将数据写入。")
                    f.write(temp.data)
                    waziLog.log("debug", f"({self.name}.{fuName}) 数据写入完成。")
        else:
            try:
                self.request.do(requestParams)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 该文件无法下载！")
                return False
        waziLog.log("info", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
        return True
    
    def getCommonInfo(self, soup):
        """
        wazi9xxx.getCommonInfo(self, soup)
        *Template*

        Get the common information.

        Parameters:
            soup: BeautifulSoup
                A set of <a> tags.
        
        Return:
            Type: list
            The common information.
            Like:
            [{
                "title": str,                   # The information's title.
                "link": str,                    # The information's link.
                "name": str                     # The information's name.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到 <a> 标签集合，正在准备获取信息。")
        commonInfo = []
        for item in soup:
            commonInfo.append({
                "title": item.text.strip(),
                "link": item.attrs["href"],
                "name": item.attrs["href"].split("/")[-2] if not item.text.strip() == "Home" else None
            })
        waziLog.log("info", f"({self.name}.{fuName}) 信息获取完毕： {commonInfo}")
        return commonInfo
    
    def getVideoDownloadLinks(self, href):
        """
        wazi9xxx.getVideoDownloadLinks(self, href)
        *Abstract*

        Get the video download links.

        Parameters:
            href: str
                The link of the video.
        
        Return:
            Type: dict
            The video download links.
            Like: {
                "posterLink": str,                          # The poster download link.
                "data": [{                                  # The videos' download links.
                    "file": str,                            # The video's file URL.
                    "label": str,                           # The video's resolution.
                    "type": str                             # The video's extended name.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到视频链接，正在准备请求： {href}")
        url = href.replace("/v/", "/api/source/")
        waziLog.log("debug", f"({self.name}.{fuName}) 修改 URL 完成，准备提交给 sendPost： {url}")
        result = wazi9xxx.sendPost(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完毕，正在提取数据。")
        videos = {
            "data": result["data"],
            "posterLink": "https://thumb.fvs.io/asset" + result["player"]["poster_file"]
        }
        waziLog.log("info", f"({self.name}.{fuName}) 数据提取完毕： {videos}")
        return videos

    def getVideosInVideoPage(self, soup):
        """
        wazi9xxx.getVideosInVideoPage(self, soup)
        *rIfF*

        Get the video links in a video page.

        Parameters:
            soup: BeautifulSoup
                A parent element of <a> tags.
        
        Return:
            Type: list
            The video links.
            Like:
            [{
                "id": str,                  # Video Id
                "title": str,               # Video Title
                "cover": str,               # Video Cover
                "link": str,                # Video Link
                "name": str                 # Video Name
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        videos = []
        items = soup.find_all("a")
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　<a> 标签集合，正在进行一个遍历。")
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
        waziLog.log("info", f"({self.name}.{fuName}) 信息获取完毕： {videos}")
        return videos
    
    def parseVideoPage(self, soup):
        """
        wazi9xxx.parseVideoPage(self, soup)
        *Uniform Standards*

        Parse the video page.

        Parameters:
            soup: BeautifulSoup
                The video page's soup.
        
        Return:
            Type: dict
            The video page's information.
            Like:
            {
                "cover": str,                           # The video's cover link.
                "orgCover": str,                        # The video's original cover link.
                "views": int,                           # The video's views.
                "breadCategories": [{                   # The video's bread categories.
                    "title": str,                       # The bread category's title.
                    "link": str,                        # The bread category's link.
                    "name": str                         # The bread category's name.
                }],
                "title": str,                           # The video's title.
                "categories": [{                        # The video's categories.
                    "title": str,                       # The category's title.
                    "link": str,                        # The category's link.
                    "name": str                         # The category's name.
                }],
                "directors": [{                         # The video's directors.
                    "title": str,                       # The director's title.
                    "link": str,                        # The director's link.
                    "name": str                         # The director's name.
                }],
                "actors": [{                            # The video's actors.
                    "title": str,                       # The actor's title.
                    "link": str,                        # The actor's link.
                    "name": str                         # The actor's name.
                }],
                "more": str,                            # The video's more information.
                "story": str,                           # The video's story.
                "tags": [{                              # The video's tags.
                    "title": str,                       # The tag's title.
                    "link": str,                        # The tag's link.
                    "name": str                         # The tag's name.
                }],
                "videos": [{                            # The video's recommended videos.
                    "id": str,                          # The video's id.
                    "title": str,                       # The video's title.
                    "cover": str,                       # The video's cover link.
                    "link": str,                        # The video's link.
                    "name": str                         # The video's name.
                }],
                "downloadLinks": {                      # The video's download information.
                    "posterLink": str,                  # The video's poster link.
                    "data": [{                          # The video's download links.
                        "file": str,                    # The video's download link.
                        "label": str,                   # The video's download resolution.
                        "type": str                     # The video's extended name.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取头部信息栏。")
        info = soup.find("div", {
            "class": "single-content movie"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取完成，正在获取视频栏。")
        trueVideo = soup.find("div", {
            "class": "single-content video"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取详细信息栏。")
        details = soup.find("div", {
            "id": "details"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 详细信息栏获取完成，正在获取推荐视频栏。")
        container = soup.find("div", {
            "class": "relpost-block-container"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行一个空值检查。")
        if not info or not details or not container:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到任何信息，请检查相关请求设置，URL 等，返回空字典！")
            return {}
        waziLog.log("debug", f"({self.name}.{fuName}) 已进行一个空值检查，正在获取面包屑标签。")
        breadCrumb = info.find("div", {
            "class": "Breadcrumb"
        }).find_all("a")
        categories = wazi9xxx.getCommonInfo(self, breadCrumb)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {categories}，正在组合信息。")
        video = {
            "cover": info.find("div", {
                "class": "poster"
            }).find("img").attrs["src"],
            "orgCover": re.sub("-\d+x\d+", "",
            info.find("div", {
                "class": "poster"
            }).find("img").attrs["src"]),
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
        waziLog.log("info", f"({self.name}.{fuName}) 信息获取完成： {video}")
        return video
    
    def parseMoviesList(self, soup):
        """
        wazi9xxx.parseMoviesList(self, soup)
        *🎺🎷*

        Parse the movies list in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.
        
        Return:
            Type: list
            List of movies.
            Like:
            [{
                "id": str,              # The movie's id.
                "title": str,           # The movie's title.
                "cover": str,           # The movie's cover link.
                "link": str,            # The movie's link.
                "name": str,            # The movie's name.
                "story": str,           # The movie's story.
                "views": int            # The movie's views.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取列表信息栏。")
        div = soup.find("div", {
            "class": "list_items"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到列表信息栏，正在检查空值。")
        if not div:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到列表信息栏，请检查相关请求设置，URL 等，返回空列表！")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取列表信息栏中的所有项目。")
        items = div.find_all("div", {
            "class": "movie-preview"
        })
        moviesList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到列表信息栏中的所有项目，正在进行遍历。")
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
        waziLog.log("info", f"({self.name}.{fuName}) 列表信息获取完成： {moviesList}")
        return moviesList
    
    def parseRecentPosts(self, soup):
        """
        wazi9xxx.parseRecentPosts(self, soup)
        *Past*

        Parse the recent posts in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.
        
        Return:
            Type: list
            List of recent posts.
            Like:
            [{
                "title": str,                   # The post's title.
                "link": str,                    # The post's link.
                "name": str                     # The post's name.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 UL 数据。")
        ul = soup.find("div", id = "recent-posts-2").find("ul")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not ul:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取 UL 数据，请检查相关请求设置，URL 等，返回空列表！")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取所有 LI 数据。")
        items = ul.find_all("li")
        recentPosts = []
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行遍历。")
        for item in items:
            recentPosts.append({
                "title": item.find("a").text.strip(),
                "link": item.find("a").attrs["href"],
                "name": item.find("a").attrs["href"].split("/")[-2]
            })
        waziLog.log("info", f"({self.name}.{fuName}) 最近文章获取完成： {recentPosts}")
        return recentPosts
    
    def parseTagsList(self, soup, tag = False):
        """
        wazi9xxx.parseTagsList(self, soup, tag = False)
        *Step 1*

        Parse the tags list in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.
            
            tag: bool
                Is this a tag page?
                Default: False

        Return:
            Type: list
            List of tags.
            Like:
            [{
                "id": str,                   # The tag's id.
                "title": str,                # The tag's title.
                "link": str,                 # The tag's link.
                "name": str                  # The tag's name.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        if not tag:
            waziLog.log("debug", f"({self.name}.{fuName}) 非 Tag 页面正在获取标签信息。")
            div = soup.find_all("div", {
                "class": "tags"
            })
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) Tag 页面正在获取标签信息。")
            div = soup.find("div", id = "categories-2").find("ul")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not div:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取标签信息，请检查相关请求设置，URL 等，返回空列表！")
            return []
        if not tag:
            waziLog.log("error", f"({self.name}.{fuName}) 非 Tag 页面正在更新 div 信息。")
            div = div[-1]
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取所有 LI 数据。")
        items = div.find_all("li")
        tagsList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行遍历。")
        for item in items:
            tagsList.append({
                "id": item.get("class")[1].split("-")[-1],
                "title": item.find("a").text.strip(),
                "link": item.find("a").attrs["href"],
                "name": item.find("a").attrs["href"].split("/")[-2]
            })
        waziLog.log("info", f"({self.name}.{fuName}) 标签获取完成： {tagsList}")
        return tagsList
    
    def parseSearch(self, soup):
        """
        wazi9xxx.parseSearch(self, soup)
        *Jazz.*

        Parse the search result in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.

        Return:
            Type: list
            List of movies.
            Like:
            [{
                "id": str,              # The movie's id.
                "title": str,           # The movie's title.
                "cover": str,           # The movie's cover link.
                "link": str,            # The movie's link.
                "name": str,            # The movie's name.
                "story": str,           # The movie's story.
                "views": int            # The movie's views.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 转移到 parseMovies 接口。")
        return wazi9xxx.parseMoviesList(self, soup)
    
    def parseTagAndMoreSearch(self, soup):
        """
        wazi9xxx.parseTagAndMoreSearch(self, soup)
        *Open.*

        Parse the tag, actor, etc result in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
            
            Index 2:
                Recent posts list.
                Like:
                [{
                    "title": str,                   # The post's title.
                    "link": str,                    # The post's link.
                    "name": str                     # The post's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 转移到 parseMoviesList, parseTagsList & parseRecentPosts 接口。")
        return (wazi9xxx.parseMoviesList(self, soup), wazi9xxx.parseTagsList(self, soup, True), wazi9xxx.parseRecentPosts(self, soup))
    
    def parseMainAndCategory(self, soup):
        """
        wazi9xxx.parseMainAndCategory(self, soup)
        *Index.*

        Parse the main page and category page in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of page.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 转移到 parseMoviesList & parseTagsList 接口。")
        return (wazi9xxx.parseMoviesList(self, soup), wazi9xxx.parseTagsList(self, soup))
    
    def parseVideo(self, soup):
        """
        wazi9xxx.parseVideo(self, soup)
        *December.*

        Parse the video page in soup.

        Parameters:
            soup: BeautifulSoup
                The soup of video page.
        
        Return:
            Type: dict
            The video page's information.
            Like:
            {
                "cover": str,                           # The video's cover link.
                "orgCover": str,                        # The video's original cover link.
                "views": int,                           # The video's views.
                "breadCategories": [{                   # The video's bread categories.
                    "title": str,                       # The bread category's title.
                    "link": str,                        # The bread category's link.
                    "name": str                         # The bread category's name.
                }],
                "title": str,                           # The video's title.
                "categories": [{                        # The video's categories.
                    "title": str,                       # The category's title.
                    "link": str,                        # The category's link.
                    "name": str                         # The category's name.
                }],
                "directors": [{                         # The video's directors.
                    "title": str,                       # The director's title.
                    "link": str,                        # The director's link.
                    "name": str                         # The director's name.
                }],
                "actors": [{                            # The video's actors.
                    "title": str,                       # The actor's title.
                    "link": str,                        # The actor's link.
                    "name": str                         # The actor's name.
                }],
                "more": str,                            # The video's more information.
                "story": str,                           # The video's story.
                "tags": [{                              # The video's tags.
                    "title": str,                       # The tag's title.
                    "link": str,                        # The tag's link.
                    "name": str                         # The tag's name.
                }],
                "videos": [{                            # The video's recommended videos.
                    "id": str,                          # The video's id.
                    "title": str,                       # The video's title.
                    "cover": str,                       # The video's cover link.
                    "link": str,                        # The video's link.
                    "name": str                         # The video's name.
                }],
                "downloadLinks": {                      # The video's download information.
                    "posterLink": str,                  # The video's poster link.
                    "data": [{                          # The video's download links.
                        "file": str,                    # The video's download link.
                        "label": str,                   # The video's download resolution.
                        "type": str                     # The video's extended name.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 转移到 parseVideoPage 接口。")
        return wazi9xxx.parseVideoPage(self, soup)
    
    def search(self, keyword, page):
        """
        wazi9xxx.search(self, keyword, page)
        *Preliminary.*

        Web search.

        Parameters:
            keyword: str
                The keyword to search.
            
            page: int or str
                The page to search. Start from 1.
        
        Return:
            Type: list
            List of movies.
            Like:
            [{
                "id": str,              # The movie's id.
                "title": str,           # The movie's title.
                "cover": str,           # The movie's cover link.
                "link": str,            # The movie's link.
                "name": str,            # The movie's name.
                "story": str,           # The movie's story.
                "views": int            # The movie's views.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已收到搜索关键词和页码： {keyword}， {page}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL 字符串。")
        if page > 1:
            url = f"{self.baseURL}page/{page}/?s={keyword}"
        else:
            url = f"{self.baseURL}?s={keyword}"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 字符串合成完毕，为 {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseSearch 接口。")
        return wazi9xxx.parseSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getVideo(self, videoId, name):
        """
        wazi9xxx.getVideo(self, videoId, name)
        *To die hating them, that was freedom. -- George Orwell*

        Get the video.

        Parameters:
            videoId: str or int
                The video's id.
            
            name: str
                The video's name.
        
        Return:
            Type: dict
            The video page's information.
            Like:
            {
                "cover": str,                           # The video's cover link.
                "orgCover": str,                        # The video's original cover link.
                "views": int,                           # The video's views.
                "breadCategories": [{                   # The video's bread categories.
                    "title": str,                       # The bread category's title.
                    "link": str,                        # The bread category's link.
                    "name": str                         # The bread category's name.
                }],
                "title": str,                           # The video's title.
                "categories": [{                        # The video's categories.
                    "title": str,                       # The category's title.
                    "link": str,                        # The category's link.
                    "name": str                         # The category's name.
                }],
                "directors": [{                         # The video's directors.
                    "title": str,                       # The director's title.
                    "link": str,                        # The director's link.
                    "name": str                         # The director's name.
                }],
                "actors": [{                            # The video's actors.
                    "title": str,                       # The actor's title.
                    "link": str,                        # The actor's link.
                    "name": str                         # The actor's name.
                }],
                "more": str,                            # The video's more information.
                "story": str,                           # The video's story.
                "tags": [{                              # The video's tags.
                    "title": str,                       # The tag's title.
                    "link": str,                        # The tag's link.
                    "name": str                         # The tag's name.
                }],
                "videos": [{                            # The video's recommended videos.
                    "id": str,                          # The video's id.
                    "title": str,                       # The video's title.
                    "cover": str,                       # The video's cover link.
                    "link": str,                        # The video's link.
                    "name": str                         # The video's name.
                }],
                "downloadLinks": {                      # The video's download information.
                    "posterLink": str,                  # The video's poster link.
                    "data": [{                          # The video's download links.
                        "file": str,                    # The video's download link.
                        "label": str,                   # The video's download resolution.
                        "type": str                     # The video's extended name.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已收到视频 ID 和视频名称： {videoId}， {name}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在合成 URL 字符串。")
        url = f"{self.baseURL}video_{videoId}/{name}/"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 字符串合成完毕，为 {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseVideo 接口。")
        return wazi9xxx.parseVideo(self, wazi9xxx.returnSoup(self, url))
    
    def downloadVideo(self, videoId, name, path, label):
        """
        wazi9xxx.downloadVideo(self, videoId, name, path, label)
        *Break.*

        Download the video.

        Parameters:
            videoId: str or int
                The video's id.
            
            name: str
                The video's name.

            path: str
                The path to save the video.
            
            label: str
                The video's resolution.
                Like "480p"
                If is None, will download the all.
        
        Return:
            Type: bool
            If the video is downloaded successfully, return True.
            Else, return False.
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Warn:
                    + Resolution is not supported.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已收到视频 ID ，视频名称，保存路径和清晰度： {videoId}， {name}， {path}， {label}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}video_{videoId}/{name}/"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 构建完毕，为 {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseVideo 接口。")
        video = wazi9xxx.parseVideo(self, wazi9xxx.returnSoup(self, url))
        waziLog.log("debug", f"({self.name}.{fuName}) 正在提取相关信息。")
        poster = video["downloadLinks"]["posterLink"]
        data = video["downloadLinks"]["data"]
        cover = video["orgCover"]
        title = video["title"]
        waziLog.log("debug", f"({self.name}.{fuName}) 提取完毕，为 {poster}， {data}， {cover}， {title}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在下载封面。")
        coverStatus = wazi9xxx.downloadFile(
            self,
            cover,
            self.fileName.toRight(title + "." + cover.split(".")[-1]),
            os.path.join(path, title)
        )
        waziLog.log("debug", f"({self.name}.{fuName}) 正在下载海报。")
        posterStatus = wazi9xxx.downloadFile(
            self,
            poster,
            self.fileName.toRight(title + "-poster." + poster.split(".")[-1].split("?")[0]),
            os.path.join(path, title)
        )
        waziLog.log("debug", f"({self.name}.{fuName}) 正在下载视频。")
        if label:
            for item in data:
                if item["label"] == label:
                    waziLog.log("debug", f"({self.name}.{fuName}) 清晰度为 {label}，为 {item['file']}。")
                    waziLog.log("debug", f"({self.name}.{fuName}) 开始下载。")
                    videoStatus = wazi9xxx.downloadFile(
                        self,
                        item["file"],
                        self.fileName.toRight(title + "-" + label + "." + item["type"]),
                        os.path.join(path, title),
                        True
                    )
                    waziLog.log("info", f"({self.name}.{fuName}) 下载情况如下： {coverStatus}， {posterStatus}， {videoStatus}。")
                    return coverStatus and posterStatus and videoStatus
            waziLog.log("warn", f"({self.name}.{fuName}) 无法找到清晰度为 {label} 的视频。")
            return False
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 视频全部下载。")
            videoStatuses = []
            for item in data:
                waziLog.log("debug", f"({self.name}.{fuName}) 清晰度为 {item['label']}，为 {item['file']}。")
                videoStatus = wazi9xxx.downloadFile(
                    self,
                    item["file"],
                    self.fileName.toRight(title + "-" + item["label"] + "." + item["type"]),
                    os.path.join(path, title),
                    True
                )
                videoStatuses.append(videoStatus)
            waziLog.log("info", f"({self.name}.{fuName}) 下载情况如下： {coverStatus}， {posterStatus}， {videoStatus}。")
            return coverStatus and posterStatus and all(videoStatuses)
    
    def getCategory(self, category, page, sort = None):
        """
        wazi9xxx.getCategory(self, category, page, sort = None)
        *Maintain.*

        Get the category page information.

        Parameters:
            category: str
                The category's name.
            
            page: int or str
                The page number. Start from 1.
            
            sort: str
                The sort method.
                If is None, will use the default sort.
                You can use "date", "views", "comments" & "imdb" (may cause error)
                Default: None
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 {category} 类别的第 {page} 页。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        if page > 1:
            url = f"{self.baseURL}video_category/{category}/page/{page}/"
        else:
            url = f"{self.baseURL}video_category/{category}/"
        if sort:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在增加排序后缀至 URL。")
            url += f"?sort={sort}"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseMainAndCategory 接口。")
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
    
    def getTag(self, tag, page):
        """
        wazi9xxx.getTag(self, tag, page)
        *Transit.*

        Get the tag page information.

        Parameters:
            tag: str
                The tag's name.
            
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
            
            Index 2:
                Recent posts list.
                Like:
                [{
                    "title": str,                   # The post's title.
                    "link": str,                    # The post's link.
                    "name": str                     # The post's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 {tag} 标签的第 {page} 页。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        if page > 1:
            url = f"{self.baseURL}video_tags/{tag}/page/{page}/"
        else:
            url = f"{self.baseURL}video_tags/{tag}/"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseTagAndMoreSearch 接口。")
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getActor(self, actor, page):
        """
        wazi9xxx.getActor(self, actor, page)
        *Hopeless.*

        Get the actor page information.

        Parameters:
            actor: str
                The actor's name.
            
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
            
            Index 2:
                Recent posts list.
                Like:
                [{
                    "title": str,                   # The post's title.
                    "link": str,                    # The post's link.
                    "name": str                     # The post's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 {actor} 演员的第 {page} 页。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        if page > 1:
            url = f"{self.baseURL}video_stars/{actor}/page/{page}/"
        else:
            url = f"{self.baseURL}video_stars/{actor}/"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseTagAndMoreSearch 接口。")
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getDirector(self, director, page):
        """
        wazi9xxx.getDirector(self, director, page)
        *Mildly.*

        Get the director page information.

        Parameters:
            director: str
                The director's name.
            
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
            
            Index 2:
                Recent posts list.
                Like:
                [{
                    "title": str,                   # The post's title.
                    "link": str,                    # The post's link.
                    "name": str                     # The post's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 {director} 导演的第 {page} 页。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        if page > 1:
            url = f"{self.baseURL}video_director/{director}/page/{page}/"
        else:
            url = f"{self.baseURL}video_director/{director}/"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseTagAndMoreSearch 接口。")
        return wazi9xxx.parseTagAndMoreSearch(self, wazi9xxx.returnSoup(self, url))
    
    def getPage(self, page):
        """
        wazi9xxx.getPage(self, page)
        *At Home.*

        Get the page information.

        Parameters:
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: tuple
            Tuple of list of information.
            Index 0:
                Movies list.
                Like:
                [{
                    "id": str,              # The movie's id.
                    "title": str,           # The movie's title.
                    "cover": str,           # The movie's cover link.
                    "link": str,            # The movie's link.
                    "name": str,            # The movie's name.
                    "story": str,           # The movie's story.
                    "views": int            # The movie's views.
                }]
            
            Index 1:
                Tags list.
                Like:
                [{
                    "id": str,                   # The tag's id.
                    "title": str,                # The tag's title.
                    "link": str,                 # The tag's link.
                    "name": str                  # The tag's name.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取第 {page} 页。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}page/{page}/"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseMainAndCategory 接口。")
        return wazi9xxx.parseMainAndCategory(self, wazi9xxx.returnSoup(self, url))
