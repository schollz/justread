# Just Read

**Copy and paste URL to get just the text content of that site.**


This is a really simple parser based off [Rodrigo's data extraction code](http://rodp.me/2015/how-to-extract-data-from-the-web.html). If you are like me and tired of seeing ads, images, links, videos, weird text - then you should try this. 

[Try it out here](http://choices.duckdns.org)


# Setup

To run just use

```bash
python justread.py
```

or 

```bash
gunicorn -w 4 -b 127.0.0.1:8009 justread:app
```


