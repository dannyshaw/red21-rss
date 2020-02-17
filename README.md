# Red 21 Sales RSS Feed Generator

Red 21 has a shitty datasource output that just gives html
It's a public url

Deploy this to heroku and set the environment variable:

`RED21_DATA_SOURCE=https://micf.api.red61.com.au/micf/reports/data?token=<yourtoken>`

Your Heroku url will now spit out your datasource table as an RSS feed which can then be used with services like https://ifttt.com to trigger notifications or other connections.

Deploy and Enjoy! :star: :sparkling_heart: 
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
