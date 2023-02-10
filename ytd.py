from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
from tqdm import tqdm
"""
Copyright (C) 2023  MazZ

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
"""YT-Downloader(ytd.py) will download YouTube videos with a provided link. You may provide the link as an argument or the 
program will ask for the user to input a link upon running. The user then chooses whether to download the file as an 
mp3(Audio Only - For music), or mp4(Whole Video) file."""
"""
Version 1.0: Able to download mp4 to specified path.
TODO:
Add option to download Audio only(mp3). 
"""

# Path for where videos/mp3 files will be downloaded. Specify your own.
path = "C:/Users/kmazz/Desktop/YTvideos/"


def vid_download(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    fs = yt.streams.get_highest_resolution().filesize
    print(f"Link: {url}\n"
          f"Title: {yt.title}\n"
          f"Author: {yt.author}\n"
          f"Views: {yt.views}\n"
          f"Length: {yt.length // 60} Min(s)\n"
          f"FileSize: {fs / 1000000}")
    cmd = input("Press [ENTER] to Download or 'q' to quit: ")
    if cmd == 'q' or cmd == 'quit':
        quit()
    else:
        done = False
        while not done:
            yd = yt.streams.get_highest_resolution()
            yt.register_on_progress_callback(on_progress)
            progress = tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(fs), colour='green')
            for i in range(fs):
                progress.update()
            yd.download(path)
            print(f"FINISHED!\nDownloaded: {yt.title}\nSaved in: '{path}\nFilesize: {fs / 1000000}mb")
            done = True


def main():
    while True:
        if len(argv) > 5:
            vid_download(argv[1])
        else:
            url = input(f"Please Enter a YouTube Link: ")
            vid_download(url)
        return False


if __name__ == '__main__':
    main()
