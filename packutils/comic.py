import core
import os
import uuid
from .helper import writeJSON

def generateComic():
    path = core.App.config["DB_PATH"]

    comicID = uuid.uuid4()
    if len(os.listdir()) <= 1:
        cmd = "touch " + path + "/" + comicID + ".json"
        os.system(cmd)
    else:
        raise Exception('user comic data exists')