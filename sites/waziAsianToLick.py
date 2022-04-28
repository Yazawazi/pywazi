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
        """
        waziAsianToLick.parseXML(self, soup)
        *To be continued.*

        Parse the XML.

        Parameters:
            soup: BeautifulSoup
                The BeautifulSoup object. XML page.
        
        Return:
            Type: list
            A list of information.
            Like:
            [{
                "url": str,                 # The url of the information.
                "name": str,                # The name of the information.
                "priority": float,          # The priority of the information.
                "id": str,                  # The id of the information.
                "title": str                # The title of the information.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取信息。")
        urls = soup.find("urlset").find_all("url")
        urlsList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　<url> 标签集合，正在进行一个遍历。")
        for url in urls:
            urlId = url.find("loc").text.strip().split("/")[3].split("-")[1]
            if url.find("loc").text.strip() == self.baseURL:
                urlId = None
            title = url.find("loc").text.strip().split("/")[-1]
            if url.find("loc").text.strip() == self.baseURL:
                title = None
            urlsList.append({
                "url": url.find("loc").text.strip(),
                "lastmod": url.find("lastmod").text.strip(),
                "priority": float(url.find("priority").text.strip()),
                "id": urlId,
                "title": title
            })
        waziLog.log("info", f"({self.name}.{fuName}) 信息获取完毕： {urlsList}")
        return urlsList
    
    def parseCategoriesAndTags(self, soup):
        """
        waziAsianToLick.parseCategoriesAndTags(self, soup)
        *Unbengable.*

        Get the categories and tags from the soup.

        Parameters:
            soup: BeautifulSoup
                The BeautifulSoup object.
        
        Return:
            Type: Tuple
            A tuple of categories and tags.
            Index 0:
                Categories:
                [{
                    "url": str,                 # The url of the category.
                    "id": str,                  # The id of the category.
                    "title": str                # The title of the category.
                    "img": str                  # The img of the category.
                    "pageNum": int              # The page number of the category.
                    "hashTag": str              # The hash tag of the category.
                }]
            
            Index 1:
                Tags:
                [{
                    "url": str,                 # The url of the tag.
                    "id": str,                  # The id of the tag.
                    "title": str                # The title of the tag.
                    "img": str                  # The img of the tag.
                    "pageNum": int              # The page number of the tag.
                    "hashTag": str              # The hash tag of the tag.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取分类和标签。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取容器 div。")
        info = soup.find("div", {
            "id": "container"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not info:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到容器 div，请检查相关代码，返回 {([], [])}")
            return [], []
        waziLog.log("debug", f"({self.name}.{fuName}) 容器 div 获取完成，正在获取所有子 <a> 标签。")
        info = info.find_all("a")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，再次进行空值检查。")
        if not info:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到所有子 <a> 标签，请检查相关代码，返回 {([], [])}")
            return [], []
        categories = []
        tags = []
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到所有子 <a> 标签，正在进行一个遍历。")
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
        waziLog.log("info", f"({self.name}.{fuName}) 分类和标签获取完毕： {(categories, tags)}")
        return categories, tags
    
    def parsePost(self, soup):
        """
        waziAsianToLick.parsePost(self, soup)
        *Winable.*

        Get the post information from the soup.

        Parameters:
            soup: BeautifulSoup
                The BeautifulSoup object.
        
        Return:
            Type: Dict
            The post information.
            Like：
            {
                "title": str,                           # The title of the post.
                "info": [{                              # The information of the post.
                    "key": str,                         # The key of the info.
                    "value": str                        # The value of the info.
                }]                          
                "imgs": [{                              # The imgs of the post.
                    "org": str,                         # The original url of the img.
                    "thumb": str                        # The thumbnail url of the img.
                }],
                "videos": [{                            # The videos of the post.
                    "poster": str,                      # The poster url of the video.
                    "src": str                          # The src url of the video.
                }]
                "imgsNum": int,                         # The number of the imgs.
                "videosNum": int,                       # The number of the videos.
                "like": int,                            # The number of the likes.
                "unLike": int,                          # The number of the unLikes.
                "category": {                           # The category of the post.
                    "url": str,                         # The url of the category.
                    "id": str,                          # The id of the category.
                    "title": str,                       # The title of the category.
                    "name": str                         # The name of the category.
                }
                "tags": [{                              # The tags of the post.
                    "url": str,                         # The url of the tag.
                    "id": str,                          # The id of the tag.
                    "title": str                        # The title of the tag.
                    "name": str                         # The name of the tag.
                }]           
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the divs or article from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已获取到　Soup，正在准备获取文章信息。")
        article = soup.find("article")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not article:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到文章信息，请检查相关代码，返回空字典！")
            return {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取基本信息。")
        metadata = article.find("div", {
            "id": "metadata_qrcode"
        }).find_all("span")
        waziLog.log("debug", f"({self.name}.{fuName}) 基本信息获取完成，正在获取图集信息。")
        imgDivs = article.find_all("div", {
            "class": "gallery_img"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 图集信息获取完成，正在获取视频信息。")
        videoElements = article.find_all("video")
        waziLog.log("debug", f"({self.name}.{fuName}) 视频信息获取完成，正在解析基本信息。")
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
        waziLog.log("debug", f"({self.name}.{fuName}) 基本信息解析完成： {infos}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在解析图集信息和视频信息。")
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
        waziLog.log("debug", f"({self.name}.{fuName}) 图集信息解析完成： {imgs}")
        waziLog.log("debug", f"({self.name}.{fuName}) 视频信息解析完成： {videos}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取分类和标签。")
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
        waziLog.log("debug", f"({self.name}.{fuName}) 分类和标签获取完成： {category}, {tags}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取赞/踩数据。")
        script = article.find("script")
        likeNumber = int(script.text.strip().split("var likes = ")[1].split(";")[0])
        unLikeNumber = int(script.text.strip().split("var unlikes = ")[1].split(";")[0])
        waziLog.log("debug", f"({self.name}.{fuName}) 赞/踩数据获取完成： {likeNumber}, {unLikeNumber}")
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
        waziLog.log("info", f"({self.name}.{fuName}) POST 信息获取完成： {post}")
        return post
        
    def getAjaxPosts(self, soup):
        """
        waziAsianToLick.getAjaxPosts(self, soup)
        *Office Life*

        Get posts from ajax page.

        Parameters:
            soup: BeautifulSoup
                BeautifulSoup object from ajax page.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the <a> set from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 ajax 页面的 <a> 标签。")
        posts = soup.find_all("a")
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not posts:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到 <a> 标签集合，请检查相关代码，返回空列表！")
            return []
        postsList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进入遍历分析。")
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
            title = BeautifulSoup(re.sub('<span class="tt_tag_[a-zA-Z]+.*?">[a-zA-Z]+.*?</span>', "", str(baseTt.span)),
                                  "lxml").text.strip()
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
                "title": title,
            })
        waziLog.log("info", f"({self.name}.{fuName}) 该页面中所有 Post 获取完成： {postsList}")
        return postsList
    
    def getTrueDownloadURL(self, soup):
        """
        waziAsianToLick.getTrueDownloadURL(self, soup)
        *Weeping Angel*

        Get the post's true download url.

        Parameters:
            soup: BeautifulSoup
                BeautifulSoup object from download page.
        
        Return:
            Type: str
            The download url.
        
        Errors:
            Python:
                Perhaps there are potential errors. 
            
            Logs:
                Error:
                    + Cannot get the <span id="download_post"> from soup.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已收到 Soup，正在获取 download_post 信息。")
        downloadPost = soup.find("span", {
            "id": "download_post"
        })
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在进行空值检查。")
        if not downloadPost:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取到 download_post 信息，请检查相关代码，返回空字符串！")
            return ""
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取下载必须数据。")
        postId = downloadPost.get("post_id")
        postName = downloadPost.get("post_name")
        dirPath = downloadPost.get("dir")
        waziLog.log("debug", f"({self.name}.{fuName}) ID： {postId}，名称： {postName}，下载目录： {dirPath}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}ajax/download_post.php?ver=1&dir=/{dirPath}&post_id={postId}&post_name={quote(postName)}"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成，正在请求。")
        downloadURL = waziAsianToLick.returnSoup(self, url, False, True, True)
        waziLog.log("info", f"({self.name}.{fuName}) 获取 URL 完成： {downloadURL}")
        return downloadURL
    
    def getSiteMapPosts(self):
        """
        waziAsianToLick.getSiteMapPosts(self)
        *Image Link: https://i.imgur.com/ (Copilot Pls)*

        Get the posts on site map.

        Return:
            Type: list
            The posts list.
            Like:
            [{
                "url": str,                 # The url of the post.
                "name": str,                # The name of the post.
                "priority": float,          # The priority of the post.
                "id": str,                  # The id of the post.
                "title": str                # The title of the post.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}sitemap/post.xml"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseXML 接口。")
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def getSiteMapCategories(self):
        """
        waziAsianToLick.getSiteMapCategories(self)
        *V1.0.0*

        Get the categories on site map.

        Return:
            Type: list
            The categories list.
            Like:
            [{
                "url": str,                 # The url of the category.
                "name": str,                # The name of the category.
                "priority": float,          # The priority of the category.
                "id": str,                  # The id of the category.
                "title": str                # The title of the category.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}sitemap/category.xml"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseXML 接口。")
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def getSiteMapTags(self):
        """
        waziAsianToLick.getSiteMapTags(self)
        *Bass Boost*

        Get the tags on site map.

        Return:
            Type: list
            The tags list.
            Like:
            [{
                "url": str,                 # The url of the tag.
                "name": str,                # The name of the tag.
                "priority": float,          # The priority of the tag.
                "id": str,                  # The id of the tag.
                "title": str                # The title of the tag.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}sitemap/tags.xml"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 parseXML 接口。")
        return waziAsianToLick.parseXML(self, waziAsianToLick.returnSoup(self, url, True))
    
    def get(self, post, cat, tag, search, page, index, ver):
        """
        waziAsianToLick.get(self, post, cat, tag, search, page, index, ver)
        *Sleep now?*

        Get the posts from ajax but not by soup.

        Parameters:
            post: str or int or None
                The post id.
            
            cat: str or int or None
                The category id.
            
            tag: str or int or None
                The tag id.
            
            search: str or None
                The search keyword.
            
            page: str or None
                The page. Only "news" supported.
            
            index: str or int or None
                The index of the post. Like normal "page". Start from 0.
            
            ver: str or int or None
                The version of the post.(?)
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.  
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) POST ID： {post}， 分类： {cat}， 标签： {tag}， 搜索： {search}， 页面： {page}"
                             f"， 页码： {index}， 版本： {ver}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}ajax/buscar_posts.php?post={post}&cat={cat}&tag={tag}&search={search}&page={page}" \
              f"&index={index}&ver={ver}"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 getAjaxPosts 接口。")
        return waziAsianToLick.getAjaxPosts(self, waziAsianToLick.returnSoup(self, url, False))
    
    def getPage(self, page):
        """
        waziAsianToLick.getPage(self, page)
        *How we do it?*

        Get the posts from ajax by page.

        Parameters:
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码信息： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
        return waziAsianToLick.get(
            self,
            "",
            "",
            "",
            "",
            "",
            page,
            ""
        )
    
    def getPostRecommendsByPost(self, postId, name, page):
        """
        waziAsianToLick.getPostRecommendsByPost(self, postId, name, page)
        *Busy*

        Get the recommends from ajax by post id.

        Parameters:
            postId: str or int
                The post id.
            
            name: str
                The name of the post.
            
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) POST ID： {postId}， 名称： {name}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}post-{postId}/{name}"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建完成： {url}，正在获取画廊信息。")
        info = waziAsianToLick.parsePost(self, waziAsianToLick.returnSoup(self, url, False))
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在构建参数。")
        tags = ","
        for i in info["tags"]:
            tags += i["id"] + ","
        tags = tags[:-1]
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
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
    
    def getCategory(self, cat, page):
        """
        waziAsianToLick.getCategory(self, cat, page)
        *Way*

        Get the posts from ajax by category.

        Parameters:
            cat: str or int
                The category.
        
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 类别： {cat}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
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
        """
        waziAsianToLick.getTag(self, tag, page)
        *Work and work not well.*

        Get the posts from ajax by tag.

        Parameters:
            tag: str or int
                The tag.
        
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 标签： {tag}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
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
        """
        waziAsianToLick.getNews(self, page)
        *Moyu and moyu well.*

        Get the posts from ajax by time order.

        Parameters:
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
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
        """
        waziAsianToLick.search(self, keyword, page)
        *4.22 PyWazi's Birthday.*

        Get the posts from ajax by search keyword.

        Parameters:
            keyword: str
                The keyword.
            
            page: str or int
                The page. Start from 0.
        
        Return:
            Type: list
            The posts.
            Like:
            [{
                "url": str,                         # Post url.
                "hashId": str,                      # Post hash id.
                "cover": str,                       # Post cover.
                "alt": str,                         # Post alt.
                "pageNum": int,                     # Post page number.
                "tags": [{                          # Post tags.
                    "tagClass": str,                # Tag class.
                    "tagName": str,                 # Tag name.
                }],
                "title": str                        # Post title.
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 搜索关键词： {keyword}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 转移至 get 接口。")
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
        """
        waziAsianToLick.getCategoriesAndTags(self)
        *Big Boom.*

        Get the categories and tags.

        Return:
            Type: Tuple
            A tuple of categories and tags.
            Index 0:
                Categories:
                [{
                    "url": str,                 # The url of the category.
                    "id": str,                  # The id of the category.
                    "title": str                # The title of the category.
                    "img": str                  # The img of the category.
                    "pageNum": int              # The page number of the category.
                    "hashTag": str              # The hash tag of the category.
                }]
            
            Index 1:
                Tags:
                [{
                    "url": str,                 # The url of the tag.
                    "id": str,                  # The id of the tag.
                    "title": str                # The title of the tag.
                    "img": str                  # The img of the tag.
                    "pageNum": int              # The page number of the tag.
                    "hashTag": str              # The hash tag of the tag.
                }]
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求，正在构建 URL。")
        url = f"{self.baseURL}page/categories"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 构建完毕： {url}，转移至 parseCategoriesAndTags 接口。")
        return waziAsianToLick.parseCategoriesAndTags(self, waziAsianToLick.returnSoup(self, url, False))
    
    def getPost(self, postId, name):
        """
        waziAsianToLick.getPost(self, postId, name)
        *Life is short, I use nothing.*

        Get the post by post id and name.

        Parameters:
            postId: int or str
                The post id.
            
            name: str
                The name of the post.
        
        Return:
            Type: Dict
            The post information.
            Like：
            {
                "title": str,                           # The title of the post.
                "info": [{                              # The information of the post.
                    "key": str,                         # The key of the info.
                    "value": str                        # The value of the info.
                }]                          
                "imgs": [{                              # The imgs of the post.
                    "org": str,                         # The original url of the img.
                    "thumb": str                        # The thumbnail url of the img.
                }],
                "videos": [{                            # The videos of the post.
                    "poster": str,                      # The poster url of the video.
                    "src": str                          # The src url of the video.
                }]
                "imgsNum": int,                         # The number of the imgs.
                "videosNum": int,                       # The number of the videos.
                "like": int,                            # The number of the likes.
                "unLike": int,                          # The number of the unLikes.
                "category": {                           # The category of the post.
                    "url": str,                         # The url of the category.
                    "id": str,                          # The id of the category.
                    "title": str,                       # The title of the category.
                    "name": str                         # The name of the category.
                }
                "tags": [{                              # The tags of the post.
                    "url": str,                         # The url of the tag.
                    "id": str,                          # The id of the tag.
                    "title": str                        # The title of the tag.
                    "name": str                         # The name of the tag.
                }]           
            }
        
        Errors:
            Python:
                Perhaps there are potential errors. 
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求，正在构建 URL。")
        url = f"{self.baseURL}post-{postId}/{name}"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 构建完毕： {url}，转移至 parsePost 接口。")
        return waziAsianToLick.parsePost(self, waziAsianToLick.returnSoup(self, url, False))
    
    def downloadPostByNative(self, postId, name, path, key = "org", video = True):
        """
        waziAsianToLick.downloadPostByNative(self, postId, name, path, key = "org", video = True)
        *Life is long, I play for fun.*

        Download the post by post id and name.
        And the download method is made by myself not by website.
        Try waziAsianToLick.downloadPost instead, it will download a zip file from website directly.

        Parameters:
            postId: int or str
                The post id.
            
            name: str
                The name of the post.
            
            path: str
                The save path of the post.
            
            key: str
                The key of the img.
                You can choose "org" or "thumb".
                org: The original url of the img.
                thumb: The thumbnail url of the img.
                Default: "org"
            
            video: bool
                Whether to download the video.
        
        Return:
            Type: tuple
            Download Information.
            (
                list[str],                                      # The downloaded files.
                list[str]                                       # The failed files' urls.
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) POST ID： {postId}，名称： {name}，"
                             f"保存路径： {path}，图片 key： {key}，是否下载视频： {video}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取 POST 信息。")
        info = waziAsianToLick.getPost(self, postId, name)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取 POST 信息完毕，进行空值检查。")
        if not info:
            waziLog.log("error", f"({self.name}.{fuName}) 获取 POST 信息失败，请检查参数！")
            return False
        title = info["title"]
        downloadFiles = []
        cannotDownloadFiles = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进行遍历下载。")
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
                waziLog.log("warn", f"({self.name}.{fuName}) 文件 {i[key]} 下载失败，将跳过。")
                cannotDownloadFiles.append(i[key])
        if video:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要下载视频，正在进行遍历下载。")
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
                    waziLog.log("warn", f"({self.name}.{fuName}) 文件 {i['src']} 下载失败，将跳过。")
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
                    waziLog.log("warn", f"({self.name}.{fuName}) 文件 {i['poster']} 下载失败，将跳过。")
                    cannotDownloadFiles.append(i["poster"])
        waziLog.log("info", f"({self.name}.{fuName}) 下载完毕，返回结果： {(downloadFiles, cannotDownloadFiles)}")
        return downloadFiles, cannotDownloadFiles

    def getPostDownloadURL(self, postId):
        """
        waziAsianToLick.getPostDownloadURL(self, postId)
        *ooo*

        Get the download url of the post.

        Parameters:
            postId: int or str
                The post id.
        
        Return:
            Type: str
            The download url of the post.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) POST ID： {postId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}download-{postId}/download"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建 URL 完毕，转移至 getTrueDownloadURL 接口。")
        return waziAsianToLick.getTrueDownloadURL(self, waziAsianToLick.returnSoup(self, url, False))

    def downloadPost(self, postId, path):
        """
        waziAsianToLick.downloadPost(self, postId, path)
        *Nara.*

        Download the post.
        It's faster than waziAsianToLick.downloadPostByNative.

        Parameters:
            postId: int or str
                The post id.
            
            path: str
                The path to save the post.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Logs:
                Error:
                    + No download link get.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) POST ID： {postId}， 保存路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在构建 URL。")
        url = f"{self.baseURL}download-{postId}/download"
        waziLog.log("debug", f"({self.name}.{fuName}) 构建 URL 完毕，正在获取 Soup。")
        soup = waziAsianToLick.returnSoup(self, url, False)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完毕，正在获取标题。")
        try:
            title = soup.find("h1").text.strip()
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 标题获取失败，请检查相关参数！")
            return False
        waziLog.log("debug", f"({self.name}.{fuName}) 标题获取完毕，正在获取下载链接。")
        link = waziAsianToLick.getTrueDownloadURL(self, soup)
        waziLog.log("debug", f"({self.name}.{fuName}) 下载链接获取完毕，进行空值检查。")
        if not link:
            waziLog.log("error", f"({self.name}.{fuName}) 下载链接获取失败，请检查相关参数！")
            return False
        waziLog.log("debug", f"({self.name}.{fuName}) 正在下载文件。")
        return waziAsianToLick.downloadFile(
            self,
            link,
            self.fileName.toRight(link.split("/")[-1]),
            os.path.join(path, self.fileName.toRight(title)),
            True
        )
