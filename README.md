[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

<h1 align="center" style="font-size: 3rem;">
Video-Downloader
</h1>

*WARNING: This project is not beign mantained anymore. Use at your own risk.*
The idea of this project is for it to be the go-to place to get videos/photos
from different social media platforms. This project was intented to help me get
some of my old Facebook videos on my personal Hard Drive but it led to the idea
of expanding the project to be able to download from all the main social media
platforms.

*Disclaimer*: Only public videos can be downloaded and all credits should be
given to the author of the downloaded video and should not be used for
commercial use.

# Installation:

Clone this repo:
```sh
git clone https://github.com/emanuel2718/Video-Downloader.git
```
Intall requirements:
```sh
pip install -r requirements.txt
```


## Currently supported platforms:
- [x] Facebook
- [x] Instagram
- [x] YouTube
- [x] TikTok (Having problems)
- [ ] Twitter

# TODO LIST:
- [x] Add at least 3/5 of the platforms from the menu.
- [x] Add option to choose from video or image (Instagram)
- [x] Check connection before requests.
- [ ] (Youtube) Add option to save audio only.
- [ ] Create testers for all the platforms.
- [ ] Make all the platforms interactions uniform throughout (i.e Ask the same things.)
- [ ] Add option to save the file under the same name of the original content.
- [ ] Default into HD; if not available use SD (Maybe ask user for format).
- [ ] Check validity of url for all platforms.
- [ ] Refactor function calling for the different platforms.
- [x] Format to: "Save as: {filename}.mp4"
- [ ] Add all the platforms from the menu.
- [x] Add system arguments functionality
- [ ] Refactor code into seperate file/classes.
