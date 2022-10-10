# Download scripts for the satellite images

To download all images, simply modify the `download_all.ps1` (for Windows Powershell) or `download_all.sh` (for Unix-based systems) script to change the file path where the images are stored, then execute that script. It may take some time to download all the files, and will require approximately ~5.5 GB of disk space once downloaded.

If you are encountering "Download Failed" errors on OSX, you may need to do a post-install step on your Python installation to get SSL certificates set up. This can be done by running the "Install Certificates.command" script in your Python installation directory - see [https://stackoverflow.com/a/42334357](https://stackoverflow.com/a/42334357) for more details.

These scripts are derived from [work by Stevens et al.](https://github.com/raspstephan/sugar-flower-fish-or-gravel)
