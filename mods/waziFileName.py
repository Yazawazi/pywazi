"""
mods/waziFileName.py

class: waziFileName
"""

from mods import waziFun
from ins.waziInsLog import waziLog


class waziFileName:
    """
    waziFileName
    *Your child's name must be legal.*

    Handles file names, etc.

    Attributes:
        name: str
            The name of the class.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziFileName.__init__(self)
        *Let the name be known.*

        Initialize the class.

        Parameters:
            None
        """
        super(waziFileName, self).__init__()
        self.name = self.__class__.__name__

    def toRight(self, name):
        """
        waziFileName.toRight(self, name)
        *Make the name right, er, I mean correct, er, not a political implication.*

        Make the file name conform to Windows naming format requirements.

        Parameters:
            name: str
                The file name.

        Return:
            Type: str
            The file name, conform to Windows naming format.

        Errors:
            None
        """
        fuName = waziFun.getFuncName()
        waziLog.log("debug", f"({self.name}.{fuName}) 收到文件名，正在删除不合法字符串：\\ / : ? \" < > | *")
        waziLog.log("debug", f"({self.name}.{fuName}) 文件名为： {name}")
        finalName = name.replace("\\", "").replace("/", "").replace(":", "").replace("?", "").replace("\"", "")\
                        .replace("<", "").replace(">", "").replace("|", "").replace("*", "").strip()
        waziLog.log("info", f"({self.name}.{fuName}) 修正后文件名： {finalName}")
        return finalName
