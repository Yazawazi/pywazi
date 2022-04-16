"""
Program for crawling web resources.
See Readme.md & doc.md for more details.

爬取网络资源的程序。
详情请看 Readme.md & doc.md。
"""
import atexit
from ins.waziInsLog import waziLog
from ins.waziInsConfig import waziConfig
from sites.waziNyaa import waziNyaa as Wn
from sites.wazi9xxx import wazi9xxx as W9
from sites.waziJavBus import waziJavBus as Wjb
from sites.waziPicAcg import waziPicAcg as Wpa
from sites.waziDanbooru import waziDanbooru as Wdb
from sites.waziExHentai import waziExHentai as Weh
from sites.waziAsianSister import waziAsianSister as Was

__VERSION__ = "2.0"
__AUTHOR__ = ["Acheron-x", "Yazawazi"]

waziNyaa = Wn()
wazi9xxx = W9()
waziJavBus = Wjb()
waziPicAcg = Wpa()
waziDanbooru = Wdb()
waziExHentai = Weh()
waziAsianSister = Was()

atexit.register(waziLog.forceSave)

class waziGet:
    def __init__(self):
        self.name = self.__class__.__name__
    
    @staticmethod
    def get(site):
        """
        waziGet.get(site)
        *walk in circles.*

        Get the class by site name.

        Parameters:
            site: str
                The site name.
        
        Return:
            Type: class
            The class by site name.
        
        Errors:
            None
        """
        if site == "nyaa":
            return waziNyaa
        elif site == "javbus":
            return waziJavBus
        elif site == "picacg":
            return waziPicAcg
        elif site == "danbooru":
            return waziDanbooru
        elif site == "exhentai":
            return waziExHentai
        elif site == "asiansister":
            return waziAsianSister
        elif site == "9xxx":
            return wazi9xxx
        else:
            return None

class waziMain:
    def __init__(self):
        self.name = self.__class__.__name__
    
    @staticmethod
    def globalParams(params):
        """
        waziMain.globalParams(params)
        *OCD*

        Set global parameters.

        Parameters:
            params: dict
                The parameters.
                {
                    "useProxies": bool,                 # Whether to use proxies.
                    "proxyAddress": str,                # The address of the proxy.
                    "proxyPort": int or str,            # The port of the proxy.
                    "advancedProxies": dict or None,    # The advanced parameters of the proxy.
                    "useHeaders": bool,                 # (*) Whether to use headers.
                    "headers": dict,                    # (*) The custom headers.
                }
                *: The parameters are not recommended. The program will auto set them. If you set them, may cause some problems.

        Return:
            Type: dict
            The parameters.

        Errors:
            None
        """
        waziNyaa.giveParams(params)
        wazi9xxx.giveParams(params)
        waziJavBus.giveParams(params)
        waziPicAcg.giveParams(params)
        waziDanbooru.giveParams(params)
        waziExHentai.giveParams(params)
        waziAsianSister.giveParams(params)
        return params

    @staticmethod
    def globalParamsByFile(filePath):
        """
        waziMain.globalParamsByFile(filePath)
        *OCD*

        Set global parameters.

        Parameters:
            filePath: str
                The path of the config file.
                Config file format:
                {
                    "useProxies": bool,                 # Whether to use proxies.
                    "proxyAddress": str,                # The address of the proxy.
                    "proxyPort": int or str,            # The port of the proxy.
                    "useHeaders": bool,                 # (*) Whether to use headers.
                    "headers": dict,                    # (*) The custom headers.
                }
                *: The parameters are not recommended. The program will auto set them. If you set them, may cause some problems.
        
        Return:
            Type: dict
            The parameters.

        Errors:
            None
        """
        jsonData = waziConfig.readConfig(filePath)
        waziMain.globalParams(jsonData)
        return jsonData

    @staticmethod
    def defConfig(filePath):
        """
        waziMain.defConfig(filePath)
        *Transvestism.*

        Use config file to define all modules.

        Parameters:
            filePath: str
                The path of the config file.

        Return:
            Type: bool
            The result.

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        jsonData = waziConfig.readConfig(filePath)
        for i in jsonData:
            if i["name"] == "JavBus":
                if "params" in i:
                    waziJavBus.giveParams(i["params"])
                if "url" in i:
                    waziJavBus.setApiUrl(i["url"])
                if "eaUrl" in i:
                    waziJavBus.setEAApiUrl(i["eaUrl"])
                if "type" in i:
                    waziJavBus.changeType(i["type"])
            elif i["name"] == "PicAcg":
                if "params" in i:
                    waziPicAcg.giveParams(i["params"])
                if "login" in i:
                    waziPicAcg.login(i["login"]["username"], i["login"]["password"])
                if "image" in i:
                    waziPicAcg.changeImageQuality(i["image"])
            elif i["name"] == "Danbooru":
                if "params" in i:
                    waziDanbooru.giveParams(i["params"])
                if "url" in i:
                    waziDanbooru.setApi(i["url"])
                if "ports" in i:
                    for j in i["ports"]:
                        waziDanbooru.setPort(j["key"], j["value"])
            elif i["name"] == "ExHentai":
                if "params" in i:
                    waziExHentai.giveParams(i["params"])
                if "cookies" in i:
                    waziExHentai.setCookies(i["cookies"])
                if "parse" in i:
                    waziExHentai.setParse(i["parse"])
                if "fullComment" in i:
                    waziExHentai.needFullComments(i["fullComment"])
                if "thumbType" in i:
                    waziExHentai.changeThumbnailMode(i["thumbType"])
                if "method" in i:
                    waziExHentai.changeMethod(i["method"])
                if "jump" in i:
                    waziExHentai.setJump(i["jump"])
            elif i["name"] == "AsianSister":
                if "params" in i:
                    waziAsianSister.giveParams(i["params"])
            elif i["name"] == "Nyaa":
                if "params" in i:
                    waziNyaa.giveParams(i["params"])
            elif i["name"] == "9xxx":
                if "params" in i:
                    wazi9xxx.giveParams(i["params"])
            elif i["name"] == "Log":
                if "save" in i:
                    waziLog.needSave(i["save"])
                if "level" in i:
                    waziLog.setMinDisplayLevel(i["level"])
            else:
                pass
        return True

"""
Try to import the global config file & config file: 
    ./global.json & ./config.json
"""
try:
    waziMain.globalParamsByFile("./global.json")
    waziMain.defConfig("./config.json")  
except:
    pass

# Remove the statement because I am afraid.

# [1]: 代码使用： https://github.com/WWILLV/iav （未注明详细的版权协议）
# [2]: Api 参考： https://github.com/AnkiKong/picacomic （MIT 版权）
#      Headers 引用： https://github.com/tonquer/picacg-windows （LGPL-3.0 版权）
#      相关信息参考： https://www.hiczp.com/wang-luo/mo-ni-bi-ka-android-ke-hu-duan.html （版权归 czp，未注明详细的版权协议）
#      在 PicAcg 部分，我参考了一位开源者的代码，但是很可惜，我已经在 GitHub 找不到他的项目了（可能是代码进行改动了）
# 感谢我的朋友： cloudwindy 提供了 ExHentai 账号信息
