import os
import platform
import shutil
import traceback
import time

from configuration_store import Config
from supported_systems import SupportedSystemsPaths

def go2sortingdir(config: Config) -> str:
    """
    Detects the type of system (Windows or Linux) and changes directory to the downloads directory accordingly.
    """
    #print(os_name)
    path = generate_full_destination_path("%s%s%s" % (get_home_directory(config.system_name), config.file_path_seperator, config.sorting_directory), config)
    #print(supported_system_enums)
    #print(len(dir(SupportedSystemsPaths)))


    #print(path)
    #print(os.getcwd())
    os.chdir(path)
    #print(os.getcwd())
    return path

def get_file_list() -> list:
    return [file for file in os.listdir() if os.path.isfile(file)]


def move_files(config: Config):
    """
    Moves all files in the sorting directory to the destination directory.
    """
    file_list = get_file_list()
    for file_name in file_list:
        file_extension = file_name.split('.')[-1]
        if file_extension in config.file_destination_paths.keys():
            destination = "%s%s%s" % (config.file_destination_paths[file_extension], config.file_path_seperator, file_name)
            print(destination)
            shutil.move(file_name, generate_full_destination_path(destination, config))



def generate_full_destination_path(path_string, config: Config):
    """
    Takes the path_string and checks if it's a full path then it just returns it and if it it's not then
    returns the relative path from home directory to path_string.
    """
    if path_string[0] in ("\\", "/", "~"):
        return path_string
    else:
        return "%s%s%s" % (get_home_directory(config.system_name), config.file_path_seperator, path_string)



def get_home_directory(os_name: str) -> str:
    """
    Quite self-explanatory, it gets the home directory.
    """
    path = ""
    supported_system_enums = dir(SupportedSystemsPaths)[:len(dir(SupportedSystemsPaths))-11]
    if os_name.upper() in supported_system_enums:
            try:
                path = SupportedSystemsPaths[os_name.upper()]
            except KeyError:
                traceback.print_exc()
    return path.value


def run():
    # Gets the system name like Windows, Linux, etc.
    os_name = platform.system()
    # Loads the configuration of the destination directory for the file types.
    config = Config(os_name)
    while True:
        # Changes directory to the Dowload directory.
        path = go2sortingdir(config)
        # print(get_file_list())
        # print(config.file_destination_paths)
        move_files(config)
        time.sleep(5)

if __name__ == '__main__':
    run() # Runs :3