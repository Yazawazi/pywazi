"""
sites/waziAsianSister.py

class: waziAsianSister
"""

import os
from mods import waziFun
from bs4 import BeautifulSoup
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziAsianSister:
    """
    waziAsianSister
    *Skin.*

    A class for crawling AsianSister.

    Attributes:
        request: waziRequest
            waziRequest()
        
        URL: waziURL
            waziURL()
        
        fileName: waziFileName
            waziFileName()
        
        headers: dict
            A dict of headers for requests.
            Default: Chrome on Windows 10
        
        proxies: dict
            A dict of proxies for requests.
            Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.
        
        name: str
            The name of this class.
    
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziAsianSister.__init__(self)
        *Milk.*

        Initialize the class.

        Parameters:
            None
        """
        super(waziAsianSister, self).__init__()
        self.request = waziRequest()
        self.URL = waziURL()
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
        waziAsianSister.giveParams(self, params)
        *Abandonment.*

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
        waziAsianSister.returnSoup(self, link)
        *Dry.*

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
    
    def downloadFile(self, url, name, path, video = False):
        """
        waziAsianSister.downloadFile(self, url, name, path, video = False)
        *Sweet Trouble.*

        Download a file from a link for asiansister.com.

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
        if "asiansister" in url:
            tempHeaders["Referer"] = "https://asiansister.com/"
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
    
    def parseVideo(self, soup):
        """
        waziAsianSister.parseVideo(self, soup)
        *Like a flower.*

        Parse the video information from the soup.

        Parameters:
            soup: BeautifulSoup
                The soup to parse.
                Like: https://asiansister.com/v_vide_247_XXXXXXXXXX

        Return:
            Type: dict
            The video information.
            {
                "title": str,                                   # The title of the video.
                "views": int,                                   # The views of the video.
                "tags": list[dict{"name": str, "link": str}],   # The tags of the video.
                "cover": str,                                   # The cover link of the video.
                "url": str,                                     # The url of the video file.
                "comments": list[dict{                          # The comments of the video.
                    "user": str,                                # The user group.
                    "avatar": str,                              # The avatar link.
                    "name": str,                                # The name of the user.
                    "time": str,                                # The time of the comment.
                    "content": str                              # The content of the comment.
                }],                                             
                "recommends": list[dict{                        # The recommends of the video.
                    "title": str,                               # The title of the video.
                    "link": str,                                # The link of the video.
                    "cover": str,                               # The cover link of the video.
                    "views": int                                # The views of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Parsing the soup that is not from asiansister video may cause the program to crash.)
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        video = {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
        video["title"] = soup.find("div", class_ = "headTitle").text
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频播放量。")
        video["views"] = int(soup.find("div", class_ = "viewCount").text.replace(" views", "").replace(",", ""))
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标签。")
        video["tags"] = []
        for tag in soup.find("div", id = "detailBox").find_all("a"):
            if tag.attrs["href"] == "tag.php?tag=":
                pass
            else:
                video["tags"].append({
                    "name": tag.text,
                    "link": "https://asiansister.com/" + tag.get("href")
                })
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
        video["cover"] = soup.find("video").attrs["poster"]
        if video["cover"].startswith("http"):
            pass
        else:
            video["cover"] = "https://asiansister.com/" + video["cover"]
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频地址。")
        video["url"] = soup.find("video").find("source").attrs["src"]
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频评论。")
        video["comments"] = []
        comments = soup.find("div", id = "comment_box")
        if comments.text == "":
            pass
        else:
            for i in comments.find_all("div", {"style": "padding:15px 10px;"}):
                comment = {}
                if i.find("img").attrs["src"] == "images/icon/admin.png":
                    comment["user"] = "admin"
                elif i.find("img").attrs["src"] == "images/icon/vip.png":
                    comment["user"] = "vip"
                else:
                    comment["user"] = "user"
                if comment["user"] == "user":
                    comment["avatar"] = "https://asiansister.com/" + i.find("img").attrs["src"]
                else:
                    comment["avatar"] = "https://asiansister.com/" + i.find_all("img")[1].attrs["src"]
                comment["name"] = i.find("div", class_ = "commentText").find_all("div")[0].text.strip()
                comment["time"] = i.find("div", class_ = "commentText").find_all("div")[1].text.strip()
                comment["content"] = i.find("div", class_ = "commentText").find_all("div")[2].text.strip()
                video["comments"].append(comment)
        waziLog.log("info", f"({self.name}.{fuName}) 正在获取相关推荐。")
        video["recommends"] = []
        recommend = soup.find("div", class_ = "sub_contant")
        for i in recommend.find_all("a"):
            if i.find("div", class_ = "recommendVideo_Image_Box").attrs["style"].split("url('")[1].split("')")[0].startswith("http"):
                cover = i.find("div", class_ = "recommendVideo_Image_Box").attrs["style"].split("url('")[1].split("')")[0]
            else:
                cover = "https://asiansister.com/" + i.find("div", class_ = "recommendVideo_Image_Box").attrs["style"].split("url('")[1].split("')")[0]
            video["recommends"].append({
                "title": str(i.find("div", class_ = "recommendVideo_Text_Box").text).strip().split("\n")[0],
                "link": "https://asiansister.com/" + i.attrs["href"],
                "cover": cover,
                "views": int(i.find("div", class_ = "recommendVideo_Text_Box").find("div").text.replace(" views", "").replace(",", ""))
            })
        waziLog.log("info", f"({self.name}.{fuName}) 获取完成： {video}，正在返回。")
        return video

    def parseGallery(self, soup):
        """
        waziAsianSister.parseGallery(self, soup)
        *Love.*

        Parse the gallery page.

        Parameters:
            soup: BeautifulSoup
                The soup of the gallery page.
                Like: https://asiansister.com/view_2096_Belle_Delphine__OnlyFans_Friendly_Neighborhoodn
        
        Return:
            Type: dict
            The gallery information.
            May like:
            {
                "title": str,                                       # The title of the gallery.
                "stars": str,                                       # The stars of the gallery, X/Y.
                "category": dict{"name": str, "link": str},         # The category of the gallery.
                "tags": list[dict{"name": str, "link": str}],       # The tags of the gallery.
                "description": str,                                 # The description of the gallery.
                "model": dict{"name": str, "link": str},            # The model of the gallery.
                "covers": list[dict{"link": str, "alt": str}],      # The covers of the gallery.
                "pictures": list[dict{"link": str, "org": str}],    # The pictures of the gallery.
                                                                    # org: The original picture.
                "pageNum": int,                                     # The number of the pictures.
                "comments": list[dict{                              # The comments of the video.
                    "user": str,                                    # The user group.
                    "avatar": str,                                  # The avatar link.
                    "name": str,                                    # The name of the user.
                    "time": str,                                    # The time of the comment.
                    "content": str                                  # The content of the comment.
                }],                                                 
                "galleries": list[dict{                             # The recommend galleries.
                    "link": str,                                    # The link of the recommend gallery.
                    "cover": str,                                   # The cover of the recommend gallery.
                    "alt": str,                                     # The alt of the recommend gallery.
                    "title": str,                                   # The title of the recommend gallery.
                    "stars": str,                                   # The stars of the recommend gallery.
                    "VIP": bool                                     # The VIP status of the recommend gallery.
                }],
                "videos": list[dict{                                # The recommend videos.
                    "data": str or None,                            # The data of the video, None if not found.
                                                                    # data: The moved cover of the video.
                                                                    # I am not sure about this.
                    "link": str,                                    # The link of the video.
                    "title": str,                                   # The title of the video.
                    "cover": str,                                   # The cover of the video.
                    "VIP": bool                                     # The VIP status of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Parsing the soup that is not from asiansister gallery may cause the program to crash.)
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        gallery = {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
        gallery["title"] = soup.find("h1").text
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊评分。")
        gallery["stars"] = soup.find("font").text.strip()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊类别。")
        gallery["category"] = {
            "name": soup.find("div", class_ = "headTitle").find("a").text,
            "link": "https://asiansister.com/" + soup.find("div", class_ = "headTitle").find("a").attrs["href"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标签。")
        gallery["tags"] = []
        for tag in soup.find("div", id = "detailBox").find_all("a"):
            if tag.attrs["href"] == "tag.php?tag=":
                pass
            else:
                gallery["tags"].append({
                    "name": tag.text,
                    "link": "https://asiansister.com/" + tag.attrs["href"]
                })
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊描述。")
        gallery["description"] = soup.find_all("div", class_ = "detailBoxHide")[1].text.strip().replace("<br>", "\n").replace("<br/>", "\n")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查附加基础信息。")
        for i in soup.find_all("div", class_ = "headTitle"):
            if i.text.strip() == "Model / Actor":
                waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊模特信息。")
                gallery["model"] = {
                    "name": soup.find("div", class_ = "modelBox").text,
                    "link": "https://asiansister.com/" + soup.find("div", class_ = "modelBox").find_previous("a").attrs["href"]
                }
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面图片列表。")
        gallery["covers"] = []
        for cover in soup.find("table").find_all("img"):
            gallery["covers"].append({
                "link": "https://asiansister.com/" + cover.attrs["data-src"],
                "alt": cover.attrs["alt"]
            })
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊详细图片列表。")
        gallery["pictures"] = []
        for picture in soup.find("center").find_all("div", class_ = "rootContant")[1].find_all("img"):
            gallery["pictures"].append({
                "link": "https://asiansister.com/" + picture.attrs["data-src"],
                "org": "https://asiansister.com/" + picture.attrs["dataurl"][5:]
            })
        gallery["pageNumber"] = len(gallery["pictures"])
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊评论。")
        gallery["comments"] = []
        comments = soup.find("center").find_all("div", class_ = "rootContant")[2].find("div", id = "comment_box")
        if comments.text == "":
            pass
        else:
            for i in comments.find_all("div", {"style": "padding:15px 10px;"}):
                comment = {}
                if i.find("img").attrs["src"] == "images/icon/admin.png":
                    comment["user"] = "admin"
                elif i.find("img").attrs["src"] == "images/icon/vip.png":
                    comment["user"] = "vip"
                else:
                    comment["user"] = "user"
                if comment["user"] == "user":
                    comment["avatar"] = "https://asiansister.com/" + i.find("img").attrs["src"]
                else:
                    comment["avatar"] = "https://asiansister.com/" + i.find_all("img")[1].attrs["src"]
                comment["name"] = i.find("div", class_ = "commentText").find_all("div")[0].text.strip()
                comment["time"] = i.find("div", class_ = "commentText").find_all("div")[1].text.strip()
                comment["content"] = i.find("div", class_ = "commentText").find_all("div")[2].text.strip()
                gallery["comments"].append(comment)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊推荐。")
        recommend = waziAsianSister.parseRecommendImagesAndVideos(self, soup)
        gallery["galleries"] = recommend[0]
        gallery["videos"] = recommend[1]
        waziLog.log("info", f"({self.name}.{fuName}) 画廊解析完毕，数据返回： {gallery}。")
        return gallery
    
    def parsePerson(self, soup):
        """
        waziAsianSister.parsePerson(self, soup)
        *Virgin.*

        Parse the person page.

        Parameters:
            soup: BeautifulSoup
                The BeautifulSoup object of the page.
                Like: https://asiansister.com/m_6__YUZUKIn
        
        Return:
            Type: dict
            The parsed person data.
            May be:
            {
                "name": str,                                    # The name of the person.
                "descriptionHTML": str,                         # The description of the person, but in HTML format.
                "views": int,                                   # The number of views of the person.
                "tags": list[dict{                              # The tags of the person.
                    "name": str,                                # The name of the tag.
                    "link": str                                 # The link of the tag.
                }],
                "galleries": list[dict{                         # The related galleries of the person.
                    "link": str,                                # The link of the recommend gallery.
                    "cover": str,                               # The cover of the recommend gallery.
                    "alt": str,                                 # The alt of the recommend gallery.
                    "title": str,                               # The title of the recommend gallery.
                    "stars": str,                               # The stars of the recommend gallery.
                    "VIP": bool                                 # The VIP status of the recommend gallery.
                }],
                "videos": list[dict{                            # The related videos of the person.
                    "data": str or None,                        # The data of the video, None if not found.
                                                                # data: The moved cover of the video.
                                                                # I am not sure about this.
                    "link": str,                                # The link of the video.
                    "title": str,                               # The title of the video.
                    "cover": str,                               # The cover of the video.
                    "VIP": bool                                 # The VIP status of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Parsing the soup that is not from asiansister person page may cause the program to crash.)
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        person = {}
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人信息。")
        person["name"] = soup.find("center").find("h1").text
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人描述。")
        person["descriptionHTML"] = str(soup.find("div", {"id": "detailBox"}))
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人浏览量。")
        person["views"] = int(soup.find("div", {"id": "detailBox"}).find("div").text.split(": ")[1].split("标签")[0].replace("Tag ", ""))
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取个人标签。")
        person["tags"] = []
        for i in soup.find("div", {"id": "detailBox"}).find("div").find("h4").find_all("a"):
            if i.attrs["href"] == "tag.php?tag=":
                pass
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 个人标签： {i.text}。")
                person["tags"].append({"name": i.text, "link": i.attrs["href"]})
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取相关推荐。")
        recommend = waziAsianSister.parseRecommendImagesAndVideos(self, soup)
        person["galleries"] = recommend[0]
        person["videos"] = recommend[1]
        waziLog.log("info", f"({self.name}.{fuName}) 解析完成，个人信息返回中。")
        return person
    
    def parseRecommendImagesAndVideos(self, soup):
        """
        waziAsianSister.parseRecommendImagesAndVideos(self, soup)
        *Emotion.*

        Parse the recommend images and videos in the page.

        Parameters:
            soup: BeautifulSoup
                The BeautifulSoup object of the page.
                Must have <div class="recommentBox"></div> and <div class="recommentBoxVideo"></div>.
        
        Return:
            Type: tuple
            The parsed recommend images and videos.
            Like:
            (
                list[dict{                                      # The recommend galleries.
                    "link": str,                                # The link of the recommend gallery.
                    "cover": str,                               # The cover of the recommend gallery.
                    "alt": str,                                 # The alt of the recommend gallery.
                    "title": str,                               # The title of the recommend gallery.
                    "stars": str,                               # The stars of the recommend gallery.
                    "VIP": bool                                 # The VIP status of the recommend gallery.
                }],
                list[dict{                                      # The recommend videos.
                    "data": str or None,                        # The data of the video, None if not found.
                                                                # data: The moved cover of the video.
                                                                # I am not sure about this.
                    "link": str,                                # The link of the video.
                    "title": str,                               # The title of the video.
                    "cover": str,                               # The cover of the video.
                    "VIP": bool                                 # The VIP status of the video.
                }]
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Parsing the soup that is not from asiansister person page may cause the program to crash.)
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐画廊和视频。")
        recommendGalleries = []
        recommendVideos = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐画廊。")
        for i in soup.find_all("div", {"class": "recommentBox"}):
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊地址。")
            gallery["link"] = "https://asiansister.com/" + i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面。")
            gallery["cover"] = i.find("img", {"class": "lazyload"}).attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面缺省字符串。")
            gallery["alt"] = i.find("img", {"class": "lazyload"}).attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
            gallery["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊星级。")
            gallery["stars"] = len(i.find_all("img", {"class": "recommentStar"}))
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该画廊是否需要 VIP。")
            if i.find("img", {"class": "rec_vip_cover"}):
                gallery["VIP"] = True
            else:
                gallery["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到画廊列表。")
            recommendGalleries.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取推荐视频。")
        for i in soup.find_all("div", {"class": "recommentBoxVideo"}):
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频是否存在 data 标签。")
            if "data" in i.attrs:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = ""
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频地址。")
            video["link"] = "https://asiansister.com/" + i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
            video["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该视频是否需要 VIP。")
            if i.find("img", {"class": "rec_vip_cover"}):
                video["VIP"] = True
            else:
                video["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到视频列表。")
            recommendVideos.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 提取页面中所有信息完成，图像信息： {recommendGalleries}, 视频信息： {recommendVideos}。")
        return recommendGalleries, recommendVideos

    def parseImagesAndVideos(self, soup):
        """
        waziAsianSister.parseImagesAndVideos(self, soup)
        *Variable.*

        From the page of the search result, get the information of the images and videos.

        Parameters:
            soup: BeautifulSoup
                The page of the search result or just page.
                https://asiansiter.com/
        
        Return:
            Type: tuple
            The information of the images and videos.
            Like this:
            (
                list[dict{                                          # Gallery information.
                    "views": int,                                   # The views of the gallery.
                    "link": str,                                    # The link of the gallery.
                    "vip": bool,                                    # Whether the gallery is VIP.
                    "cover": str,                                   # The cover of the gallery.
                    "alt": str,                                     # The alt of the cover.
                    "title": str                                    # The title of the gallery.
                }],
                list[dict{                                          # Video information.
                    "data": str or None,                            # The data of the video.
                    "views": int,                                   # The views of the video.
                    "link": str,                                    # The link of the video.
                    "vip": bool,                                    # Whether the video is VIP.
                    "cover": str,                                   # The cover of the video.
                    "title": str                                    # The title of the video.
                }]
            )

        Errors:
            Python:
                Perhaps there are potential errors.
                (Parsing the soup that is not from asiansister person page may cause the program to crash.)
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup，正在解析。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有画廊信息。")
        galleries = soup.find_all("div", class_ = "itemBox")
        waziLog.log("debug", f"({self.name}.{fuName}) 画廊提取完成，正在进行解析。")
        galleriesBox = []
        videosBox = []
        for i in galleries:
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取浏览数量。")
            gallery["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊链接。")
            gallery["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该画廊是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                gallery["vip"] = True
            else:
                gallery["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面。")
            gallery["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊封面的顶替字符串。")
            gallery["alt"] = i.find("img", class_ = "lazyload").attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取画廊标题。")
            gallery["title"] = i.find("div", class_ = "titleName").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到画廊列表。")
            galleriesBox.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("debug", f"({self.name}.{fuName}) 提取页面中所有视频信息。")
        videos = soup.find_all("div", class_ = "itemBox_video")
        for i in videos:
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频是否存在 data 标签。")
            if "data" in i.attrs:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = None
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频播放量。")
            video["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频链接。")
            video["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在检查该视频是否需要 VIP。")
            if i.find("img", class_ = "vip_cover"):
                video["vip"] = True
            else:
                video["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频封面。")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取视频标题。")
            video["title"] = i.find("div", class_ = "titleName_video").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) 正在添加到视频列表。")
            videosBox.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) 添加完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 提取页面中所有信息完成，图像信息： {galleriesBox}, 视频信息： {videosBox}。")
        return galleriesBox, videosBox

    def getPage(self, page):
        """
        waziAsianSister.getPage(self, page)
        *Keep.*

        Input a page number and get the page information.

        Parameters:
            page: int
                The page number. The first page is 1.
        
        Return:
            Type: tuple
            The information of the images and videos.
            Like this:
            (
                list[dict{                                          # Gallery information.
                    "views": int,                                   # The views of the gallery.
                    "link": str,                                    # The link of the gallery.
                    "vip": bool,                                    # Whether the gallery is VIP.
                    "cover": str,                                   # The cover of the gallery.
                    "alt": str,                                     # The alt of the cover.
                    "title": str                                    # The title of the gallery.
                }],
                list[dict{                                          # Video information.
                    "data": str or None,                            # The data of the video.
                    "views": int,                                   # The views of the video.
                    "link": str,                                    # The link of the video.
                    "vip": bool,                                    # Whether the video is VIP.
                    "cover": str,                                   # The cover of the video.
                    "title": str                                    # The title of the video.
                }]
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在生成 URL： {page}。")
        url = "https://asiansister.com/_page" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parseImagesAndVideos。")
        return waziAsianSister.parseImagesAndVideos(self, soup)

    def search(self, keyword, page):
        """
        waziAsianSister.search(self, keyword, page)
        *Find and hide.*

        Input a keyword and page number and get the page information.

        Parameters:
            keyword: str
                The keyword.
            
            page: int
                The page number. The first page is 1.
        
        Return:
            Type: tuple
            The information of the images and videos.
            Like this:
            (
                list[dict{                                          # Gallery information.
                    "views": int,                                   # The views of the gallery.
                    "link": str,                                    # The link of the gallery.
                    "vip": bool,                                    # Whether the gallery is VIP.
                    "cover": str,                                   # The cover of the gallery.
                    "alt": str,                                     # The alt of the cover.
                    "title": str                                    # The title of the gallery.
                }],
                list[dict{                                          # Video information.
                    "data": str or None,                            # The data of the video.
                    "views": int,                                   # The views of the video.
                    "link": str,                                    # The link of the video.
                    "vip": bool,                                    # Whether the video is VIP.
                    "cover": str,                                   # The cover of the video.
                    "title": str                                    # The title of the video.
                }]
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到关键字和页码，正在生成 URL： {keyword}， {page}。")
        url = "https://asiansister.com/search.php?q=" + keyword + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parseImagesAndVideos。")
        return waziAsianSister.parseImagesAndVideos(self, soup)

    def tagSearch(self, tag, page):
        """
        waziAsianSister.tagSearch(self, tag, page)
        *Ascension.*

        Input a tag and page number and get the page information.

        Parameters:
            tag: str
                The tag.
            
            page: int
                The page number. The first page is 1.
        
        Return:
            Type: tuple
            The information of the images and videos.
            Like this:
            (
                list[dict{                                          # Gallery information.
                    "views": int,                                   # The views of the gallery.
                    "link": str,                                    # The link of the gallery.
                    "vip": bool,                                    # Whether the gallery is VIP.
                    "cover": str,                                   # The cover of the gallery.
                    "alt": str,                                     # The alt of the cover.
                    "title": str                                    # The title of the gallery.
                }],
                list[dict{                                          # Video information.
                    "data": str or None,                            # The data of the video.
                    "views": int,                                   # The views of the video.
                    "link": str,                                    # The link of the video.
                    "vip": bool,                                    # Whether the video is VIP.
                    "cover": str,                                   # The cover of the video.
                    "title": str                                    # The title of the video.
                }]
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到标签和页码，正在生成 URL： {tag}， {page}。")
        url = "https://asiansister.com/tag.php?tag=" + tag + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parseImagesAndVideos。")
        return waziAsianSister.parseImagesAndVideos(self, soup)
    
    def personSearch(self, person):
        """
        waziAsianSister.personSearch(self, person)
        *Passion.*

        Person search.

        Parameters:
            person: str
                The person.
        
        Return:
            Type: dict
            The information of the images and videos.
            {
                "name": str,                                    # The name of the person.
                "descriptionHTML": str,                         # The description of the person, but in HTML format.
                "views": int,                                   # The number of views of the person.
                "tags": list[dict{                              # The tags of the person.
                    "name": str,                                # The name of the tag.
                    "link": str                                 # The link of the tag.
                }],
                "galleries": list[dict{                         # The related galleries of the person.
                    "link": str,                                # The link of the recommend gallery.
                    "cover": str,                               # The cover of the recommend gallery.
                    "alt": str,                                 # The alt of the recommend gallery.
                    "title": str,                               # The title of the recommend gallery.
                    "stars": str,                               # The stars of the recommend gallery.
                    "VIP": bool                                 # The VIP status of the recommend gallery.
                }],
                "videos": list[dict{                            # The related videos of the person.
                    "data": str or None,                        # The data of the video, None if not found.
                                                                # data: The moved cover of the video.
                                                                # I am not sure about this.
                    "link": str,                                # The link of the video.
                    "title": str,                               # The title of the video.
                    "cover": str,                               # The cover of the video.
                    "VIP": bool                                 # The VIP status of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到人物信息，正在生成 URL： {person}。")
        url = "https://asiansister.com/" + person
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parsePerson。")
        return waziAsianSister.parsePerson(self, soup)
    
    def getGallery(self, gallery):
        """
        waziAsianSister.getGallery(self, gallery)
        *Darkness.*

        Get the gallery information.

        Parameters:
            gallery: str
                The gallery.
        
        Return:
            Type: dict
            The information of the gallery.
            {
                "title": str,                                       # The title of the gallery.
                "stars": str,                                       # The stars of the gallery, X/Y.
                "category": dict{"name": str, "link": str},         # The category of the gallery.
                "tags": list[dict{"name": str, "link": str}],       # The tags of the gallery.
                "description": str,                                 # The description of the gallery.
                "model": dict{"name": str, "link": str},            # The model of the gallery.
                "covers": list[dict{"link": str, "alt": str}],      # The covers of the gallery.
                "pictures": list[dict{"link": str, "org": str}],    # The pictures of the gallery.
                                                                    # org: The original picture.
                "pageNum": int,                                     # The number of the pictures.
                "comments": list[dict{                              # The comments of the gallery.
                    "user": str,                                    # The user group.
                    "avatar": str,                                  # The avatar link.
                    "name": str,                                    # The name of the user.
                    "time": str,                                    # The time of the comment.
                    "content": str                                  # The content of the comment.
                }],                                                 
                "galleries": list[dict{                             # The recommend galleries.
                    "link": str,                                    # The link of the recommend gallery.
                    "cover": str,                                   # The cover of the recommend gallery.
                    "alt": str,                                     # The alt of the recommend gallery.
                    "title": str,                                   # The title of the recommend gallery.
                    "stars": str,                                   # The stars of the recommend gallery.
                    "VIP": bool                                     # The VIP status of the recommend gallery.
                }],
                "videos": list[dict{                                # The recommend videos.
                    "data": str or None,                            # The data of the video, None if not found.
                                                                    # data: The moved cover of the video.
                                                                    # I am not sure about this.
                    "link": str,                                    # The link of the video.
                    "title": str,                                   # The title of the video.
                    "cover": str,                                   # The cover of the video.
                    "VIP": bool                                     # The VIP status of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集信息，正在生成 URL： {gallery}。")
        url = "https://asiansister.com/" + gallery
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parseGallery。")
        return waziAsianSister.parseGallery(self, soup)
    
    def createFolder(self, path):
        """
        waziAsianSister.createFolder(self, path)
        *Darkness.*

        Create a folder.

        Parameters:
            path: str
                The path of the folder.
        
        Return:
            Type: bool
            The status of the creation.
            True: Success.
            False: Failed.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到路径信息，正在创建文件夹。")
        waziLog.log("debug", f"({self.name}.{fuName}) 路径信息： {path}。")
        isExists = os.path.exists(self.fileName.toRight(path))
        if not isExists:
            os.makedirs(self.fileName.toRight(path))
        waziLog.log("info", f"({self.name}.{fuName}) 文件夹创建完成。")

    def downloadGallery(self, gallery, path, key = "org"):
        """
        waziAsianSister.downloadGallery(self, gallery, path, key = "org")
        *Ring.*

        Download the gallery.

        Parameters:
            gallery: str
                The gallery.
            
            path: str
                Path to save.
            
            key: str
                The key of the file. Default: org.
        
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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集信息，正在生成 URL： {gallery}。")
        url = "https://asiansister.com/" + gallery
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，使用 parseGallery 获取信息。")
        info = waziAsianSister.parseGallery(self, soup)
        downloadFiles = []
        cannotDownloadFiles = []
        if "pictures" in info:
            waziLog.log("debug", f"({self.name}.{fuName}) 存在图集信息，正在下载图集。")
            for picture in info["pictures"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 正在下载图片： {picture[key]}。")
                if waziAsianSister.downloadFile(self, picture[key], picture[key].split("/")[-1], os.path.join(path, info["title"].strip())):
                    waziLog.log("debug", f"({self.name}.{fuName}) 图片下载完成： {picture[key]}。")
                    downloadFiles.append(os.path.join(os.path.join(path, info["title"].strip()), picture[key].split("/")[-1]))
                else:
                    waziLog.log("warn", f"({self.name}.{fuName}) 图片下载失败： {picture[key]}。")
                    cannotDownloadFiles.append(picture[key])
        waziLog.log("info", f"({self.name}.{fuName}) 下载完成，数据返回。")
        return (downloadFiles, cannotDownloadFiles)
    
    def getVideo(self, video):
        """
        waziAsianSister.getVideo(self, video)
        *Live Love.*

        Get the video information.

        Parameters:
            video: str
                The video.
        
        Return:
            Type: dict
            The information of the video.
            {
                "title": str,                                   # The title of the video.
                "views": int,                                   # The views of the video.
                "tags": list[dict{"name": str, "link": str}],   # The tags of the video.
                "cover": str,                                   # The cover link of the video.
                "url": str,                                     # The url of the video file.
                "comments": list[dict{                          # The comments of the video.
                    "user": str,                                # The user group.
                    "avatar": str,                              # The avatar link.
                    "name": str,                                # The name of the user.
                    "time": str,                                # The time of the comment.
                    "content": str                              # The content of the comment.
                }],                                             
                "recommends": list[dict{                        # The recommends of the video.
                    "title": str,                               # The title of the video.
                    "link": str,                                # The link of the video.
                    "cover": str,                               # The cover link of the video.
                    "views": int                                # The views of the video.
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到视频信息，正在生成 URL： {video}。")
        url = "https://asiansister.com/" + video
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，递交至 parseVideo。")
        return waziAsianSister.parseVideo(self, soup)
    
    def downloadVideo(self, video, path):
        """
        waziAsianSister.downloadVideo(self, video, path)
        *Ghost!*

        Download the video.

        Parameters:
            video: str
                The video.
            
            path: str
                Path to save.
        
        Return:
            Type: str or bool
            If success: The path of the video, else return false.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到视频信息，正在生成 URL： {video}。")
        url = "https://asiansister.com/" + video
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup 获取完成，正在从 parseVideo 中获取信息。")
        info = waziAsianSister.parseVideo(self, soup)
        waziLog.log("debug", f"({self.name}.{fuName}) 从 parseVideo 中获取信息完成，正在下载视频。")
        if waziAsianSister.downloadFile(self, info["url"], info["url"].split("?")[0].split("/")[-1], os.path.join(path, info["title"].strip()), True):
            waziLog.log("info", f"({self.name}.{fuName}) 视频下载完成，返回路径。")
            return os.path.join(os.path.join(path, info["title"].strip()), info["url"].split("?")[0].split("/")[-1])
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 视频下载失败，请重试或检查日志！")
            return False
        
    def customParse(self, content, type):
        """
        waziAsianSister.customParse(self, content, type)
        *Center.*

        Custom parse the content.

        Parameters:
            content: str
                The second half of the URL
            
            type: str
                The type of the content.
                    main: The main page.
                    person: The person page.
                    search: The search page.
                    gallery: The gallery page.
                    video: The video page.
            
        Return:
            main / tag / search -> parseImagesAndVideos()
            person -> parsePerson()
            gallery -> parseGallery()
            video -> parseVideo()
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Log:
                Warn:
                    + The type of the content is not supported.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到补充 URL 和类型，正在生成 URL： {content}， {type}。")
        url = "https://asiansister.com/" + content
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 returnSoup 获取 Soup。")
        soup = waziAsianSister.returnSoup(self, url)
        if type == "main":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析主页，已提交至 parseImagesAndVideos。")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "person":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析角色页，已提交至 parsePerson。")
            return waziAsianSister.parsePerson(self, soup)
        elif type == "tag":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析标签页，已提交至 parseImagesAndVideos。")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "search":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析搜索页，已提交至 parseImagesAndVideos。")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "gallery":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析图集页，已提交至 parseGallery。")
            return waziAsianSister.parseGallery(self, soup)
        elif type == "video":
            waziLog.log("debug", f"({self.name}.{fuName}) 解析视频页，已提交至 parseVideo。")
            return waziAsianSister.parseVideo(self, soup)
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) 无法识别的类型，已返回空列表。")
            return []
