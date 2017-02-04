.. Reaper documentation master file, created by
   sphinx-quickstart on Tue Jan 31 16:46:20 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Reaper
======

Reaper is a PyQt5 GUI that scrapes Facebook, Twitter, Reddit and Youtube apis
using the Python package ``socialreaper`` .

To use Reaper, install ``socialreaper`` and ``PyQt5``, then run ``reaper.py``

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Adding API Keys
===============
Facebook
--------
Navigate to https://developers.facebook.com/tools/explorer

From the `My Apps` menu select `Add a New App`.

Fill in the details and choose the category `Apps for Pages`.

Navigate to https://developers.facebook.com/tools/explorer and change the
application to the name of your new app.

Click `Get User Access Token` under the `Get Token` menu.

Click `Get Access Token`.

Test the new token by making an example query in the `GET` field like
``wikipedia/posts``.

Extend the access token expiry time by clicking the blue `i` icon next to the
`Access Token` field.

Click `Open in Access Token Tool`.

Click `Extend Access Token`.

Copy the new access token into the `Api Key` field in Reaper's authentication.

Twitter
-------
Navigate to https://apps.twitter.com/

Click `Create New App`.

Fill in the details and create the new app.

Click the `Keys and Access Tokens` tab.

Click `Create my Access Token`.

Copy `Consumer Key (API Key)`, `Consumer Secret (API Secret)`, `Access Token`,
`Access Token Secret` into their respective fields in Reaper's authentication.

Reddit
------
Navigate to https://www.reddit.com/prefs/apps/

Click `create another app`.

Fill in the details and select `script` as the application type.

Copy the app id (the string underneath the application's name), and
secret into their respective fields in Reaper's authentication.

Youtube
-------
Navigate to http://console.developers.google.com/

Create a new project.

Click `Youtube Data Api`.

Next to the `Youtube Data Api V3`, click `Enable`.

Click the `Create credentials` button.

Select `Other UI` as the location you will be calling from.

Select `Public Data`.

Click `What credentials do I need`.

Copy the api key into Reaper's authentication.

