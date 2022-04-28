"""
sites/waziDanbooru.py

class: waziDanbooru
"""

# 需要反反爬虫的机制和其他接口路径的更便捷的支持

import os
import json
import urllib.parse
import urllib.request
from mods import waziFun
from mods.waziURL import waziURL
from ins.waziInsLog import waziLog
from mods.waziRequest import waziRequest
from mods.waziFileName import waziFileName


class waziDanbooru:
    """
    waziDanbooru
    *Tag.*

    A class for crawling sites like https://yande.re/ https://konachan.com/
    that use Danbooru as a backend.

    Attributes:
        request: waziRequest
            waziRequest instance.
        
        URL: waziURL
            waziURL instance.
        
        fileName: waziFileName
            waziFileName instance.
        
        api: str
            Danbooru API address.
        
        headers: dict
            Request headers.
        
        proxies: dict
            Proxies for requests.
            Default: {'proxyAddress': '127.0.0.1', 'proxyPort': '7890'}
        
        ports: dict
            The ports of the API.
        
        params: dict
            A dict of user params for requests. User can set the params in config.json.
        
        name: str
            The name of this class.
    
    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziDanbooru.__init__(self)
        *Summer.*

        Initialize this class.

        Parameters:
            None
        """
        super(waziDanbooru, self).__init__()
        self.request = waziRequest()
        self.URL = waziURL()
        self.fileName = waziFileName()
        self.api = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.164 Safari/537.36"
        }
        self.proxies = {
            "proxyAddress": "127.0.0.1",
            "proxyPort": "7890"
        }
        self.ports = {
            "post": "/post.json",
            "tag": "/tag.json",
            "artist": "/artist.json",
            "comment": "/comment/show.json",
            "pool": "/pool.json",
            "poolShow": "/pool/show.json",
            "poolZip": "/pool/zip/"
        }
        self.params = {}
        self.name = self.__class__.__name__

    def giveParams(self, params):
        """
        waziDanbooru.giveParams(self, params)
        *Dreamer.*

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

    def setApi(self, url):
        """
        waziDanbooru.setApi(self, url)
        *Nature.*

        Set the API address.

        Parameters:
            url: str
                The API address.

        Return:
            Type: str
            The current API address.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Danbooru 类网站 API 地址，正在写入配置。")
        self.api = url
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成，目前 API 地址为： {self.api}")
        return self.api
    
    def setPort(self, key, value):
        """
        waziDanbooru.setPort(self, key, value)
        *〇〇*

        Set the API port.

        Parameters:
            key: str
                The key of the port.
            value: str
                The value of the port.

        Return:
            Type: str
            The current API port.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Danbooru 类网站 API 端口，正在写入配置。")
        waziLog.log("debug", f"({self.name}.{fuName}) 端口键为： {key}，请求地址为： {value}")
        self.ports[key] = value
        waziLog.log("info", f"({self.name}.{fuName}) 写入完成！")
        return self.ports

    def toAPIJson(self, port, params):
        """
        waziDanbooru.toAPIJson(self, port, params)
        *Jazz.*

        Send a request to API and return the response as json.

        Parameters:
            port: str
                The API port.
            
            params: dict
                The params for the request.
        
        Return:
            Type: object
            The response as json.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Log:
                Error:
                    + Cannot get the response.
                    + Cannot transform the response to json.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求接口和 GET 参数，正在准备使用 waziRequest 发起请求。")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求接口： {port}， GET 参数： {params}")
        url = self.URL.getFullURL(urllib.parse.urljoin(self.api, port), params)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziRequest 获取完整的参数。")
        handleParams = self.params
        handleParams["useHeaders"] = True
        tempHeaders = self.headers
        tempHeaders["Host"] = self.api.split("//")[1].split("/")[0]
        tempParams = self.request.handleParams(handleParams, "get", url, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 完整的参数获取完成： {tempParams}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在尝试通过 waziRequest 请求 URL。")
        try:
            temp = self.request.do(tempParams)
        except:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取 API 信息，返回空字典。")
            return {}
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 成功请求，正在转换为字典格式返回。")
            try:
                jsons = json.loads(temp.data.decode("utf-8"))
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法转换，疑似返回错误内容，程序返回空字典： "
                                     f"{temp.data.decode('utf-8')}")
                return {}
            else:
                waziLog.log("info", f"({self.name}.{fuName}) 转换完成，API 信息为： {jsons}")
                return jsons

    def getPosts(self, page, tags, limit):
        """
        waziDanbooru.getPosts(self, page, tags, limit)
        *Cool.*

        Get posts from API.

        Parameters:
            page: int or str
                The page number. From 1 to N.
            
            tags: str
                The tags for the posts.
            
            limit: int or str
                The limit of posts. Max is 40.
        
        Return:
            Type: list[dict{key: value}]
            The posts. Based on the website.
            Example:
                [{
                    'id': 334447,
                    'tags': '...',
                    'created_at': 1636920653,
                    'creator_id': 73632,
                    'author': 'otaku_emmy',
                    'change': 2071516,
                    'source': 'https://www.pixiv.net/en/artworks/94143720',
                    'score': 32,
                    'md5': 'a2e11789abfdd59830b33f2598b5de5e',
                    'file_size': 4911373,
                    'file_url': '...',
                    'is_shown_in_index': True,
                    'preview_url': 'https://konachan.com/data/preview/a2/e1/a2e11789abfdd59830b33f2598b5de5e.jpg',
                    'preview_width': 150,
                    'preview_height': 89,
                    'actual_preview_width': 300,
                    'actual_preview_height': 179,
                    'sample_url': '...',
                    'sample_width': 1500,
                    'sample_height': 893,
                    'sample_file_size': 349306,
                    'jpeg_url': '...',
                    'jpeg_width': 3500,
                    'jpeg_height': 2084,
                    'jpeg_file_size': 615611,
                    'rating': 's',
                    'has_children': False,
                    'parent_id': None,
                    'status': 'active',
                    'width': 5879,
                    'height': 3500,
                    'is_held': False,
                    'frames_pending_string': '',
                    'frames_pending': [],
                    'frames_string': '',
                    'frames': []
                }]
            If the posts is empty, return [].
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，标签，每页限制量信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tags}， 每页限制量： {limit}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "tags": tags,
            "limit": str(limit)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["post"], params)

    def downloadFile(self, url, orgName, path):
        """
        waziDanbooru.downloadFile(self, url, orgName, path)
        *Fatal injuries.*

        Download file from url.

        Parameters:
            url: str
                A link to download.
            
            orgName: str
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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 URL，文件名和路径，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) URL： {url}， 文件名： {orgName}， 路径： {path}")
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
        waziLog.log("debug", f"({self.name}.{fuName}) 正在处理请求参数。")
        tempParams = self.params
        tempParams["useHeaders"] = True
        tempHeaders = self.headers
        tempHeaders["Host"] = self.api.split("//")[1].split("/")[0]
        requestParams = self.request.handleParams(tempParams, "get", url, tempHeaders, self.proxies)
        waziLog.log("debug", f"({self.name}.{fuName}) 处理完毕，正在修正文件名。")
        fileName = os.path.join(path, self.fileName.toRight(orgName))
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名修正完成： {fileName}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {url}")
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
        waziLog.log("info", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
        return True

    def download(self, posts, path, key, ext):
        """
        waziDanbooru.download(self, posts, path, key, ext)
        *Self-reproach.*

        Download the file from the posts with key.

        Parameters:
            posts: list
                A list of posts.
            
            path: str
                The path to save the files.
            
            key: str
                The key of the posts to download.
            
            ext: str
                The extension of the Referer.
        
        Return:
            Type: tuple
            Download Information.
            (
                list[str],                                      # The downloaded files.
                list[dict{fileURL: str, id: int}]               # The failed files.
            )
        
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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到 Posts 和路径信息，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) Posts 信息： {posts}， 路径信息： {path}， 键名： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在检查 Posts 是否为空。")
        if not posts:
            waziLog.log("error", f"({self.name}.{fuName}) 列表为空，返回空元组。")
            return [], []
        else:
            waziLog.log("debug", f"({self.name}.{fuName}) 列表不为空，继续执行。")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取路径是否存在。")
        isExists = os.path.exists(path)
        waziLog.log("debug", f"({self.name}.{fuName}) 路径是否存在： {isExists}")
        if not isExists:
            waziLog.log("debug", f"({self.name}.{fuName}) 检测到路径不存在，准备创建。")
            try:
                os.makedirs(path)
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 创建失败，返回空元组结束任务。")
                return [], []
            else:
                waziLog.log("debug", f"({self.name}.{fuName}) 成功创建，继续执行。")
        downloadFiles = []
        cantDownload = []
        waziLog.log("debug", f"({self.name}.{fuName}) 开始遍历 API 信息列表。")
        for i in posts:
            if key in i:
                pass
            else:
                waziLog.log("error", f"({self.name}.{fuName}) 无法查询到字段 {key} 的信息。")
                return [], []
            waziLog.log("debug", f"({self.name}.{fuName}) 目前正在处理的信息： {i}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziRequest 请求： {i[key]}")
            tempHeaders = self.headers
            tempParams = self.params
            if ext:
                tempHeaders["Referer"] = ext
            tempHeaders["Host"] = self.api.split("//")[1].split("/")[0]
            tempParams["useHeaders"] = True
            requestParams = self.request.handleParams(tempParams, "get", i[key], tempHeaders, self.proxies)
            waziLog.log("debug", f"({self.name}.{fuName}) 正在获取下载文件路径。")
            fileName = os.path.join(path, self.fileName.toRight(str(i["id"]) + "." + i[key].split(".")[-1]))
            waziLog.log("debug", f"({self.name}.{fuName}) 获取完成： {fileName}")
            waziLog.log("debug", f"({self.name}.{fuName}) 正在请求： {i[key]}")
            with open(fileName, "wb") as f:
                try:
                    temp = self.request.do(requestParams)
                except:
                    waziLog.log("warn", f"({self.name}.{fuName}) 图像： {i[key]} 无法下载， ID 为： {i['id']}")
                    cantDownload.append({"fileURL": i[key], "id": i["id"]})
                else:
                    waziLog.log("debug", f"({self.name}.{fuName}) 正在将数据写入。")
                    f.write(temp.data)
                    waziLog.log("debug", f"({self.name}.{fuName}) 数据写入完成。")
            waziLog.log("debug", f"({self.name}.{fuName}) 文件： {fileName}， 完成。")
            downloadFiles.append(fileName)
        waziLog.log("info", f"({self.name}.{fuName}) 完成下载，返回元组为： {(downloadFiles, cantDownload)}")
        return downloadFiles, cantDownload

    def downloadPosts(self, page, tags, limit, path, key = "file_url", ext = False):
        """
        waziDanbooru.downloadPosts(self, page, tags, limit, path, key = "file_url", ext = False)
        *Go and work.*

        Download posts from API.

        Parameters:
            page: int or str
                The page number. From 1 to N.
            
            tags: str
                The tags.
            
            limit: int or str
                The limit of posts. Max is 40.
            
            path: str
                The path to save the files.
            
            key: str
                The key of the download file URL.
                Default is "file_url".
            
            ext: bool
                Whether to use the referer.
        
        Return:
            Type: tuple
            Download Information.
            (
                list[str],                                      # The downloaded files.
                list[dict{fileURL: str, id: int}]               # The failed files.
            )
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，标签，每页限制量信息，路径信息，正在准备下载。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 标签： {tags}， 每页限制量： {limit}， "
                             f"下载路径： {path}， 键名： {key}")
        waziLog.log("debug", f"({self.name}.{fuName}) 准备递交 getPosts 获取 API 信息列表。")
        lists = waziDanbooru.getPosts(self, page, tags, limit)
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，提交给 download 函数。")
        if ext:
            params = {
                "page": str(page),
                "tags": tags,
                "limit": str(limit)
            }
            return waziDanbooru.download(
                self,
                lists,
                path,
                key,
                self.URL.getFullURL(urllib.parse.urljoin(self.api, self.ports["post"]), params)
            )
        else:
            return waziDanbooru.download(
                self,
                lists,
                path,
                key,
                ""
            )

    def getTags(self, page, limit, order):
        """
        waziDanbooru.getTags(self, page, limit, order)
        *The life of a conservative.*

        Get the tags.

        Parameters:
            page: int or str
                The page number. From 1 to infinity.
            
            limit: int or str
                The limit number. Max is 50.
            
            order: str
                The order type.
                date: order by date.
                name: order by name.
                count: order by count.
        
        Return:
            Type: list
            The tags.
            Example:
            [{'id': 45, 'name': 'long_hair', 'count': 105004, 'type': 0, 'ambiguous': False}]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码，每页限制量和排序方式信息，正在合成 URL 。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 每页限制量： {limit}， 排序方式： {order}")
        if order in ["date", "count", "name"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 排序符合规则。")
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 排序不符合规则，返回空列表。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "limit": str(limit),
            "order": order
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["tag"], params)

    def getArtists(self, page, order):
        """
        waziDanbooru.getArtists(self, page, order)
        *Rainbow.*

        Get the artists.

        Parameters:
            page: int or str
                The page number. From 1 to infinity.
            
            order: str
                The order type.
                date: order by date.
                name: order by name.
        
        Return:
            Type: list
            The tags.
            Example:
            [{
                'id': 4958,
                'name': 'shashaki',
                'alias_id': None,
                'group_id': None,
                'urls': ['https://www.pixiv.net/en/users/9089874']
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到页码和排序方式信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 页码： {page}， 排序方式： {order}")
        if order in ["date", "name"]:
            waziLog.log("debug", f"({self.name}.{fuName}) 排序符合规则。")
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 排序不符合规则，返回空列表。")
            return []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "page": str(page),
            "order": order
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["artist"], params)

    def getComment(self, commentId):
        """
        waziDanbooru.getComment(self, commentId)
        *Three months later, Ame disappeared.*

        Get the comments.

        Parameters:
            commentId: int or str
                The comment id.
            
        Return:
            Type: dict
            The comment.
            Example:
            {
                "id": 111112,
                "created_at": "2013-02-10T04:18:34.446Z",
                "post_id": 241402,
                "creator": "WtfCakes",
                "creator_id": 58373,
                "body": "2. Kinda and kinda not. Yes metaphorically, but explicitly no."
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到评论 ID 信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 评论 ID： {commentId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(commentId)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["comment"], params)

    def getPools(self, query, page):
        """
        waziDanbooru.getPools(self, query, page)
        *Brass.*

        Get the pools.

        Parameters:
            query: str
                The image pool name.
            
            page: int or str
                The page number. From 1 to infinity.
        
        Return:
            Type: list
            The pool search result.
            Example:
            [{
                'id': 509,
                'name': "Jack-O'_Challenge",
                'created_at': '2021-08-27T17:55:55.591Z',
                'updated_at': '2021-12-02T20:39:34.488Z',
                'user_id': 73632,
                'is_public': True,
                'post_count': 160,
                'description': "..."
            }]
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集名称和页码信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集名称： {query}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "query": query,
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["pool"], params)

    def getPoolFromId(self, poolId, page):
        """
        waziDanbooru.getPoolFromId(self, poolId, page)
        *And a whole string section.*

        Get the pool from id.

        Parameters:
            poolId: int or str
                The pool id.
            
            page: int or str
                The page number. From 1 to infinity.
        
        Return:
            Type: dict
            The pool information.
            Example:
            {
                'id': 489,
                'name': 'Sailor_Moon_Redraw_2020',
                'created_at': '2020-05-20T18:50:05.132Z',
                'updated_at': '2021-04-19T18:24:09.842Z',
                'user_id': 73632,
                'is_public': True,
                'post_count': 26,
                'description': '...',
                'posts': [{
                    'id': 306979,
                    'tags': '...',
                    'created_at': '2020-05-18T06:13:47.090Z',
                    'creator_id': 257706,
                    'author': 'Dreista',
                    'change': 1845780,
                    'source': 'https://www.pixiv.net/artworks/81661508',
                    'score': 49,
                    'md5': '8ce8b8db600fab17dc05bfc9c28157a5',
                    'file_size': 6173818,
                    'file_url': '...',
                    'is_shown_in_index': True,
                    'preview_url': 'https://konachan.com/data/preview/8c/e8/8ce8b8db600fab17dc05bfc9c28157a5.jpg',
                    'preview_width': 150,
                    'preview_height': 96,
                    'actual_preview_width': 300,
                    'actual_preview_height': 191,
                    'sample_url': '...',
                    'sample_width': 1500,
                    'sample_height': 956,
                    'sample_file_size': 586758,
                    'jpeg_url': '...',
                    'jpeg_width': 4050,
                    'jpeg_height': 2580,
                    'jpeg_file_size': 1177937,
                    'rating': 's',
                    'has_children': False,
                    'parent_id': None,
                    'status': 'active',
                    'width': 4050,
                    'height': 2580,
                    'is_held': False,
                    'frames_pending_string': '',
                    'frames_pending': [],
                    'frames_string': '',
                    'frames': []
                }]
            }
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID 和页码信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 页码： {page}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(poolId),
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, self.ports["poolShow"], params)

    def downloadPool(self, poolId, page, path, key = "file_url", ext = False):
        """
        waziDanbooru.downloadPool(self, poolId, page, path, key = "file_url", ext = False)
        *Of course, the gilding of the woodwinds is a must.*
        
        Download the pool's images.

        Parameters:
            poolId: int or str
                The pool id.
            
            page: int or str
                The page number. From 1 to infinity.
            
            path: str
                The path to save the images.
            
            key: str
                The key of the image's url.
                Default: "file_url"
            
            ext: bool
                Whether to use the referer.
        
        Return:
            Type: tuple
            Download Information.
            (
                list[str],                                      # The downloaded files.
                list[dict{fileURL: str, id: int}]               # The failed files.
            )
        
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
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID、页码和路径信息，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 页码： {page}， 路径： {path}， 键名： {key}， 是否反爬虫： {ext}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在创建 GET 请求参数。")
        params = {
            "id": str(poolId),
            "page": str(page)
        }
        waziLog.log("debug", f"({self.name}.{fuName}) 请求参数创建完成： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        lists = waziDanbooru.toAPIJson(self, self.ports["poolShow"], params)
        if not lists:
            waziLog.log("error", f"({self.name}.{fuName}) 无法获取该页内容，返回空元组。")
            return [], []
        else:
            try:
                lists = lists["posts"]
            except:
                waziLog.log("error", f"({self.name}.{fuName}) 无法获取该页详细信息，返回空元组。")
                return [], []
        waziLog.log("debug", f"({self.name}.{fuName}) 获取完成，提交给 download 函数。")
        return waziDanbooru.download(self, lists, path, key, ext)

    def downloadPoolWithZip(self, poolId, needJPG, path):
        """
        waziDanbooru.downloadPoolWithZip(self, poolId, needJPG, path)
        *Forget the bright major 3rd chord.*

        Download the pool's images but in a zip file.

        Parameters:
            poolId: int or str
                The pool id.
            
            needJPG: bool
                Whether to download the JPG files.
            
            path: str
                The path to save the zip file.
        
        Return:
            Type: bool
            Whether the download is successful.
        
        Errors:
            Python:
                Perhaps there are potential errors.
                (Cannot save the file may cause the program to crash.)
            
            Logs:
                Error:
                    + Cannot get the response.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到图集 ID、是否需要 JPG 格式信息和路径，正在合成 URL。")
        waziLog.log("debug", f"({self.name}.{fuName}) 图集 ID： {poolId}， 是否需要 JPG 格式： {needJPG}， 路径： {path}")
        if needJPG:
            url = urllib.parse.urljoin(self.api, f"{self.ports['poolShow']}{poolId}?jpeg=1")
        else:
            url = urllib.parse.urljoin(self.api, f"{self.ports['poolShow']}{poolId}")
        waziLog.log("debug", f"({self.name}.{fuName}) 合成完成： {url}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 downloadFile 下载。")
        if waziDanbooru.downloadFile(self, url, f"{poolId}.zip", path):
            waziLog.log("info", f"({self.name}.{fuName}) 下载成功！")
            return True
        else:
            waziLog.log("error", f"({self.name}.{fuName}) 无法下载，请检查该站点是否允许图集直接使用 ZIP 下载。")
            return False

    def customApi(self, port, params):
        """
        waziDanbooru.customApi(self, port, params)
        *Shi4 Cai2 Ao4 Wu4*

        Custom API request.

        Parameters:
            port: str
                The port of the API.
            
            params: dict
                The parameters of the API.
        
        Return:
            Type: object
            The response as json.
        
        Errors:
            Python:
                Perhaps there are potential errors.
            
            Log:
                Error:
                    + Cannot get the response.
                    + Cannot transform the response to json.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到请求接口和请求参数。")
        waziLog.log("debug", f"({self.name}.{fuName}) 请求接口： {port}， 请求参数： {params}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在通过 waziDanbooru.toAPIJson 发起请求。")
        return waziDanbooru.toAPIJson(self, port, params)
