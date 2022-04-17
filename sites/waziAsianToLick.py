import os
import re
from mods import waziFun
from bs4 import BeautifulSoup
from urllib.parse import quote
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
    
    def returnSoup(self, link, xml, soupOff = False, headersOff = False):
        """
        waziAsianToLick.returnSoup(self, link, xml, soupOff = False, headersOff = False)
        *Copy from waziNyaa*

        Request a link and return a BeautifulSoup.

        Parameters:
            link: str
                A link to request.

            xml: bool
                Whether the link is xml or not.
            
            soupOff: bool
                Whether to return a BeautifulSoup or not.
                Default: False
            
            headersOff: bool
                Whether to turn off the headers or not.
                Default: False
        
        Return:
            Type: BeautifulSoup or str
            A BeautifulSoup of the requested link or the requested link.
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
        if not headersOff:
            tempParams = self.params
            tempParams["useHeaders"] = True
        else:
            tempParams = self.params
            tempParams["useHeaders"] = False
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) 需要检查 URL 并进行处理。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起网络请求。")
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            if xml:
                soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "xml")
            else:
                if soupOff:
                    soup = self.request.do(requestParams).data.decode("utf-8")
                else:
                    soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取，返回无效 Soup。")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 获取成功，Soup 返回中。")
            return soup
    
    def downloadFile(self, url, name, path, video = False):
        """
        waziAsianToLick.downloadFile(self, url, name, path, video = False)
        *Copy again.*

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
    
    def parseCategoriesAndTags(self, soup):
        info = soup.find("div", {
            "id": "container"
        })
        if not info:
            return [], []
        info = info.find_all("a")
        if not info:
            return [], []
        categories = []
        tags = []
        for i in info:
            infoDict = {
                "url": i.get("href"),
                "id": i.get("href").strip().split("/")[3].split("-")[1],
                "title": i.get("href").strip().split("/")[-1],
                "img": i.find("img").get("src"),
                "pageNum": int(i.find("div", {
                    "class": "contar_imagens"
                }).text.strip()),
                "hashTag": i.find("span", {
                    "class": "titulo_tag"
                }).text.strip()
            }
            if "category" in i.get("href"):
                categories.append(infoDict)
            else:
                tags.append(infoDict)
        return categories, tags
    
    def parsePost(self, soup):
        article = soup.find("article")
        if not article:
            return {}
        metadata = article.find("div", {
            "id": "metadata_qrcode"
        }).find_all("span")
        imgDivs = article.find_all("div", {
            "class": "gallery_img"
        })
        videoElements = article.find_all("video")
        if not metadata or not imgDivs or not videoElements:
            return {}
        infos = []
        for i in metadata:
            if i.b.text.strip() == "描述：":
                infos.append({
                    "key": "description",
                    "value": i.text.strip().replace("描述：", "").strip()
                })
            elif i.b.text.strip() == "创立日期：":
                infos.append({
                    "key": "createDate",
                    "value": i.text.strip().replace("创立日期：", "").strip()
                })
            elif i.b.text.strip() == "Creation date:":
                infos.append({
                    "key": "createDate",
                    "value": i.text.strip().replace("Creation date:", "").strip()
                })
            elif i.b.text.strip() == "Gallery pictures:":
                infos.append({
                    "key": "gallery",
                    "value": int(i.text.strip().replace("Gallery pictures:", "").strip().replace("pics", "").strip())
                })
            elif i.b.text.strip() == "Photos size:":
                infos.append({
                    "key": "photosSize",
                    "value": i.text.strip().replace("Photos size:", "").strip()
                })
            elif i.b.text.strip() == "Album size:":
                infos.append({
                    "key": "albumSize",
                    "value": i.text.strip().replace("Album size:", "").strip()
                })
            elif i.b.text.strip() == "下载:":
                infos.append({
                    "key": "downloadLink",
                    "value": i.a.get("href")
                })
            else:
                infos.append({
                    "key": i.b.text.replace("：", "").replace(":", "").strip(),
                    "value": i.text.strip().replace(i.b.text, "").strip()
                })
        imgs = []
        for i in imgDivs:
            imgs.append({
                "org": i.attrs["data-src"],
                "thumb": i.find("img").get("src"),
            })
        videos = []
        for i in videoElements:
            videos.append({
                "poster": i.get("poster"),
                "src": i.find("source").get("src"),
            })
        category = {}
        tags = []
        categoryAndTags = article.find("div", {
            "id": "categoria_tags_post"
        }).find_all("a")
        for i in categoryAndTags:
            info = {
                "url": i.get("href"),
                "id": i.get("href").strip().split("/")[3].split("-")[1],
                "title": i.get("href").strip().split("/")[-1],
                "name": i.text.strip()
            }
            if "category" in i.get("href"):
                category = info
            else:
                tags.append(info)
        script = article.find("script")
        likeNumber = int(script.text.strip().split("var likes = ")[1].split(";")[0])
        unLikeNumber = int(script.text.strip().split("var unlikes = ")[1].split(";")[0])
        post = {
            "title": article.find("h1").text.strip(),
            "info": infos,
            "imgs": imgs,
            "videos": videos,
            "imgsNum": len(imgs),
            "videosNum": len(videos),
            "like": likeNumber,
            "unLike": unLikeNumber,
            "category": category,
            "tags": tags,
        }
        return post
        
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
                for span in spans:
                    if "tt_tag" in span.get("class")[0]:
                        tags.append({
                            "tagClass": span.get("class")[0],
                            "tagName": span.text.strip()
                        })
            postsList.append({
                "url": post.get("href"),
                "hashId": post.get("id"),
                "cover": post.find("div", {
                    "class": "background_miniatura"
                }).find("img").get("src"),
                "alt": post.find("div", {
                    "class": "background_miniatura"
                }).find("img").get("alt").strip(),
                "pageNum": int(post.find("div", {
                    "class": "contar_imagens"
                }).text.strip()),
                "tags": tags,
                "title": BeautifulSoup(re.sub('<span class="tt_tag_[a-zA-Z]+.*?">[a-zA-Z]+.*?</span>', "", str(baseTt.span)), "lxml").text.strip(),
            })
        return postsList
    
    def getTrueDownloadURL(self, soup):
        downloadPost = soup.find("span", {
            "id": "download_post"
        })
        if not downloadPost:
            return ""
        postId = downloadPost.get("post_id")
        postName = downloadPost.get("post_name")
        dir = downloadPost.get("dir")
        url = f"{self.baseURL}ajax/download_post.php?ver=1&dir=/{dir}&post_id={postId}&post_name={quote(postName)}"
        downloadURL = waziAsianToLick.returnSoup(self, url, False, True, True)
        return downloadURL
    
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
    
    def getPage(self, page):
        return waziAsianToLick.get(self, "", "", "", "", page, "")
    
    def getPostRecommendsByPost(self, postId, name, page):
        url = f"{self.baseURL}post-{postId}/{name}"
        info = waziAsianToLick.parsePost(self, waziAsianToLick.returnSoup(self, url, False))
        tags = ","
        for i in info["tags"]:
            tags += i["id"] + ","
        tags = tags[:-1]
        return waziAsianToLick.get(
            self,
            postId,
            info["category"]["id"],
            tags,
            "",
            "",
            page,
            ""
        )
    
    def getPostRecommends(self, post, cat, tag, page):
        return waziAsianToLick.get(
            self,
            post,
            cat,
            tag,
            "",
            "",
            page,
            ""
        )
    
    def getCategory(self, cat, page):
        return waziAsianToLick.get(
            self,
            "",
            cat,
            "",
            "",
            "",
            page,
            ""
        )
    
    def getTag(self, tag, page):
        return waziAsianToLick.get(
            self,
            "",
            "",
            tag,
            "",
            "",
            page,
            ""
        )
    
    def getNews(self, page):
        return waziAsianToLick.get(
            self,
            "",
            "",
            "",
            "",
            "news",
            page,
            ""
        )
    
    def search(self, keyword, page):
        return waziAsianToLick.get(
            self,
            "",
            "",
            "",
            keyword,
            "",
            page,
            ""
        )
    
    def getCategoriesAndTags(self):
        url = f"{self.baseURL}page/categories"
        return waziAsianToLick.parseCategoriesAndTags(self, waziAsianToLick.returnSoup(self, url, False))
    
    def getPost(self, postId, name):
        url = f"{self.baseURL}post-{postId}/{name}"
        return waziAsianToLick.parsePost(self, waziAsianToLick.returnSoup(self, url, False))
    
    def downloadPostByNative(self, postId, name, path, key = "org", video = True):
        info = waziAsianToLick.getPost(self, postId, name)
        title = info["title"]
        if not info:
            return False
        downloadFiles = []
        cannotDownloadFiles = []
        for i in info["imgs"]:
            if (waziAsianToLick.downloadFile(
                self,
                i[key],
                self.fileName.toRight(i[key].split("/")[-1]),
                os.path.join(path, self.fileName.toRight(title))
            )):
                downloadFiles.append(
                    os.path.join(
                        os.path.join(path, self.fileName.toRight(title)),
                        self.fileName.toRight(i[key].split("/")[-1])
                    )
                )
            else:
                cannotDownloadFiles.append(i[key])
        if video:
            for i in info["videos"]:
                if (waziAsianToLick.downloadFile(
                    self,
                    i["src"],
                    self.fileName.toRight(i["src"].split("/")[-1]),
                    os.path.join(path, self.fileName.toRight(title)),
                    True
                )):
                    downloadFiles.append(
                        os.path.join(
                            os.path.join(path, self.fileName.toRight(title)),
                            self.fileName.toRight(i["src"].split("/")[-1])
                        )
                    )
                else:
                    cannotDownloadFiles.append(i["src"])
                if (waziAsianToLick.downloadFile(
                    self,
                    i["poster"],
                    self.fileName.toRight(i["poster"].split("/")[-1]),
                    os.path.join(path, self.fileName.toRight(title))
                )):
                    downloadFiles.append(
                        os.path.join(
                            os.path.join(path, self.fileName.toRight(title)),
                            self.fileName.toRight(i["poster"].split("/")[-1])
                        )
                    )
                else:
                    cannotDownloadFiles.append(i["poster"])
        return downloadFiles, cannotDownloadFiles

    def getPostDownloadURL(self, postId):
        url = f"{self.baseURL}download-{postId}/download"
        return waziAsianToLick.getTrueDownloadURL(self, waziAsianToLick.returnSoup(self, url, False))

    def downloadPost(self, postId, path):
        url = f"{self.baseURL}download-{postId}/download"
        soup = waziAsianToLick.returnSoup(self, url, False)
        title = soup.find("h1").text.strip()
        link = waziAsianToLick.getTrueDownloadURL(self, soup)
        return waziAsianToLick.downloadFile(
            self,
            link,
            self.fileName.toRight(link.split("/")[-1]),
            os.path.join(path, self.fileName.toRight(title)),
            True
        )
