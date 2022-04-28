import copy
import requests
import threading
from mods import waziFun
from ins.waziInsLog import waziLog


class waziDownload:
    """
    waziDownload
    *Type Annotations, But lazy.*

    Download a file in multi-threads.

    Attributes:
        proxies: dict
            The proxies to use. Default: {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
        
        headers: dict
            The headers to use. Default:
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
            }
        
        url: str
            The url to download.
        
        threadsNumber: int
            The number of threads to use. Default: 8
        
        filePath: str
            The file path to save.
        
        total: int
            The total size of the file.
        
        file: file
            The file to save.
        
        name: str
            The name of the class.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziDownload.__init__(self)
        *.*

        Initialize the class.

        Parameters:
            None
        """
        self.proxies = {
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.132 Safari/537.36"
        }
        self.url = ""
        self.threadsNumber = 8
        self.filePath = ""
        self.total = 0
        self.file = None
        self.name = self.__class__.__name__
    
    def getRange(self):
        """
        waziDownload.getRange(self)
        *SlEepINg, bUt NEed woRk NoW.*

        Get the range of the file to download.

        Return:
            ranges: list[tuple]
                The ranges of the file to download.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在计算总分段。")
        ranges = []
        offset = self.total // self.threadsNumber
        waziLog.log("debug", f"({self.name}.{fuName}) 计算完毕，正在进行一个遍历的过程。")
        for i in range(self.threadsNumber):
            if i == self.threadsNumber - 1:
                ranges.append((i * offset, self.total))
            else:
                ranges.append((i * offset, (i + 1) * offset))
        waziLog.log("info", f"({self.name}.{fuName}) 数据已计算完成： {ranges}")
        return ranges
    
    def getFileSize(self):
        """
        waziDownload.getFileSize(self)
        *pLaY SOmE BeAUUTifUL!*

        Get the size of the file to download.

        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在获取文件大小。")
        head = requests.head(
            self.url,
            headers = self.headers,
            proxies = self.proxies
        )
        if head.status_code == 302:
            head = requests.head(
                head.headers["Location"],
                headers = self.headers,
                proxies = self.proxies
            )
        self.total = int(head.headers["Content-Length"])
        waziLog.log("info", f"({self.name}.{fuName}) 文件大小获取完毕： {self.total}")
    
    def download(self, start, end):
        """
        waziDownload.download(self, start, end)
        *Anemone nikoensis.*

        Download the file but in one thread.

        Parameters:
            start: int
                The start of the range.
            
            end: int
                The end of the range.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进行一个自定义请求头的，啊，深拷贝。")
        headers = copy.deepcopy(self.headers)
        waziLog.log("debug", f"({self.name}.{fuName}) 正在写入 Range 范围数据。")
        headers["Range"] = f"bytes={start}-{end}"
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进行一个请求。")
        r = requests.get(
            self.url,
            headers = headers,
            proxies = self.proxies
        )
        waziLog.log("debug", f"({self.name}.{fuName}) 正在写入文件。")
        self.file.seek(start)
        self.file.write(r.content)
        waziLog.log("info", f"({self.name}.{fuName}) 写入完毕。")
    
    def changeThreadsNumber(self, threadsNumber):
        """
        waziDownload.changeThreadsNumber(self, threadsNumber)
        *Should I need use coroutine? Try aiohttp?*

        Change the number of threads to use.

        Parameters:
            threadsNumber: int or str
                The number of threads to use.
        
        Return:
            Type: int
            The current number of threads to use.
        
        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已取得参数： {threadsNumber}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在更改线程数量。")
        self.threadsNumber = int(threadsNumber)
        waziLog.log("info", f"({self.name}.{fuName}) 线程数量已更改： {self.threadsNumber}")
        return self.threadsNumber
    
    def run(self, url, filePath, proxies, headers):
        """
        waziDownload.run(self, url, filePath, proxies, headers)
        *dO Not tOuCH, StOP!*

        Run the download process.

        Parameters:
            url: str
                The url to download.
            
            filePath: str
                The file path to save.
            
            proxies: dict
                The proxies to use.
            
            headers: dict
                The headers to use.
        
        Return:
            Type: bool
            Whether the download process is successful.
            But if failed, it will raise an error, no "False" will be returned.
        
        Errors:
            Python:
                If the download process is failed, it will raise an error.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 已收到参数，URL： {url}，文件路径： {filePath}，代理： {proxies}，请求头： {headers}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进行一个初始化的过程。")
        self.url = url
        self.filePath = filePath
        self.proxies = proxies
        self.headers = headers
        self.getFileSize()
        waziLog.log("debug", f"({self.name}.{fuName}) 初始化完成，正在进行一个文件的打开。")
        self.file = open(self.filePath, "wb")
        ranges = self.getRange()
        threadsList = []
        waziLog.log("debug", f"({self.name}.{fuName}) 正在进行一个线程的创建。")
        for i in range(self.threadsNumber):
            t = threading.Thread(target = self.download, args = (ranges[i][0], ranges[i][1]))
            t.start()
            threadsList.append(t)
        waziLog.log("debug", f"({self.name}.{fuName}) 线程创建完毕，正在进行一个线程的等待。")
        for t in threadsList:
            t.join()
        waziLog.log("debug", f"({self.name}.{fuName}) 线程等待完毕，正在进行一个文件的关闭。")
        self.file.close()
        waziLog.log("info", f"({self.name}.{fuName}) 下载完成： {filePath}。")
        return True
