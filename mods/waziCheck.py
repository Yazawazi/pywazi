"""
mods/waziCheck.py

class: waziCheck
"""

import hmac
import time
import hashlib
from mods import waziFun
from ins.waziInsLog import waziLog


class waziCheck:
    """
    waziCheck
    *Try to understand the world.*

    Separate checksum and crypto system for ExHentai search and PicAcg encryption and decryption processing.
    But now also support Nyaa.si.

    Attributes:
        sha1: hashlib.sha1
            Just a hashlib.sha1(), eee.

        nyaaTranslations: dict
            A dictionary for translating Nyaa's class to the meaning of the class.

        nyaaSearch: dict
            A dictionary for get Nyaa's categroy id.

        tags: list
            A list that contains all the categories of ExHentai.
            (Why I call it tags? Because I am a bad programmer.)

        tagsNumber: dict
            A dictionary for get ExHentai's categroy number.

        ratingPos: dict
            A dictionary for translating ExHentai's rating position to the number.

        name: str
            The name of the class.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziCheck.__init__(self)
        *God bless you.*

        Initialize the class.

        Parameters:
            None
        """
        super(waziCheck, self).__init__()
        self.sha1 = hashlib.sha1()
        # Nyaa Translation
        self.nyaaTranslations = {
            "success": "Trusted",
            "danger": "Remake / Reencode / Remux / Reupload",
            "default": "Normal",
            "panel-success": "Trusted",
            "panel-danger": "Remake / Reencode / Remux / Reupload",
            "panel-default": "Normal"
            # Orange / Grey | I cannot find.
        }
        # Nyaa Search
        self.nyaaSearch = {
            "catgroies": {
                # Safe
                "All": "0_0",
                "Anime": "1_0",
                "Anime Music Video": "1_1",
                "Anime English-translated": "1_2",
                "Anime Non-English-translated": "1_3",
                "Anime Raw": "1_4",
                "Audio": "2_0",
                "Audio Lossless": "2_1",
                "Audio Lossy": "2_2",
                "Literature": "3_0",
                "Literature English-translated": "3_1",
                "Literature Non-English-translated": "3_2",
                "Literature Raw": "3_3",
                "Live Action": "4_0",
                "Live Action English-translated": "4_1",
                "Live Action Idol/Promotional": "4_2",
                "Live Action Non-English-translated": "4_3",
                "Live Action Raw": "4_4",
                "Pictures": "5_0",
                "Pictures Graphics": "5_1",
                "Pictures Photos": "5_2",
                "Software": "6_0",
                "Software Applications": "6_1",
                "Software Games": "6_2",
                # Unsafe
                "Art": "1_0",
                "Art Anime": "1_1",
                "Art Doujinshi": "1_2",
                "Art Games": "1_3",
                "Art Manga": "1_4",
                "Art Pictures": "1_5",
                "Real Life": "2_0",
                "Real Life Photobooks and Pictures": "2_1",
                "Real Life Videos": "2_2",
            },
            "filters": {
                "No": "0",
                "No Remakes": "1",
                "Trusted Only": "2",
            },
            "orders": {
                "Comments": {
                    "s": "comments",
                    "o": "desc"
                },
                "Size": {
                    "s": "size",
                    "o": "desc"
                },
                "Date": {
                    "s": "id",
                    "o": "asc"
                },
                "Seeders": {
                    "s": "seeders",
                    "o": "desc"
                },
                "Leechers": {
                    "s": "leechers",
                    "o": "desc"
                },
                "Completed Downloads": {
                    "s": "downloads",
                    "o": "desc"
                }
            }
        }
        # These are ExHentai's tags.
        # 这些是 ExHentai 的标签。
        self.tags = [
            "Doujinshi",
            "Manga",
            "Artist CG",
            "Game CG",
            "Western",
            "Non-H",
            "Image Set",
            "Cosplay",
            "Asian Porn",
            "Misc"
        ]
        # These are the corresponding scores for the ExHentai tag.
        # You can see the values corresponding to all tags in table.itc of ExHentai.
        #
        # 这些是 ExHentai 标签的对应分数。
        # 在 ExHentai 的 table.itc 中可以看到所有标签对应的数值。
        self.tagsNumber = {
            "Doujinshi": 2,
            "Manga": 4,
            "Artist CG": 8,
            "Game CG": 16,
            "Western": 512,
            "Non-H": 256,
            "Image Set": 32,
            "Cosplay": 64,
            "Asian Porn": 128,
            "Misc": 1
        }
        # I've listed all the possible scoring displacement codes that can occur.
        # 我将所有可能出现的评分位移代码列举出来了。
        self.ratingPos = {
            "-80px -1px": 0,
            "-80px -21px": 0,
            "-64px -21px": 0.5,
            "-64px -1px": 1,
            "-48px -21px": 1.5,
            "-48px -1px": 2,
            "-32px -21px": 2.5,
            "-32px -1px": 3,
            "-16px -21px": 3.5,
            "-16px -1px": 4,
            "0px -21px": 4.5,
            "0px -1px": 5
        }
        self.name = self.__class__.__name__

    def returnHasTorrents(self, soup):
        """
        waziCheck.returnHasTorrents(self, soup)
        *That's all I understand about it.*

        [ExHentai]
        If the page has torrents, return True, else return False.
        Why do I need to write a separate function out?
        Because I do not know. *^____^*

        Parameters:
            soup: BeautifulSoup
                The soup of the img.
                Just like:
                <img src="https://exhentai.org/img/td.png" alt="T" title="No torrents available">

        Return:
            Type: bool
            True if the page has torrents, else False.
            If it cannot find the src, it will return False.

        Errors:
            Log:
                Error:
                    + Cannot find the src.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Soup 信息，正在分析。")
        try:
            torrentsImg = soup.attrs["src"]
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 并没有查找到任何 src 数据，返回 False。")
            return False
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 查找到 src 数据，进行分析。")
            # My idea is to compare whether the download icon address matches the download icon address of the existing
            # seed gallery Although it is more intuitive to use the title parameter for comparison But I think the URL
            # is a little more current and perhaps more reliable.
            #
            # 我的思路是对比下载图标地址是否与存在种子画廊的下载图标地址是否一致
            # 尽管使用 title 参数进行对比更加直观
            # 但我认为 URL 的资源时效性更高一点，或许更加可靠。
            if torrentsImg == "https://exhentai.org/img/t.png":
                hasTorrents = True
                waziLog.log("info", f"({self.name}.{fuName}) 检测到下载图标一致，存在种子，返回 True。")
            else:
                waziLog.log("info", f"({self.name}.{fuName}) 检测到下载图标不一致，存在不种子，返回 False。")
                hasTorrents = False
        return hasTorrents

    def returnRatingNum(self, pos):
        """
        waziCheck.returnRatingNum(self, pos)
        *Knowing all her status.*

        [ExHentai]
        Get the rating number from the position.

        Parameters:
            pos: str
                The position in:
                <div class="ir" style="background-position:-16px -1px;opacity:1"></div>
                "-16px -1px" is the position.

        Return:
            Type: int or float
            The number of the rating.

        Errors:
            Log:
                Error:
                    + Cannot find the rating from the position.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到位移信息，正在分析： {pos}")
        if pos in self.ratingPos:
            waziLog.log("info", f"({self.name}.{fuName}) 成功获取位移对应评分： {self.ratingPos[pos]}。")
            return self.ratingPos[pos]
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取位移对应评分。")
            return "I can't get it, check your codes. / 我无法获取该评分，检查你的代码。"

    def getFileSHA1(self, path):
        """
        waziCheck.getFileSHA1(self, path)
        *A unique ID card. Theoretically, er, it doesn't feel unique.*

        Get the SHA-1 of the file.

        Parameters:
            path: str
                The file path.
                support relative and absolute.

        Return:
            Type: str
            The SHA-1 string of the file.
            If the file does not exist or cannot be read, it will return "".

        Errors:
            Python:
                Perhaps there are potential errors.

            Log:
                Error:
                    + Cannot not read the file.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到路径信息，正在完成 SHA1 计算： {path}")
        self.sha1 = hashlib.sha1()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试打开文件： {path}。")
        try:
            temp = open(path, "rb")
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 文件无法打开，返回空字符串。")
            return ""
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 成功打开文件，正在计算 SHA1。")
            while True:
                temp2 = temp.read(8096)
                self.sha1.update(temp2)
                if not temp2:
                    break
            temp.close()
            waziLog.log("info", f"({self.name}.{fuName}) 成功获取 SHA1 值： {self.sha1.hexdigest()}")
        return self.sha1.hexdigest()

    def getSources(self, params):
        """
        waziCheck.getSources(self, params)
        *Bit is wise.*

        [ExHentai]
        Calculate the sources of the categories in params.
        You can see the values corresponding to all tags in table.itc of ExHentai,
        and the calculation method in ehg_index.c.js.

        function toggle_category(b) {
            var a = document.getElementById("f_cats");
            var c = document.getElementById("cat_" + b);
            if (a.getAttribute("disabled")) {
                a.removeAttribute("disabled")
            }
            if (c.getAttribute("data-disabled")) {
                c.removeAttribute("data-disabled");
                a.value = parseInt(a.value) & (1023 ^ b)
            } else {
                c.setAttribute("data-disabled", 1);
                a.value = parseInt(a.value) | b
            }
        }

        Parameters:
            params: dict
                Must have the key "cats" and the value is a list.

        Return:
            Type: int
            The number of the sources.

        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在完成计算： {params}")
        giveTags = [item for item in self.tags if item not in set(params["cats"])]
        waziLog.log("info", f"({self.name}.{fuName}) 应当计算的标签是： {giveTags}")
        if len(giveTags) == 0:
            sources = 0
        else:
            calc = 0
            for i in giveTags:
                calc = calc | int(self.tagsNumber[i])
            sources = calc
        waziLog.log("info", f"({self.name}.{fuName}) 完成计算，数值是： {sources}")
        return sources

    def signature(self, url, times, method, baseURL, uuids, apiKey, secretKey):
        """
        waziCheck.signature(self, url, times, method, baseURL, uuids, apiKey, secretKey)
        *The signature is the key to the future.*

        [PicAcg]
        Calculate the signature of the request.

        Parameters:
            url: str
                The url of the request.

            times: int
                The time stamp of the request.

            method: str
                The method of the request.

            baseURL: str
                The base url of the request, usually it is "https://picaapi.picacomic.com/".

            uuids: str
                The uuid of the request.

            apiKey: str
                The api key of the request, typically it is "C69BAF41DA5ABD1FFEDC6D2FEA56B".

            secretKey: str
                The secret key of the request, usually it is
                "~d}$Q7$eIni=V)9\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn".

        Return:
            Type: str
            The signature of the request.

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在计算签名。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 时间： {times}， 方法： {method}， 基准 URL： {baseURL}，"
                             f" UUID： {uuids}， API 访问密钥： {apiKey}， 密钥： {secretKey}")
        raw = url.replace(baseURL, "") + str(times) + uuids + method + apiKey
        raw = raw.lower()
        hc = hmac.new(secretKey.encode(), digestmod = hashlib.sha256)
        hc.update(raw.encode())
        waziLog.log("info", f"({self.name}.{fuName}) 完成计算： {hc.hexdigest()}")
        return hc.hexdigest()

    def construct(self, url, method, baseURL, uuids, apiKey, secretKey):
        """
        waziCheck.construct(self, url, method, baseURL, uuids, apiKey, secretKey)
        *Now we are ready to go.*

        [PicAcg]
        Calculate the signature of the request without the time stamp.

        Parameters:
            url: str
                The url of the request.

            method: str
                The method of the request.

            baseURL: str
                The base url of the request, usually it is "https://picaapi.picacomic.com/".

            uuids: str
                The uuid of the request.

            apiKey: str
                The api key of the request, typically it is "C69BAF41DA5ABD1FFEDC6D2FEA56B".

            secretKey: str
                The secret key of the request, usually it is
                "~d}$Q7$eIni=V)9\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn".

        Return:
            Type: list
            Index 0 is the signature of the request, and index 1 is the time stamp of the request.

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在计算签名和时间。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 方法： {method}， 基准 URL： {baseURL}，"
                             f" UUID： {uuids}， API 访问密钥： {apiKey}， 密钥： {secretKey}")
        times = int(time.time())
        waziLog.log("info", f"({self.name}.{fuName}) 已获取本地时间： {times}")
        sig = waziCheck.signature(self, url, times, method, baseURL, uuids, apiKey, secretKey)
        waziLog.log("info", f"({self.name}.{fuName}) 完成签名，时间： {times}， 签名： {sig}")
        return [sig, times]

    def needFilterIt(self, backJson, filters):
        """
        waziCheck.needFilterIt(self, backJson, filters)
        *The censorship is abysmal.*

        [PicAcg]
        Filters the content specified by the filters.

        Parameters:
            backJson: list
                The content of the response.

            filters: list
                The filters.

        Return:
            Type: list
            The filtered content.

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到需要过滤的数据和过滤标签。")
        waziLog.log("debug", f"({self.name}.{fuName}) 需要过滤的数据： {backJson}， 过滤标签： {filters}")
        returnDocs = []
        waziLog.log("debug", f"({self.name}.{fuName}) 进入数据遍历。")
        for i in backJson:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在处理数据： {i}")
            if len(list(set(i["categories"]) & set(filters))) == 0:
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据可以通过，正在写入。")
                returnDocs.append(i)
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据写入完成。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 该数据无法通过，拒绝写入。")
        waziLog.log("info", f"({self.name}.{fuName}) 写入数据如下： {returnDocs}")
        return returnDocs
