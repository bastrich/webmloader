import urllib.request
import json
import os, time
import hashlib


def sha224hash(fileData):
    m = hashlib.sha224();
    m.update(fileData);
    return m.hexdigest();

threadNumber = "125517294"

os.makedirs(threadNumber)


lastPostNumber = 0

try:
    while(True):
        thread = json.loads(urllib.request.urlopen("https://2ch.hk/b/res/" + threadNumber + ".json").read().decode("utf-8"))
        newPosts = [post for post in thread["threads"][0]["posts"] if (int(post["num"]) > lastPostNumber and len([file for file in post["files"] if (file["type"] == 6)]) > 0)]
        for post in newPosts:
            for file in [file for file in post["files"] if (file["type"] == 6)]:
                f = open(threadNumber + "/" + file["name"], "wb")
                f.write(urllib.request.urlopen("https://2ch.hk/b/" + file["path"]).read())
                f.close()
        if len(newPosts) != 0:
            lastPostNumber = newPosts[len(newPosts) - 1]["num"]
        if len(newPosts) == 0:
            time.sleep(10);
except urllib.request.HTTPError:
    print("END...");