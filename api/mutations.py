from asyncore import write
import uuid
from packutils.helper import fetchJSON, writeJSON, buildUserComicFilePath

def resolve_addNewComic(obj, info, input):
    path = buildUserComicFilePath(input["userID"])
    comics = fetchJSON(path)

    comicID = str(uuid.uuid4())
    userComic = {
        "id": comicID,
        "title": input["title"],
        "listUrl": input["listUrl"],
        "latestChapter": 0,
        "latestChapterUrl": "",
        "lastReadChapter": 0,
        "lastReadChapterUrl": "",
        "isLatestChapterOpened": False
    }

    comics[comicID] = userComic
    err = writeJSON(path, comics)
    if err is None:
        return userComic
    else:
        return err

def resolve_updateUserComicLastRead(obj, info, input):
    path = buildUserComicFilePath(input["userID"])
    comics = fetchJSON(path)

    comicID = input["comicID"]
    comic = comics[comicID]

    comic["lastReadChapter"] = input["chapter"]
    comic["lastReadChapterUrl"] = input["url"]

    # Todo, fetch latest chapter from listUrl

    if input["chapter"] == comic["latestChapter"]:
        comic["isLatestChapterOpened"] = True
    
    comics[comicID] = comic

    err = writeJSON(path, comics)
    if err is None:
        return comic
    else:
        return err