from enum import Enum
import os

"""
Used to get the home directory for different systems.
"""
class SupportedSystemsPaths(Enum):
    
    WINDOWS = os.environ.get("HOMEPATH")
    LINUX = "~"
    UNIX = "~"


