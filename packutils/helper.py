import core
import json

def buildUserComicFilePath(userID: str):
    return core.App.config["DB_PATH"] + "/" + userID + ".json"

def fetchJSON(path: str):
    f = open(path, "r")
    data = json.load(f)
    f.close()

    return data

def writeJSON(path: str, data):
    try:
        jsonObject = json.dumps(data)
        with open(path, "w") as outfile:
            outfile.write(jsonObject)
        outfile.close()
        return None
    except ValueError:
        return ValueError
    