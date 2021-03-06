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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
        self.params = params
        waziLog.log("info", f"({self.name}.{fuName}) ????????????????????????????????? {self.params}")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL??????????????? Soup??? {link}")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL ??????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        requestParams = self.request.handleParams(tempParams, "get", link, tempHeaders, self.proxies)
        try:
            soup = BeautifulSoup(self.request.do(requestParams).data.decode("utf-8"), "lxml")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) ??????????????????????????? Soup???")
            return BeautifulSoup("<html></html>", "lxml")
        else:
            waziLog.log("info", f"({self.name}.{fuName}) ???????????????Soup ????????????")
            return soup
    
    def downloadFile(self, url, name, path):
        """
        waziAsianSister.downloadFile(self, url, name, path)
        *Sweet Trouble.*

        Download a file from a link for asiansister.com.

        Parameters:
            url: str
                A link to download.
            
            name: str
                The name of the file.
            
            path: str
                The path to save the file.
            
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? URL?????????????????????????????????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) URL??? {url}??? ???????????? {name}??? ????????? {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????????????????")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) ???????????????")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        if "asiansister" in url:
            tempHeaders["Referer"] = "https://asiansister.com/"
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????? {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        requestParams = self.request.handleParams(tempParams, "get", url, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
        fileName = os.path.join(path, self.fileName.toRight(name))
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????? {fileName}")
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????? {url}")
        with open(fileName, "wb") as f:
            try:
                temp = self.request.do(requestParams)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) ????????????????????????")
                return False
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????")
                f.write(temp.data)
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????")
        waziLog.log("info", f"({self.name}.{fuName}) ????????? {fileName}??? ?????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        video = {}
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        video["title"] = soup.find("div", class_ = "headTitle").text
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
        video["views"] = int(soup.find("div", class_ = "viewCount").text.replace(" views", "").replace(",", ""))
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        video["tags"] = []
        for tag in soup.find("div", id = "detailBox").find_all("a"):
            if tag.attrs["href"] == "tag.php?tag=":
                pass
            else:
                video["tags"].append({
                    "name": tag.text,
                    "link": "https://asiansister.com/" + tag.get("href")
                })
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        video["cover"] = soup.find("video").attrs["poster"]
        if video["cover"].startswith("http"):
            pass
        else:
            video["cover"] = "https://asiansister.com/" + video["cover"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        video["url"] = soup.find("video").find("source").attrs["src"]
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
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
        waziLog.log("info", f"({self.name}.{fuName}) ???????????????????????????")
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
        waziLog.log("info", f"({self.name}.{fuName}) ??????????????? {video}??????????????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        gallery = {}
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        gallery["title"] = soup.find("h1").text
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        gallery["stars"] = soup.find("font").text.strip()
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        gallery["category"] = {
            "name": soup.find("div", class_ = "headTitle").find("a").text,
            "link": "https://asiansister.com/" + soup.find("div", class_ = "headTitle").find("a").attrs["href"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        gallery["tags"] = []
        for tag in soup.find("div", id = "detailBox").find_all("a"):
            if tag.attrs["href"] == "tag.php?tag=":
                pass
            else:
                gallery["tags"].append({
                    "name": tag.text,
                    "link": "https://asiansister.com/" + tag.attrs["href"]
                })
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        gallery["description"] = soup.find_all("div", class_ = "detailBoxHide")[1].text.strip().replace("<br>", "\n").replace("<br/>", "\n")
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
        for i in soup.find_all("div", class_ = "headTitle"):
            if i.text.strip() == "Model / Actor":
                waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????")
                gallery["model"] = {
                    "name": soup.find("div", class_ = "modelBox").text,
                    "link": "https://asiansister.com/" + soup.find("div", class_ = "modelBox").find_previous("a").attrs["href"]
                }
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
        gallery["covers"] = []
        for cover in soup.find("table").find_all("img"):
            gallery["covers"].append({
                "link": "https://asiansister.com/" + cover.attrs["data-src"],
                "alt": cover.attrs["alt"]
            })
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????????")
        gallery["pictures"] = []
        for picture in soup.find("center").find_all("div", class_ = "rootContant")[1].find_all("img"):
            gallery["pictures"].append({
                "link": "https://asiansister.com/" + picture.attrs["data-src"],
                "org": "https://asiansister.com/" + picture.attrs["dataurl"][5:]
            })
        gallery["pageNumber"] = len(gallery["pictures"])
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        recommend = waziAsianSister.parseRecommendImagesAndVideos(self, soup)
        gallery["galleries"] = recommend[0]
        gallery["videos"] = recommend[1]
        waziLog.log("info", f"({self.name}.{fuName}) ???????????????????????????????????? {gallery}???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        person = {}
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        person["name"] = soup.find("center").find("h1").text
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        person["descriptionHTML"] = str(soup.find("div", {"id": "detailBox"}))
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
        person["views"] = int(soup.find("div", {"id": "detailBox"}).find("div").text.split(": ")[1].split("??????")[0].replace("Tag ", ""))
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        person["tags"] = []
        for i in soup.find("div", {"id": "detailBox"}).find("div").find("h4").find_all("a"):
            if i.attrs["href"] == "tag.php?tag=":
                pass
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) ??????????????? {i.text}???")
                person["tags"].append({"name": i.text, "link": i.attrs["href"]})
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        recommend = waziAsianSister.parseRecommendImagesAndVideos(self, soup)
        person["galleries"] = recommend[0]
        person["videos"] = recommend[1]
        waziLog.log("info", f"({self.name}.{fuName}) ???????????????????????????????????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
        recommendGalleries = []
        recommendVideos = []
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        for i in soup.find_all("div", {"class": "recommentBox"}):
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["link"] = "https://asiansister.com/" + i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["cover"] = i.find("img", {"class": "lazyload"}).attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????????????????")
            gallery["alt"] = i.find("img", {"class": "lazyload"}).attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["stars"] = len(i.find_all("img", {"class": "recommentStar"}))
            waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? VIP???")
            if i.find("img", {"class": "rec_vip_cover"}):
                gallery["VIP"] = True
            else:
                gallery["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
            recommendGalleries.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
        for i in soup.find_all("div", {"class": "recommentBoxVideo"}):
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? data ?????????")
            if "data" in i.attrs:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = ""
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            video["link"] = "https://asiansister.com/" + i.find("a").attrs["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            video["title"] = i.find("a").attrs["title"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? VIP???")
            if i.find("img", {"class": "rec_vip_cover"}):
                video["VIP"] = True
            else:
                video["VIP"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
            recommendVideos.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????")
        waziLog.log("info", f"({self.name}.{fuName}) ??????????????????????????????????????????????????? {recommendGalleries}, ??????????????? {recommendVideos}???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????? Soup??????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
        galleries = soup.find_all("div", class_ = "itemBox")
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????????????????")
        galleriesBox = []
        videosBox = []
        for i in galleries:
            gallery = {}
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? VIP???")
            if i.find("img", class_ = "vip_cover"):
                gallery["vip"] = True
            else:
                gallery["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            gallery["alt"] = i.find("img", class_ = "lazyload").attrs["alt"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            gallery["title"] = i.find("div", class_ = "titleName").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
            galleriesBox.append(gallery)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????????")
        videos = soup.find_all("div", class_ = "itemBox_video")
        for i in videos:
            video = {}
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? data ?????????")
            if "data" in i.attrs:
                video["data"] = i.attrs["data"]
            else:
                video["data"] = None
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
            video["views"] = int(i.find("div", class_ = "viewCountBox").text)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            video["link"] = "https://asiansister.com/" + i.find("a")["href"]
            waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? VIP???")
            if i.find("img", class_ = "vip_cover"):
                video["vip"] = True
            else:
                video["vip"] = False
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            if i.find("img", class_ = "lazyload").attrs["data-src"].startswith("http"):
                video["cover"] = i.find("img", class_ = "lazyload").attrs["data-src"]
            else:
                video["cover"] = "https://asiansister.com/" + i.find("img", class_ = "lazyload").attrs["data-src"]
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????")
            video["title"] = i.find("div", class_ = "titleName_video").text.strip()
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????")
            videosBox.append(video)
            waziLog.log("debug", f"({self.name}.{fuName}) ???????????????")
        waziLog.log("info", f"({self.name}.{fuName}) ??????????????????????????????????????????????????? {galleriesBox}, ??????????????? {videosBox}???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????? URL??? {page}???")
        url = "https://asiansister.com/_page" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseImagesAndVideos???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????????????? URL??? {keyword}??? {page}???")
        url = "https://asiansister.com/search.php?q=" + keyword + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseImagesAndVideos???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????????????????????????????? URL??? {tag}??? {page}???")
        url = "https://asiansister.com/tag.php?tag=" + tag + "&page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseImagesAndVideos???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? URL??? {person}???")
        url = "https://asiansister.com/" + person
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parsePerson???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? URL??? {gallery}???")
        url = "https://asiansister.com/" + gallery
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseGallery???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
        waziLog.log("debug", f"({self.name}.{fuName}) ??????????????? {path}???")
        isExists = os.path.exists(self.fileName.toRight(path))
        if not isExists:
            os.makedirs(self.fileName.toRight(path))
        waziLog.log("info", f"({self.name}.{fuName}) ????????????????????????")

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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? URL??? {gallery}???")
        url = "https://asiansister.com/" + gallery
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ????????????????????? parseGallery ???????????????")
        info = waziAsianSister.parseGallery(self, soup)
        downloadFiles = []
        cannotDownloadFiles = []
        if "pictures" in info:
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????????????????????")
            for picture in info["pictures"]:
                waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {picture[key]}???")
                if waziAsianSister.downloadFile(self, picture[key], picture[key].split("/")[-1], os.path.join(path, info["title"].strip())):
                    waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????? {picture[key]}???")
                    downloadFiles.append(os.path.join(os.path.join(path, info["title"].strip()), picture[key].split("/")[-1]))
                else:
                    waziLog.log("warn", f"({self.name}.{fuName}) ????????????????????? {picture[key]}???")
                    cannotDownloadFiles.append(picture[key])
        waziLog.log("info", f"({self.name}.{fuName}) ??????????????????????????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? URL??? {video}???")
        url = "https://asiansister.com/" + video
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseVideo???")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ????????????????????????????????? URL??? {video}???")
        url = "https://asiansister.com/" + video
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        waziLog.log("debug", f"({self.name}.{fuName}) Soup ???????????????????????? parseVideo ??????????????????")
        info = waziAsianSister.parseVideo(self, soup)
        waziLog.log("debug", f"({self.name}.{fuName}) ??? parseVideo ?????????????????????????????????????????????")
        if waziAsianSister.downloadFile(self, info["url"], info["url"].split("?")[0].split("/")[-1], os.path.join(path, info["title"].strip())):
            waziLog.log("info", f"({self.name}.{fuName}) ????????????????????????????????????")
            return os.path.join(os.path.join(path, info["title"].strip()), info["url"].split("?")[0].split("/")[-1])
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) ????????????????????????????????????????????????")
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
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? URL ???????????????????????? URL??? {content}??? {type}???")
        url = "https://asiansister.com/" + content
        waziLog.log("debug", f"({self.name}.{fuName}) ???????????? returnSoup ?????? Soup???")
        soup = waziAsianSister.returnSoup(self, url)
        if type == "main":
            waziLog.log("debug", f"({self.name}.{fuName}) ??????????????????????????? parseImagesAndVideos???")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "person":
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? parsePerson???")
            return waziAsianSister.parsePerson(self, soup)
        elif type == "tag":
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? parseImagesAndVideos???")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "search":
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? parseImagesAndVideos???")
            return waziAsianSister.parseImagesAndVideos(self, soup)
        elif type == "gallery":
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? parseGallery???")
            return waziAsianSister.parseGallery(self, soup)
        elif type == "video":
            waziLog.log("debug", f"({self.name}.{fuName}) ?????????????????????????????? parseVideo???")
            return waziAsianSister.parseVideo(self, soup)
        else:
            waziLog.log("warn", f"({self.name}.{fuName}) ?????????????????????????????????????????????")
            return []
