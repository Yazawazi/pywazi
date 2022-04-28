"""
mods/waziFun.py
"""

import inspect


def getFuncName():
    """
    waziFun.getFuncName()
    *Get his name.*

    Get a function name.

    Return:
        Type: str
        The function name.

    Errors:
        Python:
            + Sometimes may cause IndexError.
    """
    return inspect.stack()[1][3]
