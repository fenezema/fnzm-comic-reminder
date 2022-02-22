from asyncore import write
import core
import os
import uuid
from .helper import writeJSON

def generateUser(name: str):
    path = core.App.config["DB_PATH"]

    userID = uuid.uuid4()
    data = {
        userID: {
                "id": userID,
                "name": name,
                "personalToken": uuid.uuid4()
        }
    }
    if len(os.listdir()) == 0:
        err = writeJSON(path, data)
        return err
    else:
        raise Exception('users data exists')
