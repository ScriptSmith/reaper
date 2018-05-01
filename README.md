<p align="center">
<img src="ui/icon.png">
</p>

<h1 align="center">Reaper</h1>


[![Website](https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=Website)](https://reaper.social)
![Github All Releases](https://img.shields.io/github/downloads/scriptsmith/reaper/total.svg)
[![GitHub license](https://img.shields.io/github/license/scriptsmith/reaper.svg)](https://github.com/ScriptSmith/reaper/blob/master/LICENSE.txt)
[![Gitter](https://img.shields.io/gitter/room/socialreaper/socialreaper.svg)](https://gitter.im/socialreaper)

Reaper is a PyQt5 GUI that scrapes Facebook, Twitter, Reddit, Youtube, Pinterest, and Tumblr APIs 
using [socialreaper](https://github.com/ScriptSmith/socialreaper)

<p align="center">
<img width="100%" src="img/preview.gif">
</p>

Are you a developer? [Try the Python package](https://github.com/ScriptSmith/socialreaper)


## Features
- Support for 6 social media platforms
- CSV output
- Instructions for getting API keys
- API key management
- Download queuing system
- Error management
- Disk caching for big data
- Ability to read a list of inputs from CSV and text files
- Ability to append to exsting data
- **Dark** theme
- UTF-8 and ASCII support

## Download
To download the latest builds for your platform, check out the [releases](https://github.com/ScriptSmith/reaper/releases)

Installers and standalone versions are available for Windows and macOS

## Usage

Instructions for using Reaper are available on [reaper.social](https://reaper.social)

## Run source
Reaper uses string formatting that was added in Python 3.6. You need to run Reaper with Python 3.6+ or download a pre-built version from the [releases](https://github.com/ScriptSmith/reaper/releases)

Download
```
git clone https://github.com/ScriptSmith/reaper.git
cd reaper
```
Run
```
pip3 install -r requirements.txt
python3 reaper.py
```
