"""
mods/waziColor.py

class: waziColor
"""


class waziColor:
    """
    waziColor
    *Life is uncolored. I color it.*

    A true color print class for the console.
    Not support Windows CMD and Powershell.
    Tested on Windows Terminal.

    Attributes:
        None

    Methods:
        - Please use help()
    """
    def __init__(self):
        """
        waziColor.__init__(self)
        *Create new day, and set the color to white.*

        Initialize the class.

        Parameters:
            None
        """
        super(waziColor, self).__init__()

    @staticmethod
    def HexToRGB(R, G, B):
        """
        waziColor.HexToRGB(R, G, B)
        *One life to another life.*

        Static method to convert hexadecimal to RGB.

        Parameters:
            R: int
                Red value, 0x00 - 0xff.

            G: int
                Green value, 0x00 - 0xff.

            B: int
                Blue value, 0x00 - 0xff.

        Return:
            Type: dict
                {"R": str, "G": str, "B": str}

        Errors:
            None
        """
        tr = R / 0xff * 255
        tg = G / 0xff * 255
        tb = B / 0xff * 255
        return {"R": str(int(tr)), "G": str(int(tg)), "B": str(int(tb))}

    @staticmethod
    def print(jsons):
        """
        waziColor.print(jsons)
        *Try to print a colorful life.*

        Static method to print with ANSI escape codes to the console.
        Support color, background color, and text style.

        Parameters:
            jsons: dict
            Like this:
            {
                "color": {
                    "R": 255,
                    "G": 233,
                    "B": 0
                },                      # Dict, text color
                "bgColor": {
                    "R": 255,
                    "G": 233,
                    "B": 0
                },                      # Dict, background color
                "effects": {
                    "normal": True,     # Normal text style, just like as you see
                    "highLight": True,  # Highlight text style, light
                    "lowLight": True,   # Lowlight text style, dark
                    "itail": True,      # Italic text style, like a book or a poem
                    "underLine": True,  # Underline text style, make me nervous
                    "slowShine": True,  # Slow shine text style, like a broken light in night
                    "revWhite": True,   # Reverse white text style, never use it
                    "hide": True,       # Hide the text, er, I mean, invisible
                    "delLine": True     # Deleteline text style, deliberately mystifying
                },
                "text": "Text"          # String, text to print
            }

        Return:
            None

        Errors:
            None
        """
        text = ""
        if "color" in jsons:
            text += "\x1b[38;2;" + jsons["color"]["R"] + ";"
            text += jsons["color"]["G"] + ";"
            text += jsons["color"]["B"] + "m"
        if "bgColor" in jsons:
            text += "\x1b[48;2;" + jsons["bgColor"]["R"] + ";"
            text += jsons["bgColor"]["G"] + ";"
            text += jsons["bgColor"]["B"] + "m"
        if "effects" in jsons:
            if "normal" in jsons["effects"]:
                text += "\x1b[0m"
            if "highLight" in jsons["effects"]:
                text += "\x1b[1m"
            if "lowLight" in jsons["effects"]:
                text += "\x1b[2m"
            if "itail" in jsons["effects"]:
                text += "\x1b[3m"
            if "underLine" in jsons["effects"]:
                text += "\x1b[4m"
            if "slowShine" in jsons["effects"]:
                text += "\x1b[5m"
            if "revWhite" in jsons["effects"]:
                text += "\x1b[7m"
            if "hide" in jsons["effects"]:
                text += "\x1b[8m"
            if "delLine" in jsons["effects"]:
                text += "\x1b[9m"
        text += jsons["text"] + "\x1b[0m"
        print(text)
