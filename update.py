#!/usr/bin/env python3
"""Write index.html so it redirects to the newest long-form video.

Run by .github/workflows/update.yml once a day (or by hand). The feed is
fetched here, on GitHub's side, so visitors only ever talk to GitHub Pages
and YouTube. If anything goes wrong, index.html is left as it was and the
site keeps pointing at the last good video.
"""
import html
import sys
import urllib.request
import xml.etree.ElementTree as ET

CHANNEL = "UCEWIYszywEy8TK4xgfrQbPA"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL}"
ATOM = {"a": "http://www.w3.org/2005/Atom"}

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={url}">
<title>Redirecting…</title>
</head>
<body>
<p>Redirecting to <a href="{url}">{title}</a> …</p>
</body>
</html>
"""


def newest_long_form(feed_xml):
    for entry in ET.fromstring(feed_xml).findall("a:entry", ATOM):
        url = entry.find("a:link", ATOM).get("href", "")
        title = entry.find("a:title", ATOM).text or ""
        # The feed links Shorts as /shorts/<id>; the title check is a backup.
        if "/shorts/" in url or "#shorts" in title.lower():
            continue
        return url, title
    return None


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "freevbucks-updater"})
    with urllib.request.urlopen(req, timeout=30) as r:
        found = newest_long_form(r.read())
    if not found:
        print("No long-form video among the newest 15 - keeping the current link.")
        return 0
    url, title = found
    if not url.startswith("https://www.youtube.com/watch?v="):
        print(f"Unexpected link {url!r} - keeping the current link.")
        return 1
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(PAGE.format(url=html.escape(url), title=html.escape(title)))
    print(f"{title}\n{url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
