import json

"""
Initializes varibles that would be different for different systems and the destination paths for the different file types.
"""
class Config:

    def __init__(self, system_name):
        with open("config.json") as f:
            data = json.load(f)
            self.sorting_directory = data.get("SortingDirectory")
            if system_name.upper() == "WINDOWS":
                self.file_path_seperator = "\\"
                self.file_destination_paths = data.get("FileDestinationPathWindows")
            elif system_name.upper() == "LINUX":
                self.file_path_seperator = "/"
                self.file_destination_paths = data.get("FileDestinationPathLinux")
            else:
                pass
                #TODO: Custom exception for non-supported system.
