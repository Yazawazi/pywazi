"""
sites/waziPicAcg.py

class: waziPicAcg
"""

import os
import json
import uuid
import base64
from mods import waziFun
from urllib.parse import quote
from ins.waziInsLog import waziLog
from mods.waziCheck import waziCheck
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName

class waziPicAcg:
    """
    waziPicAcg
    *Hardcore Game.*

    A class for crawling the PicAcg.

    Attributes:
        imageQuality: list
            The quality of the image.
            ["original", "low", "medium", "high"]
        
        name: str
            The name of the class.
        
        headers: dict
            The headers of the request.
            Will be modified in the class.
        
        info: dict
            A dict of the information of the request.
            Save request's secret key, api key, base url, uuid.
            Will be modified in the class.
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.
        
        proxies: dict
            The proxy for the request.
            Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        leaveMsg: str
            The ID of leave message room.
        
        token: str
            The token for the request.
            The user's token will be filled in the login method.
        
        urls: dict
            The urls for the request.
        
        request: waziRequest
            A waziRequest object.
        
        check: waziCheck
            A waziCheck object.
        
        fileName: waziFileName
            A waziFileName object.
        
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziPicAcg.__init__(self)
        *su be te mi se ta i.*

        Initialize the class.

        Parameters:
            None
        
        Actions:
            + Set the headers: waziPicAcg.editHeaders(self)
        """
        super(waziPicAcg, self).__init__()
        self.imageQuality = ["original", "low", "medium", "high"]
        self.name = self.__class__.__name__
        self.headers = {
            "api-key": "",
            "accept": "application/vnd.picacomic.com.v1+json",
            "app-channel": "3",
            "time": "0",
            "nonce": "",
            "signature": "0",
            "app-version": "2.2.1.3.3.4",
            "app-uuid": "defaultUuid",
            "app-platform": "android",
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": "okhttp/3.8.1",
            "app-build-version": "45",
            "image-quality": "original",
            "accept-encoding": "gzip",
        }
        self.info = {
            "secretKey": "~d}$Q7$eIni=V)9\\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn",
            "baseUrl": "https://picaapi.picacomic.com/",
            "uuid": "",
            "apiKey": "C69BAF41DA5ABD1FFEDC6D2FEA56B"
        }
        self.params = {}
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.leaveMsg = "5822a6e3ad7ede654696e482"
        self.token = ""
        self.urls = {
            "login": "https://picaapi.picacomic.com/auth/sign-in",
            "register": "https://picaapi.picacomic.com/auth/register",
            "categories": "https://picaapi.picacomic.com/categories",
            "search": "https://picaapi.picacomic.com/comics/search",
            "comics": "https://picaapi.picacomic.com/comics",
            "comicId": "https://picaapi.picacomic.com/comics/{comicId}",
            "comicEps": "https://picaapi.picacomic.com/comics/{comicId}/eps",
            "comicPages": "https://picaapi.picacomic.com/comics/{comicId}/order/{order}/pages",
            "comicRecommend": "https://picaapi.picacomic.com/comics/{comicId}/recommendation",
            "keywords": "https://picaapi.picacomic.com/keywords",
            "myComments": "https://picaapi.picacomic.com/users/my-comments",
            "myFavourites": "https://picaapi.picacomic.com/users/favourite",
            "profile": "https://picaapi.picacomic.com/users/profile",
            "games": "https://picaapi.picacomic.com/games",
            "comicFavourite": "https://picaapi.picacomic.com/comics/{comicId}/favourite",
            "comicLike": "https://picaapi.picacomic.com/comics/{comicId}/like",
            "comicComments": "https://picaapi.picacomic.com/comics/{comicId}/comments",
            "advSearch": "https://picaapi.picacomic.com/comics/advanced-search",
            "punchIn": "https://picaapi.picacomic.com/users/punch-in",
            "gameLike": "https://picaapi.picacomic.com/games/{gameId}/like",
            "gameComments": "https://picaapi.picacomic.com/games/{gameId}/comments",
            "avatar": "https://picaapi.picacomic.com/users/avatar",
            "userTitle": "https://picaapi.picacomic.com/users/{userId}/title",
            "forgotPassword": "https://picaapi.picacomic.com/auth/forgot-password",
            "resetPassword": "https://picaapi.picacomic.com/auth/reset-password",
            "adjustExp": "https://picaapi.picacomic.com/utils/adjust-exp",
            "password": "https://picaapi.picacomic.com/users/password",
            "updateId": "https://picaapi.picacomic.com/users/update-id",
            "updateQA": "https://picaapi.picacomic.com/users/update-qa",
            "removeComment": "https://picaapi.picacomic.com/utils/remove-comment",
            "leaderBoard": "https://picaapi.picacomic.com/comics/leaderboard",
            "knight": "https://picaapi.picacomic.com/comics/knight-leaderboard",
            "randomComic": "https://picaapi.picacomic.com/comics/random",
            "collections": "https://picaapi.picacomic.com/collections",
            "banners": "https://picaapi.picacomic.com/banners",
            "init": "http://68.183.234.72/init",
            "initAndroid": "https://picaapi.picacomic.com/init?platform=android",
            "commentsChildren": "https://picaapi.picacomic.com/comments/{commentId}/childrens?page={page}",
            "replyComment": "https://picaapi.picacomic.com/comments/{commentId}",
            "chat": "https://picaapi.picacomic.com/chat",
            "apps": "https://picaapi.picacomic.com/pica-apps",
            "androidAPPs": "https://picaapi.picacomic.com/applications?platform=android&page={page}",
            "blockUser": "https://picaapi.picacomic.com/utils/block-user",
            "notifications": "https://picaapi.picacomic.com/users/notifications?page={page}",
            "announcements": "https://picaapi.picacomic.com/announcements?page={page}",
            "dirty": "https://picaapi.picacomic.com/users/{userId}/dirty",
            "userProfile": "https://picaapi.picacomic.com/users/{userId}/profile",
            "commentLike": "https://picaapi.picacomic.com/comments/{commentId}/like",
            "commentHide": "https://picaapi.picacomic.com/comments/{commentId}/hide",
            "commentReport": "https://picaapi.picacomic.com/comments/{commentId}/report",
            "commentTop": "https://picaapi.picacomic.com/comments/{commentId}/top"
        }
        self.request = waziRequest()
        self.check = waziCheck()
        self.fileName = waziFileName()
        waziLog.log("debug", f"({self.name}.__init__) 正在初始化 Headers。")
        self.editHeaders()

    def giveParams(self, params):
        """
        waziPicAcg.giveParams(self, params)
        *Oops!*

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

    def editHeaders(self):
        """
        waziPicAcg.editHeaders(self)
        *Into the Vault!*

        Edit headers.
        Generate a new uuid, and fill in the headers with other params.
        Called in __init__.

        Parameters:
            None
        
        Return:
            None
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 接到 __init__ 指令，正在创建 headers。")
        self.info["uuid"] = str(uuid.uuid1()).replace("-", "")
        self.headers["nonce"] = self.info["uuid"]
        self.headers["api-key"] = self.info["apiKey"]
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，header 已写入： {self.headers}")

    def sign(self, url, method):
        """
        waziPicAcg.sign(self, url, method)
        *Keep it secret, keep it safe!*

        Signature request.
        Use self.check.construct to construct the request headers.

        Parameters:
            url: str
                The url of request.
            
            method: str
                The method of request.
        
        Return:
            None
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL 和请求方式，正在签名。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 请求方式： {method}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 construct 获取签名。")
        sig = self.check.construct(url, method, self.info["baseUrl"], self.info["uuid"], self.info["apiKey"],
                                   self.info["secretKey"])
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {sig}，正在写入。")
        self.headers["signature"] = sig[0]
        self.headers["time"] = str(sig[1])
        waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {self.headers}")

    def up(self, url, needAuth, data, method, jsonNeed):
        """
        waziPicAcg.up(self, url, needAuth, data, method, jsonNeed)
        *Eee.*

        Send a request.

        Parameters:
            url: str
                The url of request.
            
            needAuth: bool
                Whether need auth.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，是否验证信息，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 是否验证信息： {needAuth}， 数据： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求方式： {method}， 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户配置。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 修改完成，正在通过 sign 签名。")
        waziPicAcg.sign(self, url, method)
        waziLog.log("debug", f"({self.name}.{fuName}) 签名完成。")
        if needAuth:
            waziLog.log("debug", f"({self.name}.{fuName}) 需要验证用户信息，authorization 写入 {self.token}")
            self.headers["authorization"] = self.token
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 不需要验证用户信息，authorization 为空。")
            self.headers["authorization"] = ""
        waziLog.log("debug", f"({self.name}.{fuName}) 递交至 normalUP 处理。")
        return waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)
    
    def forHeaderYesUP(self, url, data, method, jsonNeed):
        """
        waziPicAcg.forHeaderYesUP(self, url, data, method, jsonNeed)
        *Kind be nice.*

        Send a request without sign and auth but with Headers.

        Parameters:
            url: str
                The url of request.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 数据： {data}， 请求方式： {method}")
        waziLog.log("debug", f"({self.name}.{fuName}) 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        waziLog.log("debug", f"({self.name}.{fuName}) 修改完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交至 normalUP 处理。")
        return waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)

    def justUP(self, url, data, method, jsonNeed):
        """
        waziPicAcg.justUP(self, url, data, method, jsonNeed)
        *Wanna be the first one?*

        Send a request without sign and auth.

        Parameters:
            url: str
                The url of request.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 数据： {data}， 请求方式： {method}")
        waziLog.log("debug", f"({self.name}.{fuName}) 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在修改用户参数。")
        tempParams = self.params
        tempParams["useHeaders"] = False
        waziLog.log("debug", f"({self.name}.{fuName}) 修改完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 递交至 normalUP 处理。")
        return waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)

    def normalUP(self, tempParams, url, data, method, jsonNeed):
        """
        waziPicAcg.normalUP(self, tempParams, url, data, method, jsonNeed)
        *Night.*

        Re-abstraction of the request method.
        The base request method in this class.

        Parameters:
            tempParams: dict
                The params of request. User-defined.
            
            url: str
                The url of request.
            
            data: object
                The data of request.
            
            method: str
                The method of request.
            
            jsonNeed: bool
                Whether need return json.
        
        Return:
            jsonNeed: True
                Type: list or dict Object.
            
            jsonNeed: False
                Type: urllib3.response.HTTPResponse
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户参数，URL，数据，请求方式和是否返回 JSON 信息，正在请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户参数： {tempParams}， URL： {url}， 数据： {data}")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求方式： {method}， 是否返回 JSON 信息： {jsonNeed}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 mods.waziRequest.handleParams 处理用户参数。")
        requestParams = self.request.handleParams(tempParams, method.lower(), url, self.headers, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完成： {requestParams}")
        if method.lower() != "get":
            waziLog.log("debug", f"({self.name}.{fuName}) 非 get 请求，正在检查数据。")
            if data is None:
                waziLog.log("debug", f"({self.name}.{fuName}) 数据为空，写入空字典。")
                requestParams["data"] = json.dumps({}).encode()
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 数据不为空，写入数据。")
                requestParams["data"] = json.dumps(data).encode()
        if jsonNeed:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在请求并 JSON 格式化结果。")
            jsons = json.loads(self.request.do(requestParams).data.decode("utf-8"))
            waziLog.log("info", f"({self.name}.{fuName}) 格式化完成： {jsons}， 数据返回。")
            return jsons
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 请求完成后，数据自动返回。")
            return self.request.do(requestParams)

    def login(self, username, password):
        """
        waziPicAcg.login(self, username, password)
        *Pepper Salt.*

        Login in the account.
        If success, will use your token to request.
        So you have to use this method once to get your token before any authorization request is needed.

        Parameters:
            username: str
                The username of account.
            
            password: str
                The password of account.
        
        Return:
            Type: str
            The token of account.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Logs:
                Error:
                    + Login failed.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户名和密码，正在发起登录请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户名： {username}， 密码： {password}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "email": username,
            "password": password
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试请求。")
        try:
            self.token = waziPicAcg.up(self, self.urls["login"], False, body, "POST", True)["data"]["token"]
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 错误，无法获取账号。")
            return "Account not available. / 无法获取账号。"
        else:
            waziLog.log("info", f"({self.name}.{fuName}) 已获取 token： {self.token}")
            return self.token

    def getCategories(self):
        """
        waziPicAcg.getCategories(self)
        *Fear.*

        Get all categories.

        Parameters:
            None
        
        Return:
            Type: dict
            The categories.
            May like (Some categories may not have these information):
            {
                "code": int,                            # The status code of request.
                "message": str,                         # The message of request.
                "data": {                               # The data of request.
                    "categories": [{                    # The categories.
                        "title": str,                   # The title of category.
                        "thumb": {                      # The thumbnail of category.
                            "originalName": str,        # The original name of thumb.
                            "path": str,                # The path of thumb.
                            "fileServer": str           # The file server of thumb.
                        },
                        "isWeb": bool,                  # Whether the category is web.
                        "active": bool,                 # Whether the category is active.
                        "link": str,                    # The link of category.
                        "_id": str,                     # The id of category.
                        "description": str,             # The description of category.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["categories"], True, None, "GET", True)

    def getComicsWithFullParams(self, page, c, t, a, f, s, ct, ca):
        """
        ?No testing now
        waziPicAcg.getComicsWithFullParams(self, page, c, t, a, f, s, ct, ca)
        *Good game.*

        Get comics with all params.

        Parameters:
            page: int or str
                The page of comics. Start from 1.
            
            c: str
                Category of comics. Can be string from getCategories.
            
            t: str
                Tag of comics. Please use traditional Chinese.
            
            a: str
                Author of comics.
            
            f: bool
                Is this comic finished? Yes, True; No, False.
            
            s: str
                Sorting of comics.
                    ua: Default.
                    dd: From newest to oldest.
                    da: From oldest to newest.
                    vd: From users named most to users named least. (What is that? Hot?)
                    ld: From users liked most to users liked least.
            
            ct: str
                Translation of comics.
            
            ca: str
                Creator of comics' id.
        
        Return:
            Type: dict
            No test.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码、分区、标签和排序，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 分区： {c}， 标签： {t}， 排序： {s}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comics"] + "?page=" + str(page) + "&c=" + quote(c)
        newUrl += "&t=" + quote(t) + "&a=" + quote(a) + "&f=" + str(f) + "&s=" + s + "&ct=" + quote(ct) + "&ca=" + ca
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComics(self, page, c, t, s):
        """
        ?Why cannot get comics?
        waziPicAcg.getComics(self, page, c, t, s)
        *Go listen to VOY@GER.*

        Get comics with page, category, tag and sort.

        Parameters:
            page: int or str
                The page of comics. Start from 1.
            
            c: str
                Category of comics. Can be string from getCategories.
            
            t: str
                Tag of comics. Please use traditional Chinese.
            
            s: str
                Sorting of comics.
                    ua: Default.
                    dd: From newest to oldest.
                    da: From oldest to newest.
                    vd: From users named most to users named least. (What is that? Hot?)
                    ld: From users liked most to users liked least.
        
        Return:
            Type: dict
            The comics. But for now, you cannot get comics from this method.
            Will return:
            {'code': 200, 'message': 'success'}
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码、分区、标签和排序，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 分区： {c}， 标签： {t}， 排序： {s}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comics"] + "?page=" + str(page) + "&c=" + quote(c)
        newUrl += "&t=" + quote(t) + "&s=" + s
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def search(self, page, keyword):
        """
        ??????????????????????????
        waziPicAcg.search(self, page, keyword)
        *I always find the API interfaces in my decompiled code so strange.*

        Search comics with page and keyword.
        
        Parameters:
            page: int or str
                The page of search. Start from 1.
            
            keyword: str
                The keyword of search.
        
        Return:
            Type: dict
            The comics. But for now, you cannot get comics from this method.
            Will return:
            {'code': 200, 'message': 'success'}
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和关键词，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 关键词： {keyword}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["search"] + "?page=" + str(page) + "&q=" + quote(keyword)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComic(self, comicId):
        """
        waziPicAcg.getComic(self, comicId)
        *I wonder about everything.*

        Get comic with comic id.

        Parameters:
            comicId: str
                The comic id.
        
        Return:
            Type: dict
            The comic.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "comic": {                                          # The comic.
                        "_id": str,                                     # The id of comic.
                        "_creator": {                                   # The creator of comic.
                            "_id": str,                                 # The id of creator.
                            "gender": str,                              # The gender of creator.
                            "name": str,                                # The name of creator.
                            "verified": bool,                           # Whether the creator is verified.
                            "exp": int,                                 # The exp of creator.
                            "level": int,                               # The level of creator.
                            "characters": list[str],                    # The characters of creator.
                            "role": str,                                # The role of creator.
                            "title": str,                               # The title of creator.
                            "avatar": {                                 # The avatar of creator.
                                "originalName": str,                    # The original name of avatar.
                                "path": str,                            # The path of avatar.
                                "fileServer": str                       # The file server of avatar.
                            },
                            "slogan": str,                              # The slogan of creator.
                            "character": str                            # The character of creator.
                        },
                        "title": str,                                   # The title of comic.
                        "description": str,                             # The description of comic.
                        "thumb": {                                      # The thumb of comic.
                            "originalName": str,                        # The original name of thumb.
                            "path": str,                                # The path of thumb.
                            "fileServer": str                           # The file server of thumb.
                        },
                        "author": str or may be other object,           # The author of comic.
                        "chineseTeam": str or may be other object,      # The chinese team of comic.
                        "categories": list[str],                        # The categories of comic.
                        "tags": list[str],                              # The tags of comic.
                        "pagesCount": int,                              # The pages count of comic.
                        "epsCount": int,                                # The eps count of comic.
                        "finished": bool,                               # Whether the comic is finished.
                        "updated_at": str,                              # The updated time of comic.
                        "created_at": str,                              # The created time of comic.
                        "allowDownload": bool,                          # Whether the comic allow download.
                        "allowComment": bool,                           # Whether the comic allow comment.
                        "totalLikes": int,                              # The total likes of comic.
                        "totalViews": int,                              # The total views of comic.
                        "viewsCount": int,                              # The views count of comic.
                        "likesCount": int,                              # The likes count of comic.
                        "isFavorite": bool,                             # Whether the comic is favorite by user.
                        "isLiked": bool,                                # Whether the comic is liked by user.
                        "commentsCount": int                            # The comments count of comic.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicId"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComicEps(self, comicId, page):
        """
        waziPicAcg.getComicEps(self, comicId, page)
        *Anxiety.*

        Get comic eps with page.

        Parameters:
            comicId: str
                The comic id.
            
            page: int or str
                The page.
        
        Return:
            Type: dict
            The comic eps.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "eps": {                                            # The eps.
                        "docs": [{                                      # The eps list.
                            "_id": str,                                 # The id of eps.
                            "title": str,                               # The title of eps.
                            "order": int,                               # The order of eps.
                            "updated_at": str,                          # The updated time of eps.
                            "id": str                                   # The id of eps.
                        }],
                        "total": int,                                   # The total of eps.
                        "limit": int,                                   # The limit of eps.
                        "page": int,                                    # The page of eps.
                        "pages": int                                    # The pages of eps.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和分 P 数据，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 分 P 数据： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicEps"].replace("{comicId}", comicId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def advancedSearch(self, categories, keyword, sort, page):
        """
        waziPicAcg.advancedSearch(self, categories, keyword, sort, page)
        *Step by step.*

        Advanced search with categories, keyword, sort and page.
        You should use this method rather than waziPicAcg.search and waziPicAcg.getComics.

        Parameters:
            categories: list[str]
                The categories. If you do not want to use this parameter, just set it to [].
            
            keyword: str
                The keyword.
            
            sort: str
                Sorting of comics.
                    ua: Default.
                    dd: From newest to oldest.
                    da: From oldest to newest.
                    vd: From users named most to users named least. (May Hot.)
                    ld: From users liked most to users liked least.
            
            page: int or str
                The page. Start from 1.
            
        Return:
            Type: dict
            The comics.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "comics": {                                         # The comics.
                        "total": int,                                   # The total of comics.
                        "page": int,                                    # The page of comics.
                        "pages": int,                                   # The pages of comics.
                        "docs": [{                                      # The comics list.
                            "updated_at": str,                          # The updated time of comic.
                            "thumb": {                                  # The thumb of comic.
                                "originalName": str,                    # The original name of thumb.
                                "path": str,                            # The path of thumb.
                                "fileServer": str                       # The file server of thumb.
                            },
                            "author": str,                              # The author of comic.
                            "description": str,                         # The description of comic.
                            "chineseTeam": str or may other object,     # The chinese team of comic.
                            "created_at": str,                          # The created time of comic.
                            "finished": bool,                           # Whether the comic is finished.
                            "categories": [str],                        # The categories of comic.
                            "title": str,                               # The title of comic.
                            "tags": [str],                              # The tags of comic.
                            "_id": str,                                 # The id of comic.
                            "likesCount": int                           # The likes count of comic.
                        }],
                        "limit": int                                    # The limit of comics.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分类、关键词、排序和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 分类： {categories}， 关键词： {keyword}， 排序： {sort}， "
                             f"页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["advSearch"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "categories": categories,
            "keyword": keyword,
            "sort": sort
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def getComicPages(self, comicId, eps, page):
        """
        waziPicAcg.getComicPages(self, comicId, eps, page)
        *Why we run?*

        Get the pages of comic.
        
        Parameters:
            comicId: str
                The comic ID.
            
            eps: int or str
                The eps of comic.
            
            page: int or str
                The page.
        
        Return:
            Type: dict
            The pages of comic.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "pages": {                                          # The pages of comic.
                        "docs": [{                                      # The pages list.
                            "_id": str,                                 # The id of page.
                            "media": {                                  # The media of page.
                                "originalName": str,                    # The original name of page.
                                "path": str,                            # The path of page.
                                "fileServer": str                       # The file server of page.
                            },
                            "id": str                                   # The id of page.
                        }],
                        "total": int,                                   # The total of pages.
                        "limit": int,                                   # The limit of pages.
                        "page": int,                                    # The page of pages.
                        "pages": int                                    # The pages of pages.
                    },
                    "ep": {                                             # The eps of comic.
                        "_id": str,                                     # The id of ep.
                        "title": str                                    # The title of ep.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID、分 P 数据和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 分 P 数据： {eps}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicPages"].replace("{comicId}", comicId).replace("{order}", str(eps)) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getComicRecommend(self, comicId):
        """
        waziPicAcg.getComicRecommend(self, comicId)
        *Black magic.*

        Get the recommend of comic. (Fix now!)

        Parameters:
            comicId: str
                The comic ID.
        
        Return:
            Type: dict
            The recommend comics of comic.
            May like:
            {
                "code": int,                                        # The status code of request.
                "message": str,                                     # The message of request.
                "data": {                                           # The data of request.
                    "comics": [{                                    # The recommend comics.
                        "_id": str,                                 # The id of comic.
                        "title": str,                               # The title of comic.
                        "author": str,                              # The author of comic.
                        "pagesCount": int,                          # The pages count of comic.
                        "epsCount": int,                            # The eps count of comic.
                        "finished": bool,                           # The finished of comic.
                        "categories": [str],                        # The categories of comic.
                        "thumb": {                                  # The thumb of comic.
                            "originalName": str,                    # The original name of thumb.
                            "path": str,                            # The path of thumb.
                            "fileServer": str                       # The file server of thumb.
                        },
                        "likesCount": int                           # The likes count of comic.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicRecommend"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getKeywords(self):
        """
        waziPicAcg.getKeywords(self)
        *Fly me to the mars.*

        Get the hot keywords.

        Parameters:
            None
        
        Return:
            Type: dict
            The hot keywords.
            May like:
            {
                "code": int,                                        # The status code of request.
                "message": str,                                     # The message of request.
                "data": {                                           # The data of request.
                    "keywords": [str]                               # The hot keywords.
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["keywords"], True, None, "GET", True)

    def getMyComments(self, page):
        """
        waziPicAcg.getMyComments(self, page)
        *No knowledge at all.*

        Get the comments of user.

        Parameters:
            page: int or str
                The page of comments. Start from 1.
        
        Return:
            Type: dict
            The comments of user.
            May like:
            {
                "code": int,                                        # The status code of request.
                "message": str,                                     # The message of request.
                "data": {                                           # The data of request.
                    "comments": {                                   # The comments of user.
                        "docs": [],                                 # The comment lists of user. (I don't know what could exist inside.)
                        "total": int,                               # The total of comments.
                        "limit": int,                               # The limit of comments.
                        "page": str,                                # The page of comments.
                        "pages": int                                # The pages of comments.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["myComments"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getMyFavourites(self, page, s):
        """
        waziPicAcg.getMyFavourites(self, page, s)
        *But I know this.*

        Get the favourites of user.

        Parameters:
            page: int or str
                The page of favourites. Start from 1.

            s: str
                The sort of favourites.
                You can use:
                    ua: Default.
                    dd: From newest to oldest.
                    da: From oldest to newest.
        
        Return:
            Type: dict
            The favourites of user.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "comics": {                                 # The comics of user.
                        "pages": int,                           # The pages of comics.
                        "total": int,                           # The total of comics.
                        "docs": [{                              # The comic lists of user.
                            "_id": str,                         # The id of comic.
                            "title": str,                       # The title of comic.
                            "author": str,                      # The author of comic.
                            "pagesCount": int,                  # The pages count of comic.
                            "epsCount": int,                    # The eps count of comic.
                            "finished": bool,                   # The finished of comic.
                            "categories": [str],                # The categories of comic.
                            "thumb": {                          # The thumb of comic.
                                "fileServer": str,              # The file server of thumb.
                                "path": str,                    # The path of thumb.
                                "originalName": str             # The original name of thumb.
                            },
                            "totalViews": int,                  # The total views of comic.
                            "totalLikes": int,                  # The total likes of comic.
                            "likesCount": int                   # The likes count of comic.
                        }],
                        "page": int,                            # The page of comics.
                        "limit": int                            # The limit of comics.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和排序，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 排序： {s}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["myFavourites"] + "?page=" + str(page) + "&s=" + s
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getMyProfile(self):
        """
        waziPicAcg.getMyProfile(self)
        *Like stars.*

        Get the profile of user.

        Parameters:
            None
        
        Return:
            Type: dict
            The profile of user.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "user": {                                   # The user of profile.
                        "_id": str,                             # The id of user.
                        "birthday": str,                        # The birthday of user.
                        "email": str,                           # The email of user.
                        "gender": str,                          # The gender of user.
                        "name": str,                            # The name of user.
                        "slogan": str,                          # The solgan of user.
                        "title": str,                           # The title of user.
                        "verified": bool,                       # Whether the user is verified.
                        "exp": int,                             # The exp of user.
                        "level": int,                           # The level of user.
                        "characters": [str],                    # The characters of user.
                        "created_at": str,                      # The created at of user.
                        "avatar": {                             # The avatar of user.
                            "fileServer": str,                  # The file server of avatar.
                            "path": str,                        # The path of avatar.
                            "originalName": str                 # The original name of avatar.
                        },
                        "isPunched": bool,                      # Whether the user is punched.
                        "character": str                        # The character of user.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["profile"], True, None, "GET", True)

    def getGames(self, page):
        """
        waziPicAcg.getGames(self, page)
        *NONE.*

        Get the games.

        Parameters:
            page: int or str
                The page of games. Start from 1.
        
        Return:
            Type: dict
            The games.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "games": {                                  # The games.
                        "docs": [{                              # The game lists.
                            "_id": str,                         # The id of game.
                            "title": str,                       # The title of game.
                            "version": str,                     # The version of game.
                            "publisher": str,                   # The publisher of game.
                            "suggest": bool,                    # Whether the game is suggested.
                            "adult": bool,                      # Whether the game is adult.
                            "android": bool,                    # Whether the game is android.
                            "ios": bool,                        # Whether the game is ios.
                            "icon": {                           # The icon of game.
                                "originalName": str,            # The original name of icon.
                                "path": str,                    # The path of icon.
                                "fileServer": str               # The file server of icon.
                            }
                        }],
                        "total": int,                           # The total of games.
                        "limit": int,                           # The limit of games.
                        "page": int,                            # The page of games.
                        "pages": int                            # The pages of games.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["games"] + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getGameInfo(self, gameId):
        """
        waziPicAcg.getGameInfo(self, gameId)
        *Hey!*

        Get the game info.

        Parameters:
            gameId: str
                The id of game.
        
        Return:
            Type: dict
            The game info.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "game": {                                   # The game info.
                        "_id": str,                             # The id of game.
                        "title": str,                           # The title of game.
                        "description": str,                     # The description of game.
                        "version": str,                         # The version of game.
                        "icon": {                               # The icon of game.
                            "fileServer": str,                  # The file server of icon.
                            "path": str,                        # The path of icon.
                            "originalName": str                 # The original name of icon.
                        },
                        "publisher": str,                       # The publisher of game.
                        "ios": bool,                            # Whether the game is ios.
                        "iosLinks": [str],                      # The ios links of game.
                        "android": bool,                        # Whether the game is android.
                        "androidLinks": [str],                  # The android links of game.
                        "adult": bool,                          # Whether the game is adult.
                        "suggest": bool,                        # Whether the game is suggested.
                        "downloadsCount": int,                  # The downloads count of game.
                        "screenshots": [{                       # The screenshots of game.
                            "originalName": str,                # The original name of screenshot.
                            "path": str,                        # The path of screenshot.
                            "fileServer": str                   # The file server of screenshot.
                        }],
                        "androidSize": int,                     # The android size of game.
                        "iosSize": int,                         # The ios size of game.
                        "updateContent": str,                   # The update content of game.
                        "updated_at": str,                      # The updated at of game.
                        "created_at": str,                      # The created at of game.
                        "likesCount": int,                      # The likes count of game.
                        "isLiked": bool,                        # Whether the game is liked.
                        "commentsCount": int                    # The comments count of game.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["games"] + "/" + str(gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def likeOrUnLikeGame(self, gameId):
        """
        waziPicAcg.likeOrUnLikeGame(self, gameId)
        *Light.*

        Like or unlike the game.

        Parameters:
            gameId: str
                The id of game.
        
        Return:
            Type: dict
            The return of request.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "action": str                               # The action of request. (like or unlike)
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameLike"].replace("{gameId}", gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def favOrUnFavComic(self, comicId):
        """
        waziPicAcg.favOrUnFavComic(self, comicId)
        *Without Decoration.*

        Favorite (v.) or unfavorite (v.) the comic.

        Parameters:
            comicId: str
                The id of comic.
            
        Return:
            Type: dict
            The return of request.
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "action": str                               # The action of request. (favorite or un_favorite)
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicFavourite"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def likeOrUnLikeComic(self, comicId):
        """
        waziPicAcg.likeOrUnLikeComic(self, comicId)
        *To Be Continued.*

        Like or unlike the comic.

        Parameters:
            comicId: str
                The id of comic.
        
        Return:
            Type: dict
            The return of request.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "action": str                               # The action of request. (like or unlike)
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicLike"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def likeOrUnLikeComment(self, commentId):
        """
        waziPicAcg.likeOrUnLikeComment(self, commentId)
        *Draw the curtains.*

        Like or unlike the comment.

        Parameters:
            commentId: str
                The id of comment.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentLike"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def hideOrUnHideComment(self, commentId):
        """
        waziPicAcg.hideOrUnHideComment(self, commentId)
        *SNS.*

        Hide or unhide the comment.

        Parameters:
            commentId: str
                The id of comment.
        
        Return:
            Type: dict
            The return of request.

            I got 1005 error, casue I am not the admin of the site.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentHide"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getCommentsChildren(self, commentId, page):
        """
        waziPicAcg.getCommentsChildren(self, commentId, page)
        *Labor.*

        Get the children comments of the comment.

        Parameters:
            commentId: str
                The id of comment.
            
            page: int or str
                The page of comment.
        
        Return:
            Type: dict
            The children comments of the comment.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "comments": {                               # The children comments of the comment.
                        "docs": [{                              # The children comments list of the comment.
                            "_id": str,                         # The id of comment.
                            "content": str,                     # The content of comment.
                            "_user": {                          # The user of comment.
                                "_id": str,                     # The id of user.
                                "gender": str,                  # The gender of user.
                                "name": str,                    # The name of user.
                                "title": str,                   # The title of user.
                                "verified": bool,               # Whether the user is verified.
                                "exp": int,                     # The exp of user.
                                "level": int,                   # The level of user.
                                "characters": [str],            # The characters of user.
                                "role": str,                    # The role of user.
                                "avatar": {                     # The avatar of user.
                                    "originalName": str,        # The original name of avatar.
                                    "path": str,                # The path of avatar.
                                    "fileServer": str,          # The file server of avatar.
                                },
                                "slogan": str,                  # The slogan of user.
                                "character": str                # The character of user.
                            },
                            "_parent": str,                     # The parent comment id of comment.
                            "_comic": str,                      # The comic id of comment.
                            "_game": str,                       # The game id of comment.
                            "isTop": bool,                      # Whether the comment is top.
                            "hide": bool,                       # Whether the comment is hidden.
                            "created_at": str,                  # The time of comment.
                            "id": str,                          # The id of comment.
                            "likesCount": int,                  # The likes count of comment.
                            "isLiked": bool                     # Whether the comment is liked.
                        }],
                        "total": int,                           # The total of comments.
                        "limit": int,                           # The limit of comments.
                        "page": str,                            # The page of comments.
                        "pages": int                            # The pages of comments.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentsChildren"].replace("{commentId}", commentId).replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def replyComment(self, commentId, content):
        """
        waziPicAcg.replyComment(self, commentId, content)
        *the internet is truly the festering cesspool of hell born from modern society. but even so, i have nowhere else to turn to. -- NEEDY GIRL OVERDOSE.*

        Reply comment.

        Parameters:
            commentId: str
                The id of comment.
            
            content: str
                The reply content.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["replyComment"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def reportComment(self, commentId):
        """
        waziPicAcg.reportComment(self, commentId)
        *Hurt.*

        Report comment.

        Parameters:
            commentId: str
                The id of comment.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentReport"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def topOrUnTopComment(self, commentId):
        """
        waziPicAcg.topOrUnTopComment(self, commentId)
        *So much pain.*

        Top or un-top comment. What the fuck is this? Normal user can use this method.

        Return:
            Type: dict
            The return of request.
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "isTop": bool                               # Whether the comment is top.
                }          
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["commentTop"].replace("{commentId}", commentId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getGameComments(self, gameId, page):
        """
        waziPicAcg.getGameComments(self, gameId, page)
        *I am the one who is going to die.*

        Get comments of game.

        Parameters:
            gameId: str
                The id of game.
            
            page: int or str
                The page of comments. Start from 1.
        
        Return:
            Type: dict
            The comments of game.
            May like:
            {
                "code": int,                                    # The status code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "comments": {                               # The comments of game.
                        "docs": [{                              # The comments list of game.
                            "_id": str,                         # The id of comment.
                            "content": str,                     # The content of comment.
                            "_user": {                          # The user of comment.
                                "_id": str,                     # The id of user.
                                "gender": str,                  # The gender of user.
                                "name": str,                    # The name of user.
                                "title": str,                   # The title of user.
                                "verified": bool，               # The verified of user.
                                "exp": int,                     # The exp of user.
                                "level": int,                   # The level of user.
                                "characters": list[str],        # The character of user.
                                "role": str,                    # The role of user.
                                "avatar": {                     # The avatar of user.
                                    "originalName": str,        # The original name of avatar.
                                    "path": str,                # The path of avatar.
                                    "fileServer": str           # The file server of avatar.
                                },
                                "slogan": str,                  # The slogan of user.
                                "character": str                # The character of user.
                            },
                            "_game": str,                       # The game id of comment.
                            "isTop": bool,                      # Whether the comment is top.
                            "hide": bool,                       # Whether the comment is hide.
                            "created_at": str,                  # The time of comment.
                            "id": str,                          # The id of comment.
                            "likesCount": int,                  # The likes count of comment.
                            "commentsCount": int,               # The comments count of comment.
                            "isLiked": bool                     # Whether the user has liked the comment.
                        }],
                        "total": int,                           # The total of comments.
                        "limit": int,                           # The limit of comments.
                        "page": str,                            # The page of comments.
                        "pages": int                            # The pages of comments.
                    },
                    "topComments": [{                           # The top comments of game.
                        "_id": str,                             # The id of comment.
                        "content": str,                         # The content of comment.
                        "_user": {                              # The user of comment.
                            "_id": str,                         # The id of user.
                            "gender": str,                      # The gender of user.
                            "name": str,                        # The name of user.
                            "title": str,                       # The title of user.
                            "verified": bool，                   # The verified of user.
                            "exp": int,                         # The exp of user.
                            "level": int,                       # The level of user.
                            "characters": list[str],            # The character of user.
                            "role": str,                        # The role of user.
                            "avatar": {                         # The avatar of user.
                                "originalName": str,            # The original name of avatar.
                                "path": str,                    # The path of avatar.
                                "fileServer": str               # The file server of avatar.
                            },
                            "slogan": str,                      # The slogan of user.
                            "character": str                    # The character of user.
                        },
                        "ip": str,                              # The ip of comment.
                        "_game": str,                           # The game id of comment.
                        "isTop": bool,                          # Whether the comment is top.
                        "hide": bool,                           # Whether the comment is hide.
                        "created_at": str,                      # The time of comment.
                        "likesCount": int,                      # The likes count of comment.
                        "commentsCount": int,                   # The comments count of comment.
                        "isLiked": bool                         # Whether the user has liked the comment.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameComments"].replace("{gameId}", gameId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def postGameComment(self, gameId, content):
        """
        waziPicAcg.postGameComment(self, gameId, content)
        *Huu~*

        Post a comment in a game by game id.

        Parameters:
            gameId: str
                The id of game.
            
            content: str
                The comment content.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到游戏 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 游戏 ID： {gameId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["gameComments"].replace("{gameId}", gameId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)

    def getComicComments(self, comicId, page):
        """
        waziPicAcg.getComicComments(self, comicId, page)
        *Nude.*

        Get the comments of comic.

        Parameters:
            comicId: str
                The id of comic.
            
            page: int or str
                The page of comments. Start from 1.
        
        Return:
            Type: dict
            The return of request.
            May like:
            {
                "code": int,                                    # The code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "comments": {                               # The comments of comic.
                        "docs": [{                              # The comments of comic.
                            "_id": str,                         # The id of comment.
                            "content": str,                     # The content of comment.
                            "_user": {                          # The user of comment.
                                "_id": str,                     # The id of user.
                                "gender": str,                  # The gender of user.
                                "name": str,                    # The name of user.
                                "title": str,                   # The title of user.
                                "verified": bool,               # The verified of user.
                                "exp": int,                     # The exp of user.
                                "level": int,                   # The level of user.
                                "characters": list[str],        # The character of user.
                                "role": str,                    # The role of user.
                                "avatar": {                     # The avatar of user.
                                    "fileServer": str,          # The file server of avatar.
                                    "path": str,                # The path of avatar.
                                    "originalName": str         # The original name of avatar.
                                },
                                "slogan": str,                  # The slogan of user.
                                "character": str                # The character of user.
                            },
                            "_comic": str,                      # The comic of comment.
                            "isTop": bool,                      # Whether the comment is top.
                            "hide": bool,                       # Whether the comment is hide.
                            "created_at": str,                  # The time of comment.
                            "id": str,                          # The id of comment.
                            "likesCount": int,                  # The likes count of comment.
                            "commentsCount": int,               # The comments count of comment.
                            "isLiked": bool                     # Whether the user has liked the comment.
                        }],
                        "total": int,                           # The total of comments.
                        "limit": int,                           # The limit of comments.
                        "page": str,                            # The page of comments.
                        "pages": int                            # The pages of comments.
                    },
                    "topComments": [{                           # The top comments of comic.
                        "_id": str,                             # The id of comment.
                        "content": str,                         # The content of comment.
                        "_user": {                              # The user of comment.
                            "_id": str,                     # The id of user.
                            "gender": str,                  # The gender of user.
                            "name": str,                    # The name of user.
                            "title": str,                   # The title of user.
                            "verified": bool                # The verified of user.
                            "exp": int,                     # The exp of user.
                            "level": int,                   # The level of user.
                            "characters": list[str],        # The character of user.
                            "role": str,                    # The role of user.
                            "avatar": {                     # The avatar of user.
                                "originalName": str,        # The original name of avatar.
                                "path": str,                # The path of avatar.
                                "fileServer": str           # The file server of avatar.
                            },
                            "slogan": str,                  # The slogan of user.
                            "character": str                # The character of user.
                        },
                        "ip": str,                              # The ip of comment.
                        "_comic": str,                          # The comic id of comment.
                        "isTop": bool,                          # Whether the comment is top.
                        "hide": bool,                           # Whether the comment is hide.
                        "created_at": str,                      # The time of comment.
                        "likesCount": int,                      # The likes count of comment.
                        "commentsCount": int,                   # The comments count of comment.
                        "isLiked": bool                         # Whether the user has liked the comment.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicComments"].replace("{comicId}", comicId) + "?page=" + str(page)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def postComicComment(self, comicId, content):
        """
        waziPicAcg.postComicComment(self, comicId, content)
        *So cute.*

        Post a comment of comic.

        Parameters:
            comicId: str
                The id of comic.
            
            content: str
                The content of comment.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["comicComments"].replace("{comicId}", comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        body = {
            "content": content
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {body}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, body, "POST", True)
    
    def getLeaveMessageRoomComments(self, page):
        """
        waziPicAcg.getLeaveMessageRoomComments(self, page)
        *Kind word*

        Get the comments of leave message room.
        It is actually from a comic id: 5822a6e3ad7ede654696e482

        Parameters:
            page: int or str
                The page of comments. Start from 1.
        
        Return:
            Type: dict
            The return of request.
            May like:
            {
                "code": int,                                    # The code of request.
                "message": str,                                 # The message of request.
                "data": {                                       # The data of request.
                    "comments": {                               # The comments of comic.
                        "docs": [{                              # The comments of comic.
                            "_id": str,                         # The id of comment.
                            "content": str,                     # The content of comment.
                            "_user": {                          # The user of comment.
                                "_id": str,                     # The id of user.
                                "gender": str,                  # The gender of user.
                                "name": str,                    # The name of user.
                                "title": str,                   # The title of user.
                                "verified": bool,               # The verified of user.
                                "exp": int,                     # The exp of user.
                                "level": int,                   # The level of user.
                                "characters": list[str],        # The character of user.
                                "role": str,                    # The role of user.
                                "avatar": {                     # The avatar of user.
                                    "fileServer": str,          # The file server of avatar.
                                    "path": str,                # The path of avatar.
                                    "originalName": str         # The original name of avatar.
                                },
                                "slogan": str,                  # The slogan of user.
                                "character": str                # The character of user.
                            },
                            "_comic": str,                      # The comic of comment.
                            "isTop": bool,                      # Whether the comment is top.
                            "hide": bool,                       # Whether the comment is hide.
                            "created_at": str,                  # The time of comment.
                            "id": str,                          # The id of comment.
                            "likesCount": int,                  # The likes count of comment.
                            "commentsCount": int,               # The comments count of comment.
                            "isLiked": bool                     # Whether the user has liked the comment.
                        }],
                        "total": int,                           # The total of comments.
                        "limit": int,                           # The limit of comments.
                        "page": str,                            # The page of comments.
                        "pages": int                            # The pages of comments.
                    },
                    "topComments": [{                           # The top comments of comic.
                        "_id": str,                             # The id of comment.
                        "content": str,                         # The content of comment.
                        "_user": {                              # The user of comment.
                            "_id": str,                     # The id of user.
                            "gender": str,                  # The gender of user.
                            "name": str,                    # The name of user.
                            "title": str,                   # The title of user.
                            "verified": bool                # The verified of user.
                            "exp": int,                     # The exp of user.
                            "level": int,                   # The level of user.
                            "characters": list[str],        # The character of user.
                            "role": str,                    # The role of user.
                            "avatar": {                     # The avatar of user.
                                "originalName": str,        # The original name of avatar.
                                "path": str,                # The path of avatar.
                                "fileServer": str           # The file server of avatar.
                            },
                            "slogan": str,                  # The slogan of user.
                            "character": str                # The character of user.
                        },
                        "ip": str,                              # The ip of comment.
                        "_comic": str,                          # The comic id of comment.
                        "isTop": bool,                          # Whether the comment is top.
                        "hide": bool,                           # Whether the comment is hide.
                        "created_at": str,                      # The time of comment.
                        "likesCount": int,                      # The likes count of comment.
                        "commentsCount": int,                   # The comments count of comment.
                        "isLiked": bool                         # Whether the user has liked the comment.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 交给 getComicComments 处理。")
        return waziPicAcg.getComicComments(self, self.leaveMsg, int(page))
    
    def postLeaveMessageRoomComment(self, content):
        """
        waziPicAcg.postLeaveMessageRoomComment(self, content)
        *That's only two hours a day*

        Post a comment to leave message room.

        Parameters:
            content: str
                The content of comment.
        
        Return:
            Type: dict
            The return of request.

            Because I am not brave enough to commit such an act,
            I am not sure exactly how the format would return.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 内容： {content}")
        waziLog.log("debug", f"({self.name}.{fuName}) 交给 postComicComment 处理。")
        return waziPicAcg.postComicComment(self, self.leaveMsg, content)

    def getSinglePage(self, fileServer, path):
        """
        waziPicAcg.getSinglePage(self, fileServer, path)
        *Far, far away.*

        Splice the URL to get the real address.

        Parameters:
            fileServer: str
                The file server.
            
            path: str
                The path of image.
        
        Return:
            Type: str
            The real address of image.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到头部（文件地址）和尾部（文件名），正在组合。")
        url = fileServer + "/static/" + path
        waziLog.log("info", f"({self.name}.{fuName}) 组合完成： {url}")
        return url

    def punchIn(self):
        """
        waziPicAcg.punchIn(self)
        *SEA.*

        Punch in.

        Parameters:
            None
        
        Return:
            If sueccess:
                Type: dict
                {
                    "code": int,                          # The code of response.
                    "message": str,                       # The message of response.
                    "data": {                             # The data of response.
                        "res": {                          # The data of response.
                            "status": str,                # The status of response.
                            "punchInLastDay": str         # The last day of punch in.
                        }
                    }
                }
            
            If failed:
                Type: dict
                {
                    "code": int,                          # The code of response.
                    "message": str,                       # The message of response.
                    "data": {                             # The data of response.
                        "res": {                          # The data of response.
                            "status": str                 # The status of response.
                        }
                    }
                }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["punchIn"], True, None, "POST", True)

    def register(self, loginName, password, birthday, gender, displayName, qa):
        """
        waziPicAcg.register(self, loginName, password, birthday, gender, displayName, qa)
        *Why ban gender?*

        Register a new account.

        Parameters:
            loginName: str
                Username.
                Check: /^(?!.*\\.\\.)(?!.*\\.$)[^\\W][\\w.]{0,29}$/i
            
            password: str
                Password without encryption.
            
            birthday: str
                Birthday, timestamp.
            
            gender: str
                Can be m(male) f(female) bot(bot).
            
            displayName: str
                Nickname.
            
            qa: list[dict{}]
                May like:
                [{
                    "question": str,                # The question 1.
                    "answer": str                   # The answer.
                }, {
                    "question": str,                # The question 2.
                    "answer": str                   # The answer.
                }, {
                    "question": str,                # The question 3.
                    "answer": str                   # The answer.
                }]
        
        Return:
            Type: dict
            May like:
            {
                "code": int,                          # The code of response.
                "message": str                        # The message of response.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名、密码、生日、性别、昵称和问答信息，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 密码： {password}， 生日： {birthday}")
        waziLog.log("debug", f"({self.name}.{fuName}) 性别： {gender}， 昵称： {displayName}， 问答信息： {qa}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合数据。")
        data = {
            "email": loginName,
            "password": password,
            "birthday": birthday,
            "gender": gender,
            "name": displayName,
            "answer1": qa[0]["answer"],
            "answer2": qa[1]["answer"],
            "answer3": qa[2]["answer"],
            "question1": qa[0]["question"],
            "question2": qa[1]["question"],
            "question3": qa[2]["question"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["register"], False, data, "POST", True)

    def uploadAvatar(self, params):
        """
        waziPicAcg.uploadAvatar(self, params)
        *No need to be so sensitive.*

        Upload avatar or change avatar.

        Parameters:
            params: dict
                Type 1, use file path:
                    {
                        "type": "file",                 # The type of upload.
                        "path": str                     # The path of file.
                    }
                
                Type 2, use base64:
                    {
                        "type": "base64",               # The type of upload.
                        "format": str,                  # The format of image.
                        "data": str                     # The data of image.
                    }
        
        Return:
            Type: dict
            May like:
            {
                "code": int,                          # The code of response.
                "message": str                        # The message of response.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到参数，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 参数： {params}")
        if params["type"] == "base64":
            waziLog.log("debug", f"({self.name}.{fuName}) 用户给出 base64 信息，正在写入。")
            upload = "data:image/" + params["format"] + ";base64," + params["data"]
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {upload}")
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 用户给出文件路径，正在获取文件扩展名。")
            fileFormat = os.path.splitext(params["path"])[-1][1:]
            if fileFormat == "jpg":
                waziLog.log("debug", f"({self.name}.{fuName}) 自动修正 jpg 为 jpeg")
                fileFormat = "jpeg"
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {fileFormat}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取文件 base64。")
            with open(params["path"], "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在写入。")
            upload = "data:image/" + fileFormat + ";base64," + data
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成： {upload}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合数据。")
        data = {
            "avatar": upload
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["avatar"], True, data, "PUT", True)

    def setTitle(self, userId, title):
        """
        waziPicAcg.setTitle(self, userId, title)
        *No worry about the length of title.*

        Give a title for a user.

        Parameters:
            userId: str
                The id of user.
            
            title: str
                The title of user.
        
        Return:
            Type: dict
            The response of server.

            I got 1015 error, cause this request is invalid. But why?
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID 和头衔内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}， 头衔内容： {title}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["userTitle"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "title": title
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, data, "PUT", True)

    def resetPassword(self, loginName, questionNo, answer):
        """
        waziPicAcg.resetPassword(self, loginName, questionNo, answer)
        *Invalid time.*

        Reset your password.

        Parameters:
            loginName: str
                The login name of user.
            
            questionNo: int or str
                The question number of user.
            
            answer: str
                The answer of question.
        
        Return:
            Type: dict
            The response of server.

            I got 1015 error, cause this request is invalid. But why?
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名，问题编号，答案，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 问题编号： {questionNo}， 答案： {answer}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName,
            "questionNo": int(questionNo),
            "answer": answer
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["resetPassword"], False, data, "POST", True)

    def forgotPassword(self, loginName):
        """
        waziPicAcg.forgotPassword(self, loginName)
        *Incompetence.*

        If you forgot your password, you can use this method.
        But I don't know how to use it. Always return 1015 error.
        I'm really close to crying out. ≧ ﹏ ≦

        Parameters:
            loginName: str
                The login name of user.
        
        Return:
            Type: dict
            The response of server.

            I got 1015 error, cause this request is invalid. But why?
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["forgotPassword"], False, data, "POST", True)

    def adjustExp(self, userId, exp):
        """
        waziPicAcg.adjustExp(self, userId, exp)
        *The disappearance of infrastructure.*

        Adjust the exp of a user.
        May deprecated.

        Parameters:
            userId: str
                The id of user.
            
            exp: int or str
                The exp of user.
        
        Return:
            Type: dict
            The response of server.

            I got 1007 error, it means that the method not found.
            But you can find this api from the Decompiled code of PicAcg.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID 和经验值，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}， 经验值： {exp}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "exp": int(exp),
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["adjustExp"], True, data, "POST", True)

    def changePassword(self, oldPassword, newPassword):
        """
        waziPicAcg.changePassword(self, oldPassword, newPassword)
        *It works!*

        Change the password of user.

        Parameters:
            oldPassword: str
                The old password of user.
            
            newPassword: str
                The new password of user.
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                # The code of response.
                "message": str              # The message of response.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到旧密码和新密码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 旧密码： {oldPassword}， 新密码： {newPassword}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "old_password": oldPassword,
            "new_password": newPassword
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["password"], True, data, "PUT", True)

    def changeDisplayName(self, loginName, newDisplayName):
        """
        waziPicAcg.changeDisplayName(self, loginName, newDisplayName)
        *Conqueror.*

        Change the display name.

        Parameters:
            loginName: str
                The login name of user.
            
            newDisplayName: str
                The new display name of user.
        
        Return:
            Type: dict
            The response of server.

            I got 1030 error, it means that id is already updated.
            I don't know why.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登录名和新昵称，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 登录名： {loginName}， 新昵称： {newDisplayName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "email": loginName,
            "name": newDisplayName
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["updateId"], True, data, "PUT", True)

    def changeSlogan(self, newSlogan):
        """
        waziPicAcg.changeSlogan(self, newSlogan)
        *Monkey.*

        Change the slogan.

        Parameters:
            newSlogan: str
                The new slogan of user.
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                # The code of response.
                "message": str              # The message of response.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到新签名，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 新签名： {newSlogan}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "slogan": newSlogan
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["profile"], True, data, "PUT", True)

    def changeQA(self, qa):
        """
        waziPicAcg.changeQA(self, qa)
        *Phoenix.*

        Change the user safe questions and answers.

        Parameters:
            qa: list[dict{}]
            May like:
                [{
                    "question": str,                # The question 1.
                    "answer": str                   # The answer.
                }, {
                    "question": str,                # The question 2.
                    "answer": str                   # The answer.
                }, {
                    "question": str,                # The question 3.
                    "answer": str                   # The answer.
                }]
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                # The code of response.
                "message": str              # The message of response.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到新问答内容，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 问答： {qa}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "question1": qa[0]["q"],
            "question2": qa[1]["q"],
            "question3": qa[2]["q"],
            "answer1": qa[0]["a"],
            "answer2": qa[1]["a"],
            "answer3": qa[2]["a"]
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["updateQA"], True, data, "PUT", True)

    def removeUserComments(self, userId):
        """
        waziPicAcg.removeUserComments(self, userId)
        *Dictatorship.*

        Remove all comments of user.

        Parameters:
            userId: str
                The id of user.
        
        Return:
            Type: dict
            The response of server.

            I got 1007 error, it means that the method not found.
            But you can find this api from the Decompiled code of PicAcg.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["removeComment"], True, data, "POST", True)

    def getH24LeaderBoard(self):
        """
        waziPicAcg.getH24LeaderBoard(self)
        *Momentary.*

        Get the 24 hours leader board.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "comics": [{                                # The comics.
                        "_id": str,                             # The id of comic.
                        "title": str,                           # The title of comic.
                        "author": str,                          # The author of comic.
                        "totalViews": int,                      # The total views of comic.
                        "totalLikes": int,                      # The total likes of comic.
                        "pagesCount": int,                      # The pages count of comic.
                        "epsCount": int,                        # The eps count of comic.
                        "finished": bool,                       # The finished of comic.
                        "categories": [str],                    # The categories of comic.
                        "thumb": {                              # The thumb of comic.
                            "fileServer": str,                  # The file server of thumb.
                            "path": str,                        # The path of thumb.
                            "originalName": str                 # The original name of thumb.
                        },
                        "viewsCount": int,                      # The views count of comic.
                        "leaderboardCount": int,                # The leaderboard count of comic.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=H24&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getD7LeaderBoard(self):
        """
        waziPicAcg.getD7LeaderBoard(self)
        *Backtrack.*

        Get the 7 days leader board.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "comics": [{                                # The comics.
                        "_id": str,                             # The id of comic.
                        "title": str,                           # The title of comic.
                        "author": str,                          # The author of comic.
                        "totalViews": int,                      # The total views of comic.
                        "totalLikes": int,                      # The total likes of comic.
                        "pagesCount": int,                      # The pages count of comic.
                        "epsCount": int,                        # The eps count of comic.
                        "finished": bool,                       # The finished of comic.
                        "categories": [str],                    # The categories of comic.
                        "thumb": {                              # The thumb of comic.
                            "fileServer": str,                  # The file server of thumb.
                            "path": str,                        # The path of thumb.
                            "originalName": str                 # The original name of thumb.
                        },
                        "viewsCount": int,                      # The views count of comic.
                        "leaderboardCount": int,                # The leaderboard count of comic.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=D7&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getD30LeaderBoard(self):
        """
        waziPicAcg.getD30LeaderBoard(self)
        *Probably, it can still be saved.*

        Get the 30 days leader board.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "comics": [{                                # The comics.
                        "_id": str,                             # The id of comic.
                        "title": str,                           # The title of comic.
                        "author": str,                          # The author of comic.
                        "totalViews": int,                      # The total views of comic.
                        "totalLikes": int,                      # The total likes of comic.
                        "pagesCount": int,                      # The pages count of comic.
                        "epsCount": int,                        # The eps count of comic.
                        "finished": bool,                       # The finished of comic.
                        "categories": [str],                    # The categories of comic.
                        "thumb": {                              # The thumb of comic.
                            "fileServer": str,                  # The file server of thumb.
                            "path": str,                        # The path of thumb.
                            "originalName": str                 # The original name of thumb.
                        },
                        "viewsCount": int,                      # The views count of comic.
                        "leaderboardCount": int,                # The leaderboard count of comic.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["leaderBoard"] + "?tt=D30&ct=VC"
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def knightLeaderBoard(self):
        """
        waziPicAcg.knightLeaderBoard(self)
        *Climbing.*

        Get the knight leader board.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "users": [{                                 # The users.
                        "_id": str,                             # The id of user.
                        "gender": str,                          # The gender of user.
                        "name": str,                            # The name of user.
                        "slogan": str,                          # The solgan of user.
                        "title": str,                           # The title of user.
                        "verified": bool,                       # Whether the user is verified.
                        "exp": int,                             # The exp of user.
                        "level": int,                           # The level of user.
                        "characters": [str],                    # The characters of user.
                        "role": str,                            # The role of user.
                        "avatar": {                             # The avatar of user.
                            "fileServer": str,                  # The file server of avatar.
                            "path": str,                        # The path of avatar.
                            "originalName": str                 # The original name of avatar.
                        },
                        "comicsUploaded": int,                  # The comics uploaded of user.
                        "character": str                        # The character of user.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["knight"], True, None, "GET", True)

    def getRandomComics(self):
        """
        waziPicAcg.getRandomComics(self)
        *Sometimes.*

        Get the random comics.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "comics": [{                                # The comics.
                        "_id": str,                             # The id of comic.
                        "title": str,                           # The title of comic.
                        "author": str,                          # The author of comic.
                        "totalViews": int,                      # The total views of comic.
                        "totalLikes": int,                      # The total likes of comic.
                        "pagesCount": int,                      # The pages count of comic.
                        "epsCount": int,                        # The eps count of comic.
                        "finished": bool,                       # The finished of comic.
                        "categories": [str],                    # The categories of comic.
                        "thumb": {                              # The thumb of comic.
                            "originalName": str,                # The original name of thumb.
                            "path": str,                        # The path of thumb.
                            "fileServer": str                   # The file server of thumb.
                        },
                        "likesCount": int                       # The likes count of comic.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["randomComic"], True, None, "GET", True)

    def getCollections(self):
        """
        waziPicAcg.getCollections(self)
        *Telephone.*

        Get the collections.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "collections": [{                           # The collections.
                        "title": str,                           # The title of collection.
                        "comics": [{                            # The comics.
                            "_id": str,                         # The id of comic.
                            "title": str,                       # The title of comic.
                            "thumb": {                          # The thumb of comic.
                                "originalName": str,            # The original name of thumb.
                                "path": str,                    # The path of thumb.
                                "fileServer": str               # The file server of thumb.
                            },
                            "author": str,                      # The author of comic.
                            "categories": [str],                # The categories of comic.
                            "finished": bool,                   # The finished of comic.
                            "epsCount": int,                    # The eps count of comic.
                            "pagesCount": int,                  # The pages count of comic.
                            "totalLikes": int,                  # The total likes of comic.
                            "totalViews": int                   # The total views of comic.
                        }]
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["collections"], True, None, "GET", True)

    def getBanners(self):
        """
        waziPicAcg.getBanners(self)
        *Click it and save it.*

        Get the banners.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "banners": [{                               # The banners.
                        "_id": str,                             # The id of banner.
                        "title": str,                           # The title of banner.
                        "shortDescription": str,                # The short description of banner.
                        "_game": str,                           # The game of banner.
                        "link": str,                            # The link of banner.
                        "type": str,                            # The type of banner.
                        "thumb": {                              # The thumb of banner.
                            "fileServer": str,                  # The file server of thumb.
                            "path": str,                        # The path of thumb.
                            "originalName": str                 # The original name of thumb.
                        }
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["banners"], True, None, "GET", True)

    def init(self):
        """
        waziPicAcg.init(self)
        *How to use?*

        Initialize and ...

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "status": str,                                  # The status of initialization.
                "addresses": [str],                             # The addresses of initialization.
                "waka": str,                                    # The waka of initialization.
                "adKeyword": str                                # The ad keyword of initialization.
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.justUP(self, self.urls["init"], None, "GET", True)

    def initAndroid(self):
        """
        waziPicAcg.initAndroid(self)
        *Start!*
        
        Get android initialization.

        Parameters:
            None
        
        Return:
            Type: dict
            The response of server.
            May like:
            {
                "code": int,                                    # The code of response.
                "message": str,                                 # The message of response.
                "data": {                                       # The data of response.
                    "isPunched": bool,                          # Whether the user is punched.
                    "latestApplication": {                      # The latest application.
                        "_id": str,                             # The id of latest application.
                        "downloadUrl": str,                     # The download url of latest application.
                        "updateContent": str,                   # The update content of latest application.
                        "version": str,                         # The version of latest application.
                        "updated_at": str,                      # The update time of latest application.
                        "created_at": str,                      # The create time of latest application.
                        "apk": {                                # The apk of latest application.
                            "originalName": str,                # The original name of apk.
                            "path": str,                        # The path of apk.
                            "fileServer": str                   # The file server of apk.
                        }
                    },
                    "imageServer": str,                         # The image server.
                    "apiLevel": int,                            # The api level.
                    "minApiLevel": int,                         # The min api level.
                    "categories": [{                            # The categories.
                        "_id": str,                             # The id of category.
                        "title": str                            # The title of category.
                    }],
                    "notification": None or other object,       # The notification.
                    "isIdUpdated": bool,                        # Whether the id is updated.
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["initAndroid"], True, None, "GET", True)

    def changeImageQuality(self, number):
        """
        waziPicAcg.changeImageQuality(self, number)
        *TV noise make me cry.*

        Change the image quality.

        Parameters:
            number: int or str
                The number of image quality.
                    0: original
                    1: low
                    2: medium
                    3: high

        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图片素质信息，正在写入。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图片素质信息： {number}")
        self.headers["image-quality"] = self.imageQuality[int(number)]
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成： {self.headers['image-quality']}")

    def createFolder(self, path, title):
        """
        waziPicAcg.createFolder(self, path, title)
        *SYSTEM!*

        Create a folder.

        Parameters:
            path: str
                The path of folder.
            
            title: str
                The title of folder.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到创建文件夹请求，已悉知路径和标题信息，正在创建。")
        waziLog.log("debug", f"({self.name}.{fuName}) 路径： {path}， 标题信息： {title}")
        isExists = os.path.exists(os.path.join(path, self.fileName.toRight(title)))
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在该文件夹，正在创建。")
            os.makedirs(os.path.join(path, self.fileName.toRight(title)))
            waziLog.log("debug", f"({self.name}.{fuName}) 创建完成。")

    def createFolderEps(self, path, title, docTitle):
        """
        waziPicAcg.createFolderEps(self, path, title, docTitle)
        *I have to continue suffering.*

        Create a folder of eps.

        Parameters:
            path: str
                The path of folder.
            
            title: str
                The title of folder.
            
            docTitle: str
                The title of eps.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到创建子文件夹请求，已悉知路径、标题信息和分页标题信息，正在创建。")
        waziLog.log("debug", f"({self.name}.{fuName}) 路径： {path}， 标题信息： {title}， 分页标题信息： {docTitle}")
        isExists = os.path.exists(os.path.join(path, self.fileName.toRight(title), docTitle))
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 不存在该文件夹，正在创建。")
            os.makedirs(os.path.join(path, self.fileName.toRight(title), docTitle))
            waziLog.log("debug", f"({self.name}.{fuName}) 创建完成。")

    def getThumbImageLink(self, comicId):
        """
        waziPicAcg.getThumbImageLink(self, comicId)
        *Cracks cause rupture.*

        Get the thumb image link.

        Parameters:
            comicId: str
                The id of comic.
        
        Return:
            Type: list[str]
            The thumb image link and other information.
                0: original file name, Type: str
                1: comic name, Type: str
                2: thumb image link, Type: str
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在获取封面地址和标题。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getComic 获取漫画信息。")
        comicInfo = waziPicAcg.getComic(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取原始文件名和文件路径及标题。")
        originalName = comicInfo["data"]["comic"]["thumb"]["originalName"]
        filePath = comicInfo["data"]["comic"]["thumb"]["path"]
        comicName = comicInfo["data"]["comic"]["title"]
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在组合 URL。")
        fileURL = "https://storage.wikawika.xyz/static/" + filePath
        waziLog.log("debug", f"({self.name}.{fuName}) URL 组合完成： {fileURL}")
        data = [originalName, comicName, fileURL]
        waziLog.log("info", f"({self.name}.{fuName}) 数据： {data}， 返回。")
        return data

    def getThumbImage(self, comicId, path):
        """
        waziPicAcg.getThumbImage(self, comicId, path)
        *The forest is dark and deep.*

        Download the thumb image.

        Parameters:
            comicId: str
                The id of comic.
            
            path: str
                The path of folder.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和下载路径，正在下载封面。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}， 下载路径： {path}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImage 获取封面及信息。")
        thumbs = waziPicAcg.getThumbImageLink(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {thumbs}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建文件夹。")
        waziPicAcg.createFolder(self, path, thumbs[1].strip())
        waziLog.log("debug", f"({self.name}.{fuName}) 创建完成，正在发起请求。")
        temp = waziPicAcg.justUP(self, thumbs[2], None, "GET", False)
        waziLog.log("debug", f"({self.name}.{fuName}) 发起完成，正在写入。")
        filePath = os.path.join(path, self.fileName.toRight(thumbs[1].strip()), "thumb_" + self.fileName.toRight(thumbs[0]))
        with open(filePath, "wb") as f:
            f.write(temp.data)
        waziLog.log("info", f"({self.name}.{fuName}) 已写入到： {filePath}")
        return filePath

    def getChat(self):
        """
        waziPicAcg.getChat(self)
        *And a tree falls in the forest.*

        Get the chat.

        Parameters:
            None
        
        Return:
            Type: data
            The chat.
            May like:
            {
                "code": int,                                # The code of the response.
                "message": str,                             # The message of the response.
                "data": {                                   # The data of the response.
                    "chatList": [{                          # The chat list.
                        "title": str,                       # The title of the chat.
                        "description": str,                 # The description of the chat.
                        "url": str,                         # The url of the chat.
                        "avatar": str,                      # The avatar of the chat.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["chat"], True, None, "GET", True)

    def getAPPs(self):
        """
        waziPicAcg.getAPPs(self)
        *A bird that flies.*

        Get the APPs.

        Parameters:
            None
        
        Return:
            Type: dict
            The APPs.
            May like:
            {
                "code": int,                                # The code of the response.
                "message": str,                             # The message of the response.
                "data": {                                   # The data of the response.
                    "apps": [{                              # The APPs.
                        "title": str,                       # The title of the APPs.
                        "url": str,                         # The url of the APPs.
                        "icon": str,                        # The icon of the APPs.
                        "showTitleBar": bool,               # Whether show the title bar of the APPs.
                        "description": str                  # The description of the APPs.
                    }]
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, self.urls["apps"], True, None, "GET", True)
    
    def getComicImageURLs(self, pageDict):
        """
        waziPicAcg.getComicImageURLs(self, pageDict)
        *The story end with a kiss.*

        Get the comic image URLs.

        Parameters:
            pageDict: dict
                The page dictionary. waziPicAcg.getComicPages()
        
        Return:
            Type: list[str]
            The comic image URLs.

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分 P 分页字典，正在获取漫画图片地址: {pageDict}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
        urls = []
        for i in pageDict["data"]["pages"]["docs"]:
            if "fileServer" in i["media"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在 fileServer，使用返回值。")
                fileServer = i["media"]["fileServer"]
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不存在 fileServer，已填入默认值。")
                fileServer = "https://storage1.picacomic.com"
            waziLog.log("debug", f"({self.name}.{fuName}) fileServer 为 {fileServer}")
            url = waziPicAcg.getSinglePage(self, fileServer, i["media"]["path"])
            urls.append(url)
        return urls

    def singleDownloadComicImage(self, pageDict, path, comicName, docTitle):
        """
        waziPicAcg.singleDownloadComicImage(self, pageDict, path, comicName, docTitle)
        *Ramake.*

        Download the comic image in one page.

        Parameters:
            pageDict: dict
                The page dictionary. waziPicAcg.getComicPages()
            
            path: str
                The path of the comic.
            
            comicName: str
                The name of the comic.
            
            docTitle: str
                The title of the eps.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到分 P 分页字典，路径，漫画 ID 和分页标题，正在下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 分 P 分页字典： {pageDict}， 路径： {path}， 漫画 ID： {comicName}， "
                             f"分页标题： {docTitle}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备进入遍历。")
        for i in pageDict["data"]["pages"]["docs"]:
            if "fileServer" in i["media"]:
                waziLog.log("debug", f"({self.name}.{fuName}) 存在 fileServer，使用返回值。")
                fileServer = i["media"]["fileServer"]
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 不存在 fileServer，已填入默认值。")
                fileServer = "https://storage1.picacomic.com"
            waziLog.log("debug", f"({self.name}.{fuName}) fileServer 为 {fileServer}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
            temp = waziPicAcg.forHeaderYesUP(self, waziPicAcg.getSinglePage(self, fileServer, i["media"]["path"]),
                                             None, "GET", False)
            waziLog.log("debug", f"({self.name}.{fuName}) 请求发起完成，正在写入。")
            with open(os.path.join(path, self.fileName.toRight(comicName).strip(),
                                   self.fileName.toRight(docTitle).strip(),
                                   self.fileName.toRight(i["media"]["originalName"]).strip()
                                   ), "wb") as f:
                f.write(temp.data)
            waziLog.log("debug", f"({self.name}.{fuName}) 写入完成。")
    
    def yieldGetComicFilesList(self, comicId):
        """
        next(waziPicAcg.yieldGetComicFilesList(self, comicId))
        *Always so melancholy.*

        A generator to tet the comic files list one page by one page.

        Parameters:
            comicId: str
                The comic ID.
        
        Each Yield:
            At first:
                Type: list[str]
                The thumbnail information.
                    0: original file name, Type: str
                    1: comic name, Type: str
                    2: thumb image link, Type: str
            
            After:
                Type: list[str]
                The comic image URLs.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在开始获取： {comicId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImageLink 获取封面。")
        yield waziPicAcg.getThumbImageLink(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在将所有的分页信息收集起来。")
        epsList = []
        epsInfo = waziPicAcg.getComicEps(self, comicId, 1)
        for epsItem in epsInfo["data"]["eps"]["docs"]:
            epsList.append(epsItem)
        if epsInfo["data"]["eps"]["pages"] > 1:
            for i in range(2, epsInfo["data"]["eps"]["pages"] + 1):
                epsInfo = waziPicAcg.getComicEps(self, comicId, i)
                for epsItem in epsInfo["data"]["eps"]["docs"]:
                    epsList.append(epsItem)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进入循环。")
        for i in epsList:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细内容。")
            pageInfo = waziPicAcg.getComicPages(self, comicId, i["order"], 1)
            waziLog.log("debug", f"({self.name}.{fuName}) 通过 getComicImageURLs 获取链接。")
            yield waziPicAcg.getComicImageURLs(self, pageInfo)
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查页数。")
            if pageInfo["data"]["pages"]["pages"] == 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 无需进行更多的页数遍历，若有，可以进入下一个分页遍历。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 多页，正在进入 for in range。")
                for q in range(2, pageInfo["data"]["pages"]["pages"] + 1):
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在请求 {q} 页。")
                    newPage = waziPicAcg.getComicPages(self, comicId, i["order"], q)
                    waziLog.log("debug", f"({self.name}.{fuName}) 请求完成，正在通过 getComicImageURLs 获取链接。")
                    yield waziPicAcg.getComicImageURLs(self, newPage)

    def getComicFilesList(self, comicId):
        """
        waziPicAcg.getComicFilesList(self, comicId)
        *Thunder.*

        Get the comic files list at once.
        Recommended to use yieldGetComicFilesList instead.

        Parameters:
            comicId: str
                The comic ID.
        
        Return:
            Type: list[list[str]]
            The comic files list.
            Index 0:
                Type: list[str]
                The thumbnail information.
                    0: original file name, Type: str
                    1: comic name, Type: str
                    2: thumb image link, Type: str
            
            Index 1, 2, ...:
                Type: list[str]
                The comic image URLs.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID，正在开始获取： {comicId}")
        files = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImageLink 获取封面。")
        thumbs = waziPicAcg.getThumbImageLink(self, comicId)
        files.append(thumbs)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在将所有的分页信息收集起来。")
        epsList = []
        epsInfo = waziPicAcg.getComicEps(self, comicId, 1)
        for epsItem in epsInfo["data"]["eps"]["docs"]:
            epsList.append(epsItem)
        if epsInfo["data"]["eps"]["pages"] > 1:
            for i in range(2, epsInfo["data"]["eps"]["pages"] + 1):
                epsInfo = waziPicAcg.getComicEps(self, comicId, i)
                for epsItem in epsInfo["data"]["eps"]["docs"]:
                    epsList.append(epsItem)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进入循环。")
        for i in epsList:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细内容。")
            pageInfo = waziPicAcg.getComicPages(self, comicId, i["order"], 1)
            waziLog.log("debug", f"({self.name}.{fuName}) 通过 getComicImageURLs 获取链接。")
            files.append(waziPicAcg.getComicImageURLs(self, pageInfo))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在检查页数。")
            if pageInfo["data"]["pages"]["pages"] == 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 无需进行更多的页数遍历，若有，可以进入下一个分页遍历。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 多页，正在进入 for in range。")
                for q in range(2, pageInfo["data"]["pages"]["pages"] + 1):
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在请求 {q} 页。")
                    newPage = waziPicAcg.getComicPages(self, comicId, i["order"], q)
                    waziLog.log("debug", f"({self.name}.{fuName}) 请求完成，正在通过 getComicImageURLs 获取链接。")
                    files.append(waziPicAcg.getComicImageURLs(self, newPage))
                    waziLog.log("debug", f"({self.name}.{fuName}) 获取完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 全部获取完成。")
        return files

    def downloadComic(self, comicId, path):
        """
        waziPicAcg.downloadComic(self, comicId, path)
        *In fact, I really don't care.*

        Download the comic at once.

        Parameters:
            comicId: str
                The comic ID.
            
            path: str
                The path to save the comic.
        
        Return:
            Type: str
            If successful, return "Done! / 完工！"
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到漫画 ID 和下载路径，正在开始下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 漫画 ID： {comicId}，下载路径： {path}。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 getThumbImage 获取封面。")
        waziPicAcg.getThumbImage(self, comicId, path)
        waziLog.log("debug", f"({self.name}.{fuName}) 下载完成，正在获取漫画信息。")
        comicInfo = waziPicAcg.getComic(self, comicId)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，正在获取漫画名和分页。")
        comicName = comicInfo["data"]["comic"]["title"]
        waziLog.log("debug", f"({self.name}.{fuName}) 正在将所有的分页信息收集起来。")
        epsList = []
        epsInfo = waziPicAcg.getComicEps(self, comicId, 1)
        for epsItem in epsInfo["data"]["eps"]["docs"]:
            epsList.append(epsItem)
        if epsInfo["data"]["eps"]["pages"] > 1:
            for i in range(2, epsInfo["data"]["eps"]["pages"] + 1):
                epsInfo = waziPicAcg.getComicEps(self, comicId, i)
                for epsItem in epsInfo["data"]["eps"]["docs"]:
                    epsList.append(epsItem)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进入循环。")
        for i in epsList:
            waziLog.log("debug", f"({self.name}.{fuName}) 正在创建文件夹。")
            waziPicAcg.createFolderEps(self, path, comicName.strip(), i["title"].strip())
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取详细内容。")
            pageInfo = waziPicAcg.getComicPages(self, comicId, i["order"], 1)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在下载。")
            waziPicAcg.singleDownloadComicImage(self, pageInfo, path, comicName, i["title"])
            waziLog.log("debug", f"({self.name}.{fuName}) 下载完成，正在检查页数。")
            if pageInfo["data"]["pages"]["pages"] == 1:
                waziLog.log("debug", f"({self.name}.{fuName}) 无需进行更多的页数遍历，若有，可以进入下一个分页遍历。")
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 多页，正在进入 for in range。")
                for q in range(2, pageInfo["data"]["pages"]["pages"] + 1):
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在请求 {q} 页。")
                    newPage = waziPicAcg.getComicPages(self, comicId, i["order"], q)
                    waziLog.log("debug", f"({self.name}.{fuName}) 请求完成，正在通过 singleDownloadComicImage 下载。")
                    waziPicAcg.singleDownloadComicImage(self, newPage, path, comicName, i["title"])
                    waziLog.log("debug", f"({self.name}.{fuName}) 下载完成。")
        waziLog.log("info", f"({self.name}.{fuName}) 全部下载完成。")
        return "Done! / 完工！"
        
    def getAndroidAPPs(self, page):
        """
        waziPicAcg.getAndroidAPPs(self, page)
        *History.*

        Get android apps.

        Parameters:
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: dict
            The android apps.
            May like:
            {
                "code": int,                                        # The code of the response.
                "message": str,                                     # The message of the response.
                "data": {                                           # The data of the response.
                    "applications": {                               # The applications.
                        "docs": [{                                  # The list of the applications.
                            "_id": str,                             # The ID of the application.
                            "downloadUrl": str,                     # The download URL of the application.
                            "updateContent": str,                   # The update content of the application.
                            "version": str,                         # The version of the application.
                            "created_at": str,                      # The time of the application.
                            "apk": {                                # The apk of the application.
                                "originalName": str,                # The original name of the apk.
                                "path": str,                        # The path of the apk.
                                "fileServer": str                   # The file server of the apk.
                            }
                        }],
                        "total": int,                               # The total number of the applications.
                        "limit": int,                               # The limit of the applications.
                        "page": int,                                # The page number of the applications.
                        "pages": int                                # The total number of the pages.
                    },
                    "apiLevel": int,                                # The api level of the response.
                    "minApiLevel": int                              # The min api level of the response.
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["androidAPPs"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def blockUser(self, userId):
        """
        waziPicAcg.blockUser(self, userId)
        *Burying.*

        Block a user.

        Parameters:
            userId: str
                The ID of the user.
        
        Return:
            Type: dict
            The response of server.

            I got 1007 error, it means that the method not found.
            But you can find this api from the Decompiled code of PicAcg.
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在组合字典。")
        data = {
            "userId": userId
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 组合完成： {data}， 正在发起请求。")
        return waziPicAcg.up(self, self.urls["blockUser"], True, data, "POST", True)

    def getNotifications(self, page):
        """
        waziPicAcg.getNotifications(self, page)
        *No.*

        Get notifications.

        Parameters:
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: dict
            The notifications.
            May like:
            {
                "code": int,                                        # The code of the response.
                "message": str,                                     # The message of the response.
                "data": {                                           # The data of the response.
                    "notifications": {                              # The notifications.
                        "docs": [],                                 # The list of the notifications. I do not know what is the structure of the notification.
                        "total": int,                               # The total number of the notifications.
                        "limit": int,                               # The limit of the notifications.
                        "page": int,                                # The page number of the notifications.
                        "pages": int                                # The total number of the pages.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["notifications"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getAnnouncements(self, page):
        """
        waziPicAcg.getAnnouncements(self, page)
        *Yes.*

        Get announcements.

        Parameters:
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: dict
            The announcements.
            May like:
            {
                "code": int,                                        # The code of the response.
                "message": str,                                     # The message of the response.
                "data": {                                           # The data of the response.
                    "announcements": {                              # The announcements.
                        "docs": [{                                  # The list of the announcements.
                            "_id": str,                             # The ID of the announcement.
                            "title": str,                           # The title of the announcement.
                            "content": str,                         # The content of the announcement.
                            "created_at": str,                      # The time of the announcement.
                            "thumb": {                              # The thumbnail of the announcement.
                                "originalName": str,                # The original name of the thumbnail.
                                "path": str,                        # The path of the thumbnail.
                                "fileServer": str                   # The file server of the thumbnail.
                            }
                        }],
                        "total": int,                               # The total number of the announcements.
                        "limit": int,                               # The limit of the announcements.
                        "page": str,                                # The page number of the announcements.
                        "pages": int                                # The total number of the pages.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["announcements"].replace("{page}", str(page))
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def getUserDirty(self, userId):
        """
        waziPicAcg.getUserDirty(self, userId)
        *Good old memories.*

        Get user dirty.

        Parameters:
            userId: str
                The user ID.
        
        Return:
            Type: dict
            The user dirty status.
            May like:
            {
                "code": int,                                        # The code of the response.
                "message": str,                                     # The message of the response.
                "data": {                                           # The data of the response.
                    "dirty": bool                                   # The dirty status of the user.
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["dirty"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "POST", True)

    def getUserProfile(self, userId):
        """
        waziPicAcg.getUserProfile(self, userId)
        *Infection.*

        Get user profile.

        Parameters:
            userId: str
                The user ID.
        
        Return:
            Type: dict
            The user profile.
            May like:
            {
                "code": int,                                        # The code of the response.
                "message": str,                                     # The message of the response.
                "data": {                                           # The data of the response.
                    "user": {                                       # The user profile.
                        "_id": str,                                 # The ID of the user.
                        "gender": str,                              # The gender of the user.
                        "name": str,                                # The name of the user.
                        "slogan": str,                              # The slogan of the user.
                        "title": str,                               # The title of the user.
                        "verified": bool,                           # Whether the user is verified.
                        "exp": int,                                 # The exp of the user.
                        "level": int,                               # The level of the user.
                        "avatar": {                                 # The avatar of the user.
                            "originalName": str,                    # The original name of the avatar.
                            "path": str,                            # The path of the avatar.
                            "fileServer": str                       # The file server of the avatar.
                        },
                        "character": str                            # The character of the user.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到用户 ID，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 用户 ID： {userId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 URL。")
        newUrl = self.urls["userProfile"].replace("{userId}", userId)
        waziLog.log("debug", f"({self.name}.{fuName}) URL 创建完毕： {newUrl}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在发起请求。")
        return waziPicAcg.up(self, newUrl, True, None, "GET", True)

    def latestUpdate(self, page):
        """
        waziPicAcg.latestUpdate(self, page)
        *Last words.*

        Get the latest update comics.
        Use waziPicAcg.advancedSearch.

        Parameters:
            page: int or str
                The page number. Start from 1.
        
        Return:
            Type: dict
            The latest update comics.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "comics": {                                         # The comics.
                        "total": int,                                   # The total of comics.
                        "page": int,                                    # The page of comics.
                        "pages": int,                                   # The pages of comics.
                        "docs": [{                                      # The comics list.
                            "updated_at": str,                          # The updated time of comic.
                            "thumb": {                                  # The thumb of comic.
                                "originalName": str,                    # The original name of thumb.
                                "path": str,                            # The path of thumb.
                                "fileServer": str                       # The file server of thumb.
                            },
                            "author": str,                              # The author of comic.
                            "description": str,                         # The description of comic.
                            "chineseTeam": str or may other object,     # The chinese team of comic.
                            "created_at": str,                          # The created time of comic.
                            "finished": bool,                           # Whether the comic is finished.
                            "categories": [str],                        # The categories of comic.
                            "title": str,                               # The title of comic.
                            "tags": [str],                              # The tags of comic.
                            "_id": str,                                 # The id of comic.
                            "likesCount": int                           # The likes count of comic.
                        }],
                        "limit": int                                    # The limit of comics.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，正在发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 已递交至 advancedSearch 处理。")
        return waziPicAcg.advancedSearch(self, [], "", "dd", page)

    def filterIt(self, backJson, filters):
        """
        waziPicAcg.filterIt(self, backJson, filters)
        *Yiiiie.*

        Filter the comics.

        Parameters:
            backJson: dict
                The comics. Accept waziPicAcg.advancedSearch(), waziPicAcg.getComics() and waziPicAcg.search() return value.
            
            filters: list[str]
                The filters. Fill in the categories you do not want.
        
        Return:
            Type: dict
            The comics.
            May like:
            {
                "code": int,                                            # The status code of request.
                "message": str,                                         # The message of request.
                "data": {                                               # The data of request.
                    "comics": {                                         # The comics.
                        "total": int,                                   # The total of comics.
                        "page": int,                                    # The page of comics.
                        "pages": int,                                   # The pages of comics.
                        "docs": [{                                      # The comics list.
                            "updated_at": str,                          # The updated time of comic.
                            "thumb": {                                  # The thumb of comic.
                                "originalName": str,                    # The original name of thumb.
                                "path": str,                            # The path of thumb.
                                "fileServer": str                       # The file server of thumb.
                            },
                            "author": str,                              # The author of comic.
                            "description": str,                         # The description of comic.
                            "chineseTeam": str or may other object,     # The chinese team of comic.
                            "created_at": str,                          # The created time of comic.
                            "finished": bool,                           # Whether the comic is finished.
                            "categories": [str],                        # The categories of comic.
                            "title": str,                               # The title of comic.
                            "tags": [str],                              # The tags of comic.
                            "_id": str,                                 # The id of comic.
                            "likesCount": int                           # The likes count of comic.
                        }],
                        "limit": int                                    # The limit of comics.
                    }
                }
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到需要过滤的内容和过滤标签，正在通过 needFilterIt 完成过滤。")
        returnJson = backJson
        returnJson["data"]["comics"]["docs"] = self.check.needFilterIt(backJson["data"]["comics"]["docs"], filters)
        waziLog.log("info", f"({self.name}.{fuName}) 过滤完成： {returnJson}")
        return returnJson

    def logout(self):
        """
        waziPicAcg.logout(self)
        *Wave.*

        Login out the account.

        Parameters:
            None
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到登出请求，正在请求登出。")
        self.token = ""
        waziLog.log("debug", f"({self.name}.{fuName}) 清空 Token 完毕，重置请求头。")
        self.editHeaders()
        waziLog.log("info", f"({self.name}.{fuName}) 登出完毕。")
