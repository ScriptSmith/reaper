#!/bin/bash
git pull
cd ../socialreaper/
git pull
cd ../reaper/
pip3 install -e ../socialreaper/
rm -r dist/
pyinstaller reaper.spec
cd dist/
codesign -s "Developer ID Application: Adam Smith" --deep reaper.app
pkgbuild --install-location /Applications --component reaper.app --identifier Reaper --version $1 --sign "Developer ID Installer: Adam Smith" Reaper.pkg
zip -r reaper.zip reaper.app
cd ..
