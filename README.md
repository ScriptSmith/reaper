<p align="center">
<img src="ui/icon.png">
</p>

<h1 align="center">Reaper</h1>


[![Website](https://img.shields.io/website-up-down-green-red/https/shields.io.svg?label=reaper.social)](https://reaper.social)
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

## Quick Start

Reaper is easiest to run with Python 3.10-3.12.

### Windows (PowerShell)
```powershell
git clone https://github.com/ScriptSmith/reaper.git
cd reaper
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python reaper.py
```

### macOS / Linux
```bash
git clone https://github.com/ScriptSmith/reaper.git
cd reaper
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python reaper.py
```

## API Key Setup

Reaper depends on external platform APIs. Before collecting data:

1. Create API credentials for each provider you need (for example Reddit, YouTube, Tumblr, Pinterest, Twitter/X, Facebook).
2. Open Reaper and go to the API keys page.
3. Enter credentials for the enabled sources.
4. Save keys and run a small test job first.

## API Status Reality Check

This project integrates external APIs that change over time. A source being listed in the UI does not guarantee the upstream endpoint is still available.

Recommended validation workflow:

1. Test each source with a minimal request before running large jobs.
2. Watch the Error Manager output for auth/endpoint hints.
3. Disable or hide sources that are no longer supported in your fork until updated.

## Troubleshooting

### RecursionError on startup (`maximum recursion depth exceeded`)

If you saw this in older builds, upgrade to a version that includes Issue #13 fix.  
The bug was in `components/globals.py` path resolution and was triggered by some Windows folder layouts.

### `ModuleNotFoundError` or import failures

1. Confirm your virtual environment is activated.
2. Reinstall dependencies:
   `pip install --upgrade pip && pip install -r requirements.txt`
3. Verify Python version:
   `python --version`

### PyQt5 install problems

1. Use a supported Python version (3.10-3.12 recommended).
2. Upgrade pip before installing.
3. On Linux, ensure Qt runtime/system packages are installed by your distro package manager.

### Invalid API keys / source errors

1. Re-check token permissions and expiry at the provider side.
2. Test one source at a time to isolate failures.
3. Check Reaper logs in your app data/log directory if startup succeeds but jobs fail.
