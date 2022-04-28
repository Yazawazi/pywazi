"""
mods/waziLog.py

class: waziLog
"""

import os
import time
from mods.waziColor import waziColor


class waziLog:
    """
    waziLog
    *Log and print.*

    A class for log printing and exporting without logging module.

    Attributes:
        color: waziColor
            For color printing.
        
        min: int
            The minimum level of log display.
            Default: -1
        
        save: bool
            Whether to save the log.
            Default: False
        
        saveName: str
            The name of the log file.
            Default: ""
        
        cache: list
            The cache of the log messages.

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziLog.__init__(self)
        *Clean.*

        Initialize the class.

        Parameters:
            None
        
        Actions:
            + Create logs folder: waziLog.createLogsFolder(self)
            + Set save name: waziLog.setSaveName(self)
        """
        super(waziLog, self).__init__()
        self.color = waziColor()
        self.min = -1
        self.save = False
        self.saveName = ""
        self.cache = []
        self.createLogsFolder()
        self.setSaveName()

    @staticmethod
    def createLogsFolder():
        """
        waziLog.createLogsFolder(self)
        *Give them a home.*

        Create the log's folder if it doesn't exist.
        Called in __init__.

        Return:
            None

        Errors:
            Python:
                Perhaps there are potential errors.
        """
        os.makedirs("logs", exist_ok = True)

    def setSaveName(self):
        """
        waziLog.setSaveName(self)
        *T I M E*

        Set the save name of the log file.
        Called in __init__.

        Return:
            None
        
        Errors:
            None
        """
        self.saveName = "LOG_" + time.strftime("%Y-%m-%d %H.%M.%S", time.localtime(time.time())) + ".log"

    def needSave(self, boolean):
        """
        waziLog.needSave(self, boolean)
        *Save or not.*

        Set whether to save the log.

        Parameters:
            boolean: bool
                Whether to save the log.
        
        Return:
            Type: bool
            Whether to save the log.
        
        Errors:
            None
        """
        self.save = boolean
        return self.save

    def setMinDisplayLevel(self, levelNumber):
        """
        waziLog.setMinDisplayLevel(self, levelNumber)
        *You can't see me.*

        Set the minimum level of log display.

        Parameters:
            levelNumber: int
                The minimum level of log display.
                -1: None
                0: Error
                1: Warn
                2: Info
                3: Debug
        
        Return:
            Type: int
            The minimum level of log display.
        
        Errors:
            None
        """
        self.min = levelNumber
        return self.min
    
    def forceSave(self):
        """
        waziLog.forceSave(self)
        *Glowing.*

        Force save the log.

        Return:
            None
        
        Errors:
            None
        """
        if self.save:
            with open("./logs/" + self.saveName, "a", encoding = "utf-8") as f:
                texts = ""
                for text in self.cache:
                    texts += text + "\n"
                f.write(texts)
            self.cache = []

    def outputLog(self, text):
        """
        waziLog.outputLog(self, text)
        *Got?*

        Output one log message to the log file.

        Parameters:
            text: str
                The log message.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        if self.save:
            self.cache.append(text)
            if len(self.cache) > 100:
                with open("./logs/" + self.saveName, "a", encoding = "utf-8") as f:
                    texts = ""
                    for text in self.cache:
                        texts += text + "\n"
                    f.write(texts)
                self.cache = []

    def log(self, level, text):
        """
        waziLog.log(self, level, text)
        *I work for me, not for you.*

        Print and call the outputLog method.

        Parameters:
            level: str
                The level of the log.
                debug, info, warn, error
            
            text: str
                The log message.
        
        Return:
            None
        
        Errors:
            Python:
                Perhaps there are potential errors.
        """
        if level == "debug":
            printText = "[DEBUG \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 3:
                color = self.color.HexToRGB(0xff, 0xe9, 0x00)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "info":
            printText = "[INFO \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 2:
                color = self.color.HexToRGB(0x00, 0xaa, 0xda)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "warn":
            printText = "[WARN \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 1:
                color = self.color.HexToRGB(0xff, 0xaa, 0x4d)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
        if level == "error":
            printText = "[ERROR \t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "] " + text
            if self.min >= 0:
                color = self.color.HexToRGB(0xff, 0x72, 0x76)
                self.color.print({
                    "color": color,
                    "text": printText
                })
            waziLog.outputLog(self, printText)
