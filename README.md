# Description

## Automatic file sorter

It moves files depending on their file extension to their respective destination directory. **The destination directory for each fileextension can be configured** in the config.json file. Also **the directory to move files from** can be configured in the config.json file. To run it automatically whenever there are changes in a directory one can use **inotify** for linux or a VBscript with **SystemFileWatcher**. To run periodically then use **crontab** on linux or the **TaskScheduler** on windows.
