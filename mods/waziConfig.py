"""
mods/waziConfig.py

class: waziConfig
"""

import json
from mods import waziFun
from ins.waziInsLog import waziLog


class waziConfig:
    """
    waziConfig
    *Data in program, data in file.*

    Get data from file.

    Attributes:
        name: str
            The name of the class.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziConfig.__init__(self)
        *Config config = new Config();*

        Initialize the class.

        Parameters:
            None
        """
        super(waziConfig, self).__init__()
        self.name = self.__class__.__name__

    def readConfig(self, filePath):
        """
        waziConfig.readConfig(self, filePath)
        *Read his life, read his data.*

        From the json file, read the config.

        Parameters:
            filePath: str
                The json config file path.
                support relative and absolute.

        Return:
            Type: dict
            The json data, it is a dict, and should be config.

        Errors:
            Python:
                + Open file may fail.
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到配置文件路径信息和保存信息，准备读取并返回内容。")
        waziLog.log("debug", f"({self.name}.{fuName}) 文件路径： {filePath}")
        waziLog.log("debug", f"({self.name}.{fuName}) 正在打开。")
        with open(filePath, "rb") as f:
            jsonData = json.load(f)
        waziLog.log("debug", f"({self.name}.{fuName}) 数据已取得： {jsonData}")
        waziLog.log("info", f"({self.name}.{fuName}) 数据已返回。")
        return jsonData
