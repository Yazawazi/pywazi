"""
mods/waziDebug.py

class: waziDebug
"""

import sys
import traceback
import webbrowser


class waziDebug:
    """
    waziDebug
    *Debug with internet. Lazy, lazy.*

    Use stackoverflow to debug.

    Attributes:
        (private) _function: function
            The function to debug.

    Methods:
        - Please use help()
    """
    def __init__(self, function):
        """
        waziDebug.__init__(self, function)
        *May useful.*

        Initialize the class.

        Parameters:
            function: function
                The function to debug.
        """
        self._function = function
    
    def __call__(self, *args, **kwargs):
        """
        waziError.__call__(self, *args, **kwargs)
        *Iris.*

        Debug the function.

        Parameters:
            *args: list
                The args of the function.
            
            **kwargs: dict
                The kwargs of the function.

        Return:
            Function return
            If error, will open the stackoverflow and exit the program.

        Errors:
            None
        """
        try:
            info = self._function(*args, **kwargs)
        except Exception:
            error = traceback.format_exc()
            url = "https://stackoverflow.com/search?q=%5Bpython%5D+" + error.split("\n")[-2]
            webbrowser.open(url)
            traceback.print_exc()
            sys.exit(1)
        else:
            return info
