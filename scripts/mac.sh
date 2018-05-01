#!/bin/bash
git pull
pip3 install -r requirements.txt
pip3 install git+https://github.com/ScriptSmith/socialreaper.git
rm -r dist/
pyinstaller reaper.spec
cd dist/
codesign -s "Developer ID Application: Adam Smith" --deep reaper.app
pkgbuild --install-location /Applications --component reaper.app --identifier Reaper --version $1 --sign "Developer ID Installer: Adam Smith" Reaper.pkg
zip -r reaper.zip reaper.app
cd ..
