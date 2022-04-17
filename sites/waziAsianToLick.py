import os
import re
import json
from mods import waziFun
from bs4 import BeautifulSoup
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
    
    def getSiteMapPosts(self):
        # https://asiantolick.com/sitemap/post.xml
        pass
    
    def getSiteMapCategories(self):
        # https://asiantolick.com/sitemap/category.xml
        pass
    
    def getSiteMapTags(self):
        # https://asiantolick.com/sitemap/tags.xml
        pass
    
    def get(self, post, cat, tag, search, page, index, ver):
        # https://asiantolick.com/ajax/buscar_posts.php?post=&cat=&tag=&search=&page=&index=0&ver=31
        pass
    
    def getPost(self, postId, name):
        pass

    def downloadPost(self, postId, name, path):
        pass
